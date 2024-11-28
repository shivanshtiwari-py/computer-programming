# Count the frequency of each character in a string.
string = "hello world"
freq = {}
for char in string:
    freq[char] = freq.get(char, 0) + 1
print(freq)
