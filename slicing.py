# slicing operation
"""s="Hello World"
print(s[0:5])
print(s[:5])
print(s[5:])"""

# varialble conversion int to float and float to int
"""f=5.8
i=int(f)
a=float(i)
print(f)
print("int=",i)
print("again float=",a)"""

# modulars and divide finding quotent and reminder
"""print(7%4)
print(7/4)"""

# odd or even no
"""a=int(input("Enter a Number"))
b=a%2
if (b==0):
    print("It is even")
else:
    print("It is odd")"""

# gratest of three number    
"""a=int(input("Enter a Number"))
b=int(input("Enter a Number"))
c=int(input("Enter a Number")) 

if a>b and a>c:
    print(a,"A is greater")

elif b>a and b>c:
    print(b,"b is greater")

else:
    print(c,"C is greater")"""

# list    
"""lis=[10,11,13,15,17,22,32,44,14,23,23,15,17,10]
print("list=",lis)
lis.append(55)
print("Edited list=",lis)

lis.clear()
print("Cleared list=",lis)

print(lis.count(15))"""

"""lis1=[1,3,5,7]
lis2=[2,4,6,8]
print(lis1+lis2)"""

# while loop
"""i=0
while (True):
    i=i+1
    print(i)
    if i==10:
        break"""

"""for i in range(100,0,-2):
    print(i,end=",")"""

# Matrix multiplication
"""matrix1=[[1,2,3],
         [4,5,6],
         [5,6,7]]

matrix2=[[1,2,3],
         [4,5,6],
         [5,6,7]]

outmatrix=[]

for i in range(3):
    for j in range(3):
        outmatrix.append(matrix1[i][j]*matrix2[i][j])
print(outmatrix)"""

# string reverse 
"""words="Hi How are you"
k=len(words)
for s in range(k-1,-1,-1):
    print(words[s])"""
    
#string is equal or not
s1=input("Enter a String 1")
s2=input("Enter a String 2")
k=len(s2)
for s in range(k-1,-1,-1):
    s3=s2[s] 
    print(s2)
if s1==s2:
    print("String is Palindrome")
else:
    print("String is not Palindrome")

