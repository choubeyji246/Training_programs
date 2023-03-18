"""class vehicles:
    def __init__(self):
        self.__vehicle_id=None
        self.__vehicle_type=None
        self.__cost=None
    def set_att(self,vehicle_id,vehicle_type,cost):
        self.__vehicle_id=vehicle_id
        self.__vehicle_type=vehicle_type
        self.__cost=cost
    def get_amt(self):
        if self.__vehicle_type != "Two_wheeler" and self.__vehicle_type != "Four_wheeler":
            print("Invalid Type")
        elif self.__vehicle_type == "Two_wheeler":
            self.__amt=(2/100)*self.__cost
        else:
            self.__amt=(6/100)*self.__cost
        return self.__amt
    def get_type(self):
        return  self.__vehicle_type
    def get_id(self):
        return  self.__vehicle_id
        
            
v1=vehicles()
v1.set_att(101,"Two_wheeler",50000)
print("premium vehicle amt of",v1.get_type(),"is", v1.get_amt(),"with id ",v1.get_id())
v2=vehicles()
v2.set_att(1001,"Four_wheeler",500000)
print("premium vehicle amt of",v2.get_type(),"is", v2.get_amt(),"with id ",v2.get_id())"""






"""class Student:
    def __init__(self):
        self.__id=None
        self.__marks=None
        self.__age=None
    def set_att(self,sid,marks,age):
        self.__id=sid
        self.__marks=marks
        self.__age=age
    def get_id(self):
        return self.__id
    def get_marks(self):
        return self.__marks
    def get_age(self):
        return self.__age
    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False
    def validate_marks(self):
        if 0<=self.__age<=100:
            return True
        else:
            return False
    def check_qualification(self):
        if self.validate_age() and self.validate_marks():
            if self.__marks>=65:
                return True
            else:
                return False
        else:
            return False
    def select_course(self):
        if self.check_qualification():
            print("course id : 1001, 1002")
            print("fees for course id 1001: 25575\n","fees for course id 1002: 15500")
            dic={1001:25575,1002:15500}
            self.course_id=int(input("please select course id\n"))
            if self.course_id==1001:
                if self.__marks>=85:
                    self.fees=dic[self.couse_id]-((25/100)*dic[self.course_id])
                else:
                    self.fees=dic[self.course_id]
            else:
                if self.__marks>=85:
                    self.fees=dic[self.couse_id]-((25/100)*dic[self.course_id])
                else:
                    self.fees=dic[self.course_id]
        else:
            return False
            
    def get_admission(self):
        self.select_course()
    def get_course_id(self):
        return self.course_id
    def get_fees(self):
        return self.fees
    
            
s1=Student()
s1.set_att(int(input("sid")),int(input("marks")),int(input("age")))
print(s1.check_qualification())
s1.get_admission()
print("Student with id ",s1.get_id(),"got admitted in course with id ",s1.get_course_id(),"\n His fees will be ",s1.get_fees())

s2=Student()
s2.set_att(int(input("sid")),int(input("marks")),int(input("age")))
print(s2.check_qualification())

if s2.get_admission():
    print("Student with id ",s2.get_id(),"got admitted in course with id ",s2.get_course_id(),"\n His fees will be ",s2.get_fees())
else:
    print("not eligible")"""







class customer:
    def __init__(self,qty):
        self.qty=qty
        
    def validate_quantity(self):
        if 1<=self.qty<=5:
            return True
        else:
            return False
        

class pizzaservice(customer):
    counter=100      
    def __init__(self,pizza_type):
        self.pizza_type=pizza_type
    
      
    def validate_pizza_type(self):
        if self.validate_quantity(): 
            if self.pizza_type=="small" or self.pizza_type=="medium":
                return True
            else:
                return False        



    def calculate_pizza_cost(self):
        if self.pizza_type=="small":
            self.cost=150
            if bool(input("if topping required then write True else write False")):
                self.cost+=35
                pizzaservice.counter+=1
                print(self.pizza_type[0]+str(pizzaservice.counter))
                return self.cost
        elif self.pizza_type=="medium":
            self.cost=200
            if bool(input("if topping required then write True else write False")):
                self.cost+=50
                pizzaservice.counter+=1
                print(self.pizza_type[0]+str(pizzaservice.counter))
                return self.cost
        else:
            self.cost=-1
            return self.cost
        
            

class Doordelivery(pizzaservice):
    def __init__(self,type1,distance):
        super().__init__(type1)
        self.distance=distance
    def validate_distance_in_kms(self,distance):
        if 1<=self.distance<=10:
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        if self.distance <=5:
            print(super().calculate_pizza_cost()+5)
            #self.cost=self.cost+5
        else:
            print(super().calculate_pizza_cost()+7)

#p1=pizzaservice("small")
#p1.calculate_pizza_cost()
d1=Doordelivery("small",5)
d1.calculate_pizza_cost()




























































