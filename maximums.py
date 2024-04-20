def max_of_two(x, y):
    if x>y:
        return x
    elif x<y:
        return y
    elif x==y:
        return x
def max_of_three(x, y, z):
    if (x>=y and x>z) or (x>y and x>=z):
        return x
    elif (y>=x and y>z) or (y>x and y>=z):
        return y
    elif (z>=x and z>y) or (z>x and z>=y):
        return z
    elif x==y==z:
        return x
print(max_of_two(5, 4))
print(max_of_two(-2,-3))
print(max_of_two(0,0))
print(max_of_three(5,4,7))
print(max_of_three(-2,-3,-1))
print(max_of_three(0,0,0))
