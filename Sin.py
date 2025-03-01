from KnownTrig import known_sin, known_cos, known_sinx_dict
from Factorial import factorial
from math import pi

def sin(radians: float, closest_known_value: float=0, terms: int=25) -> float:
    """
    Taylor series approximation for sin. The taylor series says that any differentiable function can be represented approximately as a 
    polynomial with Sigma(n=0, n=inf, (f^n(a)/n!)(x-a)^n) where 'a' is the x coordinate where your approximation will be the closest to the 
    real value of sin. For general use, it is okay to use zero as long as you have enough terms, as it will be very close unless you are using
    a number with a very large magnitude. Really, you can only use a value of 'a' that has a known sin value (like 0, pi/6, pi/3, pi/2, etc).
    This function supports the use of any sin value on the unit circle for your 'a' value. You control the value of 'a' by using the closest_known_value 
    parameter, but that isn't necessary unless you're using values that would be out of the reasonable range of precision provided by your terms. 

    If you wish to have good answers for any value on the unit circle, I don't recommend going below 23 for your terms.

    """
    # Account for large magnitude numbers by converting the original radian measure to its unit circle equivalent
    radians = radsOnUnitCircle(radians)

    # Validate the closest known value
    acceptable_guesses = [radian_measure for radian_measure in known_sinx_dict.keys()]
    def badGuess() -> None:
        raise ValueError("Bad Guess for sinx! Must be a multiple of something on the unit circle!")      
    a = closest_known_value if closest_known_value in acceptable_guesses else badGuess()

    # Automatically give known values if the radian is in the table of known values
    if radians in known_sinx_dict.keys():
        return known_sinx_dict[radians]

    # Computing the sigma
    sinx: float = 0
    for n in range(0, terms):
        sinx = sinx + ( (sin_derivative(n)(a)) / (factorial(n)) ) * ( (radians - a) ** n )

    return sinx


def sin_derivative(n: int):
    """ Function that returns a function that is the nth derivative of sinx """
    if n == 0:
        return known_sin
    
    fraction: float = (n % 4) / 4
    match fraction:
        case 0.25: 
            return known_cos
        case 0.5:
            def negative_known_sin(x: float) -> float:
                return -(known_sin(x))
            return negative_known_sin
        case 0.75:
            def negative_known_cos(x: float) -> float:
                return -(known_cos(x))
            return negative_known_cos
        case 0: 
            return known_sin
        case _:
            raise ValueError("idek")
        

def radsOnUnitCircle(radians) -> float:
    if radians <= 2*pi and radians >= 0:
        return radians

    rads = None
    if radians > 2*pi:
        # solving 0 <= radians - 2pin <= 2pi for n if n is an integer
        upper_n = ( (radians) / (2*pi) )
        n = upper_n - (upper_n % 1)
        rads = radians - (2*pi*n)
    if radians < 0:
        # solving 0 <= radians + 2pin <= 2pi for n if n is an integer
        upper_n = ( (2*pi - radians) / (2*pi))
        n = upper_n - (upper_n % 1)
        rads = radians + (2*pi*n)

    return rads



if __name__ == "__main__":
    print(sin(2323))
