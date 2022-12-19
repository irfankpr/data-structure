class node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prntList(self):
        if self.head is None:
            print("empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,", ",end="")
                n = n.ref

    def create(self, arry):
        a = LinkedList()
        for i in arry:
            a.ADDend(i)
        print("------ > new list initialised")
        a.prntList()

    def ADDbegn(self, data):
        newNode = node(data)
        newNode.ref = self.head
        self.head = newNode
        print("--------> new node added at begning :", data)

    def ADDend(self, data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
        else:
            N = self.head
            while N.ref is not None:
                N = N.ref
            N.ref = newnode

    def ADDbyVal(self, data, val):
        if self.head is None:
            print("Linked list is empty")
        else:
            N = self.head
            while N.data != val:
                if N.ref == None:
                    break
                else:
                    N = N.ref
            else:
                if N.ref == None:
                    self.ADDend(data)
                else:
                    newnode = node(data)
                    ref = N.ref
                    N.ref = newnode
                    newnode.ref = ref
        print("------------ >there is no node", val, "in list")

    def ADDbyIndex(self, data, index):
        if self.head is None:
            print("---------- > The list is empty")
        elif index == 0:
            newnode = node(data)
            newnode.ref = self.head
            d = self.head
            self.head = newnode
            del d
        else:
            N = self.head
            No = 0
            while N.ref is not None:
                if No == index - 1:
                    ref = N.ref
                    newnode = node(data)
                    newnode.ref = ref
                    N.ref = newnode
                    break
                else:
                    No += 1
                    N = N.ref
            else:
                print("-------- > list onlu have index of : ", No - 1)
        print("------------ >new node added at index ", index)

    def del_by_val(self, val):
        if self.head.data == val:
            d = self.head
            self.head = self.head.ref
            del d
        else:
            N = self.head
            while N.ref is not None:
                if N.ref.data == val:
                    d = N.ref
                    N.ref = N.ref.ref
                    del d
                    break
                else:
                    N = N.ref
            else:
                print("there is no node ", val, "in list")
        print("------- > Value ", val, "delted from list")

    def del_by_index(self, index):
        if index == 0:
            d = self.head
            self.head = self.head.ref
            del d
        else:
            No = 0
            N = self.head
            while N.ref is not None:
                if No == index - 1:
                    d = N.ref
                    N.ref = N.ref.ref
                    del d
                    break
                else:
                    N = N.ref
                    No += 1
            else:
                print("list onlu have index of : ", No - 1)
        print("-------- >value deleted aT index", index, )


print("enter 5 elements to initialise an linked list")
ary=[]
for i in range(0,5):
    ary.append(input())
a=LinkedList()
a.create(ary)

print('1: APPEND AN NODE\n2: ADD AT BEGNING\n3: ADD AFTER A VALUE\n4:ADD BY INDEX\n5: DELETE BY VALUE\n6:DELETE BY INDEX')
