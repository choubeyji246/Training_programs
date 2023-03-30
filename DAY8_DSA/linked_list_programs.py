#Remove duplicates
"""class Node:
    def __init__(self,data,next):
        self.data=data
        self.nxt=next
        
class linkedList:
    def __init__(self):
        self.head=None
   
    def insert_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.nxt:
            itr=itr.nxt

        itr.nxt=Node(data,None)


  
    def remove_duplicates(self):
        itr=self.head
        while itr.nxt:
            if itr.data == itr.nxt.data:
                itr.nxt=itr.nxt.nxt
            else:
                itr=itr.nxt
        
    def print_list(self):
        itr=self.head
        llstr=""
        while itr:
            llstr+=str(itr.data)+"--->"
            itr=itr.nxt

        print(llstr)
        




ll=linkedList()
list(map(ll.insert_end,input().split()))
ll.remove_duplicates()
ll.print_list()"""









'''Given a linked list of characters. Write a python function to return a new string that is created by appending all the 
characters given in the linked list as per the rules given below.
Rules:
Replace '*' or '/' by a single space
In case of two occurences of '*' or '/', replace those two occurences of '*' or '/', replace those two occurences by a single
space and convert the next character to upper case

Assume that
There will be not be more than two consecutives occurences of '*' or '/'
The linked list will always end with an alphabet   

Sample Input
A,n,*,/,a,p,p,l,e,*,a,/,d,a,y,*,*,k,e,e,p,s,/,*,a,/,/,d,o,c,t,o,r,*,A,w,a,y

Expected Output 
An apple a day keeps doctor away
'''     


"""class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_end(self,data):
        if self.head is None:
            node=Node(data,None)
            self.head=node
            return
        
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
            
    def print_list(self):
        itr=self.head
        llstr=""
        while itr:
            llstr+=str(itr.data)+"--->"
            itr=itr.next
        print(llstr)
    def remove_alpha(self):
        itr=self.head
        s=""
        while itr:
            if (itr.data == "/" or itr.data == "*") and (itr.next.data =="/" or itr.next.data =="*"):
                s+=" "
                itr=itr.next
            elif itr.data == "/" or itr.data == "*":
                s+=" "
            else:
                s+=itr.data
            itr=itr.next
        return s
                
            
ll=LinkedList()
list(map(ll.insert_end,input().split(",")))
ll.print_list()
print(ll.remove_alpha())"""







            




