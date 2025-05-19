Builtin Decorators
==================

This list is a complete list of decorators builtin to the reStructuredPython compiler and how to use them.

How to include a decorator/function
-----------------------------------

To include a decorator via the ``include`` keyword, simply add it to the top of your file where you would include ``cdata`` header files.

For example, to include the timer decorator, you can import it and use it like this:

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

Decorators
----------

See:

.. toctree::
   :maxdepth: 2

   access_control
   logging
   memoization
   retry
   strict_types
   timer