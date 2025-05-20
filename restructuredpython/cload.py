import importlib
import struct
import sys
import os
import ctypes
import tomllib as toml

spec = importlib.util.find_spec("restructuredpython")
if spec and spec.origin:
    package_dir = os.path.dirname(spec.origin)
    io_dll = os.path.join(package_dir, "lib", "windows-libs", "io64.dll")

    io32_dll = os.path.join(package_dir, "lib", "windows-lib", "io32.dll")

    io_so = os.path.join(package_dir, "lib", "linux-libs", "io.so")

    io_dylib = os.path.join(package_dir, "lib", "macos-libs", "io.dylib")

if sys.platform == "win32":
    if (struct.calcsize("P") * 8) == 32:
        lib = ctypes.WinDLL(io32_dll)
    else:
        lib = ctypes.WinDLL(io_dll)
elif sys.platform == "darwin":
    lib = ctypes.CDLL(io_dylib)
else:
    lib = ctypes.CDLL(io_so)


lib.check_file_exists.argtypes = [ctypes.c_char_p]
lib.check_file_exists.restype = ctypes.c_int

lib.read_file.argtypes = [ctypes.c_char_p]
lib.read_file.restype = ctypes.c_char_p

lib.write_file.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
lib.write_file.restype = ctypes.c_int

lib.read_binary_file.argtypes = [
    ctypes.c_char_p, ctypes.POINTER(
        ctypes.c_size_t)]
lib.read_binary_file.restype = ctypes.POINTER(ctypes.c_char)


def load_toml_binary(filename):
    filename = str(filename)
    size = ctypes.c_size_t()
    raw_data_ptr = lib.read_binary_file(filename.encode(), ctypes.byref(size))

    if not raw_data_ptr:
        raise FileNotFoundError(f"Could not read {filename}")

    raw_data = ctypes.string_at(raw_data_ptr, size.value)
    return toml.loads(raw_data.decode())


def read_file_utf8(filename: str) -> str:
    size = ctypes.c_size_t()
    filename_bytes = filename.encode('utf-8')

    ptr = lib.read_binary_file(filename_bytes, ctypes.byref(size))
    if not ptr:
        raise FileNotFoundError(f"File not found: {filename}")

    raw_bytes = ctypes.string_at(ptr, size.value)

    try:
        text = raw_bytes.decode('utf-8')
    except UnicodeDecodeError as e:
        raise ValueError(f"File is not valid UTF-8: {e}")

    return text