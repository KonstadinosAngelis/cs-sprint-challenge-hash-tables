def has_negatives(a):
    cache = {}

    for i in a:
        if i == 0:
            pass

        if -i in cache:
            cache[-i] += 1
        else:
            cache[i] = 1      

    outputArr = []
    for e in cache.items():
        if e[1] == 2:
            if e[0] < 0:
                outputArr.append(-e[0])
            else:
                outputArr.append(e[0])
    return outputArr


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
