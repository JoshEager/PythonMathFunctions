from math import pi, sqrt


known_sinx_dict = {
    0: 0, 
    pi/6: 1/2,
    pi/4: sqrt(2)/2, 
    pi/3: sqrt(3)/2, 
    pi/2: 1,  
    2*pi/3: sqrt(3)/2,
    3*pi/4: sqrt(2)/2, 
    5*pi/6: 1/2,    
    pi: 0,      
    7*pi/6: -1/2,   
    5*pi/4: -sqrt(2)/2, 
    4*pi/3: -sqrt(3)/2,
    3*pi/2: -1,  
    5*pi/3: -sqrt(3)/2, 
    7*pi/4: -sqrt(2)/2, 
    11*pi/6: -1/2, 
    2*pi: 0 
}

known_cosx_dict = {
    0: 1,
    pi/6: sqrt(3)/2,
    pi/4: sqrt(2)/2,
    pi/3: 1/2,
    pi/2: 0,
    2*pi/3: -1/2,
    3*pi/4: -sqrt(2)/2,
    5*pi/6: -sqrt(3)/2,
    pi: -1,
    7*pi/6: -sqrt(3)/2,
    5*pi/4: -sqrt(2)/2,
    4*pi/3: -1/2,
    3*pi/2: 0,
    5*pi/3: 1/2,
    7*pi/4: sqrt(2)/2,
    11*pi/6: sqrt(3)/2,
    2*pi: 1
}

def known_sin(x: float) -> float:
    try: 
        return known_sinx_dict[x]
    except KeyError:
        raise ValueError("Tried to reference a known sin value that was not actuallly known!")
    
def known_cos(x: float) -> float:
    try: 
        return known_cosx_dict[x]
    except KeyError:
        raise ValueError("Tried to reference a known value of cos that was not actually known!")