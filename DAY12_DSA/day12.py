"""#selection sort
A = [64, 25, 12, 22, 11]
for i in range(len(A)):
    min_index = i
    for j in range(i+1, len(A)):
        if A[min_index] > A[j]:
            min_index = j       
    A[i], A[min_index] = A[min_index], A[i]
print ("Sorted array")
for i in range(len(A)):
    print(A[i],end=" ")"""











"""The owner of a BakeHouse wants to keep track of the tables 
that are occupied in his cafe. Assume that there are 10 tables in his cafe numbered from 1 to 10. As and when a table is occupied, it must be added to the occupied_table_list and when a customer leaves, the corresponding table must be removed from the list.

BakeHouse
- occupied_table_list
_init_()
+ get_occupied_table_list()
+ allocate_table()
+ deallocate_table(table_number)
Write a python program to implement BakeHouse class. 
Represent occupied_table_list using an appropriate data 
structure.


Note: Table numbers should be maintained in ascending order in the occupied_table_list.


Tables should be allocated and de-allocated as mentioned in the example below:

Example: Suppose tables 1, 2, 3 and 4 are initially allocated. Now if a new customer arrives, he should be allocated table 5 and the table list should
be accordingly updated. If now customer at table 2 leaves, table list should be accordingly updated and the next new customer should be allocated table 2
as it is the first free table.


Implement the allocation logic in allocate_table() method and de-allocation logic in deallocate_table() method."""




"""class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
    
class BakeHouse:
    def __init__(self):
        self.head=None
    def get_occupied_lst(self):                 
        occupied_table_list = []
        itr = self.head
        while itr:
            occupied_table_list.append(itr.data)
            itr = itr.next
        return occupied_table_list
    def allocate_table(self):
        if self.head is None:
            self.head=Node(1,None)
        else:
            table=1
            itr=self.head
            while itr:
                if itr.data == table:
                    table+=1
                itr=itr.next
            itr=self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(table,None)
            
    def deallocate_table(self,table):
        if self.head is None:
            print("All tables are deallocated")
        elif self.head.data == table:   
            self.head = self.head.next
        else:
            itr=self.head
            while itr.next:
                if itr.next.data ==table:
                    itr.next=itr.next.next
                    break
                itr=itr.next
            
    def display_table(self):
        itr=self.head
        llstr=""
        while itr:
            llstr+=str(itr.data)+"---->"
            itr=itr.next
        print(llstr)
b=BakeHouse()
b.allocate_table()
b.allocate_table()
b.allocate_table()
b.allocate_table()
b.allocate_table()
b.display_table()
print(b.get_occupied_lst())
b.deallocate_table(2)
b.display_table()           
print(b.get_occupied_lst())"""
    
    
        







#quick sort

"""def partition(array, low, high):
	pivot = array[high]
	i = low - 1
	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	return i + 1
def quick_sort(array, low, high):
	if low < high:
		pi = partition(array, low, high)
		quick_sort(array, low, pi - 1)
		quick_sort(array, pi + 1, high)

array = [10, 7, 8, 9, 1, 5]
quick_sort(array, 0, len(array) - 1)

print(array)"""







"""Write a python program that accepts a text and displays a 
string which contains the word with the largest frequency
 in the text and the 
frequency itself separated by a space.
Rules:
The word should have the largest frequency.
In case multiple words have the same frequency, then choose 
the word that has the maximum length.
Assumptions:
The text has no special characters other than space.
The text would begin with a word and there will be only a 
single space between the words.
Perform case insensitive string comparisons wherever 
necessary."""



"""st=input().split()
dict={}
dict1={}
for i in st:
    if i not in dict:
        dict[i]=st.count(i)
#print(dict)
m=0
for i in dict:
    if dict[i]>=m:
        m=dict[i]
        dict1[i]=m
#print(dict1)
m=0 
for i in dict1:
    if len(i)>m:
        m=len(i)
for i in dict1:
    if m==len(i):
        print(i,dict[i])"""




        
    
    
    

"""Write a python function, check_anagram() which accepts two 
strings and returns True, if one string is an anagram of 
another string. 
Otherwise returns False.
The two strings are considered to be an anagram if they
 contain repeating characters but none of the characters repeat at the same position.
The length of the strings should be the same."""





"""def check_anagram(str1,str2):
    if len(str1)==len(str2):
        return False
    list1=sorted(str1)
    list2=sorted(str2)
    if list1 == list2:
        for i in range(len(str2)):
            if str1[i]==str2[i]:
                return False
        return True
    else:
        return False
str1=input()
str2=input()
print(check_anagram(str1,str2))"""








"""The number, 197, is called a circular prime because all
 rotations of the digits: 197, 971, and 719, are themselves
 prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 
13, 17, 31, 37, 71, 73, 79, and 97.

Write a python program to find and display the number of 
circular primes less than the given limit."""



"""def isPrime(n):
    for i in range(2,int((n**0.5))+1):
        if n%i == 0:
            return False
    return True

def circularPrime(n):
    c=0
    for i in range(len(str(n))):
        st=int(str(n)[i:]+str(n)[:i])
        if isPrime(st):
            c+=1
        if c==len(str(n)):
            return True
    return False
        
limit=int(input())
for i in range(2,limit+1):
    if circularPrime(i):
        print(i)"""
    
    













"""Coorg Fruit Farm is a retail chain which sells fruits grown in their orchards in Coorg, India.40 min
They want to keep track of customers who buy fruits from them and also the billing process.


Write a python program to implement the class diagram given below.

RULES TO FOLLOW
=================
Class Description:
Fruit Info class:
fruit_name_list: Static list which contains the list of fruits available
fruit_price_list: Static list which contains the price/kg of fruits
The above two lists have one-to-one correspondence, initialize it with the data given in the table
get_fruit_price(fruit_name): Accept a fruit name and return its price/kg. If fruit is not available, return -1

Fruit Name	Apple	Guava	Orange	Grape	Sweet Lime
Price per Kg	200	80	70	110	60
Purchase class:
Initialize static variable counter to 101
calculate_price(): Calculate and return total fruit price based on rules given below
For valid fruit name (hint: invoke get_fruit_price(fruit_name)),
Calculate price based on price/kg and quantity of the fruit purchased by the customer
If price/kg of the fruit is maximum among the fruits in fruit lists and quantity purchased is more than 1kg, apply 2% discount on calculated price
If price/kg of the fruit is minimum among the fruits in fruit lists and quantity purchased is 5kg or more, apply 5% discount on calculated price
If the customer is a "wholesale" customer, provide an additional 10% discount. Apply this discount on already discounted price, 
if any one of the above two points are applicable. Else apply it on calculated price
Auto-generate purchase id starting from 101 prefixed by “P”. Example – P101,P102 P103 etc.
Return final fruit price
Else, return -1.
Note:
Perform case sensitive string comparison 
There will be only one fruit with maximum price and one with minimum price

For testing:
Create objects of Customer and Purchase class
Invoke calculate_price() on Purchase object
Display the details"""

"""class fruit_info:
    def __init__(self, fruits_lst, price_lst):
        self.fruits_lst = fruits_lst
        self.price_lst = price_lst

    def get_fruit_price(self, fruit_name):
        index = self.fruits_lst.index(fruit_name)
        if index >= 0:
            return self.price_lst[index]
        else:
            return -1
    

class purchase():
    counter=101
    def __init__(self,customer,fruit_name,quantity):
        self.__purchase_id="p"+str(purchase.counter)
        purchase.counter+=1
        self.customer=customer
        self.fruit_name=fruit_name
        self.quantity=quantity
        
    
    def calculate_price(self):
        fruit_info_obj = fruit_info(['Apple', 'Guava', 'Orange', 'Grape', 'Sweet Lime'], [200, 80, 70, 110, 60])
        price = fruit_info_obj.get_fruit_price(self.fruit_name)
        if price == -1:
            return -1
        total_price = price * self.quantity
        max_price_index = fruit_info_obj.price_lst.index(max(fruit_info_obj.price_lst))
        min_price_index = fruit_info_obj.price_lst.index(min(fruit_info_obj.price_lst))
        if price == fruit_info_obj.price_lst[max_price_index] and self.quantity > 1:
            total_price *= 0.98
        elif price == fruit_info_obj.price_lst[min_price_index] and self.quantity >= 5:
            total_price *= 0.95
        if self.customer == "wholesaler":
            total_price *= 0.9
        return f"{total_price} with purchaseId {self.__purchase_id}"
        
p1 = purchase("Ankit","Apple",2)
print(p1.calculate_price())

p1 = purchase("wholesaler","Apple",2)
print(p1.calculate_price())"""











"""Write a python program to help an airport manager to generate
 few statistics based on the ticket details available for a 
day.
Go through the below program and complete it based on the comments mentioned in it.
Note: Perform case sensitive string comparisons wherever necessary.




#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number

#Global variable
ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056",
"BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]
print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
#find_passengers_per_flight()
print(sort_passenger_list())
"""





"""def find_passengers_flight(st):
    for i in ticket_list:
        if st in i:
            print(i)
def find_passengers_destination(st):
    for i in ticket_list:
        if st == i.split(":")[-2]:
            print(i)
def sort_passenger_list():
    l=[]
    for i in ticket_list:
        l.append(i.split(":")[-1])
    l.sort()
    for i in l:
        for j in ticket_list:
            if i in j:
                print(j)
                break
            
        

ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056",
"BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]
find_passengers_flight("AI")
print()
find_passengers_destination("LON")
print()
#find_passengers_per_flight()
sort_passenger_list()"""



















"""4.A teacher is conducting a camp for a group of five children.
 Based on their performance and behavior during the camp, the
 teacher rewards them with chocolates.
Write a Python function to Find the total number of chocolates
received by all the children put together.
Assume that each child is identified by an id and it is stored
 in a tuple and the number of chocolates given to each child
 is stored in a list.
The teacher also rewards a child with few extra chocolates 
for his/her best conduct during the camp.
If the number of extra chocolates is less than 1, an error 
message "Extra chocolates is less than 1", should be 
displayed.
If the given child Id is invalid, an error message 
"Child id is invalid" should be displayed. Otherwise,
 the extra chocolates 
provided for the child must be added to his/her existing 
number of chocolates and display the list containing the
 total number of chocolates received by each child.


child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

functions

calculate_total_chocolates()

reward_child(child_id_rewarded,extra_chocolates)"""


"""
def calculate_total_chocolates():
    return sum(chocolates_received)
def reward_child(child_id_rewarded,extra_chocolates):
    if child_id_rewarded not in child_id:
        print("Child_id is invalid")
    elif extra_chocolates < 1:
        print("Extra chocolates is less than 1")
    else:
        indx=child_id.index(child_id_rewarded)
        chocolates_received[indx]+=extra_chocolates
        print(chocolates_received)
        print(calculate_total_chocolates())

child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]
reward_child(30,8)"""













"""Softsytems Ltd is a private firm that provides software solutions to its customers.40 min
The management wants to calculate salary for the employees. There are two types of employees namely graduates 
who are in probation period and laterals who are experienced joiners in the company. 
Write a python program based on the class diagram given below.

RULES TO FOLLOW
===================
Class Description:
Employee class:
validate_basic_salary(): Basic salary of an employee is always more than 3000
If basic salary is valid, return true. Else return false
validate_qualification(): Employee should posses either a "Bachelors" or "Masters" degree
If qualification is valid, return true. Else return false
Graduate class:
validate_job_band(): Graduates can be in "A", "B" or "C" job band
If job band is valid, return true. Else return false
calculate_gross_salary(): Calculate gross salary
Validate basic salary, qualification and job band
If valid,
Compute gross salary as basic salary + PF+ TPI amount + incentive
    PF is 12% of basic salary
    Identify TPI amount based on cgpa
    Identify incentive based on job band. Incentive should be applied on basic
    salary (Refer tables given)
Return gross salary
Else return -1
Job Band	A	B	C	D	E	F
Incentive %	4	6	10	13	16	20

CGPA	4 to 4.25	4.26 to 4.5	4.51 to 4.75	4.76 to 5
TPI Amount	1000	1700	3200	5000
Lateral class:
validate_job_band(): Laterals can be in "D", "E" or "F" job band
If job band is valid, return true. Else return false
calculate_gross_salary(): Calculate gross salary
Validate basic salary, qualification and job band
If valid,
Compute gross salary as basic salary + PF + SME bonus + incentive
    PF is 12% of basic salary
    Identify SME bonus based on skill set
    Identify incentive based on job band. Incentive should be applied on basic salary (Refer
    tables given)
Return gross salary
Skill Set	SME Bonus
AGP	        6500
AGPT	        8200
AGDEV	        11500
Else return -1
Perform case sensitive string comparison.
For testing:
Create objects of Graduate and Lateral classes
Invoke calculate_gross_salary() on Graduate and Lateral objects
Display the details"""








"""class Employee:
    def __init__(self,salary,qualification):
        self.salary=salary
        self.qualification=qualification
    def validate_basic_salary(self,salary):
        if self.salary >3000:
            return True
        return False
    
        
    def validate_qualification(self,qualification):
        if self.qualification =="Bachelors" or self.qualification =="Masters":
            return True
        return False
        
class Graduate(Employee):
    def __init__(self,salary,band,qualification,cgpa):
        super().__init__(salary,qualification)
        self.band=band
        self.cgpa=cgpa
    def validate_job_band(self,band):
        if band == "A" or band == "B" or band == "C":
            return True
        return False
    def calculate_gross_salary(self):
        if self.validate_job_band(self.band) and self.validate_qualification(self.qualification) and self.validate_basic_salary(self.salary):
            PF=0.12*self.salary
            if 4 <= self.cgpa <= 4.25:
                tpi = 1000
            elif 4.26 <= self.cgpa <= 4.5:
                tpi = 1700
            elif 4.51 <= self.cgpa <= 4.75:
                tpi = 3200
            elif 4.76 <= self.cgpa <= 5:
                tpi = 5000
            else:
                tpi = 0
            if self.band == 'A':
                incentive = 0.04 * self.salary
            elif self.band == 'B':
                incentive = 0.06 * self.salary
            else:
                incentive = 0.10 * self.salary
            gross_salary = self.salary + PF + tpi + incentive
            return gross_salary
        else:
            return -1
            
class Lateral(Employee):
    def __init__(self,salary,band,qualification,skill_set):
        self.band=band
        self.skill_set=skill_set
        super().__init__(salary,qualification)
        
    def validate_job_band(self):
        if self.band in ["D","E","F"]:
            return True
        return False
    def calculate_gross_salary(self):
        if self.validate_basic_salary(self.salary) and self.validate_qualification(self.qualification) and self.validate_job_band():
            pf = 0.12 * self.salary
            if self.skill_set == 'AGP':
                sme_bonus = 6500
            elif self.skill_set == 'AGPT':
                sme_bonus = 8200
            elif self.skill_set == 'AGDEV':
                sme_bonus = 11500
            else:
                sme_bonus = 0
            if self.band == 'D':
                incentive = 0.13 * self.salary
            elif self.band == 'E':
                incentive = 0.16 * self.salary
            else:
                incentive = 0.20 * self.salary
            gross_salary = self.salary + pf + sme_bonus + incentive
            return gross_salary
        else:
            return -1




g=Graduate(10000,"B","Masters",4.11)
print(g.calculate_gross_salary())
l=Lateral(20000,"E","Masters","AGP")
print(l.calculate_gross_salary())"""
