#Write a function cumulative_sum(lst) that returns a list where each element is the cumulative sum up to that index.
def cumulative_sum(lst):
    cumulative_list = []
    total = 0
    for num in lst:
        total += num
        cumulative_list.append(total)
    return cumulative_list
