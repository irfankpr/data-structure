class node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        newnode = node(val)
        newnode.ref = self.top
        self.top = newnode

    def pop(self):
        print("Popped : ", self.top.data)
        d = self.top
        self.top = self.top.ref
        del d

    def print(self):
        s = self.top
        while s is not None:
            print(s.data,",",end="")
            s = s.ref

    def peek(self):
        print(self.top.data)


S = stack()
op = None
while op != "0":
    print("1: PUSH  2: POP  3:print  4: PEEK  0: Exit")
    op = input("enter Your option : ")
    if op == "1":
        S.push(input("Enter the data : "))
    elif op == "2":
        S.pop()
    elif op == "3":
        S.print()
    elif op == "4":
        S.peek()
    elif op != 0:
        print("invalid entry !")
else:
    print("exited ......")
