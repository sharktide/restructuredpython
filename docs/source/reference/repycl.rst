repycl Command
==============

The ``repycl`` command compiles and directly executes reStructuredPython code **with compiler optimizations** in one step.

.. code-block:: shell

   repycl path/to/file.repy

It automatically compiles your code to and then runs it. This is useful for:

- Running code without transpiling intermediate `.py` files
- Runtime optimizations and performance testing
- Debugging optimized loops or runtime decorators