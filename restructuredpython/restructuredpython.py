import argparse
import re
import sys
import os

# Define token patterns for parsing (updated to handle 'elif', 'else', 'try', and 'except')
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

# Create a regex pattern for all token types
token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)

def tokenize(code):
    """Tokenizes the rePython source code."""
    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value!r}')
        else:
            yield kind, value

def parse_repython(code):
    """Parses the rePython code and converts it to valid Python code."""
    lines = code.splitlines()
    
    # Check for misplaced 'else', 'elif', or 'except' statements directly after a closing brace
    for i in range(1, len(lines)):
        if lines[i].startswith(('} else', '} elif')):
            raise SyntaxError(f"Syntax error: Misplaced '{lines[i].strip()}' statement at line {i + 1}. (REPY-0001)")
        if lines[i].startswith('} except'):
            raise SyntaxError(f"Syntax error: Misplaced '{lines[i].strip()}' statement at line {i + 1}. (REPY-0002)")
        
    # Replace curly braces with colons after control structures and remove closing braces
    code = re.sub(r'\b(if|for|while|def|try|elif|)\s+([^\{]+)\s*\{', r'\1 \2:', code)  # Opening brace -> colon
    code = re.sub(r'\belse\s*\{', 'else:', code)  # Handle else separately
    code = re.sub(r'\bexcept\s*\{', 'except:', code)  # Handle except separately
    code = code.replace('}', '')  # Remove closing braces

    return code

def main():
    parser = argparse.ArgumentParser(description="Compile REPY files.")
    parser.add_argument("filename", help="The REPY file to compile.")
    args = parser.parse_args()

    input_file = args.filename
    
    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: The file {input_file} does not exist.")
        sys.exit(1)

    # Read input
    with open(input_file, 'r') as f:
        source_code = f.read()

    # Parse the code and convert it to Python code
    python_code = parse_repython(source_code)

    # Generate the output file path (same name but with .py extension)
    output_file = os.path.splitext(input_file)[0] + '.py'

    # Save the Python code to the output file
    with open(output_file, 'w') as f:
        f.write(python_code)

    print(f"Successfully compiled {input_file} to {output_file}")

if __name__ == "__main__":
    main()
