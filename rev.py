

courses=("cse","ai","ds","eee")
tupled=courses
print(tupled.index("cse",0,2))
s="hi how are you"
s.replace('H','A')
print(s)

#string reverse

s="malaya"
s1="no idea"

print(str(reversed(s1)))
for i in s:
    print(i)
for j in range(5,0,-1):
    print(j)
    print(s[j])
    
    
    
    s="malayalam"
    s1=""

    print(str(reversed(s1)))
    for i in (0,5,1):
        print(s[i])
    for j in range(5,0,-1):
        print(s[j])
    if(s==s1):
        print("palindrome")
    else:
         print("not palindrome")