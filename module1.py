def welcome(fname,lname):
    print("First name=",fname)
    print("Last name=",lname)


def square(n):
    print(n*n)


pi= 3.145145145


def login(username,password):
    if username==password:
        print("You have login successfully")
    else:
        print("You have entered wrong credentials")


def addition(val):
    print("Addition of two number=",val+val)


def chk_even_odd(number):
    if number%2==0:
        print(number,"This is even number")
    else:
        print(number,"This is odd number")


def func(number):
    if number>0:
        print(number,"is positive")
    if number<0:
        print(number,"is negative")
    if number==0:
        print(number,"is zero")


def name(*value):
    print(value)


def msg(age):
    age= int(input("Enter your age:"))
    if age>=18:
        print("You are eligible for license")
    else:
        print("You are not eligible")


def number(a,b):
    if b>a:
        print("b is greater than a")
    elif a==b:
        print("a and b are equal")
    else:
        print("a is greater than b")


def mark():
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


def large():
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


def func():
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


def func():
    day= str(input("Enter any day:"))
    if day=="sat" or day=="sun":
        print("Weekend")
    else:
        print("Working day")


def chk_vowel():
    ch= str(input("Enter any character:"))
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
        print("Entered character is vowel")
    else:
        print("Entered character is not vowel")


def chk_equal():
    a= int(input("Enter first number:"))
    b= int(input("Enter second number:"))
    if a==b:
        print("Value are equal")
    else:
        print("Value are not equal")


def vote():
    age= int(input("Enter the age of candidate:"))
    if age>18:
        print("You are eligible for casting your vote")
    else:
        print("You are not eligible for casting your vote")