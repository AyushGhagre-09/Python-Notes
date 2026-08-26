# Age Group Categorization

age=int(input("Enter you age : "))

if age<13:
    print("child")
elif age>=13 and age<=19:
    print("Teenager")
elif age>=20 and age<=59:
    print("Adult")
else:
   print("Senior")