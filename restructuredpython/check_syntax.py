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
