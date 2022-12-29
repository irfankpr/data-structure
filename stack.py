class stack():
    s = []

    def __init__(self):
        self.top = -1

    def pop(self):
        print("popped : ",self.s[self.top])
        self.s.pop()
        print(self.s)
        self.top -= 1

    def push(self, val):
        self.s.append(val)
        print(self.s)
        self.top += 1

    def clear(self):
        self.s.clear()
        print(self.s)
        self.top = -1

    def peek(self):
        print(self.s[self.top])


S = stack()
op = None
while op != "0":
    print("1: PUSH  2: POP  3:Clear  4: PEEK  0: Exit")
    op = input("enter Your option : ")
    if op == "1":
        S.push(input("Enter the data : "))
    elif op == "2":
        S.pop()
    elif op == "3":
        S.clear()
    elif op == "4":
        S.peek()
    elif op != 0:
        print("invalid entry !")
else:
    print("exited ......")
