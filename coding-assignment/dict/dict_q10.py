# Create a dictionary comprehension that maps each letter in a string to its frequency count in that string.
string = "hello world"
frequency = {char: string.count(char) for char in set(string)}
print(frequency)
