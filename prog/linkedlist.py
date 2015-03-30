#!/usr/bin/python

class Node():
    def  __init__(self,data):
        self.data = data
        self.nextNode = None

class llist():
    def __init__(self,head= None):
       self.head = head


    def insert(self,node):
        if not self.head:
            self.head = node   # when the first node is being added
        else:
            node.nextNode = self.head # for the remaining nodes
            self.head = node

    def size(self):
        current = self.head
        size = 0
        while current is not None:
            size += 1
            current = current.nextNode
        return size 
    
    def delete(self,data):
        if self.head is None:
            print ("Error !! The linked list is empty")
            
        else:
            current = self.head
            previous = None
            found = False
            while not found:
                # if the node your looking for is the current node
                if current.data == data:
                    found = True               
                # if the current is None means you reached the end of the linked list and did not find the element you are looking for   
                elif current is None:
                    print("Node not in liked list")
                # you store the previous node and move current to next
                else:
                    previous = current
                    current = current.nextNode
            # if the element your searching for is the first node in the list then only head needs to be moved to next 
            if previous is None:
                self. head = current.nextNode
            # if its any other node then move the previous to current.next
            else:
                previous.nextNode = current.nextNode   


    def printlist(self):
        if  self.head is None:
             print("list is empty")
        else:
            current = self.head
            while current is not None:
                print current.data
                current = current.nextNode

         
ll = llist()
data = [1,2,3,4,5]
for d in data:
    n = Node(d)
    ll.insert(n)              
ll.printlist()
ll.delete(4)
ll.printlist()
 
