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

import argparse
import re
import os
import tempfile
from pathlib import Path
import sys
import tomllib as toml
import fnmatch

from .parser import parse_repython
from .cload import *
from .tempload import *
from textformat import *


def compile_header_file(header_filename, mode="classic"):
    """Compiles a .cdata file and returns the corresponding Python code."""
    header_filename = Path(header_filename).resolve()
    header_filename = str(header_filename)
    if lib.check_file_exists(header_filename) == 0:
        raise FileNotFoundError(
            f"{bcolors.BOLD}{bcolors.FAIL}Header file {header_filename} not found.{bcolors.ENDC}")
    try:
        header_code = lib.read_file(header_filename)
        if not header_code.strip():
            raise ValueError(
                f"{bcolors.BOLD}{bcolors.FAIL}Header file {header_filename} is empty.{bcolors.ENDC}")
    except Exception as e:
        print(
            f"{bcolors.WARNING}Error opening file {header_filename}: {e}{bcolors.ENDC}")
        return ""

    return parse_repython(header_code, mode)


PREDEFINED_HEADERS_DIR = os.path.join(os.path.dirname(__file__), "predefined")


def process_includes(code, input_file, mode="classic"):
    """Processes #include directives, handling both predefined and user-defined files."""
    include_pattern = r'\s*include\s+[\'"]([^\'"]+)[\'"]'
    includes = re.findall(include_pattern, code)

    header_code = ""

    for include in includes:
        # predefined
        predefined_path = os.path.join(
            PREDEFINED_HEADERS_DIR, include.replace(
                '.', os.sep) + '.py')
        if lib.check_file_exists(predefined_path):
            header_code += compile_header_file(predefined_path) + "\n"
            continue
        # userdefined
        if not input_file == ".":
            if not os.path.isabs(include):
                include = os.path.join(
                    os.path.dirname(
                        os.path.abspath(input_file)),
                    include)

        if lib.check_file_exists(include):
            header_code += compile_header_file(include, mode) + "\n"
        else:
            print(
                f"{
                    bcolors.BOLD}{
                    bcolors.FAIL}Error: Included file '{include}' not found.{
                    bcolors.ENDC}")
            continue

    code_without_includes = re.sub(include_pattern, '', code)

    return header_code, code_without_includes


def main():
    parser = argparse.ArgumentParser(description="Compile REPY files.")
    parser.add_argument("filename", help="The REPY file to compile.")
    args = parser.parse_args()

    input_file = args.filename

    input_file = str(input_file)

    if lib.check_file_exists(input_file) == 0:
        print(
            f"{
                bcolors.BOLD}{
                bcolors.FAIL}Error: The file {input_file} does not exist.{
                bcolors.ENDC}")
        return
    if input_file.endswith('repyconfig.toml'):
        data = load_toml_binary(input_file)
        try:
            compile_value = data["config"]["compile"]
        except BaseException:
            compile_value = "null"
            raise BaseException(
                f"{bcolors.BOLD}{bcolors.FAIL}Error reading compile value from config{bcolors.ENDC}")
        try:
            exclude_files = data["config"]["exclude"]
        except BaseException:
            exclude_files = []
            print(
                f"{bcolors.WARNING}[WARNING] No excluded files found in config{bcolors.ENDC}")
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
                source_code_z = lib.read_file(file_path_z)

                header_code_z, code_without_includes_z = process_includes(
                    source_code_z, file_path_z)

                python_code_z = parse_repython(code_without_includes_z)

                final_code_z = header_code_z + python_code_z

                output_file_z = os.path.splitext(file_path_z)[0] + '.py'

                lib.write_file(output_file_z, final_code_z)

                print(
                    f"{bcolors.OKGREEN}Compiled {file_path_z} to {output_file_z}{bcolors.ENDC}")
    else:
        with open(input_file, 'r') as f:
            source_code = f.read()

        header_code, code_without_includes = process_includes(
            source_code, input_file)

        python_code = parse_repython(code_without_includes)

        final_code = header_code + python_code

        output_file = os.path.splitext(input_file)[0] + '.py'

        lib.write_file(output_file, final_code)

        print(
            f"{
                bcolors.BOLD}{
                bcolors.OKGREEN}Compiled {input_file}{
                bcolors.ENDC}{
                    bcolors.OKGREEN} --> {output_file}{
                        bcolors.ENDC}")


def launch():
    parser = argparse.ArgumentParser(description="Preview REPY execution.")
    parser.add_argument("filename", help="The REPY file to preview.")
    args = parser.parse_args()

    input_file = args.filename
    input_file = str(input_file)

    if lib.check_file_exists(input_file) == 0:
        print(
            f"{
                bcolors.BOLD}{
                bcolors.FAIL}Error: The file {input_file} does not exist.{
                bcolors.ENDC}")
        return

    with open(input_file, 'r') as f:
        source_code = f.read()

    header_code, code_without_includes = process_includes(
        source_code, input_file, mode="launch")

    python_code = parse_repython(code_without_includes, mode="launch")

    final_code = header_code + python_code

    try:
        execute_code_temporarily(final_code)
    except Exception as e:
        print(f"Error during execution: {e}")


if __name__ == "__main__":
    main()
