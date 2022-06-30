rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

# using 2 for loops
matrix = []
for i in range(rows):
    colm = []
    for j in range(columns):
        colm.append(2)
    matrix.append(colm)
print(matrix)    
# using list comprehensions
    
matrix1 = [[1 for j in range(columns)] for i in range(rows)]   
    
print(matrix1)    
        