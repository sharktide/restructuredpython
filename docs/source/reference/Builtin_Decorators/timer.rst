decorators.timer
================

Times the execution of the decorated function and prints the output.

Main use: debugging.

Output format:

.. code-block:: python

    print(f"{func.__name__} took {end_time - start_time:.2f} seconds.")

How to include:

.. code-block:: repy

    include 'decorators.timer'

    @timer
    def myfunction() {
        time.sleep(1)
    }

Or you could do this:

.. code-block:: repy

    include 'decorators'

    @decorators.timer
    def myfunction() {
        pass
    }