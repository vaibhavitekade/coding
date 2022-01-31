ch =ord(input("Enter any character:"))
if ch>=65 and ch<=90:
    print("Your entered character is in upper case")
elif ch>=97 and ch<=122:
    print("Your enetered character is in lower case")
elif ch>=48 and ch<=57:
    print("Your entered character is in digit")
else:
    print("Your entered character is in special symbol")