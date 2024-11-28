#Write a function count_digits(n) that returns the number of digits in a number.
def count_digits(n):
    return len(str(abs(n)))
