def count_down(n: int):
    if n >= 0:
        print(n)
        count_down(n - 1)
        
        

count_down(n=5)