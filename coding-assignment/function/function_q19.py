# Given a queue of persons represented by an array of integers, where each person is identified by a specific integer, find the minimum kilograms of apples that need to be distributed, ensuring that each person receives 1 kilogram of apples only once.
def minimumApple(arr):
    a = list(set(arr))
    c = 0
    for i in a:
        c += 1
    return c


print(minimumApple([1, 2, 1]))
