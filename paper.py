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
percentage= total/6.0
print("Total=",total)
print("Percentage=",percentage)