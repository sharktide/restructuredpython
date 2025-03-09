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
