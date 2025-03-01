# rePython

The all in one python.
reStructuredPython aka 'rePython' is a version of python with javascript-like syntax for a cleaner, easier to read syntax that compiles into python. 

To use, download the REPY file in the src/ folder of this repository and put it in the root dir of your porject. To compile repy to py use the following command:

```shell
python path/to/REPY path/to/your/file.repy
```

Differences from python:

For, if, elif, else and function definitions now use curly brackets like this:

```repy
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
```
Compiles into:
```python
x = int(input('gimme a num'))
if x == 2 :
    print("x is 2!")
    if (input("say 'yes'") == 'yes') :
        print('Hi')
    
 
elif x < 2 :
    print("x is less than 2!")
 
else:
    print("x is greater than 2!")


for i in range(10) :
    print(i)


def my_function(param) :
    return param
```

Please contribute and raise issues! We just started and this is a pioneering project.