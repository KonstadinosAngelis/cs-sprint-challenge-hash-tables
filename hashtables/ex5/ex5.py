def finder(files, queries):
    cache = {}

    for idx, e in enumerate(files):
        output = e.split("/")

        if output[-1] in cache:
            cache[output[-1]].append(files[idx]) 
        else:
            cache[output[-1]] = [files[idx]]

    outputArr = []
    for e in queries:
        if e in cache:
            for t in cache[e]:
                outputArr.append(t)
    return outputArr


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz',
        '/test/EF/foo'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
