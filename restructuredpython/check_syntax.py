from textformat import *


def check_syntax(input_lines):
    for i in range(len(input_lines)):
        line = input_lines[i].strip()

        if line.startswith(('} else', '} elif')):
            raise SyntaxError(
                f"{
                    bcolors.BOLD}{
                    bcolors.FAIL}ERROR: Misplaced '{line}' statement at line {
                    i +
                    1}. (REPY-0001){
                    bcolors.ENDC}")
        if line.startswith('} except'):
            raise SyntaxError(
                f"{
                    bcolors.BOLD}{
                    bcolors.FAIL}Misplaced 'except' statement at line {
                    i +
                    1}. (REPY-0002){
                    bcolors.ENDC}")
        if line.startswith('} def'):
            raise SyntaxError(
                f"{bcolors.BOLD}{bcolors.FAIL}Misplaced 'def' statement at line {i + 1}. (REPY-0003){bcolors.ENDC}")
        if line.startswith('} class'):
            raise SyntaxError(
                f"{
                    bcolors.BOLD}{
                    bcolors.FAIL}Misplaced 'class' statement at line {
                    i +
                    1}. (REPY-0004){
                    bcolors.ENDC}")
        if line.startswith('} case'):
            raise SyntaxError(
                f"{bcolors.BOLD}{bcolors.FAIL}Misplaced 'case' statement at line {i + 1}. (REPY-0005){bcolors.ENDC}")
