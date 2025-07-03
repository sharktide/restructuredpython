Function Chaining
=================

    In reStructuredPython 0.7.0, a new feature called function chaning was created. You can chain functions using the ``|>`` operartor to increase readablility and efficency

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