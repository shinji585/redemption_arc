def reverse_string(n: str) -> str: 
    if not n: 
        return ""
    n = n.strip()
    return n[-1] + reverse_string(n[:-1])


print(reverse_string("cat"))