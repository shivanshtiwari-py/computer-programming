#Write a function is_palindrome(word) that returns True if a word is a palindrome.
def is_palindrome(word):
    return word == word[::-1]
