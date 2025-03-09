reStructuredPython 0.4.0
=========================

The all in one, new python.
reStructuredPython aka 'rePython' is a version of Python with JavaScript-like syntax for a cleaner, easier-to-read text that compiles into Python.

To download the reStructuredPython compiler using the Python package index:

.. code-block:: shell

    pip install --upgrade restructuredpython

Download our vscode extension `from the Visual Studio marketplace <https://marketplace.visualstudio.com/items?itemName=RihaanMeher.restructuredpython>`_.

To use the reStructuredPython compiler:

.. code-block:: shell

    repy path/to/your/file.repy

It is that simple!

reStructuredPython code is written in a file extension .repy.  
Intellisense features are coming soon!

Differences from Python
======================

Control statements now use curly brackets like this:

.. code-block:: repy

    x = int(input('gimme a num'))
    if x == 2 {
        print("x is 2!")
        if (input("say 'yes'") == 'yes') {
            print('Hi')
        }
    } 
    elif x < 2 {
        print("x is less than 2!")
    } 
    else {
        print("x is greater than 2!")
    }

    for i in range(10) {
        print(i)
    }

    def my_function(param) {
        return param
    }

Compiles into:

.. code-block:: python

    x = int(input('gimme a num'))
    if x == 2 :
        print("x is 2!")
        if (input("say 'yes'") == 'yes') :
            print('Hi')
    
    elif x < 2 :
        print("x is less than 2!")
    
    else:
        print("x is greater than 2!")


    for i in range(10) :
        print(i)


    def my_function(param) :
        return param

View the ``tests/*`` folder for more examples.

Please contribute and raise issues! We just started and this is a pioneering project.

Changelog
=========
View the changelog at `https://github.com/sharktide/repython/blob/main/CHANGELOG.md <https://github.com/sharktide/repython/blob/main/CHANGELOG.md>`_.

Common mistakes
===============
These mistakes will result in a syntax error thrown by the REPY compiler or invalid Python.  
View the ``ERRORS.md`` file at `https://github.com/sharktide/repython/blob/main/errors.md <https://github.com/sharktide/repython/blob/main/errors.md>`_.
