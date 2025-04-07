def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

for i in range(10): # 生成从 1 到 9 的斐波那契数列的前10项
    print(fib(i))
