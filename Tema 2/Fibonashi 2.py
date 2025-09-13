def fibonacci(n):
    gato = [0, 1]
    for i in range(2, n):
        gato.append(gato[-1] + gato[-2])
    return gato

if __name__ == "__main__":
    n = 10
    fibo = fibonacci(n)
    print(fibo)