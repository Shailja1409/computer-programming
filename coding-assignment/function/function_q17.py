# Given two strings S1 and S2 as input, the task is to merge them alternatively i.e. the first character of S1 then the first character of S2 and so on till the strings end.
# NOTE: Add the whole string if other string is empty.


def merge(S1, S2):
    p = ""
    for i in range(len(S1) + len(S2)):
        if i < len(S1) and i < len(S2):
            p += S1[i]
            p += S2[i]

    if len(S1) > len(S2):
        p += S1[len(S2) :]
    elif len(S2) > len(S1):
        p += S2[len(S1) :]

    return p


print(merge("make", "noice"))
