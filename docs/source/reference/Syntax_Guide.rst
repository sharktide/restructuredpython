Syntax Guide
============

reStructuredPython introduces a syntax that combines Python's functionality with JavaScript-like conventions. Below are some key syntax elements:

1. **Control Loop Syntax** Latest in 0.6.0

    Control loops and class/function definitions use curly brackets instead of ":" like in regular Python

   .. code-block:: repy

        x = int(input('gimme a num'))
        if x == 2 {
            print("x is 2!")
            if (input("say 'yes'") == 'yes') {
                print('Hi')
            }
        } 
        elif x < 2 {
            print("x is less than 2!")
        } 
        else {
            print("x is greater than 2!")
        }

        for i in range(10) {
            print(i)
        }

        def my_function(param) {
            return param
        }

2. **Header Files** Latest in 0.5.0

    reStructuredPython offers a new and exciting feature not present in regular python. The addition of header files, written in a ``.cdata`` file extension are regular ``.repy`` files written in reStructuredPython that are compiled and automatically included in the final compilation of a ``.repy`` file.

    Example usage:

    .. code-block:: repy

        include 'path/to/my/file.cdata'

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

3. **Function Chaining** Latest in 0.7.0

    In reStructuredPython 0.7.0, a new feature called function chaning was created. In 0.7.0, you can chain functions using the ``|>`` operartor to increase readablility and efficency

    Example:

    .. code-block:: repy

        def preprocess(data) {
            return data * 2
        }
        def analyze(data) {
            return data + 3
        }
        def summarize(data) {
            return f"Result: {data}"
        }
        result = 5 |> preprocess |> analyze |> summarize
        print(result)

    This compiles into:

    .. code-block:: python

        def preprocess(data) :
            return data * 2
        def analyze(data) :
            return data + 3
        def summarize(data) :
            return f"Result: {data}"
        result = summarize(analyze(preprocess(5)))
        print(result)

    This is best used in conjunction with header files.

4. **Multiline Comments** Latest in 0.8.0

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

    This should be pretty easy to grasp for a developer who knows the syntax of the C and JavaScript familes to use.
    This feature is also useful for including documentation in files when a docstring is too long or not an option.

            

    

    