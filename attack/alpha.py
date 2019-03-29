
def alpha (records, reducer):
    d = {}
    for record in records:
        if record is not None:
            key, value = record
            if key in d:
                d[key].append(value)
            else:
                d[key] = [value]
    return d

#records
#.map
#{ case (n,a) => (a,1) }
#.reduce { case (x,y) => (x._1+y._1, x._2 + y._2) }
#.map
#{ case (sum,count) => sum / count }
ageList = [("Alice", 10),("Alice", 15),("Bob", 30)]
listResult= alpha(ageList, lambda x, y: x + y/2)
print("list result is ", listResult )
average = 0
for record in listResult:
    ageList = record[1]
    averagePerName=0
    for age in ageList:
        averagePerName+=averagePerName + age /2
    average += average + averagePerName
print("average age is", average)