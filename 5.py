def subsets(lst):
    mask = 1 << len(lst)
    for i in range(mask):
        subset = []
        for j in range(len(lst)):
            if i & (1 << j):
                subset.append(lst[j])
        yield subset

from sys import stdin
exec('\n'.join(stdin))