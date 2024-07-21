a=int(input("enter you fsast sub mark: "))
b=int(input("enter you second sub mark: "))
c=int(input("enter you third sub mark: "))

if(a<33 or b<33 or c<33):
    print("you are fail because mark is under 33%")
elif((a+b+c)/3 <40):
    print("you are fail")
else:
    print("you are pass")