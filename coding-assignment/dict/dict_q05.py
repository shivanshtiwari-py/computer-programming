# Given a dictionary, remove a key-value pair based on user input and print the updated dictionary.
example_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_remove = input("Enter the key to remove: ")
example_dict.pop(key_to_remove, None)
print(example_dict)
