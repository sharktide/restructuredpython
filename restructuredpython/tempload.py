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
    "__name__": "__main__"
}

def execute_code_temporarily(code):
    """Executes the compiled python code"""
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_file_path = os.path.join(tmpdir, "_runtime.rpyt")
        lib.write_file(temp_file_path, code)
        try:
            exec(open(temp_file_path).read(), exec_globals)
        except Exception as e:
            print(f"{bcolors.FAIL}Error during execution: {e}")
