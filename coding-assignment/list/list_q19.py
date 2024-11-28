#Write a function find_mode(lst) that returns the most frequently occurring element in a list.
from collections import Counter

def find_mode(lst):
    count = Counter(lst)
    max_frequency = max(count.values())
    mode = [key for key, value in count.items() if value == max_frequency]
    return mode[0] if len(mode) == 1 else mode
