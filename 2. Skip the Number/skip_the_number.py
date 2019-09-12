def alternate_fib(n): 
    if (n < 0): 
        return -1

    a = 0 
    b = 1
  
    print(a, end = " ")
    for i in range(2, n): 
        c = b + a
          
        if (i % 2 == 0): 
            print(c, end = " ")
  
        a = b
        b = c

if __name__ == '__main__':
    n = int(input())
    alternate_fib(n)