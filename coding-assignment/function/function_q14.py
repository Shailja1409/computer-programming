# For an input year N, find whether the year is a leap or not.
def isLeap(N):
    if N % 400 == 0 or (N % 100 != 0 and N % 4 == 0):
        return 1
    else:
        return 0


print(isLeap(2024))
