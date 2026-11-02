def sum_digits(n: int): 
    result = 0
    for i in range(n):
      last_number = n%10
      n = n // 10
      result += last_number
    return result 


print(sum_digits(527))
    

def sum_digits_recursive(n: int) -> int: 
    if n == 0: 
        return 0 
    return n % 10 + sum_digits_recursive(n // 10)


print(sum_digits_recursive(527))