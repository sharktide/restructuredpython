Header Files
============

    reStructuredPython offers a new and exciting feature not present in regular python. The addition of header files, written in a ``.cdata`` or ``.repy`` file extension are regular ``.repy`` files written in reStructuredPython that are compiled and automatically prepended in the final compilation of a ``.repy`` file.

    Example usage:

    .. code-block:: repy

        include 'path/to/my/file.repy'

        afunctiondefinedintheheaderfile()

    ``file.cdata``:

    .. code-block:: repy

        def afunctiondefinedintheheaderfile() {
            print('This function was made in a header file')
        }
    
    Result:

    .. code-block:: python

        def afunctiondefinedintheheaderfile() :
            print('This function was made in a header file')

        afunctiondefinedintheheaderfile()
