import time
def Fibonacci_iteration(n):
    if n<0:
        return False
    elif n<1:
        return 0
    number1,number2=0,1
    for i in range(n-1):
          result=number1+number2
          number1=number2
          number2=result
    return result 
def Fibonacci_recursion(n):
    if n<0:
        return False
    elif n<1:
        return 0
    elif n<3:
        return 1
    else:
        return Fibonacci_recursion(n-1)+Fibonacci_recursion(n-2)
start1=time.time()
Fibonacci_iteration(34)
end1=time.time()
start2=time.time()
Fibonacci_recursion(34)
end2=time.time()
time1=end1-start1
time2=end2-start2
print("Czas działania metody iteracyjnej:",time1)
print("Czas działania metody rekurencyjnej:",time2)


