# WAP to calculate factorial of any number
'''fact=1
n= int(input("Enter any number:"))
for i in range(1,n+1):
    fact=fact*i
print("Factorial is:",fact)'''
#==========================================================

# WAP to calculate Fibanocci series
'''n= int(input("Enter range:"))
f1=0
f2=1
print(f1,f2,end=' ')
for i in range(2,n):
    f3=f1+f2
    print(f3,end=' ')
    f1=f2
    f2=f3'''
#===========================================================

# WAP to find palindrome number
'''num= int(input("Enter any number:"))
rev=0
nsave=num
while num>0:
    rem= int(num%10)
    rev= int((rev*10)+rem)
    num= int(num/10)
if nsave==rev:
    print(nsave,"is palindrome number")
else:
    print(nsave,"is not palindrome number")'''
#=========================================================

# WAP to find armstrong number
'''num= int(input("Enter any number:"))
sum=0
nsave=num
while num>0:
    rem= int(num%10)
    sum= int(sum+(rem*rem*rem))
    num= int(num/10)
if nsave==sum:
    print(nsave,"is armstrong number")
else:
    print(nsave,"is not armstrong number")'''
