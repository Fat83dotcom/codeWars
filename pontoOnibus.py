bS = [[10, 0], [3, 5], [5, 8]]


def number(bus_stops):
    # peopleIn = 0
    # peopleOut = 0
    # for stops in bus_stops:
    #     peopleIn += stops[0]
    #     peopleOut += stops[1]
    # return peopleIn - peopleOut

    return sum(bs[0] - bs[1] for bs in bus_stops)


print(number(bS))
