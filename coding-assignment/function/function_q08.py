#Write a function count_vowels(s) that returns the count of vowels in a given string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
