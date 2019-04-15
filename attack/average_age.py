from functools import reduce


def alpha(nameAgeList):
    ageMap = map(lambda args: (args[1], 1), nameAgeList)
    addedAgeTuple = reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]),
                           ageMap)  # In Python 2, the map() built-in function returns an iterator https://thepythonguru.com/python-builtin-functions/map/
    # In Python 2, the map()  function returns a list instead of an iterator (which is not very efficient in terms of memory consumption), so we don’t need to wrap map()  in a list()  call.
    averageAge = addedAgeTuple[0] / addedAgeTuple[1]
    return averageAge

# nameAgeList = [("Alice", 10),("Alice", 15),("Bob", 30)]
# averageAge=alpha(nameAgeList)
# print ("asdas" + str(averageAge))

# #why does the line below work? There are three basic sequence types: lists, tuples, and range objects.
# print("reducing a pair works", reduce(lambda x,y: (x+y), (5, 25)))
