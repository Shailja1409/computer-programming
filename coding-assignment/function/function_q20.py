# Given an array arr containing equal number of positive and negative elements, arrange the array such that every positive element is followed by a negative element.
# Note: The relative order of positive and negative numbers should be maintained.


def arranged(arr):
    po = []
    na = []
    for i in arr:
        if i > 0:
            po.append(i)
        else:
            na.append(i)
    c = []
    for i, j in zip(po, na):
        c.append(i)
        c.append(j)

    return c


print(arranged([2, 4, -1, -6, 5, -8]))
