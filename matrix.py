matrix1 = [
    [ 1, 0, 2],
    [-5, 3, 6],
    [ 0,-1, 4]
]

matrix2 = [
    [ 1, 0, 2, 7],
    [-5, 3, 6, 8],
    [ 0,-1, 4, 9]
]

system1 = [
    [-1,-6,-23],
    [-2,5,5],
]

matrix3 = [
    [ 1, 0],
    [-5, 3],
]

determinant_selection = [[(1,2),()]]

def solve_2x2_system(matrix):
    m = matrix
    
    # print(f"original matrix {m}")

    if len(m) != 2:
        print("longer than 2! failed!")

    determinant = determinant_2x2(m)

    #this is stupid. everything I do, .copy, [:], list(), everything makes a stupid goddamn reference.
    m_solve_x = [[m[0][0],m[0][1]],[m[1][0],m[1][1]]]
    m_solve_x[0][0] = m[0][2]
    m_solve_x[1][0] = m[1][2]

    # print(f"original matrix {m}")

    m_solve_y = [[m[0][0],m[0][1]],[m[1][0],m[1][1]]]
    m_solve_y[0][1] = m[0][2]
    m_solve_y[1][1] = m[1][2]

    # print(f"original matrix {m}")
    
    print(m_solve_x)
    print(m_solve_y)

    det_x = determinant_2x2(m_solve_x)
    det_y = determinant_2x2(m_solve_y)

    print(det_x)
    print(det_y)

    solve_x = det_x/determinant
    solve_y = det_y/determinant

    return solve_x,solve_y

def transpose_3x3(matrix):
    m = matrix
    new_matrix = [
        [m[0][0],m[1][0],m[2][0]],
        [m[0][1],m[1][1],m[2][1]],
        [m[0][2],m[1][2],m[2][2]]
        ]
    return new_matrix

def inverse_3x3(matrix):
    for i in range(0,8):
        pass

def print_3x3(matrix):
    m = matrix
    if m:
        print(f"-------Matrix-------")
        print(f"{m[0][0]} {m[0][1]} {m[0][2]}")
        print(f"{m[1][0]} {m[1][1]} {m[1][2]}")
        print(f"{m[2][0]} {m[2][1]} {m[2][2]}")
    else:
        print("Failed!")

def determinant_2x2(matrix):
    m = matrix

    determinant = (m[0][0]*m[1][1])-(m[1][0]*m[0][1])
    return determinant


def determinant_3x3(matrix): #This code does not work because I don't understand how determenat scales, it only works for 3x3.
    m = matrix
    
    # if matrix is not square, fail!
    # modulo the indexes by the lenth or width of matrix.
    if len(m) != 3:
        print("matrix is not 3x3!")
        return False

    for row in m:
        if len(row) != 3:
            print("matrix is not 3x3!")
            return False
    print("matrix is 3x3!")
    
    determinant_pos = 0
    determinant_neg = 0

    matrix_size = len(m)

    for row in range(0,matrix_size):
        determinant_pos_third = 1
        determinant_neg_third = 1
        for colum in range(0,matrix_size):
            # print(f"row index: {row}")
            # print(f"colum index: {colum}")

            determinant_pos_third *= m[(colum)%matrix_size][(row+colum)%matrix_size]
            # print(m[(row+colum)%matrix_size][(colum)%matrix_size])

            determinant_neg_third *= m[matrix_size-1-(colum)%matrix_size][(row+colum)%matrix_size]

        determinant_pos += determinant_pos_third
        determinant_neg += determinant_neg_third
    return(determinant_pos-determinant_neg)

def int_input():
    while True:
        user_input = input()
        try:
            return int(user_input)
        except:
            print("not an int!")

def main():
    # print_3x3(matrix1)
    # # print_3x3(transpose_3x3(matrix1))
    # print(f"-------Determinant-------")
    # print(determinant(matrix1))
    # print(f"-------Determinant-------")
    # print(determinant(matrix2))
    print(f"-------Determinant 3x3-------")
    print(determinant_3x3(matrix1))
    print(f"-------Determinant 2x2-------")
    print(determinant_2x2(matrix3))
    print(f"-------System Solve 2x2-------")
    print(solve_2x2_system(system1))

    while True:
        user_input = input()

        if user_input == "end":
            break
        
        if user_input == "solve 2x2 system":
            matrix_to_solve = [[],[]]
            for i in range(0,1):
                for j in range(0,2):
                    print("Matrix input")
                    matrix_to_solve[i].append(int_input())
            print(matrix_to_solve)

main()