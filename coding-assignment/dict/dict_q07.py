# Given two dictionaries, merge them into a single dictionary. If there are duplicate keys, keep the value from the second dictionary.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)