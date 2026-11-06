def reverse_string(texto: str) -> str: 
    counter = len(texto)
    inverse_text = "" 
    while counter > 0: 
        counter -= 1 
        inverse_text += texto[counter]
    return inverse_text

def reverse_string_using_recursive_call(text: str) -> str: 
    counter = len(text) - 1 
    return recursive_reverse_string(text, counter)

def recursive_reverse_string(texto: str, counter: int) -> str: 
    if counter < 0: 
        return ""
    return texto[counter] + recursive_reverse_string(texto=texto,counter=counter - 1)

print(reverse_string("hola"))
print(reverse_string_using_recursive_call("hola"))