# Given a number, N. Find the sum of all the digits of N
def sumOfDigits(N):
    c = 0
    while N:
        d = N % 10
        N = N // 10
        c += d
    return c


print(sumOfDigits(123))
