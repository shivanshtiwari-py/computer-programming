#Write a function common_elements(lst1, lst2) that returns a list of common elements between two lists.
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))
