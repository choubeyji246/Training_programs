#nearest greater palindrome

"""n=int(input())
while(True): #or for i in range(n+1,sys.maxsize)
    if str(n+1)[::-1]==str(n+1):
        print(n+1)
        break
    n=n+1"""


        
#medical speciality
"""l=list(map(str,input().split()))
dic={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
max1=0
v=""
for i in range(1,len(l),2):
    if l.count(l[i])>max1:
        max1=l.count(l[i])
        v=l[i] 
print(dic[v])"""



#common comparison
"""st1="".join(input().split()) 
st2=" ".join(input().split())
min1=min([len(st1),len(st2)])
if(len(st1)==min1):
    for i in st1:
        if i in st2:
            print(i,end="")
    else:
        print(-1)
else:
    for i in st2:
        if i in st1:
            print(i,end="")
    else:
        print(-1)"""
    


