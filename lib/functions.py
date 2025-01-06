#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    

def greet(name):
    print(f"Hello, {name}!")  

greet("Guido")    

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")


def add(num1, num2):
   return(num1 + num2)

add(45,55)
    

def halve(int):
    return(int/2)
halve(100)
    


# Key differences:
# 1. 'DEF' keyword used to identify code as function
# 2. follow by 'FUNCTION_NAME'
# 3. (parameters in parentheses)
# 4. COLON at the END OF LINE
# 5. INDENTATION used to denote code block
# 6. PRINT('code block')
# 7. RETURN keyword used to return specified value
# 8. ## return type is not specified, it is inferred by the return statement
#7