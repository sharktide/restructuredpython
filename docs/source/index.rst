reStructuredPython Documentation
================================

Welcome to the reStructuredPython documentation! reStructuredPython, also known as 'rePython', is a superset of python with full compatibility with existing python libaries that compiles back into standard python!

https://github.com/sharktide/restructuredpython

Getting Started
---------------

To begin using reStructuredPython, install the compiler via pip:

.. code-block:: shell

   pip install --upgrade restructuredpython

After installation, you can compile your .repy files to .py using the following command:

.. code-block:: shell

   repy path/to/your/file.repy

Or you can directly run .repy programs via the ``repycl`` command if using 1.1.0+
.. code-block:: shell

   repycl path/to/your/file.repy

Features
--------

* **JavaScript-like Syntax:** Enjoy a syntax reminiscent of JavaScript, making it familiar and intuitive for developers with a JavaScript background.
* **Header Files** In reStructuredPython, enjoy having the ability to create header files, similar to C++ for easier, and more organized development. View the `syntax <https://restructuredpython.readthedocs.io/en/latest/reference/Syntax_Guide.html>`_ guide for more details.
* **Seamless Compilation:** reStructuredPython code compiles directly into Python, ensuring compatibility with existing Python libraries and frameworks.
* **Enhanced Readability:** The syntax enhancements which include multiline comments aim to improve code readability and reduce verbosity.
* **repyconfig.toml:** Easily control the build of your projects with a repyconfig.toml
* **Strict Types** Enhance your python projects wil strict types in functions with the builtin strict_types decorator

Documentation
-------------

* **Syntax Guide:** Learn about the specific syntax changes and how to write reStructuredPython code effectively.
* **Installation Guide:** Step-by-step instructions on setting up reStructuredPython in your development environment.
* **Syntax Reference:** Comprehensive details on the available functions, classes, and modules within reStructuredPython.
* **Examples:** Explore practical examples demonstrating the use of reStructuredPython in various scenarios.
* **Builtin functions and decorators** Starting 1.0.0, builtin decorators have been added using the ``include`` keyword.

Community and Support
---------------------

Join the reStructuredPython community to contribute, ask questions, and stay updated:

* **GitHub Repository:** Access the source code, report issues, and contribute to the project at https://github.com/sharktide/restructuredpython.
* **Discussions:** Participate in discussions with other users and developers to share ideas and get support.


Checking the version of reStructuredPython
------------------------------------------

If reStructuredPython is already installed on your systen, you may
check the version of reStructuredPython via the following methods

- ``pip show restructuredpython``
- ``repy --version``
- ``repy -v``
- ``repycl --version``
- ``repycl -v``

.. toctree::
   :maxdepth: 2
   :caption: Contents

   error_index/index
   changelog
   guides/Getting_Started
   guides/Install
   reference/index
   reference/Builtin_Decorators
   reference/optimize
   reference/repycl
   reference/repy
   tutorials/Example_Programs
   roadmap

