password=input("enter the password")
length=len(password)

if length<6:
    print("Weak")
elif length>=6 and length<=10:
   print("Medium")
else:
    print("Strong")
