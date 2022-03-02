import copy
wordsDict = {
    "Hello": 56,
    "at" : 23 ,
    "test" : 43,
    "this" : 43,
    "who" : [56, 34, 44]
    }
otherDict = copy.deepcopy(wordsDict)
wordsDict["who"].append(100)
print(wordsDict)
