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

from .cload import lib, optimize_function, optimize_loop
from textformat import bcolors
import tempfile
import os

exec_globals = {
    "__name__": "__main__",
    "optimize_loop": optimize_loop,
    "optimize_function": optimize_function
}

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

def execute_code_temporarily(code):
    """Executes the compiled python code"""
    with tempfile.TemporaryDirectory() as tmpdir:
        rewritten_code = wrap_loops_for_optimization(code)
        temp_file_path = os.path.join(tmpdir, "_runtime.rpyt")
        lib.write_file(temp_file_path, rewritten_code)
        try:
            exec(open(temp_file_path).read(), exec_globals)
        except Exception as e:
            print(f"{bcolors.FAIL}Error during execution: {e}")
