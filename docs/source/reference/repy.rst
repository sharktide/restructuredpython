repy Command
===============

The ``repy`` command is the original compiler for reStructuredPython.

It takes a `.repy` (reStructuredPython) file and compiles it into standard Python (`.py`) output.

How to use
----------

.. code-block:: shell

   repy path/to/source.repy

This will generate a Python file in the same directory named `source.py`.

---

Supported Features
------------------

✅ The `repy` command processes the following features:

- Function Chaining :doc:`Features/chaining`
- Multiline Comments :doc:`Features/comments`
- Optional curly brackets on control loops (like c/cpp/cs/js) :doc:`Features/control`
- Built-in Decorators :doc:`Builtin_Decorators/index`
- Header Files :doc:`Features/headers`
- Regular Python (thats right: regular python is 100% compatible! See :doc:`Features/index` for more info)

❌ The `repy` command **does** not processes the following features:

-  Runtime execution (use :doc:`repycl <reference/repycl>` for that)

⚠️ The `repy` command **will** process the following features, but the compiled python will depend on the ``restructuredpython`` module to be installed.

- <OPTIMIZE ...> markers

---

.. CLI Options
.. -----------

.. Optional arguments:

.. - ``-o <file>`` or ``--output <file>``  
..   Output path for the compiled `.py` file.

.. - ``--check``  
..   Run syntax checks only; no output file is created.

.. - ``--mode classic|strict``  
..   Choose a parsing mode (defaults to `classic`).

.. Example:

.. .. code-block:: shell

..    repy my_code.repy --output compiled.py --mode strict

.. ---

When to Use repy vs repycl
---------------------------

Use ``repy`` when:

- You just want to compile `.repy` to `.py`
- You're integrating with another Python toolchain
- You're distributing `.py` files

Use ``repycl`` when:

- You want to compile and run in one step
- You depend on runtime features like optimizations
- You're using features that need <...> markers (eg. <OPTIMIZE ...>, and don't want to compile

See also: :doc:`repycl <repycl>`
