#Write a function flatten_list(nested_lst) that flattens a list of lists into a single list.
def flatten_list(nested_lst):
    flat_list = [item for sublist in nested_lst for item in sublist]
    return flat_list
