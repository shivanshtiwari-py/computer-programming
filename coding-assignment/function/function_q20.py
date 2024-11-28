#Write a function compound_interest(principal, rate, time) that calculates compound interest.
def compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time - principal
