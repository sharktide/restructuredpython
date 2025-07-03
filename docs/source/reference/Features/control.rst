Control Loop Syntax
===================

Control loops and class/function definitions/with statements etc. **MAY** use curly brackets instead of ":" like in regular Python. However, using regular python will **NOT** throw an error.

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

However, make sure not to do something like this:

.. code-block:: python

    if (condition) {
        pass
    } elif (somethingelse) {    # <--- } else or } elif or } def or } case etc. not allowed and will throw an error!
        pass
    }