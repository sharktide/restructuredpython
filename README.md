# This is reStructuredPython 2
![Publish Python Package](https://github.com/sharktide/restructuredpython/actions/workflows/publish.yml/badge.svg?branch=main)
![Latest Version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fsharktide%2Frestructuredpython%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=%24.project.version&label=Latest)
[![PyPI Downloads](https://static.pepy.tech/badge/restructuredpython/month)](https://pepy.tech/projects/restructuredpython)
![Python 3.11 3.12 3.13](https://img.shields.io/badge/Python-3.11+-orange)

The all in one, new python.
reStructuredPython aka 'rePython' is a superset of python with many new features, such as header files, similar to C and C++, Optional Javascript-like syntax with curly brackets {} around control loops, function chanining and more. All the features can be found in the syntax/feature guide of our documentation https://restructuredpython.readthedocs.io/en/latest/reference/Syntax_Guide.html

To download the reStructuredPython compiler using the python package index:

```shell
pip install --upgrade restructuredpython
```
Download our vscode extension with intellisense support [from the visual studio marketplace](https://marketplace.visualstudio.com/items?itemName=RihaanMeher.restructuredpython)

To use the reStructuredPython compiler:

```shell
repy path/to/your/file.repy
```
It is that simple!

# Basics
reStructuredPython code is written in a file extension .repy and reStructuredPython header files are written with the file extension .cdata. Functions can now be chained in a more readable syntax. Control loops an be defined with curly brackets, instead of colons. View entries 1, 2, and 3 of the [syntax guide](https://restructuredpython.readthedocs.io/en/latest/reference/Syntax_Guide.html) for more details. 

# Contributing

Please contribute and raise issues! We just started and this is a pioneering project. Fork the repository, make your changes, update the documentation in the docs/* folder, add examples (if applicable) in the tests/.repy and their compiled versions in tests/.py directory as well as in docs/source/tutorials/programs and in docs/source/tutorials/compiled_programs. Once you have ensured all features work of the compiler by test-compiling the other files in tests/.repy/*, make a pull request with the github issue number is applicable, short concise title and description of your changes. Warining: The first paragraph of the pull request description will go to be part of the changelong, so keep it short and clear. PLEASE DO NOT label your changes as a new version. That will be done manually or by a bot.

# Changelog

View the changelog at https://restructuredpython.readthedocs.io/en/latest/changelog.html

# Common mistakes

These mistakes will reslut in a syntax error thrown by the REPY compiler or invalid python.
View the error index at https://restructuredpython.readthedocs.io/en/latest/compiler/error_index/
