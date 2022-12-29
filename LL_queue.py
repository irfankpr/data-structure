class node:
    def __init__(self, data):
        self.data = data
        self.back = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enque(self, val):
        if self.front is None and self.rear is None:
            newnode = node(val)
            self.front = newnode
            self.rear = newnode
        else:
            newnode = node(val)
            self.rear.back = newnode
            self.rear = newnode

    def deque(self):
        d = self.front
        print("dequeued :", d.data)
        self.front = self.front.back

    def print(self):
        n = self.front
        while n is not None:
            print(n.data, ",",end="")
            n = n.back


Q = Queue()
op = None
while op != "0":
    print("\n1: Enqueue  2: Dequeue  3:print  0: Exit")
    op = input("enter Your option : ")
    if op == "1":
        Q.enque(input("Enter the data : "))
    elif op == "2":
        Q.deque()
    elif op == "3":
        Q.print()
    elif op != 0:
        print("invalid entry !")
else:
    print("exited ......")