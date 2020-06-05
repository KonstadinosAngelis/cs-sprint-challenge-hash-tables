# Your code here



def finder(files, queries):
    cache = {}

    for idx, e in enumerate(files):
        output = e.split("/")

        if output[-1] in cache:
            cache[output[-1]][1] += 1
        else:
            cache[output[-1]] = [idx, 1]

    outputArr = []
    for e in queries:
        if e in cache:
            # print(cache[e][1])
            for t in range(cache[e][1]):
                outputArr.append(files[cache[e][0]])
    print(outputArr)
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
