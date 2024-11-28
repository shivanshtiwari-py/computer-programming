#Write a function interleave_lists(lst1, lst2) that interleaves two lists.
def interleave_lists(lst1, lst2):
    return [item for pair in zip(lst1, lst2) for item in pair]
