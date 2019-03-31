from functools import reduce

def alpha (nameAgeList):
    ageList = list(map(lambda args: (args[1],1), nameAgeList))
    addedAgeList = list(reduce(lambda x, y: (x[0] + y[0], x[1]+y[1]), ageList))
    averageAge=reduce(lambda sum, count: sum/count, addedAgeList)
    return averageAge

nameAgeList = [("Alice", 10),("Alice", 15),("Bob", 30)]
averageAge=alpha(nameAgeList)
print (averageAge)


