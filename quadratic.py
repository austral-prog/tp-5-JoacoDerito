def roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        r1 = (-b + (discriminant)**0.5) / (2*a)
        r2 = (-b - (discriminant)**0.5) / (2*a)
        return "(" + str(r1) + ", " + str(r2) + ")"
    elif discriminant == 0:
        r1 = -b / (2*a)
        return "(" + str(r1) + ")"
    else:
        return "( )"
def value_y(a, b, c, x):
    return a*x**2 + b*x + c
def to_string(a, b, c):
    return "f(x) = " + str(a) + " * X^2 + " + str(b) + " * X + " + str(c)
def derivation(a, b):
    return "f'(x) = " + str(2*a) + "x + " + str(b)
print(roots(1, -3, 2))  
print(roots(1, -2, 1))  
print(roots(1, 2, 3))   
print(value_y(1, -3, 2, 0))   
print(value_y(1, -3, 2, 1))   
print(value_y(1, -3, 2, -1))  
print(to_string(2, -3, 1))    
print(derivation(2, -3))   
