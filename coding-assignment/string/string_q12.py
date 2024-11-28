#Find the longest word in a string.
string = "Python is a powerful programming language"
longest_word = max(string.split(), key=len)
print(longest_word)
