'''def msg():
    print("Hello world")
msg()'''
#======================================================================

'''import time
def msg():
    print("Hello world")
    time.sleep(2)
msg()
print("First time call done")
msg()
print("Second time called")
msg()
print("Third time called")'''
#======================================================================

'''import time
def welcome():
    print("Welcome to python class")
print("First time call")
welcome()
time.sleep(2)
print("Second time call")
welcome()
time.sleep(2)
print("Third time call")
welcome()
print("Fourth time call")
welcome()'''
#======================================================================

'''def login():
    username= input("Enter your username:")
    password= input("Enter your password:")
    if username==password:
        print("Login successfully")
    else:
        print("You have entered wrong credentials")
login()'''
#======================================================================

'''def login():
    while True:
        username= input("Enter your username:")
        password= input("Enter your password:")
        if username==password:
            print("Login successfully")
            break
        else:
            print("You have entered wrong credentials")
login()'''
#======================================================================

'''def info(first_name,last_name):
    print("First name=",first_name)
    print("Last name=",last_name)
info("Vaibhavi","Tekade")'''
#=======================================================================

'''def add(num1,num2):
    return num1+num2
print(add(2,3))'''
#=======================================================================

'''def add(num1,num2):
    return num1+num2
result= add(2,3)
print("Result=",result)'''
#=======================================================================

'''def add(a,b):
    r= a+b
    m= a-b
    n= a*b
    p= a/b
    return r,m,n,p
result= add(10,5)
print("Result=",result)'''
#=======================================================================

'''def chk_even_odd(number):
    if number%2==0:
        print(number,"This is even number")
    else:
        print(number,"This is odd number")
chk_even_odd(5)
chk_even_odd(10)'''
#=======================================================================

'''def func(fname,lname):
    print("Hi",fname)
    print("Hi",lname)
func(fname="Vaibhavi",lname="Tekade")'''
#========================================================================

'''def add(v1,v2):
    print(v1+v2)
v1= int(input("Enter value one:"))
v2= int(input("Enter value two:"))
add(v1,v2)'''
#========================================================================

'''def add(val1,val2):
    add= val1+val2
    return add
result= add(10,11)
print("Addition of two number=",result)'''
#========================================================================

'''def func(city= "Nagpur"):
    print("I am from",city)
func("Delhi")
func("Pune")
func()'''
#=========================================================================

'''def func(**name):
    print("My name is",name["lname"])
func(fname="prashant",lname="jha")'''
#========================================================================

'''def add_product(a,b):
    add= a+b
    product= a*b
    return add,product
x,y=add_product(10,20)
print("The addition is",x)
print("The product is",y)'''
#========================================================================

'''def func(name):
    for i in name:
        print(i)
name_of_p= ["prashant","rahul","sandip","sunil"]
func(name_of_p)'''
#========================================================================

'''def func(name):
    for i in name:
        print(i)
name_of_p= ("prashant","rahul","sandip","sunil")
func(name_of_p)'''
#========================================================================

'''def func(name):
    for i in name:
        print(i)
name_of_p= {"prashant","rahul","sandip","sunil"}
func(name_of_p)'''
#=======================================================================

'''def func(name):
    for i in name:
        print(i)
name_of_p= "vaibhavi"
func(name_of_p)'''
#=======================================================================

'''def func(name):
    for i in name:
        print(i)
name_of_p= input("Enter the name:")
func(name_of_p)'''
#=======================================================================

'''def func(name):
    j=0
    for i in name:
        if i=="n":
            print("The character present inside at index no",j,"value is",name)
            break
        j=j+1
name= input("Enter the name:")
func(name)'''
#======================================================================

'''def name(*value):
    print(value)
name("ashish","prashant","sunil")'''
#======================================================================

'''def name(*value):
    print(value)
name("ashish","prashant","sunil",1001)'''
#======================================================================

'''def func():
    number= int(input("Enter any number:"))
    if number>0:
        print(number,"is positive")
    if number<0:
        print(number,"is negative")
    if number==0:
        print(number,"is zero")
func()'''
#======================================================================

'''def msg():
    age= int(input("Enter your age:"))
    if age>=18:
        print("You are eligible for license")
    else:
        print("You are not eligible")
msg()'''
#======================================================================

'''def number():
    a= int(input("Enter first number:"))
    b= int(input("Enter second number:"))
    if b>a:
        print("b is greater than a")
    elif a==b:
        print("a and b are equal")
    else:
        print("a is greater than b")
number()'''
#======================================================================

'''def func():
    a= 200
    b= 33
    c= 350
    if a>b and c>a:
        print("Both condition are true")
    else:
        print("Both are false")
func()'''
#======================================================================

'''def mark():
    p1= int(input("Enter paper1 marks:"))
    p2= int(input("Enter paper2 marks:"))
    p3= int(input("Enter paper3 marks:"))
    p4= int(input("Enter paper4 marks:"))
    p5= int(input("Enter paper5 marks:"))
    p6= int(input("Enter paper6 marks:"))
    p7= int(input("Enter paper7 marks:"))
    if p1>=40 and p2>=40 and p3>=40 and p4>=40 and p5>=40 and p6>=20 and p7>=20:
        print("You are pass")
    else:
        print("You are fail")
    total1= p6+p7
    total= p1+p2+p3+p4+p5+total1
    percentage=total/6.0
    print("Total=",total)
    print("Percentage=",percentage)
mark()'''
#======================================================================

'''def large():
    n1= int(input("Enter first number:"))
    n2= int(input("Enter second number:"))
    n3= int(input("Enter third number:"))
    n4= int(input("Enter fourth number:"))
    n5= int(input("Enter fifth number:"))
    max=n1
    if max<n2:
        max=n2
    if max<n3:
        max=n3
    if max<n4:
        max=n4
    if max<n5:
        max=n5
    print("Largest element is:",max)
large()'''
#======================================================================

'''def small():
    n1= int(input("Enter first number:"))
    n2= int(input("Enter second number:"))
    n3= int(input("Enter third number:"))
    n4= int(input("Enter fourth number:"))
    n5= int(input("Enter fifth number:"))
    min=n1
    if min>n2:
        min=n2
    if min>n3:
        min=n3
    if min>n4:
        min=n4
    if min>n5:
        min=n5
    print("Smallest element is:",min)
small()'''
#=======================================================================

'''def func():
    p1= int(input("Enter paper1 marks:"))
    p2= int(input("Enter paper2 marks:"))
    p3= int(input("Enter paper3 marks:"))
    gender= str(input("Enter gender (F/M):"))
    total= p1+p2+p3
    perc= total/3
    if perc>=65 and gender=='F':
        print("Admitted")
    else:
        print("Admission cancelled")
func()'''
#======================================================================

'''def func():
    day= str(input("Enter any day:"))
    if day=="sat" or day=="sun":
        print("Weekend")
    else:
        print("Working day")
func()'''
#=====================================================================

'''def chk_vowel():
    ch= str(input("Enter any character:"))
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
        print("Entered character is vowel")
    else:
        print("Entered character is not vowel")
chk_vowel()'''
#=======================================================================

'''def chk_equal():
    a= int(input("Enter first number:"))
    b= int(input("Enter second number:"))
    if a==b:
        print("Value are equal")
    else:
        print("Value are not equal")
chk_equal()'''
#=======================================================================

'''def vote():
    age= int(input("Enter the age of candidate:"))
    if age>18:
        print("You are eligible for casting your vote")
    else:
        print("You are not eligible for casting your vote")
vote()'''
#======================================================================

'''def grade():
    p1= int(input("Enter percentage:"))
    if p1>=40 and p1<60:
        print("Your grade is C")
    elif p1>=60 and p1<=80:
        print("Your grade is B")
    elif p1>=80 and p1<=100:
        print("Your grade is A")
    else:
        print("Fail")
grade()'''
#==========================================================================

'''def function():
    ch= ord(input("Enter any character:"))
    if ch>=65 and ch<=90:
        print("Your entered character is in upper case")
    elif ch>=97 and ch<=122:
        print("Your entered character is in lower case")
    elif ch>=48 and ch<=57:
        print("Your entered character is in digit")
    else:
        print("Your entered character is in special symbol")
function()'''
#===========================================================================

'''def function():
    name= input("Enter name:")
    if name=='Ashish':
        print("Hello my name is ashish but i am not a tester")
    else:
        print("Did not match the pattern")
function()'''
#=============================================================================

# Write a python function to sum all the numbers in a list element in list will be decide by user.
'''def function():
    list= []
    for i in range(1,11):
        number= int(input("Enter number:"))
        list.append(number)
    print("Sum of number in list:",sum(list))
function()'''
#================================================================================

# Write a python function to multiply all the numbers in a list element in list will be decide by user.
'''def function():
    list= []
    product=1
    for i in range(1,11):
        number= int(input("Enter number:"))
        list.append(number)
        product= product*i
    print("multiply the of number in list:",product)
function()'''
#==================================================================================

# Write a python function to calculate the factorial of a number
'''def function():
    fact=1
    n= int(input("Enter any number:"))
    for i in range(1,n+1):
        fact=fact*i
    print("Factorial is:",fact)
function()'''
#====================================================================================

# Write a python function that takes a list and return a new list with unique element of the first list
'''def function(list):
    a= set(list)
    print(sorted(a))
function([1,2,3,3,3,3,4,4,5])'''
#==================================================================================

# Write a python function to print the even numbers from a given list.
'''def even():
    list= [1,2,3,4,5,6,7,8,9,10]
    for num in list:
        if num%2==0:
            print(num)
even()'''
#===================================================================================

# Write different function to single to calculate area and perimeter of a rectangle, square, circle, triangle
'''def calculate():
    l=10
    b=20
    a=5
    r=3
    h=6
    PI=3.14
    print("Area of rectangle:",l*b)
    print("Area of square:",a*a)
    print("Area of circle:",PI*r*r)
    print("Area of triangle:",1/2*b*h)
    print("Perimeter of rectangle:",2*(l+b))
    print("Perimeter of square:",4*a)
    print("Perimeter of circle:",2*PI*r)
calculate()'''
#====================================================================================