decorators.logging
==================

Logs all arguments passed and returned by a function

Main use: debugging

Output format:

.. code-block:: python

    print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
    result = func(*args, **kwargs)
    print(f"{func.__name__} returned {result}")

How to include:

.. code-block:: repy

    include 'decorators.logging'

    @logging
    def myfunction(*args, **kwargs) {
        pass
    }

Or you could do this:

.. code-block:: repy

    include 'decorators'

    @decorators.logging
    def myfunction(*args, **kwargs) {
        pass
    }