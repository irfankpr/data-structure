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
            print("\nList : [ ", end="")
            while n is not None:
                print(n.data, ", ", end="")
                n = n.ref
            print(" ]\n")

    def create(self, arry):
        for i in arry:
            self.ADDend(i)
        print("------ > new list initialised : ", end="")
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

    def ADDbyVal(self, val, data):
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

    def ADDbyIndex(self, index, data):
        if self.head is None:
            print("---------- > The list is empty")
        elif index == 0:
            newnode = node(data)
            newnode.ref = self.head
            d = self.head
            print("------------ >new node added at index ", index)
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
                    print("------------ >new node added at index ", index)
                    break
                else:
                    No += 1
                    N = N.ref
            else:
                print("-------- > list only have index of : ", No)

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
                print("list onlu have index of : ", No)
        print("-------- >value deleted aT index", index, )


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
