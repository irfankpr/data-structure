a = [2, 3, 1, 5, 23, 67, 4, 8, 4, 7]
i = 0
n = 0
while i < len(a) - 1:
    j = 0
    while j < len(a) - i - 1:
        if a[j] > a[j + 1]:
            b = a[j]
            a[j] = a[j + 1]
            a[j + 1] = b
        j += 1
        n += 1
    i += 1
    n += 1
print(a)
print(n)
print(len(a))
