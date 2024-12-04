n=5
for i in range(n):
    for j in range(i + 1):
        print("*" ,end=" ")
    print()


"""n=5
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
        print()"""
    
    
"""n=5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()"""
    
    
"""n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range (i+1):
         print("*", end=" ")
         print()"""
    
         #Left pascal

"""n=int(input("enter the number of rows:"))
for i in range(n):
    print(" * "*(i+1))
for j in range(n): 
    print(" * "*(n-j-1))"""
    
        #Square(2)
    
""" n=5
for i in range(n):
    print(" * "*n)"""
   
    
         #Triangle
"""n=5
for i in range(n):
    print(" " * (n- i -1), end="")
    print(" * " * (i + 1))"""
          
          
   
         #Hourglass
         
"""def hourglass_pattern(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i)
    for i in range(2, n + 1):
        print(" " * (n - i) + "* " * i)
    
hourglass_pattern(5)"""


    #fig 1
for i in range(6):
    print(" *" * i)
#fig5
for i in range(6,-1,-1):
    print(" *" * i)
#fig3
for i in range(6):
    print(" *" * i) 
for i in range(6,-1,-1):
    print(" *" * i)
"""
for i in range(5,-1,-1):
    n="  " * i 
    a=len(n)
 
    print(n,"*"+" "*(a-5),"s")
    
for c in range(6):
    print("  " * c , "*")"""

#fig10
n=5    
for i in range(n):
    print(" *" * n)

#fig2
n=5    
for i in range(n):
    print(" " * (n -i -1),end="")
    print("* " * (i + 1))    

#fig4
n=5    
for i in range(n,-1,-1):
    print(" " * (n -i -1),end="")
    print("* " * (i + 1))

#fig11
n=5    
for i in range(n,-1,-1):
    print(" " * (n -i -1),end="")
    print("* " * (i + 1))    
n=5    
for i in range(n+1):
    print(" " * (n -i -1),end="")
    print("* " * (i + 1)) 

#fig9
n=5    
for i in range(n):
    print("  " * (n -i -1),end="")
    print(" *" * (i + 1)) 
    

"""n=5
for i in range(n):
    print("  " * (n -i -1),end="")
    print("* " * (i + 1))
n=5    
for i in range(n,-1,-1):
    print("  " * (n -i -1),end="")
    print("* " * (i + 1))"""
    

