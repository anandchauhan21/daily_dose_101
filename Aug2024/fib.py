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

# for both fnction time complexity is 0(2**n) and space complexity is 0(n)
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
n=int(input("Enter the value of n:"))
print("Fibonacci(", n,")= ", fibo(n))