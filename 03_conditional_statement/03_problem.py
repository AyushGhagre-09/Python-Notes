marks=int(input("Enter your marks : "))

if marks>=101:
    print("Please enter valid marks")
    exit()

if marks>=90 and marks<=100:
    print("A")
elif marks>=80 and marks<=90:
    print("B")
elif marks>=70 and marks<=79:
    print("C")
elif marks>=60 and marks<=69:
    print("D")
else:
    print("F")