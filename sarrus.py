# Is always 3x3
matrix = [
        [2,-3,1],
        [1,2,1],
        [1,-5,0]
        ]

def alter_matrix(matrix):
    for mat in matrix: 
        mat.append(mat[0])
        mat.append(mat[1])


def do_math(matrix):
    pos_diagonals = []
    neg_diagonals = []
    for num in range(3):
        pos_diagonal = []
        neg_diagonal = []
        for number in range(3):
            neg_diagonal.append(matrix[number][-1-number-num])
            pos_diagonal.append(matrix[number][number+num])
        pos_diagonals.append(pos_diagonal)
        neg_diagonals.append(neg_diagonal)
    pos_value = 0
    neg_value = 0
    for number in range(3):
        pos_value += pos_diagonals[number][0] * pos_diagonals[number][1] * pos_diagonals[number][2]
        neg_value -= neg_diagonals[number][0] * neg_diagonals[number][1] * neg_diagonals[number][2]
    print(f"The value is {pos_value + neg_value}")

def resolve_sarrus(matrix):
    alter_matrix(matrix)
    do_math(matrix)


def main():
   resolve_sarrus(matrix) 


if __name__ == '__main__':
    main()
