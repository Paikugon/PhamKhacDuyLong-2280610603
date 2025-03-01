def DelByKey(dict, key):
    if key in dict:
        del dict[key]
        return key + " has been deleted"
    else:
        return "Key not found"
    
# Test
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
key = 'b'
print(DelByKey(dict, key))
print("New dictionary:", dict)