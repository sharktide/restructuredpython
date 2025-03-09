Overview
========

reStructuredPython, also known as 'rePython', is an alternative Python implementation that introduces JavaScript-like syntax for a cleaner and more readable code structure. The reStructuredPython compiler converts ``.repy`` files into standard Python code.

Key Features
------------

* **Curly-Braced Control Statements:** Control structures in reStructuredPython utilize curly braces, similar to JavaScript, enhancing readability.

Installation
------------
To install the reStructuredPython compiler, use pip:

.. code-block:: bash

    pip install restructuredpython

Usage
-----

After installation, compile a .repy file by running:

.. code-block:: bash

    repy path/to/your/file.repy

Example
-------

Consider the following reStructuredPython code in ``example.repy``:

.. code-block:: repy

    x = int(input("Enter a number: "))
    if (x > 0) {
        print("Positive number")
    } else if (x < 0) {
        print("Negative number")
    } else {
        print("Zero")
    }

Running ``repy example.repy`` compiles this into standard Python code, which can then be executed as usual.

*Note: reStructuredPython is designed for users who prefer a JavaScript-like syntax within the Python ecosystem. While it offers syntactic differences, the compiled output remains standard Python code.*


