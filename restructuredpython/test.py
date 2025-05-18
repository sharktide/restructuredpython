import ctypes

lib = ctypes.CDLL("restructuredpython/io.dll")  # Windows: file_ops.dll

lib.check_file_exists.argtypes = [ctypes.c_char_p]
lib.check_file_exists.restype = ctypes.c_int

lib.read_file.argtypes = [ctypes.c_char_p]
lib.read_file.restype = ctypes.c_char_p

lib.write_file.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
lib.write_file.restype = ctypes.c_int

# Usage in Python
filename = b"restructuredpython/source.c.repy"  # Byte string for C compatibility
print(lib.check_file_exists(filename))
if lib.check_file_exists(filename) == 1:
    print('h')
    content = lib.read_file(filename)
    print(content.decode())  # Convert back to Python string

    # Write compiled output
    lib.write_file(b"output.py", content)

print('done')
