import argparse
import re
import sys
import os
import warnings

token_specification = [
    ('IF', r'if'),  # if
    ('FOR', r'for'),  # for
    ('WHILE', r'while'),  # while
    ('DEF', r'def'),  # def
    ('ELIF', r'elif'),  # elif
    ('ELSE', r'else'),  # else
    ('TRY', r'try'),  # try
    ('EXCEPT', r'except'),  # except
    ('IDENT', r'[A-Za-z_][A-Za-z0-9_]*'),  # variable or function name
    ('NUMBER', r'\d+'),  # numbers
    ('LBRACE', r'\{'),  # opening brace
    ('RBRACE', r'\}'),  # closing brace
    ('LPAREN', r'\('),  # opening parenthesis
    ('RPAREN', r'\)'),  # closing parenthesis
    ('EQUALS', r'='),  # equals sign
    ('SKIP', r'[ \t\n\r]+'),  # skip whitespace
    ('MISMATCH', r'.'),  # anything else
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
        for i in range(1, len(input_lines)):
            if input_lines[i].startswith(('} else', '} elif')):
                raise SyntaxError(f"Misplaced '{input_lines[i].strip()}' statement at line {i + 1}. (REPY-0001)")
            if input_lines[i].startswith('} except'):
                raise SyntaxError(f"Misplaced '{input_lines[i].strip()}' statement at line {i + 1}. (REPY-0002)")

def parse_repython(code):
    """Parses the rePython code and converts it to valid Python code."""
    string_pattern = r'(\".*?\"|\'.*?\')|f\".*?\"|f\'.*?\''
    
    strings = re.findall(string_pattern, code)
    
    for s in strings:
        code = code.replace(s, s.replace("{", "{{").replace("}", "}}"))
    
    modified_code = []
    inside_block = False
    brace_stack = []
    lines = code.splitlines()

    check_syntax(lines)

    
    for line in lines:
        if re.match(r'^\s*(if|for|while|def|try|elif|else|except)\s.*\{', line):
            modified_code.append(line.split('{')[0] + ':')
            brace_stack.append('{')  
            inside_block = True
        elif re.match(r'^\s*\}', line) and inside_block:
            brace_stack.pop()
            inside_block = len(brace_stack) > 0
        else:
            # For all other lines (non-blocks), just append them without changes
            modified_code.append(line)


    return '\n'.join(modified_code)

def main():
    parser = argparse.ArgumentParser(description="Compile REPY files.")
    parser.add_argument("filename", help="The REPY file to compile.")
    args = parser.parse_args()

    input_file = args.filename
    
    if not os.path.exists(input_file):
        print(f"Error: The file {input_file} does not exist.")
        sys.exit(1)

    with open(input_file, 'r') as f:
        source_code = f.read()

    python_code = parse_repython(source_code)

    output_file = os.path.splitext(input_file)[0] + '.py'

    with open(output_file, 'w') as f:
        f.write(python_code)

    print(f"Successfully compiled {input_file} to {output_file}")

if __name__ == "__main__":
    main()
