class Queue():
    q = []

    def enque(self, val):
        self.q.append(val)
        print(self.q)

    def deque(self):
        self.q.pop(0)
        print(self.q)

    def clear(self):
        self.q.clear()
        print(self.q)


Q = Queue()
op = None
while op != "0":
    print("1: Enqueue  2: Dequeue  3:Clear  0: Exit")
    op = input("enter Your option : ")
    if op == "1":
        Q.enque(input("Enter the data : "))
    elif op == "2":
        Q.deque()
    elif op == "3":
        Q.clear()
    elif op != 0:
        print("invalid entry !")
else:
    print("exited ......")
