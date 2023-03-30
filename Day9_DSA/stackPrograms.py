"""class Evaluate:
    def __init__(self,capacity):
        self.top=-1
        self.capacity=capacity
        self.array=[]
    def isEmpty(self):
        return True if top ==-1 else False
    def peek(self):
        return self.array[-1]
    def pop(self):
        self.top-=1
        return self.array.pop()
    def push(self,data):
        self.top+=1
        self.array.append(data)
    def evaluateExp(self,exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                val1=self.pop()
                val2=self.pop()
                self.push(str(eval(val2+i+val1)))
        return int(self.pop())
exp="231*+9-"
obj=Evaluate(len(exp))
print(obj.evaluateExp(exp))"""
             
        
