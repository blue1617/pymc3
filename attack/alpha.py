from functools import reduce

def alpha (nameAgeList):
    ageMap = map(lambda args: (args[1],1), nameAgeList)
    addedAgeTuple = reduce(lambda x, y: (x[0] + y[0], x[1]+y[1]), ageMap)#The map() built-in function returns an iterator https://thepythonguru.com/python-builtin-functions/map/
    #In Python 2, the map()  function returns a list instead of an iterator (which is not very efficient in terms of memory consumption), so we don’t need to wrap map()  in a list()  call.
    averageAgeIdenityMap = map(lambda args: args, addedAgeTuple)#map of identity functions
    averageAge = reduce(lambda sum, count: sum/count, averageAgeIdenityMap)
    # averageAgeIdenityMap = list(map(lambda args: args, addedAgeTuple))  # map of identity functions
    # averageAge = averageAgeIdenityMap[0]/averageAgeIdenityMap[1]# alternative return directly the division of the first and the second value in the list
    return averageAge

nameAgeList = [("Alice", 10),("Alice", 15),("Bob", 30)]
averageAge=alpha(nameAgeList)
print (averageAge)

#why does the line below work? There are three basic sequence types: lists, tuples, and range objects.
print("reducing a pair works", reduce(lambda x,y: (x+y), (5, 25)))

