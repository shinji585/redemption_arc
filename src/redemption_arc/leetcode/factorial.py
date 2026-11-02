def factorial_function(n: int) -> int: 
    if n == 0: 
        return 1 
    
    return n * factorial_function(n -1)

print(factorial_function(3))