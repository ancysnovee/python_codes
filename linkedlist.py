class node:
    def __init__(self,data):
        self.data=data
        self.link=None

class sll:
    def __init__(self):
        self.head=None

    def add_begin(self,data):
        new_node=node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.link = self.head
            self.head = new_node

    def add_end(self,data):
        new_node = node(data)
        n=self.head
        while n.link is not None:
            n=n.link

        n.link = new_node

    def add_after(self,data,x):
        new_node=node(data)
        n=self.head
        while n is not None:
            if n.data==x:
                break
            n=n.link

        if n is None:
            print("node is not presrnt")
        else:

            new_node.link=n.link
            n.link=new_node
        
    def add_before(self,data,x):
        new_node=node(data)
        n=self.head
        if x==self.head.data:
            return self.add_begin(data)
        
        while n is not None:
            if n.link.data==x:
                break
            n=n.link
        new_node.link=n.link
        n.link=new_node
        


    def printll(self):
        if self.head is None:
            print("linked list is empty")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end = " ")
                n=n.link
            print("none")


n1=sll()
n1.add_begin(49)
n1.add_begin(34)

n1.add_end(67)
n1.add_after(89,67)

n1.add_before(11,34)

n1.printll()
