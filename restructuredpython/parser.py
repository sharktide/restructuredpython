# Copyright 2025 Rihaan Meher

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .check_syntax import check_syntax
import re

def wrap_loops_for_optimization(code):
    """
    Rewrites for/while loops with <OPTIMIZE ...> annotations into runtime functions
    with decorators.
    """
    lines = code.splitlines()
    modified_lines = []
    i = 0
    loop_counter = 0

    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("@optimize_loop("):
            decorator_line = lines[i]
            loop_line = lines[i + 1].strip()
            loop_indent = len(lines[i + 1]) - len(loop_line)
            func_name = f"_repy_optimized_loop_{loop_counter}"
            loop_counter += 1

            modified_lines.append(decorator_line)
            modified_lines.append(" " * loop_indent + f"def {func_name}():")
            modified_lines.append(" " * (loop_indent + 4) + loop_line)
            i += 2

            # Copy indented body lines until dedent or EOF
            while i < len(lines):
                body_line = lines[i]
                if body_line.strip() == "":
                    modified_lines.append(body_line)
                    i += 1
                    continue
                body_indent = len(body_line) - len(body_line.lstrip())
                if body_indent <= loop_indent:
                    break
                modified_lines.append(" " * (loop_indent + 8) + body_line.strip())
                i += 1

            modified_lines.append(" " * loop_indent + f"{func_name}()")
        else:
            modified_lines.append(lines[i])
            i += 1

    return "\n".join(modified_lines)

def parse_repython(code, mode="classic"):
    """Parses reStructuredPython and converts it to Python."""
    required_imports = set()
    def chain_pipeline(code):
        parts = [part.strip() for part in code.split('|>')]
        if len(parts) > 1:
            def nest(parts):
                if len(parts) == 1:
                    return parts[0]
                else:
                    return f'{parts[-1]}({nest(parts[:-1])})'
            variable, pipeline = parts[0].split('=') if '=' in parts[0] else ('', parts[0])
            variable = variable.strip()
            pipeline = pipeline.strip()
            if variable:
                nested_call = nest([pipeline] + parts[1:])
                return f'{variable} = {nested_call}'
            else:
                return nest(parts)
        return code

    modified_code = []
    inside_block = False
    brace_stack = []
    lines = code.splitlines()

    check_syntax(lines, mode=mode)

    inside_comment_block = False
    pending_optimize = None

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Detect <OPTIMIZE ...> directive
        if stripped.startswith("<OPTIMIZE") and stripped.endswith(">"):
            match = re.match(r'<OPTIMIZE\s+(.+?)>', stripped)
            if match:
                pending_optimize = match.group(1).strip()
            continue

        processed_line = chain_pipeline(line)

        # Handle comment blocks
        if inside_comment_block:
            if processed_line.endswith("*/"):
                modified_code.append(f"# {processed_line[:-2].strip()}")
                inside_comment_block = False
            else:
                modified_code.append(f"# {processed_line.strip()}")
            continue
        elif processed_line.startswith("/*") and processed_line.endswith("*/"):
            modified_code.append(f"# {processed_line[2:-2].strip()}")
            continue
        elif processed_line.startswith("/*"):
            modified_code.append(f"# {processed_line[2:].strip()}")
            inside_comment_block = True
            continue
        elif processed_line.endswith("*/"):
            modified_code.append(f"# {processed_line[:-2].strip()}")
            continue

        # Apply decorator before next block
        if pending_optimize:
            if re.match(r'^\s*(for|while)\s+.*\{', processed_line):
                modified_code.append(f"@optimize_loop({pending_optimize})")
                required_imports.add("optimize_loop")
                pending_optimize = None
            elif re.match(r'^\s*def\s+.*\{', processed_line):
                modified_code.append(f"@optimize_function({pending_optimize})")
                required_imports.add("optimize_function")
                pending_optimize = None

        # Block conversions
        if re.match(r'^\s*(if|for|while|def|try|elif|else|except|class|match|with|case)\s.*\{', processed_line):
            modified_code.append(processed_line.split('{')[0] + ':')
            brace_stack.append('{')
            inside_block = True
        elif re.match(r'^\s*\}', processed_line) and inside_block:
            brace_stack.pop()
            inside_block = len(brace_stack) > 0
        elif re.match(r'^\s*match\(', processed_line):
            modified_code.append(processed_line.split('{')[0] + ':')
            brace_stack.append('{')
            inside_block = True
        elif re.match(r'^\s*case', processed_line):
            modified_code.append(processed_line.split('{')[0] + ':')
            brace_stack.append('{')
            inside_block = True
        else:
            modified_code.append(processed_line)

    # Insert necessary imports at the top
    import_lines = []
    if "optimize_loop" in required_imports or "optimize_function" in required_imports:
        imports = []
        if "optimize_function" in required_imports:
            imports.append("optimize_function")
        if "optimize_loop" in required_imports:
            imports.append("optimize_loop")
        import_lines.append(f"from restructuredpython.predefined.subinterpreter import {', '.join(imports)}")

    raw_code = '\n'.join(import_lines + modified_code)
    final_code = wrap_loops_for_optimization(raw_code)
    return final_code

