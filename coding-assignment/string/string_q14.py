#Remove duplicate characters from a string.
string = "programming"
result = ''.join(sorted(set(string), key=string.index))
print(result)
