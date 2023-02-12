#Recursive version of the code
def factorialMethod(x):
    if x == 1:
        return 1
    return x*factorialMethod(x-1)
print(factorialMethod(100))

#Iterative version of the code
def factorialMethod2(y):
    total = 1
    for y in range(1,y+1):
        total*=y
    return total
print(factorialMethod2(1000))