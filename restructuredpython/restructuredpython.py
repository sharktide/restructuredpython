import argparse
import re
import sys
import os
import warnings
from pathlib import Path

# Define token specifications
token_specification = [
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
    ('PIPE', r'\|>'), # pipeline operator
    ('IDENT', r'[A-Za-z_][A-Za-z0-9_]*'),  # variable or function name
    ('NUMBER', r'\d+'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('EQUALS', r'='),
    ('SKIP', r'[ \t\n\r]+'),
    ('MISMATCH', r'.'),
]

token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)

def tokenize(code):
    """Tokenizes the rePython source code."""
    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            warnings.warn(f'Unexpected character {value!r}. Continuing with compilation')
            yield kind, value
        else:
            yield kind, value

def check_syntax(input_lines):
    for i in range(len(input_lines)):
        line = input_lines[i].strip()
        
        if line.startswith(('} else', '} elif')):
            raise SyntaxError(f"Misplaced '{line}' statement at line {i + 1}. (REPY-0001)")
        if line.startswith('} except'):
            raise SyntaxError(f"Misplaced 'except' statement at line {i + 1}. (REPY-0002)")
        if line.startswith('} def'):
            raise SyntaxError(f"Misplaced 'def' statement at line {i + 1}. (REPY-0003)")
        if line.startswith('} class'):
            raise SyntaxError(f"Misplaced 'class' statement at line {i + 1}. (REPY-0004)")
        if line.startswith('} case'):
            raise SyntaxError(f"Misplaced 'case' statement at line {i + 1}. (REPY-0005)")

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

            # Separate the variable assignment from the pipeline
            variable, pipeline = parts[0].split('=') if '=' in parts[0] else ('', parts[0])
            variable = variable.strip()
            pipeline = pipeline.strip()
            
            # If there's a variable assignment, construct the nested calls, otherwise just return the pipeline
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

    for line in lines:
        processed_line = chain_pipeline(line)
        # Handle statements that begin with a keyword and have an opening brace
        if re.match(r'^\s*(if|for|while|def|try|elif|else|except|class|match|with|case)\s.*\{', processed_line):
            # Replace the { with a colon (:) and track the opening brace
            modified_code.append(processed_line.split('{')[0] + ':')
            brace_stack.append('{')
            inside_block = True
        # Handle the case where we encounter a closing brace
        elif re.match(r'^\s*\}', processed_line) and inside_block:
            brace_stack.pop()  # Pop the opening brace from the stack
            inside_block = len(brace_stack) > 0  # Check if we still have open blocks
        elif re.match(r'^\s*match\(', processed_line):
            # Specifically handle the match statement to remove { and add :
            modified_code.append(processed_line.split('{')[0] + ':')
            brace_stack.append('{')
            inside_block = True
        elif re.match(r'^\s*case', processed_line):
            # Handle case blocks to remove { and add :
            modified_code.append(processed_line.split('{')[0] + ':')
            brace_stack.append('{')
            inside_block = True
        else:
            modified_code.append(processed_line)

    return '\n'.join(modified_code)

def compile_header_file(header_filename):
    """Compiles a .cdata file and returns the corresponding Python code."""
    
    # Make sure the file exists
    header_filename = Path(header_filename).resolve()
    header_filename = header_filename.as_posix()
    header_filename = Path(header_filename).resolve()
    print(f"Resolved header file path: {header_filename}")
    
    if not header_filename.exists():
        raise FileNotFoundError(f"Header file {header_filename} not found.")
    try:
        with header_filename.open('r') as f:
            header_code = f.read()
        if not header_code.strip():
            raise ValueError(f"Header file {header_filename} is empty.")
    except Exception as e:
        print(f"Error opening file {header_filename}: {e}")
        return ""
    
    return parse_repython(header_code)

def process_includes(code, input_file):
    """Processes #include directives and compiles included .d.repy files."""
    include_pattern = r'\s*include\s+[\'"]([^\'"]+)[\'"]'
    
    includes = re.findall(include_pattern, code)
    if includes:
        print(f"All include files: {includes}")
    else:
        print("No include found.")

    header_code = ""
    for include in includes:
        print(f"Processing include: {include}")
        
        if not os.path.isabs(include):
            include = os.path.join(os.path.dirname(os.path.abspath(input_file)), include)
        
        if os.path.exists(include):
            print(f"Compiling included file: {include}") 
            header_code += compile_header_file(include) + "\n"
        else:
            print(f"Error: Included file '{include}' not found.")
            continue

    code_without_includes = re.sub(include_pattern, '', code)

    return header_code, code_without_includes

# Example use case
def main():
    parser = argparse.ArgumentParser(description="Compile REPY files.")
    parser.add_argument("filename", help="The REPY file to compile.")
    args = parser.parse_args()

    input_file = args.filename

    if not os.path.exists(input_file):
        print(f"Error: The file {input_file} does not exist.")
        return
    
    with open(input_file, 'r') as f:
        source_code = f.read()

    header_code, code_without_includes = process_includes(source_code, input_file)

    python_code = parse_repython(code_without_includes)

    final_code = header_code + python_code

    output_file = os.path.splitext(input_file)[0] + '.py'

    with open(output_file, 'w') as f:
        f.write(final_code)

    print(f"Successfully compiled {input_file} to {output_file}")

if __name__ == "__main__":
    main()
