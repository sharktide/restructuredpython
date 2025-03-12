def preprocess(data) :
    return data * 2
def analyze(data) :
    return data + 3
def summarize(data) :
    return f"Result: {data}"
result = summarize(analyze(preprocess(5)))
print(result)