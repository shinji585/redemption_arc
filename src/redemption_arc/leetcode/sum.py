result = 0
for n in range(1,5): 
    result += n 
    
print(result)

def sum_to_n(n: int): 
    if not n: 
        return 0     
    return n + sum_to_n(n - 1) 

print(sum_to_n(4))