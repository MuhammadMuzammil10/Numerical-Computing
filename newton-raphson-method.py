x = float(3)
def f_x(x):
    return x**2 - 4*x -7 
    # return x**3 - 20
def f_prime_x(x):
    return 2*x - 4
    # return 3*x**2 

while True:
    root = x - (f_x(x) / f_prime_x(x))
    print(root)
    if round(root , 2) == round(x , 2):
        print("Answer is: " , root)
        break
    else:
        x = root