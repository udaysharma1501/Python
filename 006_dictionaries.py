'''
    changeable, unordered collection of unique key:value pairs
    fast
        becasue they use hashing, allowing us to access a value quickly
'''
capitals = {'USA':'WDC', 'India':'Delhi'}

print(capitals['India']) # key acts as an index for the data

# print(capitals['Bangladesh']) # as non existant keys throw an error, it's safer to use the get method
print(capitals.get('Bangladesh')) 

print("printing all keys: "+str(capitals.keys()))
print("printing all values: "+str(capitals.values()))

print("printing everything: "+str(capitals.items()) + "\n")

for key, value in capitals.items():
    print(key, value)

capitals.update({'Germany':'Berlin'})
print("printing everything after appending: "+str(capitals.items()) + "\n")

capitals.update({'USA':'LA'}) # can also overwrite
print("printing after overwrite: "+str(capitals.items()) + "\n")

capitals.pop('Germany') # removal upon listing of key 
print("printing after removal of germany: "+str(capitals.items()) + "\n")

capitals.clear() # to clear everything
print("printing after clearing: "+str(capitals.items()) + "\n")