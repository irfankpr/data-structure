class node:
    def __init__(self, data):
        self.pre = None
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prntList(self):
        if self.head is None:
            print("empty")
        else:
            n = self.head
            print("\nList : [ ", end="")
            while n is not None:
                print(n.data, ", ", end="")
                n = n.next
            print(" ]\n")

    def create(self, arry):
        for i in arry:
            self.ADDend(i)
        print("------ > new list initialised : ", end="")
        a.prntList()

    def ADDbegn(self, data):
        newNode = node(data)
        self.head.pre = newNode
        newNode.next = self.head
        self.head = newNode
        print("--------> new node added at begning :", data)

    def ADDend(self, data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
        else:
            N = self.head
            while N.next is not None:
                N = N.next
            N.next = newnode
            newnode.pre = N

    def ADDbyVal(self, val, data):
        if self.head is None:
            print("Linked list is empty")
        else:
            N = self.head
            while N.data != val:
                if N.next == None:
                    print("------------ >there is no node", val, "in list")
                    break
                else:
                    N = N.next
            else:
                if N.next == None:
                    self.ADDend(data)
                else:
                    newnode = node(data)
                    pre = N
                    next = N.next
                    pre.next = newnode
                    newnode.pre = pre
                    newnode.next = next
                    next.pre = newnode

    def ADDbyIndex(self, index, data):
        if self.head is None:
            print("---------- > The list is empty")
        elif index == 0:
            newnode = node(data)
            newnode.next = self.head
            self.head.pre = newnode
            self.head = newnode
            print("------------ >new node added at index ", index)
        else:
            N = self.head
            No = 0
            while N is not None:
                if No == index:
                    pre = N.pre
                    next = N
                    newnode = node(data)
                    pre.next = newnode
                    newnode.pre = pre
                    newnode.next = next
                    next.pre = newnode
                    print("------------ >new node added at index ", index)
                    break
                else:
                    No += 1
                    N = N.next
            else:
                print("-------- > list only have index of : ", No)

    def del_by_val(self, val):
        if self.head.data == val:
            d = self.head
            self.head = self.head.next
            self.head.pre = None
            del d
        else:
            N = self.head
            while N is not None:
                if N.data == val:
                    next = N.next
                    pre = N.pre
                    pre.next = next
                    if next is not None:
                        next.pre = pre
                    break
                else:
                    N = N.next
            else:
                print("there is no node ", val, "in list")
        print("------- > Value ", val, "delted from list")

    def del_by_index(self, index):
        if index == 0:
            d = self.head
            self.head = self.head.next
            self.head.pre = None
            del d
        else:
            No = 0
            N = self.head
            while N is not None:
                if No == index:
                    pre = N.pre
                    next = N.next
                    pre.next=next
                    if next is not None:
                        next.pre=pre

                    print("-------- >value deleted aT index", index, )
                    del N
                    break
                else:
                    N = N.next
                    No += 1
            else:
                print("list onlu have index of : ", No)


print("enter 5 elements to initialise an linked list")
ary = []
for i in range(0, 5):
    ary.append(input())
a = LinkedList()
a.create(ary)
print(
    '\n1: APPEND AN NODE\n2: ADD AT BEGNING\n3: ADD AFTER A NODE\n4:ADD BY INDEX\n5: DELETE BY NODE\n6:DELETE BY INDEX\n7: EXIT')
opt = int(input("\n ----> Select your option :"))
while opt != 7:
    if opt == 1:
        a.ADDend(input("--> Enter the value : "))
    elif opt == 2:
        a.ADDbegn(input("--> Enter the value : "))
    elif opt == 3:
        a.ADDbyVal(input("--> Enter the node : "), input("--> Enter the value : "))
    elif opt == 4:
        a.ADDbyIndex(int(input("--> Enter the index : ")), input("--> Enter the value : "))
    elif opt == 5:
        a.del_by_val(input("--> Enter the node : "))
    elif opt == 6:
        a.del_by_index(int(input("--> Enter the index : ")))
    else:
        print("\n>>>>>>>> Invalid opction <<<<<<<<<<<")
    a.prntList()
    print(
        '1: APPEND AN NODE\n2: ADD AT BEGNING\n3: ADD AFTER A VALUE\n4: ADD BY INDEX\n5: DELETE BY VALUE\n6: DELETE BY INDEX\n7: EXIT')
    opt = int(input("\n ----> Select your option :"))
else:
    print("\n>>>>>>>>>>>>>>  EXITED  <<<<<<<<<<<<<")
