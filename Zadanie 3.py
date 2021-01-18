def Fibonacci_recursion(n):
    if n<0:
        return False
    elif n<1:
        return 0
    elif n<3:
        return 1
    else:
        return Fibonacci_recursion(n-1)+Fibonacci_recursion(n-2)
n=int(input("Podaj ilość liczb: "))
for i in range(1,n+1):
    print(Fibonacci_recursion(i))
