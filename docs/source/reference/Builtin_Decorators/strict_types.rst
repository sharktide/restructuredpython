decorators.strict_types
=======================

Allows strict type checking for functions

Example:

.. code-block:: repy

    include 'decorators.strict_types'
    @strict_types
    def add(a: int, b: int) -> int:
        return a + b

    print(add(2, 3))
    print(add(2, 'hi')) # raises an error

Or

.. code-block:: repy

    include 'decorators'
    @decorators.strict_types
    def add(a: int, b: int) -> int:
        return a + b

    print(add(2, 3))
    print(add(2, 'hi')) # raises an error

Notes: This works with the return value, and with different types of input, even though not displayed in example.