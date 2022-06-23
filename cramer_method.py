import numpy as np
from sarrus import resolve_sarrus

matrix = np.array([
        [3,6,2,7],
        [4,2,-3,9],
        [9,4,8,1],
        ])

def cramer_method(matrix):
    shape = np.shape(matrix)[1]-1
    coef_matrix = np.array(matrix[:, :shape])
    val_matrix = np.array(matrix[:, shape])
    delimeters = []
    for index in range(shape):
        sub_matrix = np.array(coef_matrix[:])
        sub_matrix[:, index] = val_matrix
        delimeters.append(resolve_sarrus(sub_matrix))
    print(delimeters)


def main():
    cramer_method(matrix)


if __name__ == "__main__":
    main()

