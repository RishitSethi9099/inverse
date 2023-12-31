from determinant import determinant
print('[green]ENTER A 3X3 MATRIX TO FIND ITS INVERSE[/green]')
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
d = int(input("Enter the value of d: "))
e = int(input("Enter the value of e: "))
f = int(input("Enter the value of f: "))
g = int(input("Enter the value of g: "))
h = int(input("Enter the value of h: "))
i = int(input("Enter the value of i: "))
matrix= [[a,b,c],
         [d,e,f],
         [g,h,i]]
x=matrix[0] 
y = matrix[1]
z = matrix[2]
print(f"The matrix is: {x}\n\t\t{y}\n\t\t{z}")

def cofactor(matrix):
    cofactor_matrix = []
    for i in range(len(matrix)):
        cofactor_row = []
        for j in range(len(matrix)):
            minor = []
            for row in (matrix[:i]+matrix[i+1:]):
                minor.append(row[:j]+row[j+1:])
            cofactor_row.append(((-1)**(i+j))*determinant(minor))
        cofactor_matrix.append(cofactor_row)
    return cofactor_matrix

def transpose(matrix):
    transpose_matrix = []
    for i in range(len(matrix)):
        transpose_row = []
        for j in range(len(matrix)):
            transpose_row.append(matrix[j][i])
        transpose_matrix.append(transpose_row)
    return transpose_matrix

def inverse(matrix):
    det = determinant(matrix)
    if det == 0:
        return "Inverse does not exist"
    else:
        return (f'1/{det}*{transpose(cofactor(matrix))}')
    
print(inverse(matrix))
