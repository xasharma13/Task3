from functools import reduce
def deep_get(dictionary, keys, default=None):
return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default,   keys.split("."), dictionary)

person = {'person':{'name':{'first':'John'}}}
print (deep_get(person, "person.name.first"))
John
print (deep_get(person, "person.name.lastname"))
None
print (deep_get(person, "person.name.lastname", default="No lastname"))
No lastname
