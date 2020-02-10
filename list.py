import operator
mydict = {"a":"645", "b":"3987", "c": "093","d":"111", "e":"646", "f":" 20"}
newdict = dict(sorted(mydict.items(), key=operator.itemgetter(1), reverse=True)[:3])
print (newdict)