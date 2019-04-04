from functools import reduce

def alpha (nameAgeList):
    ageList = map(lambda args: (args[1],1), nameAgeList)
    addedAgeList = reduce(lambda x, y: (x[0] + y[0], x[1]+y[1]), ageList)#this returns a pair
    #map of identity functions, why does the line below work? reduce a pair of numbers (5, 25s)
    averageAge = reduce(lambda sum, count: sum/count, addedAgeList)#return directly the division of the first and the second value in the list
    return averageAge

nameAgeList = [("Alice", 10),("Alice", 15),("Bob", 30)]
averageAge=alpha(nameAgeList)
print (averageAge)


