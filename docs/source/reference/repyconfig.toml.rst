repyconfig.toml Configuration Guide
===================================

The repyconfig.toml can be used to alter the default settings of the compiler in the following scenarios:
* If it is called via ``repy path/to/repyconfig.toml``

*Note: While the repyconfig.toml does not have to be in the root directory, all paths in the file must be relative to the directory of command execution, and must follow the schema such as for relative paths:* ``./path/to/file.repy``. *No backslashes allowed*

Introduced in 1.2.0, it has a very simple schema but will be expanded on jn future versions.

Example schema:

.. code-block:: toml

    [config]
    compile = "all"
    exclude = ["./tests/*", "./docs/*"]

Explanation:

- ``compile = "all"``: Will compile all files in the root directory except those files/dirs mentioned in ``exclude``
- ``exclude = ["./tests/*", "./docs/*"]`` Will not compile these files/directories

Complete reference

Section ``config`` (1/1): Contains main information for the compiler

  Key ``compile`` (1/2) Type: str: Contains information about what files to compile

    ``"all"``: Compiles all files in the given diretory, except those listed in the key ``exclude``

  Key ``exclude`` (2/2) Type: List: A list of paths and directories to exclude.

    Written as ``["./path/to/dir/", "./path/to/file.repy", ...]``

More items coming soon.
