def maldicion_cofre(n: list[int]) -> int: 
    return sum(x for x in n if x > 0)

print(maldicion_cofre([12,-5,8,0,7,-3,10]))