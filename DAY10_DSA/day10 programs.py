
"""#Linear Search
def linear_search(l,length,k):
    for i in range(0,length):
        if l[i]==k:
            return i
    return -1

l=list(map(int,input().split()))
k=int(input())
result=linear_search(l,len(l),k)
if result ==-1:
    print("element not found")
else:
    print("Element found at index :",result)"""



"""#Binary search
def binary_search(l,k,low,high):
    while low<=high:
        mid=(low+high)//2
        if l[mid]==k:
            return mid
        elif l[mid]<k:
            low=mid+1
        else:
            high=mid-1
    return -1
            


l=list(map(int,input().split()))
k=int(input())
result=binary_search(l,k,0,len(l))
if result ==-1:
    print("element not found")
else:
    print("Element found at index :",result)"""




"""-----------------------------------------Tree------------------------------------------"""
#Tree Traversal Binary Tree
"""class Node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.val = item
        
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val) + "->",end='')
        inorder(root.right)
            
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) + "->",end='')
    
def preorder(root):
    if root:
        print(str(root.val) + "->",end='')
        preorder(root.left)
        preorder(root.right)
            
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Inorder traversal")
inorder(root)
print("\nPostorder traversal")
postorder(root)
print("\nPreorder traversal")
preorder(root)"""








"""#Binary search Tree
class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key) + "->",end="")
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left= insert(node.left,key)
    else:
        node.right = insert(node.right,key)
    return node
def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

def deleteNode(root,key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root

root = None
root = insert(root,8)
root = insert(root,3)
root = insert(root,1)
root = insert(root,6)
root = insert(root,7)
root = insert(root,10)
root = insert(root,14)
root = insert(root,4)

print("Inorder traversal: ", end=" ")
inorder(root)
print("\nDelete 10")
root = deleteNode(root, 10)
inorder(root)"""









"""11.A train is identified by its name and list of compartments.
The compartments are identified by its name,total seating 
capacity and the number of passengers.
Implement the class Train as given in the class diagram.
Train
- train_name
- compartment_list
_init_(train_name,compartment_list)
+ get_train_name()
+ get_compartment_list()
+ count_compartments ()
+ check_vacancy()
Write a python program to implement the following:
count_compartments()- returns the total number of compartments
 in the train
check_vacancy()-returns the count of the compartments in which
 more than 50% of the seats are vacant
Note : Compartment list is maintained as a linked list where 
data in each node refers to a compartment."""









"""class compartment:
    def __init__(self,data):
        self.data=data
        self.next=None

class CompartmentLinkedList:
    def __init__(self):
        self.head=None
    
    def insertAtEnd(self,data):
        if self.head==None:
            self.head=compartment(data)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=compartment(data)
    
    def traverseList(self):
        itr=self.head
        while itr is not None:
            print(itr.data)
            itr=itr.next
    
    def length(self):
        count=0
        itr=self.head
        while itr:
            itr=itr.next
            count+=1
        print(count)
    


class train:
    def _init_(self,name,compartmentList):
        self.name=name
        self.compartmentList=compartmentList
    
    def get_train_name(self):
        return self.name
    
    def get_compartment_list(self):
        self.compartmentLinkedList.traverseList()
    
    def count_compartments(self):
        self.compartmentList.length()

    def check_vacancy(self):
        itr=self.compartmentList.head
        counter=0
        while itr:
            temp=itr.data
            if temp[1]<0.5*temp[2]:
                counter+=1
            itr=itr.next
        print("compartments with more than 50% vacancy= ",counter)


    
compartmentList1=CompartmentLinkedList()
compartmentList1.insertAtEnd(["SL",250,400])
compartmentList1.insertAtEnd(["2AC",125,280])
compartmentList1.insertAtEnd(["3AC",120,300])
compartmentList1.insertAtEnd(["FC",160,300])
compartmentList1.insertAtEnd(["1AC",100,210])


train1=train("Express",compartmentList1)
print(train1.get_train_name())
train1.get_compartment_list()
train1.count_compartments()
train1.check_vacancy()"""









"""The central library at Mysore has a set of very interesting
 books and journals. The books are arranged in the 
alphabetical order of their author names. 
So it is very easy for the readers to search for the book.
The library has got a set of new books. The librarian wants
 to arrange them in order too. As some books are already 
arranged in the order, find a suitable way of arranging the 
new set of books amidst them.

Write a python program to arrange all the books in the 
alphabetical order of the author names.
sort_item_list_by_author(): Accepts the new list of books 
and returns it sorted in the alphabetical order of their 
author names.
add_new_items(): Accepts the new list of books, sorts it and
 merges it with the existing books in the library.
Hint - Use sort_item_list_by_author() method for sorting the 
books.
sort_items_by_published_year(): Sorts the list of books (item_list) based on the increasing order of their published years. If there are multiple items that
are published in the same year, then sort them based on the alphabetical order of their author names.
Note: While sorting the author names in alphabetical order, ignore the special characters including space, if there are any.

Library
- item_list
_init_(item_list)
+ get_item_list()
+ sort_item_list_by_author(new_item_list)
+ add_new_items(new_item_list)
+ sort_items_by_published_year()


Item
- item_name
- author_name
- published_year
_init_(item_name,author_name,published_year)
+ get_item_name()
+ get_author_name()
+ get_published_year()
_str_()





class books:
    def __init__(self,data):
        self.data=data
        self.nxt=None

class library:
    def __init__(self,item_list):
        self.head=None
        self.item_list=item_list
        if item_list:
            self.item_list=sorted(item_list,key=lambda x:x.author_name)
            
    def get_item_list(self):
        return self.item_list
    def sort_tem_list_by_author(self,new_item_list):
        item_list = self.get_item_list() + new_item_list
        item_list=sorted(item_list,key=lambda x:x.author_name)
        return item_list
        
    def add_new_items(self,new_item_list):
        if self.head is None:
            self.head=books(self.sort_tem_list_by_author(new_item_list))
        else:
            itr=self.head
            while itr.nxt:
                itr=itr.nxt
            itr.nxt=books(self.sort_tem_list_by_author(new_item_list))
        self.item_list = self.sort_items_by_published_year(self.get_item_list() + new_item_list)
    def sort_items_by_published_year(self,item_list):
        item_list=sorted(item_list,key=lambda x:x.published_year)
        return item_list
    def display_list(self):
        itr=self.head
        llstr=""
        while itr:
            llstr+=str(itr.data)+"--->"
            itr=itr.nxt
        print(llstr)

class Item:
    def __init__(self,item_name,author_name,published_year):
        self.item_name=item_name
        self.author_name=author_name
        self.published_year=published_year

    def get_item_name(self):
        return self.item_name
    def get_author_name(self):
        return self.author_name
    def get_published_year(self):
        return self.published_year
    def __str__(self):
        return f"{self.item_name} by {self.author_name}in {self.published_year}"


        

book1=Item("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book2=Item("To Kill a Mockingbird", "Harper Lee", 1960)
book3=Item("Pride and Prejudice", "Jane Austen", 1813)
book4=Item("1984", "George Orwell", 1949)

lib=library([book1,book2])
print('\n'.join(map(str, lib.get_item_list())))

lib.add_new_items([book3,book4])
print("after adding new list")
print('\n'.join(map(str, lib.get_item_list())))"""























"""The International Cricket Council (ICC) wanted to do some 
analysis of international cricket matches held in last 
10 years.

Given a list containing match details as shown below:
[match_detail1,match_detail2……]

Format of each match_detail in the list is as shown below:
country_name : championship_name : total_number_of_matches_played : number_of_matches_won
Example: AUS:CHAM:5:2 means Australia has participated in 
Champions Trophy 5 times and have won 2 times.

Write a python program which performs the following:

find_matches (country_name): Accepts the country_name and 
returns the list of details of matches played by that country.
max_wins(): Returns a dictionary containing the championship name as the key and the list of country/countries which have won the maximum number of matches
in that championship as the value.
find_winner(country1,country2): Accepts name of two countries and returns the country name which has won more number of matches in all championships.
If both have won equal number of matches, return "Tie".
Perform case sensitive string comparison wherever necessary.
match_list – ['ENG:WOR:2:0', 'AUS:CHAM:5:2', 'PAK:T20:5:1', 'AUS:WOR:2:1', 'SA:T20:5:0', 'IND:T20:5:3', 'PAK:WOR:2:0', 'SA:WOR:2:0', 'SA:CHAM:5:1', 'IND:WOR:2:1']    

Sample Input	         Expected Output
find_matches ("AUS")	['AUS:CHAM:5:2', 'AUS:WOR:2:1']
max_wins()	        {'WOR': ['AUS', 'IND'], 'CHAM': ['AUS'], 'T20': ['IND']}
find_winner("AUS","IND") IND"""









 


def find_matches(st):
    l=[]
    for i in match_list:
        if st in i:
            l.append(i)
    return l
    
def max_wins():
    max_win_dict = {}
    for i in match_list:
        country, tournament, total_matches, wins = i.split(":")
        if tournament not in max_win_dict:
            max_win_dict[tournament] = []
        max_wins = -1
        for j in match_list:
            country2, tournament2, total_matches2, wins2 = j.split(":")
            if tournament == tournament2 and int(wins2) > max_wins:
                max_wins = int(wins2)
        if int(wins) == max_wins:
            max_win_dict[tournament].append(country)
    return max_win_dict


"""l=[]
        for i in self.match_list:
            l.append(i.split(":"))
        print(l) #[['ENG', 'WOR', '2', '0'], ['AUS', 'CHAM', '5', '2'], ['PAK', 'T20', '5', '1'], ['AUS', 'WOR', '2', '1'], ['SA', 'T20', '5', '0'], ['IND', 'T20', '5', '3'], ['PAK', 'WOR', '2', '0'], ['SA', 'WOR', '2', '0'], ['SA', 'CHAM', '5', '1'], ['IND', 'WOR', '2', '1']]
        cl=[]
        for i in l:
            if i[1] not in cl:
                cl.append(i[1])
        print(cl) #['WOR', 'CHAM', 'T20']
        mw=[]
        for i in cl:
            max=0
            for j in l:
                if j[1]==i:
                    if int(j[3])>max:
                        max=int(j[3])
            mw.append(max)
        print(mw)
        d={}
        for i in range(len(cl)):
                temp=[]
                for j in l:
                    if j[1]==cl[i] and int(j[3])==mw[i]:
                        temp.append(j[0])
                # d.update({cl[i]:temp})
                d[cl[i]]=temp
        print(d)"""
        
        
        
    
def find_winner(st1,st2):
    m1=find_matches(st1)
    m2=find_matches(st2)
    s1=0
    s2=0
    for i in m1:
        s1+=int(i[-1])
    for i in m2:
        s2+=int(i[-1])
    if s1>s2:
        return m1[0][0:3]
    elif s2>s1:
        return m2[0][0:3]
    else:
        return "Tie"
        
    
    

match_list=['ENG:WOR:2:0', 'AUS:CHAM:5:2', 'PAK:T20:5:1', 'AUS:WOR:2:1', 'SA:T20:5:0', 'IND:T20:5:3', 'PAK:WOR:2:0', 'SA:WOR:2:0', 'SA:CHAM:5:1', 'IND:WOR:2:1']
print(find_matches("AUS"))
print(max_wins())
print(find_winner("AUS","IND"))











