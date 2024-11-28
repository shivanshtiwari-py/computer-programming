#Remove all punctuation from a string.
import string as str_lib
text = "Hello, world! How are you?"
result = ''.join(char for char in text if char not in str_lib.punctuation)
print(result)
