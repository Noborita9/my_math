import numpy as np

matrix = np.array([
    [2,4,9,5],
    [5,0,5,6],
    [3,2,1,3],
    ])

def cramer_method(matrix):
    shape = np.shape(matrix)[1]-1
    coef_matrix = np.array(matrix[:, :shape])
    val_matrix = np.array(matrix[:, shape])
    delimeters = []
    for index in range(shape):
        sub_matrix = np.array(coef_matrix[:])
        sub_matrix[:, index] = val_matrix
    print(delimeters)


def main():
    cramer_method(matrix)


if __name__ == "__main__":
    main()

