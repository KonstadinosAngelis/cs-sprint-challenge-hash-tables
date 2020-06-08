class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}

    for e in tickets:
        cache[e.source] = e.destination
    
    pointer = cache["NONE"]
    outputArr = [pointer]

    while cache[pointer] != "NONE":
        outputArr.append(cache[pointer])
        pointer = cache[pointer]

    return outputArr
