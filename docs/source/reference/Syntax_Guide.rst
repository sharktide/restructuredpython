Syntax Guide
============

reStructuredPython introduces a syntax that combines Python's functionality with JavaScript-like conventions. Below are some key syntax elements:

1. **Control Loop Syntax**

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

2. **Header Files**

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




            

    

    