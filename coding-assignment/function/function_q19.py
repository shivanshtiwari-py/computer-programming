#Write a function second_largest(lst) that returns the second largest element in a list.
def second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) > 1 else None
