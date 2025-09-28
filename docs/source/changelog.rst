Changelog
=============================

*Note: This changelog skips version 0.1.1*

Major release 2
---------------

.. raw:: html

    <details>
    <summary>2.5.0 - 2.5.1</summary>
        <details>
            <summary>2.5.0</summary>
            <ul>
                <li>Introduced &lt;OPTIMIZE&gt; markers, which allow restructuredpython code to be executed faster than cpython would normally when restructuredpython is installed.
            </ul>
        </details>
        <details>
            <summary>2.5.1</summary>
            <ul>
                <li>Add syntax guide back for SEO and clarity by @sharktide in #95</li>
                <li>Add -v and --version flags by @sharktide in #84</li>
                <li>Explicitly state <OPTIMIZE ...> on functions does nothing by @sharktide in #109</li>
            </ul>
        </details>
    </details>

    <details>
    <summary>2.4.0</summary>
        <ul>
            <li>Exposed check_syntax as public and exposed new .parse function as public</li>
        </ul>
    </details>

    <details>
    <summary>2.3.0</summary>
        <ul>
            <li>Fixed <a href="https://github.com/sharktide/restructuredpython/issues/28">#28</a>, <a href="https://github.com/sharktide/restructuredpython/issues/31">#31</a>, <a href="https://github.com/sharktide/restructuredpython/issues/32">#32</a>, <a href="https://github.com/sharktide/restructuredpython/issues/33">#33<a>, <a href="https://github.com/sharktide/restructuredpython/issues/34">#34</a></li>
            <li>Added the LICENSE file <a href="https://github.com/sharktide/restructuredpython/issues/34">#34</a></li>
            <li>Fixed random fails from .decode() <a href="https://github.com/sharktide/restructuredpython/issues/31">#31</a>
        </ul>
    </details>
    <details>
    <summary>2.2.0 - 2.2.1</summary>
        <details>
        <summary>2.2.1</summary>
            <ul>
                <li>Fixed importlib errors on newer python versions <a href="https://github.com/sharktide/restructuredpython/issues/29">#29</a></li>
            </ul>
        </details>
        <details>
        <summary>2.2.0</summary>
            <ul>
                <li>Add color to error messages using the textfmt module</li>
            </ul>
        </details>
    </details>

    <details>
    <summary>2.1.0 - 2.1.1</summary>
        <details>
            <summary>2.1.1</summary>
            <ul>
                <li>Fix <a href="https://github.com/sharktide/restructuredpython/issues/25">#25</a></li>
        </details>
        <details>
            <summary>2.1.0</summary>
            <ul>
                <li>The strict_types decorator is here! Refer to <a href="https://restructuredpython.readthedocs.io/en/latest/reference/Builtin_Decorators/strict_types.html">reference/builtin_decorators/decorators.strict_types</a> of the documentation!</li>
            </ul>
        </details>
    </details>

.. raw:: html

    <details>
    <summary>2.0.0</summary>
    <ul>
        <li>Completely overhauled the compiler's to sideload I/O operations to a .dll/.so/.dylib made with C</li>
    </ul>
    </details>

Major release 1
---------------

.. raw:: html

    <details>
    <summary>1.1.0</summary>
    <ul>
        <li>Added the repycl command, which autocompiles and launches reStructuredPython programs</li>
    </ul>
    </details>

.. raw:: html

    <details>
    <summary>1.0.0</summary>
    <ul>
        <li>Add builtin decorators. view <a href="https://restructuredpython.readthedocs.io/en/latest/reference/Builtin_Decorators.html">this page</a> for a complete list</li>
    </ul>
    </details>

Major release 0
---------------

.. raw:: html

    <details>
    <summary>0.8.0</summary>
    <ul>
        <li>Addded multiline comments similar to JavaScript using /* and */</li>
    </ul>
    </details>

.. raw:: html

    <details>
    <summary>0.7.0</summary>
    <ul>
        <li>Addded function chaining</li>
    </ul>
    </details>

.. raw:: html

    <details>
    <summary>0.6.0</summary>
    <ul>
        <li>Add support for with, match, and case statements.</li>
    </ul>
    </details>

.. raw:: html

    <details>
    <summary>0.5.0</summary>
    <ul>
        <li>Add options for using header files in python (by the ``include 'path/to/my/file.cdata``. CDATA files are regular reStructuredPython files that will be automatically added to the top of a compiled ``.repy`` file.)</li>
    </ul>
    </details>

.. raw:: html

    <details>
    <summary>0.4.0</summary>
    <ul>
        <li>Added support for class statements (Added errors REPY-0003, REPY-0004)</li>
    </ul>
    </details>

.. raw:: html

    <details>
    <summary>0.3.0</summary>
    <ul>
        <li>Remodeled the compiler to not interfere with other Python constructions or definitions such as format strings.</li>
    </ul>
    </details>

.. raw:: html

    <details>
    <summary>0.2.0</summary>
    <ul>
        <li>Added support for try and catch statements.</li>
    </ul>
    </details>

.. raw:: html

    <details>
    <summary>0.1.0</summary>
    <ul>
        <li>Created the reStructuredPython compiler! 🎉</li>
    </ul>
    </details>
