#include "Python.h"
#include <stdio.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject representing a Python string.
 */
void print_python_string(PyObject *p)
{
    Py_UNICODE *str;
    Py_ssize_t length;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    length = PyUnicode_GetLength(p);
    str = PyUnicode_AsUnicode(p);

    printf("  type: str\n");
    printf("  length: %zd\n", length);
    printf("  value: %ls\n", str);
}
