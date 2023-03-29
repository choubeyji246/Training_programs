#Stack
"""class stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def is_full(self):
        if self.__top==self.__max_size-1:
            return True
        return False
    def is_empty(self):
        if self.__top==-1:
            return True
        return False
    def push(self,data):
        if self.is_full():
            print("Stack is full")
        else:
            self.__top+=1
            self.__elements[self.__top]=data
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            data=self.__elements[self.__top]
            self.__top-=1

            return data

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            index=self.__top
            while index>=0:
                print(self.__elements[index])
                index-=1
    def get_max_size(self):
        return self.__max_size



ball_stack=stack(4)
print("Is stack Empty:",ball_stack.is_empty())
ball_stack.push(1)
ball_stack.push(2)
ball_stack.push(3)
ball_stack.display()
print("Is stack is full:",ball_stack.is_full())
print("The maximum size of stack is: ",ball_stack.get_max_size())
print("The element deleted is : ",ball_stack.pop())
ball_stack.display()"""




#queue
"""class queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__front=0
        self.__rear=-1
    def is_full(self):
        if self.__rear==self.__max_size-1:
            return True
        return False
    def is_empty(self):
        if self.__front>self.__rear:
            return True
        return False
    def enqueue(self,data):
        if self.is_full():
            print("queue is full")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            for i in range(self.__front,self.__rear+1):
                print(self.__elements[i])
    def get_max_size(self):
        return self.__max_size
    
queue1=queue(10)
print("Is queue empty: ",queue1.is_empty())
queue1.enqueue(100)
queue1.enqueue(200)
queue1.enqueue(300)
queue1.enqueue(400)
queue1.enqueue(500)
print("Is queue full: ",queue1.is_full())
queue1.display()
print("deleted element: ",queue1.dequeue())
queue1.display()"""




#queue problem
'''Given a queue of whole numbers. Write a python function to return a new queue which contains the evenly divisible numbers.

Note: A number is said to be evenly divisible if it is divisble by all the numbers in the given range without any reaminder.
Consider the range to be from 1 to 10 (both inclusive)
Assume that there will always be few elements in the input queue, which are evenly divisible by the  numbers in the mentioned
range.

Example:
Input Queue: 13983,10080,7113,2520,2500(front -rear)
Output Queue: 10080,2520(front-rear)'''

"""class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if (self.__max_size)-1==self.__rear:
            return True
        return False

    def is_empty(self):
        if self.__front>self.__rear:
            return True
        return False

    def enqueue(self,data):
        if self.is_full():
            print("Queue is Full!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if self.is_empty():
            print("Queue Empty!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        if self.is_empty():
            print("Queue Empty!")
        else:
            for index in range(self.__front,self.__rear+1):
                print(self.__elements[index])
n=int(input("Size of Queue:"))
ques=Queue(5)
ans=Queue(5)
print("Input Queue:")
size=n
while(size):
    ques.enqueue(int(input()))
    size-=1
for i in range(n):
    data=ques.dequeue()
    for j in range(1,11):
        if data%j==0:
            continue
        break
    else:
        ans.enqueue(data)
print("Output Queue")
ans.display()"""







#two ponters for two list

"""list1=list(map(str,input().split()))
list2=list(map(str,input().split()))
list3=[]
for i in range(len(list1)):
    for j in range(len(list2)-i-1,-1,-1):
        if list2[j]=='None':
            list3.append(list1[i])
            break
        else:
            list3.append(list1[i]+list2[j])
            break
print(" ".join(list3))"""






#merging two queues
"""class queue:
    def __init__(self,max_size):
        self.max_size=max_size
        self.elements=[None]*max_size
        self.front=0
        self.rear=-1
    def get_len(self):
        return self.max_size
    def is_full(self):
        if self.rear==self.max_size-1:
            return True
        return False
    def is_empty(self):
        if self.rear==-1:
            return True
        return False
    def enqueue(self,data):
        if self.is_full():
            print("Queue is empty")
        else:
            self.rear+=1
            self.elements[self.rear]=data
    def dequeue(self):
        if self.is_empty():
            print("Queue Empty!")
        else:
            data=self.elements[self.front]
            self.front+=1
            return data
    def display(self):
        for i in range(self.front,self.rear+1):
            print(self.elements[i],end=",")




l1=list(input().split())
l2=list(input().split())

q1=queue(len(l1))
q2=queue(len(l2))
for i in l1:
    q1.enqueue(i)
for i in l2:
    q2.enqueue(i)
q3=queue(len(l1)+len(l2))
c=0
for i in range(len(l1)+len(l2)):
    if i%2==0 and c<q1.get_len():
        q3.enqueue(q1.dequeue())
        c+=1
    else:
        q3.enqueue(q2.dequeue())
q3.display()"""





        
    






            







































        
