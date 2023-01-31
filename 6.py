import os

def fibonacci(n):
    fib_list=[1]
    if n <= 0:
        return("Invalid value!")
    elif n == 1:
        return(fib_list)

    else:    
        a = 0
        b = 1
        for i in range(1, n):
            c = a + b
            a = b
            b = c
            fib_list.append(b)
        return(fib_list)
 


print(fibonacci(100))


os.system('pause')