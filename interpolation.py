from sympy import solve , symbols , Eq
table = { 0:0 , 10 : 227.04 , 15 : 362.78 , 20 : 517.35 , 22.5 : 602.97 , 30 : 901.67}
number = 16
# Find the maximum key less than or equal to the given number
low = max((key for key in table.keys() if key <= number), default=None)
high = min( (key for key in table.keys() if key >= number) )

a0 , a1 = symbols('a0 a1')
equation1 = Eq( a0 + low*a1 , table[low])
equation2 = Eq( a0 + high*a1 , table[high])

solution = solve((equation1 , equation2), (a0 , a1))


final_solution = solution[a0] + solution[a1]*number
