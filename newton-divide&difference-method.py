# Function for calculating divided difference table 
def dividedDifferenceTable(x, y, n):
    for i in range(1, n):
        for j in range(n-i):
            y[j][i] = ((y[j + 1][i - 1] - y[j][i - 1]) / (x[j + i] - x[j]))
        
# Function for displaying divided difference table 
def printDividedDifferenceTable(x ,y, n):
    for i in range(n):
        for j in range(n - i):
            print(round(y[i][j], 4) , "\t" , end=" ")
        print()

# Function to find the product term of the formula
def product_term(i , value , x):
    pro = 1
    for j in range(i):
        pro = pro * (value - x[j])
    # print(pro , " pro")
    return pro
    
# Function for applying Newton's divided difference formula     
def applyFormula(value , x , y , n):
    sum = y[0][0]
    for i in range(1,n):
        sum = sum + (product_term( i , value , x) * y[0][i])
    return sum
        
x = [5, 7, 11, 13, 21]
n = len(x)
y = [[0 for j in range(n - i)] for i in range(n)]


# y[][] is used for divided difference table where y[][0] is used for input 
y[0][0] = 150
y[1][0] = 392
y[2][0] = 1452
y[3][0] = 2366
y[4][0] = 9702

# calculating divided difference table 
dividedDifferenceTable(x , y, n)

print("Newton’s divided difference interpolation method.")

# displaying divided difference table 
printDividedDifferenceTable(x , y, n)

# value to be interpolated 
value = 10; 

print("Value at ", value , " is ", applyFormula(value , x , y , n))
