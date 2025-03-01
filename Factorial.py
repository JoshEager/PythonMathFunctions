

def factorial(n: int) -> int:
    """ Calculate the factorial of n """
    
    # Base Case
    if n == 0: 
        return 1
    
    return factorial(n - 1) * n
