
#matrix

"""mat=[[1,2,3,4],[4,6,7,8,],[9,10,11,12],[13,14,15,16]]
for i in range(len(mat)):
    for j in range(len(mat)):
        if mat[i][j]%2!=0:
            mat[i][j]=mat[i][j]**2
        else:
            mat[i][j]=mat[i][j]**3
print(mat)"""


"""mat=[[1,2,3,4],[4,6,7,8,],[9,10,11,12],[13,14,15,16]]
mat=[[mat[i][j]**2 if mat[i][j]%2!=0  else mat[i][j]**3 for j in range(len(mat))]  for i in range(len(mat))]
print(mat)"""

#paired ouputs

"""mylist=list(map(int,input().split()))
list_b=list(map(int,input().split()))
result=[]
for i in list_b:
    result.append(i)                         #or we can write as result.append((i,mylist.index(i))
    result.append(mylist.index(i))
print(result)
print([(result[i],mylist.index(i)) for i in range(0,len(result))])
print([{result[i]:mylist.index(i)} for i in range(0,len(result))])"""



#STOP WORDS

"""sentences=["a new world record was set",
           "in the holy city of ayodhya",
           "on the eve of diwali on teusday",
           "with over three lakhs diya or earthen lamps",
           "lit up simultaneously on the bank of river sarayu river"]
stopwords=["for","a","of","the","and","to","in","on","with","was"]

result=[]
for sentence in sentences:
    row_data=[]
    for word in sentence.split():
        if word not in stopwords:
            row_data.append(word)
    result.append(row_data)
print([" ".join(i) for i in result] )"""


#random qusetion from 5-8 elements
#3 2 6 5 1 4 8 9

"""lst=list(map(int,input().split()))
print(sum(lst)-sum(lst[lst.index(5):lst.index(8)+1])+int("".join(map(str,lst[lst.index(5):lst.index(8)+1]))))"""


#rotate string rhdt:246,ghfdt:1246
"""s=list(map(str,input().split(",")))
stt=[]
numm=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)
    numm.append(n)
print(stt)
print(numm)
def rotate(ss,n):
    n=list(str(n))
    s=0
    print(n)
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1]
    else:
        return ss[2:]+ss[:2]
for i in range(len(numm)):
    print(rotate(stt[i],numm[i]))"""




#sum of highest prime factors
"""import math
def hprime(n):
    l=[]
    for i in range(2,n+1):
        flag=True
        for j in range(2,int(math.sqrt(i))+1):
            if(i%j==0):
                flag=False
                break
        if flag==True:
            l.append(i)
    for i in l:
        if n%i==0:
            large=i
    return large
n=int(input())
l=[]
for i in range(n,n+9):
    l.append(hprime(i))
print(l)
print(sum(l))"""

    
    



        

    

