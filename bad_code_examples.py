# This file contains intentionally bad code to test CodeRabbitAI's review capabilities

def x(a,b,c,d,e,f,g,h):  # Too many parameters, bad naming
    """
    Check if all input parameters are truthy.
    
    This function performs a deeply nested conditional check to determine if all eight input parameters are considered truthy (non-zero, non-empty, non-None).
    
    Parameters:
        a: First input parameter to check
        b: Second input parameter to check
        c: Third input parameter to check
        d: Fourth input parameter to check
        e: Fifth input parameter to check
        f: Sixth input parameter to check
        g: Seventh input parameter to check
        h: Eighth input parameter to check
    
    Returns:
        bool: True if all parameters are truthy, False otherwise
    
    Note:
        - The function uses deeply nested conditional statements
        - Recommends refactoring to improve readability, e.g., using `all()` function
    """
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
        """
        Initialize a new instance of the class with predefined numeric attributes.
        
        This constructor sets three single-letter instance variables with default integer values:
        - x: Set to 1
        - y: Set to 2
        - z: Set to 3
        
        Note: While functional, using single-letter variable names is discouraged in favor of more descriptive names.
        """
        self.x = 1
        self.y = 2
        self.z = 3  # Too many single-letter variables
    
    def BADLY_NAMED_METHOD(self):  # Incorrect method naming convention
        """
        Generate a list of even numbers between 0 and 9 (inclusive).
        
        This method uses a while loop to iterate through numbers and collect even integers.
        Typically, this could be more concisely implemented using a list comprehension.
        
        Returns:
            list: A list containing even numbers [0, 2, 4, 6, 8]
        """
        l = []  # Single-letter variable
        i = 0
        while i < 10:  # Could be a for loop
            if i % 2 == 0:
                l.append(i)
            i += 1
        return l

def very_long_function_with_many_lines():  # Function too long
    """
    Prints a sequence of 22 numbered lines and returns a descriptive string.
    
    This function demonstrates an excessively long implementation that violates best practices
    for code readability and maintainability. It sequentially prints lines from 1 to 22
    and returns a self-referential message about its length.
    
    Returns:
        str: A string indicating the function's excessive length
    """
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
    """
    Return a static greeting string, ignoring input parameters.
    
    This function always returns the string "Hello" regardless of the input parameters.
    The parameters `param1` and `param2` are not used in the function body, which suggests
    they are unnecessary and can be removed.
    
    Parameters:
        param1: Unused input parameter
        param2: Unused input parameter
    
    Returns:
        str: The static string "Hello"
    
    Warning:
        The function parameters are not utilized, which is considered a code smell.
        Consider removing unused parameters or using them in the function implementation.
    """
    return "Hello"

def complex_calculation(a, b):  # Overly complex logic
    """
    Performs a complex nested calculation with multiple nested loops and conditional checks.
    
    Computes a cumulative result by iterating through nested ranges and applying multiple conditions.
    The function accumulates values in the result based on specific mathematical and divisibility criteria.
    
    Parameters:
        a (int): First range limit for the outermost loop
        b (int): Second range limit for the middle loop
    
    Returns:
        int: Accumulated result after applying complex nested calculation logic
    
    Notes:
        - Time complexity is O(a * b^2) due to triple nested loops
        - Computation involves multiplication and modulo operations
        - Result depends on specific conditions of temp value
    """
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
    """
    Compute the fourth power of a number with sign preservation.
    
    This function calculates the fourth power (x^4) for positive numbers,
    the negative fourth power for negative numbers, and returns 0 for zero.
    
    Parameters:
        x (int or float): The input number to be processed
    
    Returns:
        int or float: The fourth power of the input number, preserving its sign
    """
    return x * x * x * x if x > 0 else -x * x if x < 0 else 0  # Too complex one-liner

# Inconsistent spacing and formatting
def  bad_formatting (  x,y    ,z):
    """
    Adds three numeric values together.
    
    Parameters:
        x (numeric): First number to be added
        y (numeric): Second number to be added
        z (numeric): Third number to be added
    
    Returns:
        numeric: Sum of x, y, and z
    """
    return    x+  y+z

# Magic numbers
def calculate_price(quantity):
    """
    Calculate the total price for a given quantity with an optional bulk discount.
    
    Parameters:
        quantity (int): The number of items to purchase. Must be a positive integer.
    
    Returns:
        float: The total price of the items, with a 15% discount applied for purchases 
               over 15 items.
    
    Notes:
        - Base price per item is $19.99
        - Bulk discount of 15% is applied for quantities exceeding 15 items
    """
    if quantity > 15:
        return quantity * 19.99 * 0.85
    else:
        return quantity * 19.99

# Global variables
GLOBAL_COUNTER = 0

def increment_counter():
    """
    Increments the global counter and returns its updated value.
    
    This function modifies the global variable `GLOBAL_COUNTER` by incrementing it by 1 and returns the new value.
    
    Note:
        - Uses global state, which can lead to unpredictable behavior in concurrent environments
        - Not thread-safe
        - Side effect of modifying a global variable
    
    Returns:
        int: The incremented value of the global counter
    """
    global GLOBAL_COUNTER
    GLOBAL_COUNTER += 1
    return GLOBAL_COUNTER

# Mixed string quotes
def string_mess():
    """
    Concatenates strings defined with different quote styles.
    
    Returns:
        str: A combined string created by concatenating 's1', 's2', and 's3' 
        using different string quote types (double, single, and triple quotes).
    """
    s1 = "double quotes"
    s2 = 'single quotes'
    s3 = """triple quotes"""
    return s1 + s2 + s3

# Redundant code
def redundant():
    """
    Generate a list of numbers from 0 to 9 that are even, or divisible by 3 or 5.
    
    Returns:
        list: A list containing even numbers and numbers divisible by 3 or 5 from the range 0-9.
    
    Note:
        This implementation contains redundant conditional checks and can be simplified.
    """
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