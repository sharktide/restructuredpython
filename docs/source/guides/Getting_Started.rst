Getting started
===============

Welcome to reStructuredPython! 🎉  
This guide will walk you through installing the compiler, writing your first `.repy` program, and compiling or running it.

What is reStructuredPython?
---------------------------

reStructuredPython (aka **rePython**) is a superset of Python designed to:

- Use modern syntax inspired by JavaScript, C#, C/C++ and many other languages
- Compile back to 100% standard Python
- Support modular language features (like `|>` pipelines, braced blocks, multiline comments, and optional optimizations)

It's designed to look modern, feel powerful, and remain compatible with the Python ecosystem.

---

Installation
------------

Install the latest version using pip:

.. code-block:: shell

   pip install --upgrade restructuredpython

Make sure ``repy`` and ``repycl`` are now available in your terminal:

.. code-block:: shell

   repy -h
   repycl -h

---

Writing Your First Program
--------------------------

Create a file named `hello.repy`:

.. code-block:: repy

    /* This is a multiline
    comment */

    #hello.repy
    name = "sharktide"
    def say_hello(name) {
        print("reStructuredPython is Awesome!")
        return name
    }
    def say_bye(name) {
    print(f'Bye {name}')
    }
    name |> say_hello |> say_bye

---

Transpile or Run
----------------

To compile `.repy` into `.py`:

.. code-block:: shell

   repy hello.repy

This will generate `hello.py`.

To compile **and run** the program:

.. code-block:: shell

   repycl hello.repy

The `repycl` command handles compilation and runtime execution, especially for features like `optimize_loop` and `strict_types`.

---

.. Optional: Enable/Disable Features
.. ---------------------------------

.. reStructuredPython is **modular** — you can enable or disable language features using a `repyconfig.toml`.

.. Example:

.. .. code-block:: toml

.. ..    [features]
..    control_blocks = true
..    pipelines = false
..    optimizations = true

.. See :doc:`Feature Toggles <Feature_Toggles>` for more details.

.. ---

Next Steps
----------

- 📚 Explore the :doc:`Syntax Guide <../reference/Syntax_Guide>` for full syntax support
- ⚙️ Learn more about :doc:`repy <reference/repy>` and :doc:`repycl <../reference/repycl>`
- 🚀 Check out some of the :doc:`features <reference/Features/index>`
Happy coding!
