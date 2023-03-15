"""sen=input()
c=0                             
k=0
for i in sen:
    if i.isalpha():
        c=c+1
    elif i.isdigit():
        k=k+1
    else:
        continue
print(list([c,k]))"""

"""logic for above program

def func(string):
    countalpha=0
    countnum=0
    for i in string:
        if 'a'<= i<= 'z':
            countalpha+=1
        if  'A'<=i<='Z':
            countalpha+=1
        if '0'<=i<='9':
            countnum+=1
    print("number of alphabets=",countalpha)
    print("number of numbers=",countnum)
  
func("a 33 ffds 84 bc123") """



"""def pairs(lst,n):
    c=0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j] == n:
                c=c+1
    return c
        

lst=list(map(int,input().split()))
n=int(input())
print(pairs(lst,n))"""



"""sen=input()
if(len(sen)<2):
    print(-1)
else:
    print(sen[0:2]+sen[-2:])"""





"""st=input()
if st[-3:]=="ing":
    print(st+"ly")
elif len(st)<3:
    print(st)
else:
    print(st+"ing")"""


"""def check_double(n):
    c=0
    double=2*n
    print(double)
    for i in str(n):
        if i in str(double) and len(str(double))==len(str(n)):
            c+=1
    if(c==len(str(n))):
        return True
    else:
        print(c)
        return False

n=int(input())
print(check_double(n))"""



"""def more_average(marks):
    l=[]
    avg=sum(marks)/len(marks)
    for i in marks:
        if i>=avg:
            l.append(i)
    per=(len(l)/len(marks))*100
    return per

def count_marks(marks):
    l=[]
    for i in range(25):
        l.append(marks.count(i))
    return l
def sort_marks(marks):
    l=list(marks)
    l.sort()
    return l




marks=tuple(map(int,input().split()))
print(more_average(marks))
print(count_marks(marks))
print(sort_marks(marks))"""





"""def translate(dic,lst):
    for i in lst:
        print(dic[i],end=" ")
    
dic={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
lst=list(map(str,input().split()))
translate(dic,lst)"""



#subarray program

"""n1=int(input())
n2=int(input())
l=list(map(int,input().split()))
lst=[]
c=0
for i in range(len(l)+1):
    for j in range(i):
        lst.append(l[j:i])
print(lst)
for i in lst:
    if sum(i)%2!=0:
        c+=1
print(c)"""
        
    



       








