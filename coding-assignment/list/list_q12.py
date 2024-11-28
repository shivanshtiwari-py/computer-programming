# Write a function remove_element(lst, value) that removes all occurrences of value from a list.
def remove_element(lst, value):
    return [x for x in lst if x != value]
