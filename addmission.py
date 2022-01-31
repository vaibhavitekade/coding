p1= int(input("Enter paper1 marks:"))
p2= int(input("Enter paper2 marks:"))
p3= int(input("Enter paper3 marks:"))
gender= str(input("Enter gender (F/M):"))
total= p1+p2+p3
perc= total/3
if perc>=62 and gender=='F':
    print("Admitted")
else:
    print("Admission cancelled")