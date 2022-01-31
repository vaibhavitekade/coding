'''for i in range(10):
    if i==5:
        print("This is right time to take break at 5pm")
        break
    print(i)'''
#==============================================================

'''mycart= [10,20,200,300,800,60,700]
for i in mycart:
    if i>400:
        print("This my purchased cart item")
        break
    print(i)'''
#==============================================================

'''mycart= [10,20,200,300,800,60,700]
for i in mycart:
    if i>400:
        print("This my purchased cart item")
        continue
    print(i)'''
#=============================================================

# To print odd number in the range 0 to 9
'''for i in range(0,10):
    if i%2!=0:
        print(i)'''
#============================================================

'''count=0
for i in range(9):
    if i%2==0:
        print(i)
    else:
        print(i)
        count+=1
print("Count= ",count)'''
#============================================================

'''mycart= [10,20,68,60,70]
for item in mycart:
    if item>400:
        print("This is not in my budget")
        continue
    print(item)
else:
    print("You have purchased everything")'''
#============================================================

'''name= input("Enter name:")
i=0
for x in name:
    if x=='n':
        print("The character present at index no ",i,"value: ",x)
        break
    i=i+1'''
#===========================================================

'''for i,j in zip(range(1,6),range(5,0,-1)):
    if i==3 and j==3:
        continue
    else:
        print(i," ",j)'''