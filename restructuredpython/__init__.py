from .restructuredpython import *
from .parser import *

def parse(source_code):
    header_code, code_without_includes = process_includes(source_code, ".")

    python_code = parse_repython(code_without_includes)

    final_code = header_code + python_code

    return final_code

__all__ = ["parse", "check_syntax"]