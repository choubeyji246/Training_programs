# day5 pizza service program

"""class Customer:
    def validate_quantity(self, quantity):
        if quantity >= 1 and quantity <= 5:
            return True
        else:
            return False

class PizzaService:
    counter = 100
    
    def __init__(self, pizza_type, quantity, additional_topping):
        self.pizza_type = pizza_type
        self.quantity = quantity
        self.additional_topping = additional_topping
        self.pizza_cost = -1
        
    def validate_pizza_type(self):
        if self.pizza_type.lower() == "small" or self.pizza_type.lower() == "medium":
            return True
        else:
            return False
    
    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and Customer().validate_quantity(self.quantity):
            pizza_cost_table = {"small": 150, "medium": 200}
            additional_topping_cost_table = {"small": 35, "medium": 50}
            
            pizza_cost = pizza_cost_table[self.pizza_type.lower()] * self.quantity
            if self.additional_topping:
                pizza_cost += additional_topping_cost_table[self.pizza_type.lower()] * self.quantity
                
            self.pizza_cost = pizza_cost
            self.service_id = self.pizza_type[0].upper() + str(PizzaService.counter + 1)
            PizzaService.counter += 1
            return self.pizza_cost
        else:
            self.pizza_cost = -1
            return self.pizza_cost
    
class DoorDelivery(PizzaService):
    def __init__(self, pizza_type, quantity, additional_topping, distance_in_kms):
        super().__init__(pizza_type, quantity, additional_topping)
        self.distance_in_kms = distance_in_kms
        
    def validate_distance_in_kms(self):
        if self.distance_in_kms >= 1 and self.distance_in_kms <= 10:
            return True
        else:
            return False
        
    def calculate_pizza_cost(self):
        if super().calculate_pizza_cost() != -1 and self.validate_distance_in_kms():
            delivery_charge_table = {1: 5, 6: 7}
            
            if self.distance_in_kms <= 5:
                self.pizza_cost += delivery_charge_table[1] * self.quantity
            else:
                self.pizza_cost += delivery_charge_table[1] * self.quantity
                self.pizza_cost += delivery_charge_table[6] * (self.distance_in_kms - 5) * self.quantity
                
        else:
            self.pizza_cost = -1

pizza_service = PizzaService("Small", 3, True)
pizza_service.calculate_pizza_cost()
print("Service ID:", pizza_service.service_id)
print("Pizza cost:", pizza_service.pizza_cost)

door_delivery = DoorDelivery("Medium", 2, False, 8)
door_delivery.calculate_pizza_cost()
print("Service ID:", door_delivery.service_id)
print("Pizza cost:", door_delivery.pizza_cost)"""






"""#bank question

class overDraw(Exception):
    pass
class limit(Exception):
    pass


class customer:
    def __init__(self,customer_id, customer_name, age, account):
        self.customer_id=customer_id
        self.customer_name=customer_name
        self.age=age
        self.account=account
    def withdraw(self, amount):
        try:
            if amount > self.account.balance:
                raise overDraw("Insufficient balance.")
            if self.account.balance - amount < self.account.get_min_balance():
                raise limit("Withdrawal amount will result in balance below minimum balance limit.")
        except overDraw as od:
            print(od)
        except limit as l:
            print(l)
        else:
            self.account.balance -= amount
            print(f"Withdrawal successful. Current balance: {self.account.balance}")
            PrivilegedCustomer.increase_bonus(self)
        

    def take_card(self):
        return "please take out your card"

    def get_customer_id(self):
        return self.customer_id

    def get_customer_name(self):
        return self.customer_name
        

    def get_age(self):
        return self.age

    def get_account(self):
        print(self.account.account_type)
        print(self.account.balance)
        print(self.account.min_balance)
        


class account:
    def __init__(self,account_type,balance,min_balance):
        self.account_type=account_type
        self.balance=balance
        self.min_balance=min_balance
    def get_account_type(self):
        return self.account_type

    def get_balance(self):
        return self.balance

    def get_min_balance(self):
        return self.min_balance

    def set_balance(self,balance):
        pass
        
        
    

class PrivilegedCustomer(customer):
    def __init__ (self,customer_id, customer_name, age, account, bonus_points):
        super().__init__(customer_id, customer_name, age, account)
        self.bonus_points=bonus_points
        

    def withdraw(self,amount):
        return super().withdraw(amount)
           

    def get_bonus_points(self):
        return self.bonus_points

    def increase_bonus(self):
        if self.account.get_balance()>1000:
            self.bonus_points+=10
        else:
            self.bonus_points+=2

    

withdraw=int(input("Amount: "))
account=account("Savings",10000,1000)
p1=PrivilegedCustomer(100,"Gopal",40,account,100)
print("Customer id: ",p1.get_customer_id())
print("Customer name: ",p1.get_customer_name())
print("age: ",p1.get_age())
p1.withdraw(withdraw)
print("Bonus points: ",p1.get_bonus_points())
print("Account Type: ",p1.account.get_account_type())
print("Account balance: ",p1.account.get_balance())
print(p1.take_card())"""









































