// # Copyright 2025 Rihaan Meher

// # Licensed under the Apache License, Version 2.0 (the "License");
// # you may not use this file except in compliance with the License.
// # You may obtain a copy of the License at

// #     http://www.apache.org/licenses/LICENSE-2.0

// # Unless required by applicable law or agreed to in writing, software
// # distributed under the License is distributed on an "AS IS" BASIS,
// # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// # See the License for the specific language governing permissions and
// # limitations under the License.

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>
#include <string.h>

// Original C function declarations
extern int check_file_exists(const char *filename);
extern char* read_file(const char *filename);
extern int write_file(const char *filename, const char *data);
extern char* read_binary_file(const char *filename, size_t *size);

int check_file_exists(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file) {
        fclose(file);
        return 1;
    }
    return 0;
}

char* read_file(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (!file) return NULL;

    fseek(file, 0, SEEK_END);
    long size = ftell(file);
    rewind(file);

    char *buffer = (char*)malloc(size + 1);
    fread(buffer, size, 1, file);
    buffer[size] = '\0';
    fclose(file);
    return buffer;
}

int write_file(const char *filename, const char *data) {
    FILE *file = fopen(filename, "w");
    if (!file) return 0;

    fputs(data, file);
    fclose(file);
    return 1;
}

char* read_binary_file(const char *filename, size_t *size) {
    FILE *file = fopen(filename, "rb");
    if (!file) return NULL;

    fseek(file, 0, SEEK_END);
    *size = ftell(file);
    rewind(file);

    char *buffer = (char*)malloc(*size);
    fread(buffer, *size, 1, file);
    fclose(file);
    return buffer;
}

// Wrappers that expose C types but are valid PyObject*
static PyObject* py_check_file_exists(PyObject *self, PyObject *args) {
    const char* filename;
    if (!PyArg_ParseTuple(args, "s", &filename)) return NULL;

    int exists = check_file_exists(filename);
    return PyLong_FromLong(exists);
}

static PyObject* py_read_file(PyObject *self, PyObject *args) {
    const char* filename;
    if (!PyArg_ParseTuple(args, "s", &filename)) return NULL;

    char* result = read_file(filename);
    if (!result) Py_RETURN_NONE;

    PyObject* py_result = PyUnicode_FromString(result);
    free(result);
    return py_result;
}

static PyObject* py_write_file(PyObject *self, PyObject *args) {
    const char* filename;
    const char* data;
    if (!PyArg_ParseTuple(args, "ss", &filename, &data)) return NULL;

    int result = write_file(filename, data);
    return PyLong_FromLong(result);
}

static PyObject* py_read_binary_file(PyObject *self, PyObject *args) {
    const char* filename;
    if (!PyArg_ParseTuple(args, "s", &filename)) return NULL;

    size_t size = 0;
    char* data = read_binary_file(filename, &size);
    if (!data) Py_RETURN_NONE;

    PyObject* result = PyBytes_FromStringAndSize(data, size);
    free(data);
    return result;
}

// Function table
static PyMethodDef methods[] = {
    {"check_file_exists", py_check_file_exists, METH_VARARGS, "Check if file exists"},
    {"read_file", py_read_file, METH_VARARGS, "Read file contents"},
    {"write_file", py_write_file, METH_VARARGS, "Write data to file"},
    {"read_binary_file", py_read_binary_file, METH_VARARGS, "Read binary contents"},
    {NULL, NULL, 0, NULL}
};

// Module definition
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "libio",     // name of module
    NULL,        // module documentation
    -1,
    methods
};

PyMODINIT_FUNC PyInit_libio(void) {
    return PyModule_Create(&moduledef);
}
