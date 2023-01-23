a = [2, 3, 1, 5, 23, 67, 4, 8, 4, 7]
i = 0
j = 0

while i < len(a):
    j = i + 1
    while j < len(a):
        if a[i] > a[j]:
            b = a[i]
            a[i] = a[j]
            a[j] = b
        j += 1
    i += 1

print(a)
