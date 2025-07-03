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

import importlib.util
import struct
import sys
import os
import ctypes
import tomllib as toml
import time
from textformat import *
from .predefined.subinterpreter.optimize import optimize_loop, optimize_function

def time_opening(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Loading {
                func.__name__} module took {
                end_time -
                start_time:.2f} seconds.")
        return result
    return wrapper


spec = importlib.util.find_spec("restructuredpython")
if spec and spec.origin:
    package_dir = os.path.dirname(spec.origin)
    io_dll = os.path.join(package_dir, "lib", "windows-libs", "io64.dll")
    io32_dll = os.path.join(package_dir, "lib", "windows-lib", "io32.dll")
    io_so = os.path.join(package_dir, "lib", "linux-libs", "io.so")
    io_dylib = os.path.join(package_dir, "lib", "macos-libs", "io.dylib")
load_s = time.perf_counter()

import restructuredpython.api.libio as lib

load_e = time.perf_counter()
count = load_e - load_s
print(f"{bcolors.OKBLUE}Loading modules took {count}s{bcolors.ENDC}")

def load_toml_binary(filename):
    raw_data = lib.read_binary_file(filename)
    if raw_data is None:
        raise FileNotFoundError(f"{bcolors.FAIL}Could not read {filename}{bcolors.ENDC}")
    return toml.loads(raw_data.decode())
