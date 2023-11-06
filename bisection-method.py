# selecting interval
def f(x):
    # return x**3 - 4*x - 9
    return x**3 + x - 1
i = 0
x = f(i)
while True:
    i += 1
    y = f(i)
    if( x > 0 and y < 0) or ( x < 0 and y > 0) :
        a = i - 1 
        b = i
        break

def bisection_method(f, a, b, tolerance = 1e-9 , max_iteration = 1000 ):
    
    if abs(b-a) < tolerance:
        return (a + b) / 2
    
    # Recursive case: find the midpoint
    c = (a + b) / 2
    
    # If f(c) is very close to zero, return c as the root
    if abs(f(c)) < tolerance:
        return c
    
    # If f(c) and f(a) have opposite signs, update the interval to [a, c]
    elif f(c) * f(a) < 0:
        return bisection_method(f, a, c, tolerance , max_iteration )
    
    # If f(c) and f(b) have opposite signs, update the interval to [c, b]
    else:
        return bisection_method(f, c, b, tolerance , max_iteration )

        
# Find the root using bisection method with a tolerance of 1e-9
root = bisection_method(f, a, b, tolerance=1e-9)

print("Approximate root: ", root)
    



