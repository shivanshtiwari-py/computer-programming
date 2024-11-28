#Check if one string is a subsequence of another.
s1 = "abc"
s2 = "aebdc"
it = iter(s2)
if all(char in it for char in s1):
    print("Subsequence")
else:
    print("Not a Subsequence")
