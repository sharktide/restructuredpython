Installation Guide
==================

To install and use reStructuredPython, follow the steps below:

There are two methods: Either use one of the `Installation Wizards <https://github.com/sharktide/restructuredpython/releases/v1.0.0/>`_, (Make sure to pick the right one for your system (.bat or .ps1 for windows, .sh for macOS/Linux, or .ps1 (again)/.jar if you have java or powershell installed) or follow the steps below.
1. **Install reStructuredPython:**

Open your terminal or command prompt and run the following command to install reStructuredPython using pip:

.. code-block:: shell

    pip install --upgrade restructuredpython

2. **Compile reStructuredPython Code:**

After installation, you can compile ``.repy`` files to standard Python code. Navigate to your project directory and run:

.. code-block:: shell

    repy path/to/your_file.repy

Replace ``path/to/your_file.repy`` with the path to your reStructuredPython file. This command will generate a corresponding ``.py`` file that you can execute with the standard Python interpreter.

3. (Optional) Install Visual Studio Code Extension:

For enhanced development experience, including syntax highlighting, you can install the reStructuredPython extension for Visual Studio Code from the `Visual Studio Marketplace <https://marketplace.visualstudio.com/items?itemName=RihaanMeher.restructuredpython>`_

4. Test

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

