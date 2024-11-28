#Write a function gcd(a, b) that returns the greatest common divisor of two numbers.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
