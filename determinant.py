from rich import print


def determinant(matrix):

    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
    else:
        det = 0
        for i in range(len(matrix)):
            det += ((-1)**i)*matrix[0][i]*determinant([row[:i]+row[i+1:] for row in matrix[1:]])
        return det
    
if __name__ == "__main__":
    print('[green]ENTER A 3X3 MATRIX TO FIND ITS DETERMINANT[/green]')
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
    
    x=  matrix[0] 
    y = matrix[1]
    z = matrix[2]
    
    print(f"The matrix is: {x}\n\t\t{y}\n\t\t{z}")
    
    print(determinant(matrix))
 



