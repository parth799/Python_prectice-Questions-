a=int(input("enter your number: "))
    #
'''f=1
for i in range(1,a+1):
    f=f*i
print(f"the  factorial of thi number is {f}")'''
    #
'''a =int(input("enter number:"))
def factorial_a(n):
   p=1
   for i in range(n):
      p=p*(i+1)
   return p
print(factorial_a(a))
   '''
    #
def factorial_b(n):
    if n == 1 or n==0:
        return 1
    return n * factorial_b(n-1)
print(factorial_b(a))