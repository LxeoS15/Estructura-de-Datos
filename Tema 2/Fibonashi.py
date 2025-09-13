def recurt_fibo(n):
    if n <= 1:
        return n
    else:
        return(recurt_fibo(n-1) + recurt_fibo(n-2))
print(recurt_fibo(8))