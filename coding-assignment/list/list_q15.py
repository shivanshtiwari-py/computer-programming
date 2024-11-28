#Write a function rotate_list(lst, k) that rotates a list k positions to the right.
def rotate_list(lst, k):
    k %= len(lst)  # To handle k > len(lst)
    return lst[-k:] + lst[:-k]
