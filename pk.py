a=float(input("Enter your first number:"))
b=float(input("Enter your second number:"))
c=input("Enter the operation you want ' + - * / ' :")
if c=="+":
    print("The answer is:",a+b)
elif c=="-":
    print("The answer is:",a-b)
elif c=="*":
    print("The answer is:",a*b)
elif c == "/":
    print("The answer is:",a/b)
else:
    print("Enter a valid operation.")