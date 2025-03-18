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

This is the list of built in decorators avalible in reStructuredPython.

1. **decorators.timer**

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

2. **decorators.logging**

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

3. **decorators.memoization**

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

4. **decorators.retry**

Retry a function a set amount of times if a error occurs with a set delay.

Arguments:
.. code-block:: python
    retry(retries=3, delay=1)

*Defaults to 3 retries and 1 second delay.

.. code-block:: repy

    include 'decorators.memoization'

    @retry(3, 1)
    def myfunction(*args, **kwargs) {
        result = "something"
        return result
    }

Or you could do this:

.. code-block:: repy

    include 'decorators'

    @decorators.retry(3, 1)
    def myfunction(*args, **kwargs) {
        result = "something"
        return result
    }

5. **decorators.access_control

Allows only certain user roles to use a function

Example:

.. code-block:: repy

    include 'decorators.access_control'

    @access_control(allowed_roles=['admin', 'moderator'])
    def delete_user_account(user_role, username) {
        print(f"User '{username}' has been deleted by '{user_role}'.")

    # Simulated role-based access
    delete_user_account('admin', 'john_doe')  # This works.
    delete_user_account('guest', 'john_doe')  # This raises an exception.

.. code-block:: repy

    include 'decorators'

    @decorators.access_control(allowed_roles=['admin', 'moderator'])
    def delete_user_account(user_role, username) {
        print(f"User '{username}' has been deleted by '{user_role}'.")

    # Simulated role-based access
    delete_user_account('admin', 'john_doe')  # This works.
    delete_user_account('guest', 'john_doe')  # This raises an exception.
