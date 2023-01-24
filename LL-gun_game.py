class node:
    def __init__(self, data):
        self.next = None
        self.data = data


class circle:
    def __init__(self):
        self.head = None

    def create(self, num):
        for i in range(1, num + 1):
            newnode = node(i)
            if self.head is None:
                self.head = newnode
            else:
                N = self.head
                while N.next is not None:
                    N = N.next
                N.next = newnode
            if i == num:
                newnode.next = self.head

    def fire(self,val):
        N = self.head
        while N.data != val:
            N=N.next
        while N.next is not N:
            d = N.next
            N.next = d.next
            print("firing", d.data)
            del d
            N = N.next
        else:
            print("surviver is : ", N.data)


C = circle()

C.create(int(input("Number of peoples in the circle : ")))
C.fire(int(input("who start fto fire ? : ")))
