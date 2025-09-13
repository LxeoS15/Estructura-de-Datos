def factorial(n):
    if (n<=1):
        return 1
    else:
        subSolution = factorial(n-1)
        solution = subSolution * n
        return solution
    
print(factorial(11))
    