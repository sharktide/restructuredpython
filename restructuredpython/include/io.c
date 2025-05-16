#include <stdio.h>
#include <stdlib.h>
#include <string.h>

__declspec(dllexport) int check_file_exists(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file) {
        fclose(file);
        return 1;
    }
    return 0;
}

__declspec(dllexport) char* read_file(const char *filename) {
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

__declspec(dllexport) int write_file(const char *filename, const char *data) {
    FILE *file = fopen(filename, "w");
    if (!file) return 0;

    fputs(data, file);
    fclose(file);
    return 1;
}

__declspec(dllexport) char* read_binary_file(const char *filename, size_t *size) {
    FILE *file = fopen(filename, "rb");
    if (!file) return NULL;

    fseek(file, 0, SEEK_END);
    *size = ftell(file);  // Get file size
    rewind(file);

    char *buffer = (char*)malloc(*size);
    fread(buffer, *size, 1, file);
    fclose(file);

    return buffer;
}