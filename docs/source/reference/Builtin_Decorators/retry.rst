decorators.retry
================

Retry a function a set amount of times if a error occurs with a set delay.

Arguments:
.. code-block:: python
    
    retry(retries=3, delay=1)

*Defaults to 3 retries and 1 second delay.

.. code-block:: repy

    include 'decorators.retry'

    @retry(3, 1)
    def myfunction(*args, **kwargs) {
        result = "something"
        if mycondition() {
            raise SyntaxError('Retry this!')
        return result
    }

Or you could do this:

.. code-block:: repy

    include 'decorators'

    @decorators.retry(3, 1)
    def myfunction(*args, **kwargs) {
        result = "something"
        if mycondition() {
            raise SyntaxError('Retry this!')
        return result
    }