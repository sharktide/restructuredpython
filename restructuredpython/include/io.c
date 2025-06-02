// Copyright 2025 Rihaan Meher

// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at

//     http://www.apache.org/licenses/LICENSE-2.0

// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT __attribute__((visibility("default")))
#endif

EXPORT int check_file_exists(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file) {
        fclose(file);
        return 1;
    }
    return 0;
}

EXPORT char* read_file(const char *filename) {
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

EXPORT int write_file(const char *filename, const char *data) {
    FILE *file = fopen(filename, "w");
    if (!file) return 0;

    fputs(data, file);
    fclose(file);
    return 1;
}

EXPORT char* read_binary_file(const char *filename, size_t *size) {
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