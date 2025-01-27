# This file contains intentionally bad code to test CodeRabbitAI's review capabilities

def x(a,b,c,d,e,f,g,h):  # Too many parameters, bad naming
    """do stuff"""
    if a:  # Deeply nested conditions
        if b:
            if c:
                if d:
                    if e:
                        if f:
                            if g:
                                if h:
                                    return True
    return False

class badclass:  # Incorrect class naming convention
    def __init__(self):
        self.x = 1
        self.y = 2
        self.z = 3  # Too many single-letter variables
    
    def BADLY_NAMED_METHOD(self):  # Incorrect method naming convention
        l = []  # Single-letter variable
        i = 0
        while i < 10:  # Could be a for loop
            if i % 2 == 0:
                l.append(i)
            i += 1
        return l

def very_long_function_with_many_lines():  # Function too long
    print("Line 1")
    print("Line 2")
    print("Line 3")
    print("Line 4")
    print("Line 5")
    print("Line 6")
    print("Line 7")
    print("Line 8")
    print("Line 9")
    print("Line 10")
    print("Line 11")
    print("Line 12")
    print("Line 13")
    print("Line 14")
    print("Line 15")
    print("Line 16")
    print("Line 17")
    print("Line 18")
    print("Line 19")
    print("Line 20")
    print("Line 21")
    print("Line 22")
    return "This function is too long"

def unused_params(param1, param2):  # Unused parameters
    return "Hello"

def complex_calculation(a, b):  # Overly complex logic
    result = 0
    temp = 0
    for i in range(a):
        for j in range(b):
            for k in range(j):
                temp += i * j * k
                if temp > 100:
                    if temp % 2 == 0:
                        if temp % 3 == 0:
                            result += temp
    return result

# Missing docstrings
def mystery_function(x):
    return x * x * x * x if x > 0 else -x * x if x < 0 else 0  # Too complex one-liner

# Inconsistent spacing and formatting
def  bad_formatting (  x,y    ,z):
    return    x+  y+z

# Magic numbers
def calculate_price(quantity):
    if quantity > 15:
        return quantity * 19.99 * 0.85
    else:
        return quantity * 19.99

# Global variables
GLOBAL_COUNTER = 0

def increment_counter():
    global GLOBAL_COUNTER
    GLOBAL_COUNTER += 1
    return GLOBAL_COUNTER

# Mixed string quotes
def string_mess():
    s1 = "double quotes"
    s2 = 'single quotes'
    s3 = """triple quotes"""
    return s1 + s2 + s3

# Redundant code
def redundant():
    result = []
    for i in range(10):
        if i % 2 == 0:
            result.append(i)
        else:
            if i % 3 == 0:
                result.append(i)
            else:
                if i % 5 == 0:
                    result.append(i)
    return result 