#Check if a string has all unique characters.
string = "abcdefg"
if len(string) == len(set(string)):
    print("Unique characters")
else:
    print("Duplicates exist")
