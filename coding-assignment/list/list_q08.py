#Write a function element_frequency(lst) that returns a dictionary with the frequency of each element in a list.
def element_frequency(lst):
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency
