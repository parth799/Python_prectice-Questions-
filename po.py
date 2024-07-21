from operator import truediv


num = int(input("enter the number:"))
prime=True
for i in range(2, num):
    if(num%i==0):
        prime=False
        break
if prime:
    print("this number is prime")
else:
    print("this number is not prime")

