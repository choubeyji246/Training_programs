"""class queue:
    def __init__(self,size):
        self.front=0
        self.rear=-1
        self.size=size
        self.elements=[None]*size
    def enqueue(self,data):
        if self.rear == self.size-1:
            print("Queue is full")
        else:
            self.rear+=1
            self.elements[self.rear]=int(data)
    def dequeue(self):
        if self.front>self.rear:
            print("Queue is empty")
            return
        else:
            value=self.elements[self.front]
            self.front+=1
            return value
    def display(self):
        for i in range(self.front,self.rear+1):
            print(self.elements[i])
    def count_ele(self):
        c=0
        for i in range(self.front,self.rear+1):
            c+=1
        return c
            
print("Enter the required size")
size=int(input())
q=queue(size)
#list(map(q.enqueue,input().split()))
#[q.enqueue(input()) for i in range(size)]
qo=queue(size)
qe=queue(size)
q.display()
print("length of queue: ",q.count_ele())
i=0
length=q.count_ele()
while i<length:
    n=q.dequeue()
    if n%2==0:
        qe.enqueue(n)
    else:
        qo.enqueue(n)
    i+=1
print("even queue")
qe.display()
print("Odd queue")
qo.display()"""







'''Write a python function which accepts two linked lists containing integer data and an integer ,n merges the two linked
lists, such that list2 is merged with list1 after n number of nodes.
Assume that value of n will always be less than or equal to the number of nodes in list 1

Sample Input                       Expected Output
list1                              1->2->4->3->5
list2                              9->8->11
n - 2                              1->2->9->8->11->4->3->5 '''





"""def merger(ll1,ll2,n):
    itr1=ll1.head
    c=1
    while c<n:
        c+=1
        itr1=itr1.nxt
    temp=itr1.nxt
    itr1.nxt=ll2.head
    itr2=ll2.head
    while itr2.nxt:
        itr2=itr2.nxt
    itr2.nxt=temp
    return ll1
    

class Node:
    def __init__(self,data,next):
        self.data=data
        self.nxt=next
class linkedList:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        if self.head is None:
            self.head=Node(int(data),None)
            return
        itr=self.head
        while itr.nxt:
            itr=itr.nxt
        itr.nxt=Node(int(data),None)
    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return
        else:
            itr=self.head
            llstr=" "
            while itr:
                llstr+=str(itr.data)+"---->"
                itr=itr.nxt
        print(llstr)
            
    
            
        
ll1=linkedList()
ll2=linkedList()
list(map(ll1.insert_end,input().split()))
list(map(ll2.insert_end,input().split()))
n=int(input())
ll1.display()
ll2.display()
ll1=merger(ll1,ll2,n)
ll1.display()"""









#replace
"""class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_end(self, data):
        if self.head is None:
            self.head = Node(int(data), None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(int(data), None)
        
    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        llstr = ""
        itr = self.head
        while itr:
            llstr += str(itr.data) + " -> "
            itr = itr.next
        print(llstr)
        
    def replace(self, n):
        if self.head is None:
            print("Linked List is empty")
            return
        
        max_ele = self.head.data
        itr = self.head
        while itr:
            if max_ele < itr.data:
                max_ele = itr.data
            itr = itr.next
        
        itr = self.head
        while itr:
            if itr.data == max_ele:
                itr.data = n
                break
            itr = itr.next
        
        
ll1 = LinkedList()
list(map(ll1.insert_end, input().split()))
n = int(input())
ll1.replace(n)
ll1.display()"""















"""#cars Problem
class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
class service:
    def __init__(self,car_lst):
        self.head=None
        self.car_lst=car_lst
    def get_car_lst(self):
        return self.car_lst
    def find_cars_by_year(year):
        
    def insert(self,data):
        if self.head is None:
            self.head=Node(data,None)
        else:
            itr=self.head
            while itr.nxt:
                itr=itr.nxt
            itr.nxt=Node(data,None)
    def add_cars(self,data):
        for i in data:
            self.insert(i)
        
    def remove_cars_from_karnataka(self):
        pass
    def display(self):
        

class car:
    def __init(self,reg,pb_yr):
        pass


car1=car("OD 14M 0908",2017)
car2=car("OD 14M 0907",2017)   
car3=car("OD 14M 0906",2017)
s=servive()
s.add_cars([car1,car2,car3])"""









''' Given a queue of numbers.Write a python function to push every second element in the queue to a stack, if it is the
triangle number of the previous element in the queue and return the stack.

The output stack should be of the same size as that of the input queue

Number d is said to be a triangle number of n,
if d = 1 + 2 + 3 + ... + (n-2) + (n-1) + n.
For example 28 is said to be the triangle number of 7,
if 1+2+3+4+5+6+7 is equal to 28

Sample Input                                        Expected Output
Input queue (front->rear)                           7,28,35,3,6,5,15,2,5
Output stack (top-> bottom)                         15,6,28'''











class queue:
    def __init__(self,size):
        self.front=0
        self.rear=-1
        self.size=size
        self.elements=[None]*size

    def enqueue(self,data):
        if self.rear == self.size-1:
            print("Queue is full")
        else:
            self.rear+=1
            self.elements[self.rear]=int(data)

    def dequeue(self):
        if self.front>self.rear:
            print("Queue is empty")
            return
        else:
            value=self.elements[self.front]
            self.front+=1
            return value

    def display(self):
        for i in range(self.front,self.rear+1):
            print(self.elements[i])

    def count_ele(self):
        c=0
        for i in range(self.front,self.rear+1):
            c+=1
        return c       

    def triangle(self):
        for i in range(self.front, self.rear):
            s = 0
            for j in range(self.elements[i]+1):
                s += j
            if s == self.elements[i+1]:
                stack.push(s)


class stack:
    def __init__(self,size):
        self.top=-1
        self.elements=[None]*size

    def push(self,data):
        self.elements.append(data)

    def pop(self):
        return self.elements.pop()

    def display(self):
        return self.elements[::-1]

print("Enter the required size")
size=int(input())
q=queue(size)
list(map(q.enqueue,input().split(",")))
q.display()
s=stack(size)
q.triangle()
s.display()



























        
