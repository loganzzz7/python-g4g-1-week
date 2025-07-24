def newList(a):
    b = [0] * len(a)
    for i in range(len(a)):
        while i > 0:
            b[i] = a[i - 1] + a[i] + a[i + 1]
        else:
            b[i] = 0 + a[i] + a[i + 1]
    return b