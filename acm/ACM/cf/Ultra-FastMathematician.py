str1=input()
str2=input()
a=int(str1,2)
b=int(str2,2)
x=len(str1)
y=str(bin(a^b))[2:]
z=len(y)
y='0'*(x-z)+y;
print(y)
