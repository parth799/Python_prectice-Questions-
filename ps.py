def maximum(n1,n2,n3):
    if (n1>n2):
        if(n1>n3):
            return n1
        else:
            return n3
    else:
        if(n2>n3):
            return n2
        else:
            return n3

m = maximum(5,10,15)
print("maximum value is" + str(m))
