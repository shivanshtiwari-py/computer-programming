# Write a function that takes a dictionary and a key as input, and returns the value associated with that key. If the key does not exist, return "Key not found".
def get_value(dictionary, key):
    return dictionary.get(key, "Key not found")

example_dict = {'a': 1, 'b': 2, 'c': 3}
print(get_value(example_dict, 'b'))
print(get_value(example_dict, 'd'))
