#!/usr/bin/python
from collections import deque
class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BST():
    def __init__(self,head  = None):
        self.head = None
        self.d = deque()
        self.s1 = []
        self.s2 = [] 
    def insert(self,node):
        if self.head is None:
            self.head = node
            print "inserting head as %s"%self.head
        else:
            self.balance(node,self.head)
   
    def balance(self,node,root):
        print "node is %s and root.data is %s" %(node.data,root.data)        
        if node.data < root.data:
            if root.left is None:
                print "going left"
                root.left = node
                return
            else:
                #"in else loop for left insert"
                self.balance(node,root.left)
        else:
            if root.right is None:
                print "trying right" 
                root.right = node
                return
            else:
                print "in else loop for right"
                self.balance(node,root.right)

             
    def inorder(self,root):
        if root is None:
            return
        else:
           # print "node is %s " %(root.data) 
            self.inorder(root.left)
            print root.data
            self.inorder(root.right) 
    
    def preorder(self,root):
        if root is None:
            return
        else:
            print root.data 
            self.preorder(root.left)
            self.preorder(root.right)
            


    def postorder(self,root):
        if root is None:
            return
        else:
            self.postorder(root.left)
            self.postorder(root.right)
            print root.data
    
    def bfs(self,root):
        if root is None: 
            if len(self.d) == 0:
                return
            else:
                next = self.d.popleft()
                self.bfs(next)

        else:
            print root.data
            self.d.append(root.left)
            self.d.append(root.right)
            #print len(self.d),self.d
            next = self.d.popleft()
            self.bfs(next)

    def push(self,root,flag):
        if  root is not None:
            if flag == "left":
                if root.right is not None:
                    self.s1.append(root.right)
                if root.left is not None:
                    self.s1.append(root.left)
            else:
                if root.left is not None:
                    self.s2.append(root.left)
                if root.right is not None:
                    self.s2.append(root.right)

    def zigzag(self,root):
        if root is not None:
            print root.data
            self.push(root,"left")
            while len(self.s1) != 0 or len(self.s2) !=0:
                while len(self.s1) !=0:
                    next1 = self.s1.pop()
                    print next1.data
                    self.push(next1,"right")
                while len(self.s2) != 0:
                    next2 = self.s2.pop()
                    print next2.data
                    self.push(next2,"left")
            
            

            



ar = [6,2,-1,7,-4,3,5,9,8]
b = BST()
for a in ar:
    n = Node(a)
    #print n 
    b.insert(n)
print "inorder: "
b.inorder(b.head)
print "pre order:"
b.preorder(b.head)
print "post order:"
b.postorder(b.head)
print "bfs" 
b.bfs(b.head) 
print "zigzag"
b.zigzag(b.head)       
