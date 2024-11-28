#Write a function partition_even_odd(lst) that partitions a list into two lists, one with even numbers and one with odd numbers.
def partition_even_odd(lst):
    evens = [x for x in lst if x % 2 == 0]
    odds = [x for x in lst if x % 2 != 0]
    return evens, odds
