"""
#Q1
s=input("Enter a string ")
i=0
while i<len(s):
    if (s[i]>'Z' and s[i]<'a') or s[i]<'A' or s[i]>'z':
        print("no")
        break
    i+=1
else:
    print("yes")


#Q2

s1=input("Enter a string ")
a=input("Enter a character ")
if a in s1:
    print("yes")
else:
    print("No")
   

#Q3

s1=input("Enter a string ")
a=['a','e','i','o','u']
i=0
for e in a:
    if e in s1:
        i+=1
        print("Yes")
        break
if i==0:
    print("no")

#Q4
s1=input("Enter a string ")
i=0
b=0
a=0
while i<len(s1):
    if s1[i]==' ':
        a=0
        i+=1
        continue
    else:
        if a==0:
            b+=1
        a+=1
        i+=1
print("total no of words is",b)

#Q5

s1=input("Enter a string ")
i=0
j=len(s1)-1
while i<=len(s1)//2:
    a=s1[i]
    s1[i]=s1[j]
    s1[j]=a
    i+=1
    j-=1
print(s1)


#Q1
s1=input("Enter a string ")
a1=''.join([chr(e) for e in range(97,123)])
a2=''.join(chr(e) for e in range(65,91))
a=a1+a2
print(a)
for e in s1:
    if e not in a:
        print("Strings has non alphabet character ")
        break
else:
    print("String has only alphabet characters")




#Q2



s1=input("Enter a string ")
a="aeiouAEIOU"
i=0
for e in s1:
    if e in a:
        i+=1

print(i)

s1=input("Enter a string ")
print("Word count=",len(s1.split(" ")))
"""
#Q5
s1=input("Enter a string ")
print(s1[::-1])



