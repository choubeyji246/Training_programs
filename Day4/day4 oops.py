"""class example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        num=num
    def get_num(self):
        return self.num
obj=example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())"""  #output= 10 10


"""class customer:
    def  __init__(self):
        cust_id=100
c1=customer()
print(c1.cust_id)"""  #output=error


"""class customer:
    def  __init__(self,id):  # output =100
        self.id=100
c1=customer(200)
print(c1.id)"""


"""class Book:
    def __init__(self):
        self.title=None
my_fav=Book()
my_fav.title="Head First Programming"
your_fav=Book()
your_fav.title="Head First Programming"

my_fav.title="Learning python"

print("My favourite is ",my_fav.title)
print("My favourite is ",your_fav.title)    output:My favourite is  Learning python
                                            My favourite is  Head First Programming"""





"""
class shoe:
    def __init__(self,price,material):
        self.price=price                         #output:<__main__.shoe object at 0x000001494E6E1C30>
        self.material=material                      #1000 canvas
s1=shoe(1000,"canvas")
print(s1)
print(s1.price,s1.material)"""


"""class shoe:
    def __init__(self,price,material):
        self.price=price                         #the unique id of object 2528679232272
        self.material=material                       
s1=shoe(1000,"canvas")
print("the unique id of object",id(s1))"""






"""class shoe:
    def __init__(self,price,material):
        self.price=price                         #shoe with price: 1000 and material: canvas
        self.material=material
        

    def __str__(self):
            return "shoe with price: "+str(self.price)+" and material: "+ self.material
            
s1=shoe(1000,"canvas")
print(s1)"""



"""class mobile:
    def __init__(self):   #------> to check wether object is created or not
        print(id(self))  
    def display(self):                                                         
        print("calculating details")
        
    def purchase(self):
        self.display()
        print("calculating price")
mobile().purchase()
mobile().purchase()  same id
m1=mobile()
m2=mobile()  different id
print(m1)
print(m2)"""






"""class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        self.total_price=None
    def purchase(self):
        if self.brand=="Apple":
            discount=10
        else:
            discount=5
        self.total_price= self.price - self.price * (discount/100)
        print("Total price of",self.brand, "mobile is", self.total_price)
    def amt_ret(self):
        return self.total_price
        
mob1=Mobile("Apple",20000)
mob2=Mobile("Samsung",10000)
mob1.purchase()
mob2.purchase()
print(mob1.amt_ret())
print(mob2.amt_ret())"""





"""class Customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id=cust_id
        self.name=name
        self.age=age
        self.__wallet_balance=wallet_balance
    def update_balance(self,amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance+=amount
    def show_balance(self):
        print("The balance is ",self.__wallet_balance)
    def getter(self):
        return self.__wallet_balance
        
c1=Customer(100, "Gopal",24,1000)
c1.update_balance(500)
c1.show_balance()
#print(c1.__wallet_balance) #it will throw an error as we have made wallet_balance as private by using __
print(c1.getter())"""




"""class Dam:
    def __init__(self,name,length):
        self.name=name
        self.__length=length
    def get_length(self):
        return self.__length

dam1=Dam("ABC dam",3.5)
print("Dam name:",dam1.name)
print("Dam Length",dam1.get_length())"""





"""class Table:
    def __init__(self):
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None
    def assign_data(self,glass_top,wooden_top):
        self.__glass_top=glass_top
        self.__wooden_top=wooden_top
    def identify_rate(self,glass_top,wooden_top):
        self.assign_data(glass_top,wooden_top)
        if(self.__glass_top==True):
            rate=20000
        elif(self.__wooden_top==True):
            rate=30000
        else:
            rate=0
        return rate
dining_table=Table()
rate=dining_table.identify_rate(False, True)
print(rate)"""








"""class Table:
    def _init_(self):
        self.no_of_legs=4
        self.glass_top=None
        self.wooden_top=None
dining_table=Table()
print(dining_table)
back_table=Table()
print(back_table)
front_table=back_table
print(front_table)
back_table=dining_table
print(back_table)
print(dining_table,back_table,front_table)"""


























        
