Multiline Comments
==================

    In reStructuredPython 0.8.0, we added multiline comments with an near identical syntax to JavaScript to make large comments in programs easier to write, a feature that python doesn't have.

    Example:

    .. code-block:: repy

        /* This is a multiline comment
        that spans multiple lines */
        if True:
            print("Hello World")
    This compiles into:

    .. code-block:: repy

        # This is a multiline comment
        # that spans multiple lines
        if True:
            print("Hello World")

    This feature is extremely useful for including documentation in files when a docstring is not wanted
