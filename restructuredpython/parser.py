from .check_syntax import check_syntax
import re


def parse_repython(code):
    """Parses reStructuredPython and converts it to Python."""
    def chain_pipeline(code):
        parts = [part.strip() for part in code.split('|>')]
        if len(parts) > 1:
            def nest(parts):
                if len(parts) == 1:
                    return parts[0]
                else:
                    return f'{parts[-1]}({nest(parts[:-1])})'

            variable, pipeline = parts[0].split(
                '=') if '=' in parts[0] else ('', parts[0])
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

    check_syntax(lines)

    inside_comment_block = False

    for line in lines:
        processed_line = chain_pipeline(line)

        if inside_comment_block:
            if processed_line.endswith("*/"):
                modified_code.append(f"# {processed_line[:-2].strip()}")
                inside_comment_block = False
            else:
                modified_code.append(f"# {processed_line.strip()}")
        elif processed_line.startswith("/*") and processed_line.endswith("*/"):
            modified_code.append(f"# {processed_line[2:-2].strip()}")
        elif processed_line.startswith("/*"):
            modified_code.append(f"# {processed_line[2:].strip()}")
            inside_comment_block = True
        elif processed_line.endswith("*/"):
            modified_code.append(f"# {processed_line[:-2].strip()}")
        else:
            if re.match(
                r'^\s*(if|for|while|def|try|elif|else|except|class|match|with|case)\s.*\{',
                    processed_line):
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

    return '\n'.join(modified_code)
