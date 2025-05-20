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