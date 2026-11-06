def is_palindrome(text: str) -> bool:
    if len(text) < 2:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])

def is_palindrome_version2(text: str) -> bool: 
    if len(text) < 2: 
        return True
    
    
    return text[0:] == text[::-1] 
    

print(is_palindrome("abba"))
print(is_palindrome("hola"))
print(is_palindrome_version2("abba"))
print(is_palindrome_version2("hola"))