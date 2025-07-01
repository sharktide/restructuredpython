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

from .restructuredpython import *
from .parser import *


def parse(source_code):
    header_code, code_without_includes = process_includes(source_code, ".")

    python_code = parse_repython(code_without_includes)

    final_code = header_code + python_code

    return final_code


__all__ = ["parse", "check_syntax"]
