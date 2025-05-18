decorators.memoization
======================

If a function is called repeatedly with the same arguments, this decorator will not run the funciton and check in its cache if the result already exists and return that.

Main use: Preformance

How to include:

.. code-block:: repy

    include 'decorators.memoization'

    @logging
    def myfunction(*args, **kwargs) {
        result = "something"
        return result
    }

Or you could do this:

.. code-block:: repy

    include 'decorators'

    @decorators.logging
    def myfunction(*args, **kwargs) {
        result = "something"
        return result
    }