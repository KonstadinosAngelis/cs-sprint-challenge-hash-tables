def intersection(arrays):
    cache = {}

    for a in arrays:
        for e in a:
            if e in cache:
                cache[e] += 1
            else:
                cache[e] = 1

    outputArr = []
    for i in cache.items():
        if i[1] == len(arrays):
            outputArr.append(i[0])
    return outputArr


if __name__ == "__main__":
    arrays = [[1,2,3,4,5], [12, 7, 2, 9, 1], [99, 2, 7, 1,]]
    print(intersection(arrays))
