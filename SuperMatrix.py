import numpy as np
class SuperMatrix():
    def __init__(self, matrix) -> None:
        self.matrix = matrix
        self.size = np.shape(self.matrix)
        self.delimeter = None

    def sarrus_resolve(self):
        extended_matrix = np.array(self.matrix)
        extended_matrix = np.append(extended_matrix, extended_matrix[:, 0:2], axis=1)
        delimeter = 0
        for repetition in range(3):
            pos_val = np.array([])
            neg_val = np.array([])
            for number in range(3):
                pos_val = np.append(pos_val, extended_matrix[number][number+repetition])
                neg_val = np.append(neg_val, extended_matrix[number][-1-number-repetition])
            p_hold = 1
            n_hold = 1
            for vp, vn in zip(pos_val, neg_val):
                p_hold *= vp
                n_hold *= vn
            n_hold *= -1
            delimeter += p_hold + n_hold
        self.delimeter = delimeter
        return delimeter

    def prop4(self):
        mat_copy = np.array(self.matrix)
        column = mat_copy[:, 0]
        main_number = 0
        for number in reversed(column):
            if number != 0:
                main_number = number
                break
        main_number_index = [len(column), len(mat_copy)]
        col_sublist = column[:main_number_index[0]]
        multipliers = [ mul/main_number for mul in col_sublist]
        multipliers.append(1)
        for number in range(main_number_index[0]-1):
            mat_copy[number] = mat_copy[number] - (mat_copy[main_number_index[0]-1] * multipliers[number])
        return mat_copy



matrix = SuperMatrix(np.array([
    [2,4,9,5],
    [5,0,5,6],
    [3,2,1,3],
    [1,3,8,1],
    ]))
matrix.prop4()
print(matrix.prop4())
