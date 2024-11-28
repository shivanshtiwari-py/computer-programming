#Write a function is_armstrong(n) that returns True if a number is an Armstrong number.
def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return n == sum(d ** len(digits) for d in digits)
