#Print all permutations of a string.
from itertools import permutations
string = "abc"
perm = [''.join(p) for p in permutations(string)]
print(perm)
