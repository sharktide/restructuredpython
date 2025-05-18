import argparse
import re
import sys
import os
import warnings
import tempfile
from pathlib import Path
import ctypes
import sys
import tomllib as toml
import fnmatch
import pkgutil
import importlib
import struct

spec = importlib.util.find_spec("restructuredpython")
if spec and spec.origin:
    package_dir = os.path.dirname(spec.origin)
    io_dll = os.path.join(package_dir, "lib", "windows-libs", "io64.dll")
    
    io32_dll = os.path.join(package_dir, "lib", "windows-lib", "io32.dll")

    io_so = os.path.join(package_dir, "lib", "linux-libs", "io.so")

    io_dylib = os.path.join(package_dir, "lib", "macos-libs", "io.dylib")

if sys.platform == "win32":
    if (struct.calcsize("P") * 8) == 32:
        lib = ctypes.WinDLL(io32_dll)
    else:
        lib = ctypes.WinDLL(io_dll)
elif sys.platform == "darwin":
    lib = ctypes.CDLL(io_dylib)
else:
    lib = ctypes.CDLL(io_so)


lib.check_file_exists.argtypes = [ctypes.c_char_p]
lib.check_file_exists.restype = ctypes.c_int

lib.read_file.argtypes = [ctypes.c_char_p]
lib.read_file.restype = ctypes.c_char_p

lib.write_file.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
lib.write_file.restype = ctypes.c_int

lib.read_binary_file.argtypes = [
    ctypes.c_char_p, ctypes.POINTER(
        ctypes.c_size_t)]
lib.read_binary_file.restype = ctypes.POINTER(ctypes.c_char)


def load_toml_binary(filename):
    filename = str(filename)
    size = ctypes.c_size_t()
    raw_data_ptr = lib.read_binary_file(filename.encode(), ctypes.byref(size))

    if not raw_data_ptr:
        raise FileNotFoundError(f"Could not read {filename}")

    raw_data = ctypes.string_at(raw_data_ptr, size.value)
    return toml.loads(raw_data.decode())
def read_file_utf8(filename: str) -> str:
    size = ctypes.c_size_t()
    filename_bytes = filename.encode('utf-8')
    
    ptr = lib.read_binary_file(filename_bytes, ctypes.byref(size))
    if not ptr:
        raise FileNotFoundError(f"File not found: {filename}")
    
    raw_bytes = ctypes.string_at(ptr, size.value)

    try:
        text = raw_bytes.decode('utf-8')
    except UnicodeDecodeError as e:
        raise ValueError(f"File is not valid UTF-8: {e}")
    
    return text


token_specification = [
    ('COMMENT', r'/\*.*?\*/'),
    ('IF', r'if'),
    ('FOR', r'for'),
    ('WHILE', r'while'),
    ('DEF', r'def'),
    ('ELIF', r'elif'),
    ('ELSE', r'else'),
    ('TRY', r'try'),
    ('EXCEPT', r'except'),
    ('CLASS', r'class'),
    ('WITH', r'with'),
    ('MATCH', r'match'),
    ('CASE', r'case'),
    ('PIPE', r'\|>'),
    ('IDENT', r'[A-Za-z_][A-Za-z0-9_]*'),
    ('NUMBER', r'\d+'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('EQUALS', r'='),
    ('SKIP', r'[ \t\n\r]+'),
    ('MISMATCH', r'.'),
]

token_regex = '|'.join(
    f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)


def tokenize(code):
    """Tokenizes the rePython source code and handles multiline comments."""
    inside_multiline_comment = False
    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup
        value = mo.group()

        if kind == 'SKIP':
            continue

        elif kind == 'COMMENT':
            if value.startswith('/*') and value.endswith('*/'):
                comment_lines = value[2:-2].splitlines()
                for line in comment_lines:
                    yield 'COMMENT', f"# {line.strip()}"
                continue
        elif kind == 'MISMATCH':
            warnings.warn(
                f"Unexpected character {
                    value!r}. Continuing with compilation")  # fmt: skip
            yield kind, value

        else:
            yield kind, value


def check_syntax(input_lines):
    for i in range(len(input_lines)):
        line = input_lines[i].strip()

        if line.startswith(('} else', '} elif')):
            raise SyntaxError(
                f"Misplaced '{line}' statement at line {
                    i + 1}. (REPY-0001)")  # fmt: skip
        if line.startswith('} except'):
            raise SyntaxError(
                f"Misplaced 'except' statement at line {
                    i + 1}. (REPY-0002)")  # fmt: skip
        if line.startswith('} def'):
            raise SyntaxError(
                f"Misplaced 'def' statement at line {
                    i + 1}. (REPY-0003)")  # fmt: skip
        if line.startswith('} class'):
            raise SyntaxError(
                f"Misplaced 'class' statement at line {
                    i + 1}. (REPY-0004)")  # fmt: skip
        if line.startswith('} case'):
            raise SyntaxError(
                f"Misplaced 'case' statement at line {
                    i + 1}. (REPY-0005)")  # fmt: skip


def parse_repython(code):
    """Parses the rePython code and converts it to valid Python code."""
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


def compile_header_file(header_filename):
    """Compiles a .cdata file and returns the corresponding Python code."""
    header_filename = Path(header_filename).resolve()
    header_filename = str(header_filename)
    if lib.check_file_exists(header_filename.encode()) == 0:
        raise FileNotFoundError(f"Header file {header_filename} not found.")
    try:
        header_code = read_file_utf8(header_filename)
        if not header_code.strip():
            raise ValueError(f"Header file {header_filename} is empty.")
    except Exception as e:
        print(f"Error opening file {header_filename}: {e}")
        return ""

    return parse_repython(header_code)


PREDEFINED_HEADERS_DIR = os.path.join(os.path.dirname(__file__), "predefined")


def process_includes(code, input_file):
    """Processes #include directives, handling both predefined and user-defined files."""
    include_pattern = r'\s*include\s+[\'"]([^\'"]+)[\'"]'
    includes = re.findall(include_pattern, code)

    header_code = ""

    for include in includes:
        # predefined
        predefined_path = os.path.join(
            PREDEFINED_HEADERS_DIR, include.replace(
                '.', os.sep) + '.py')
        if lib.check_file_exists(predefined_path.encode()):
            header_code += compile_header_file(predefined_path) + "\n"
            continue
        # userdefined
        if not os.path.isabs(include):
            include = os.path.join(
                os.path.dirname(
                    os.path.abspath(input_file)),
                include)

        if lib.check_file_exists(include.encode()):
            header_code += compile_header_file(include) + "\n"
        else:
            print(f"Error: Included file '{include}' not found.")
            continue

    code_without_includes = re.sub(include_pattern, '', code)

    return header_code, code_without_includes


def execute_code_temporarily(code):
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_file_path = os.path.join(tmpdir, "compiled_repy.py")
        lib.write_file(temp_file_path.encode(), code.encode())
        try:
            exec(open(temp_file_path).read(), {"__name__": "__main__"})
        except Exception as e:
            print(f"Error during execution: {e}")
            print(f"You can view the generated file at {(temp_file_path)}")


def main():
    parser = argparse.ArgumentParser(description="Compile REPY files.")
    parser.add_argument("filename", help="The REPY file to compile.")
    args = parser.parse_args()

    input_file = args.filename

    input_file = str(input_file)

    if lib.check_file_exists(input_file.encode()) == 0:
        print(f"Error: The file {input_file} does not exist.")
        return
    if input_file.endswith('repyconfig.toml'):
        data = load_toml_binary(input_file)
        try:
            compile_value = data["config"]["compile"]
        except BaseException:
            compile_value = "null"
            print("[WARNING] Error reading compile value from config")
        try:
            exclude_files = data["config"]["exclude"]
        except BaseException:
            exclude_files = []
            print("[WARNING] No excluded files found in config")
        if compile_value == 'all':
            extension = ".repy"
            matching_files = []
            for dirpath, _, filenames in os.walk("."):
                for filename in filenames:
                    if filename.lower().endswith(extension.lower()):
                        file_path_temp = os.path.join(dirpath, filename)
                        if any(fnmatch.fnmatch(file_path_temp, pattern)
                               for pattern in exclude_files):
                            continue
                        matching_files.append(file_path_temp)
            for file_path_z in matching_files:
                file_path_z = str(file_path_z)
                source_code_z = lib.read_file(file_path_z.encode()).decode()

                header_code_z, code_without_includes_z = process_includes(
                    source_code_z, file_path_z)

                python_code_z = parse_repython(code_without_includes_z)

                final_code_z = header_code_z + python_code_z

                output_file_z = os.path.splitext(file_path_z)[0] + '.py'

                lib.write_file(output_file_z.encode(), final_code_z.encode())

                print(
                    f"[DEBUG] Successfully compiled {file_path_z} to {output_file_z}")
    else:
        source_code = lib.read_file(input_file.encode()).decode()

        header_code, code_without_includes = process_includes(
            source_code, input_file)

        python_code = parse_repython(code_without_includes)

        final_code = header_code + python_code

        output_file = os.path.splitext(input_file)[0] + '.py'

        lib.write_file(output_file.encode(), final_code.encode())

        print(f"[DEBUG] Successfully compiled {input_file} to {output_file}")


def launch():
    parser = argparse.ArgumentParser(description="Preview REPY execution.")
    parser.add_argument("filename", help="The REPY file to preview.")
    args = parser.parse_args()

    input_file = args.filename
    input_file = str(input_file)

    if lib.check_file_exists(input_file.encode()) == 0:
        print(f"Error: The file {input_file} does not exist.")
        return

    source_code = lib.read_file(input_file.encode()).decode()

    header_code, code_without_includes = process_includes(
        source_code, input_file)

    python_code = parse_repython(code_without_includes)

    final_code = header_code + python_code

    try:
        execute_code_temporarily(final_code)
    except Exception as e:
        print(f"Error during execution: {e}")


if __name__ == "__main__":
    main()
