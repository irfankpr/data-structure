a = []
for i in range(0, 5):
    a.append(input("Enter value : "))
a.sort()
print(a)
key = input("enter search key : ")
s = 0
e = len(a)

while s <= e:
    mid = (s + e) // 2
    if a[mid] < key:
        s = mid
    elif a[mid] > key:
        e = mid
    else:
        print("element is at : ", mid)
        break
