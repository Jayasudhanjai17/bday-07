
"""
a=int(input("Enter the Number"))
b=int(input("Enter the Number"))
c=int(input("Enter the Number"))

ans=(a if(a>b and a>c)else(b if(b>a and b>c)else c))
print(ans)



# second program

age=int(input("Enter the age"))
if age>=18:
    print("Eligible to vote")
    
else:
    print("Not eligible to vote")
    """


# third Program -To find the sum of digit till 1 digit
"""
num=int(input("Enter the input"))
sum=0
res=0
while num>0:
    d=num%10
    print(d)
    sum+=d
    num=num/10
print(sum)    
res=sum%9
if res!=0:
    print(res)
else:
    print(9)
    """

#Second Attempt
sum=0
num=input()
for x in num:
    d=int(x)
    sum+=d
sol=sum%9
if sol!=0:
    print(sol)
else:
    print(9)

    








