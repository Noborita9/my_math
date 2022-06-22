import numpy as np
matrix = np.array([
        [6,2,1,11,1],
        [1,3,15,5,42],
        [9,2,1,6,1],
        [2,1,8,-7,9],
        [1,7,2,-9,1],
        ])


def resolve_matrix(matrix):
    column = matrix[:, 0]
    main_number = 0
    for number in reversed(column):
        if number != 0:
            main_number = number
            break
    main_number_index = [len(column), len(matrix)]
    print(main_number_index)
    col_sublist = column[:main_number_index[0]]
    multipliers = [ mul/main_number for mul in col_sublist]
    multipliers.append(1)
    for number in range(main_number_index[0]-1):
        matrix[number] = matrix[number] - (matrix[main_number_index[0]-1] * multipliers[number])

def main():
    cp_matrix = np.array(matrix)
    resolve_matrix(cp_matrix)
    print(f"cp_matrix = \n{cp_matrix}")
    print(f"matrix = \n{matrix}")


if __name__ == "__main__":
    main()

