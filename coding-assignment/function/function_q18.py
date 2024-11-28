# There is a table on which N balls are kept starting from index 1 to N in horizontal direction. Each ball is either of  red (denoted by 'R') or of blue (denoted by 'B') color. Any red ball which is placed on even indices and blue balls placed on odd indices is considered as wrongly placed. You need return the number of balls placed wrong on the table.


def countWrongPlacedBalls(s):
    c = 0
    for i in range(0, len(s)):
        if i % 2 == 0:
            if s[i] == "B":
                c += 1
        else:
            if s[i] == "R":
                c += 1
    return c


print(countWrongPlacedBalls("RBRBRRB"))
