#classic fibonachi

def fib(n):
    if n <=2:
        return 1
    return fib(n-1) + fib(n-2)
#print(fib(50))

#  for both of functions time and space complexity is 0(n)
def foo(n):
    if n <=1:
        return
    return foo(n-1)

def bar(n):
    if n <= 1:
        return
    return bar(n-2)

# for both function time complexity is 0(2**n) and space complexity is 0(n)
def dib(n):
    if n <=1:
        return
    dib(n-1)
    dib(n-1)
def lib(n):
    if n <=1:
        return
    lib(n-2)
    lib(n-2)

#  for both of functions time and space complexity is 0(n) Linear time complexity.
Dict={0:0, 1:1}
def fibo(n):
    if n not in Dict:
        val=fibo(n-1)+fibo(n-2)
        Dict[n]=val
    return Dict[n]
#n=int(input("Enter the value of n:"))
#print("Fibonacci(", n,")= ", fibo(n))

# Grid traveler

# time complexity 0(2**n+m) and space 0(n+m)

def grid(m,n):
    if m == 1 and n == 1:return 1;
    if m == 0 or n == 0:return 0;
    return grid(m-1,n) + grid(m,n-1)


# time complexity 0(m*n) and space 0(n+m)
def gridnew(m,n,memo= {}):
    key = str(m)+","+str(n)
    if key in memo:return memo[key];
    if m == 1 and n == 1:return 1;
    if m == 0 or n == 0:return 0;
    memo[key]=gridnew(m-1,n,memo) + gridnew(m,n-1,memo)
    return memo[key]
print(gridnew(18,18))
