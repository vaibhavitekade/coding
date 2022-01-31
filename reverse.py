#WAP to reverse 123 into 321 without using any loop

num=123
a= int(num%10)
num= num/10
b= int(num%10)
num= num/10
c= int(num)
rev= (a*100)+(b*10)+(c*1)
print("Reverse number is",rev)