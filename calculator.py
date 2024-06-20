print("----SIMPLE CALCULATOR-------")
first=input("enter first number: ")
second=input("enter second number : ")
operator=input("enter the operator: ")
first=int(first)
second=int(second)
if operator=="+":
    print("Sum of the number is",first+second)
elif operator=="-":
    print("Difference of the number is",first-second)
elif operator=="*":
    print("Product of the number is",first*second)
elif operator=="/":
    print("Division of the number is",first/second)
elif operator=="%":
    print("Remainder of the number is",first%second)
else:
    print("invalid operator used")