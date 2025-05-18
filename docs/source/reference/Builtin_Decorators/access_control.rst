decorators.access_control
=========================

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