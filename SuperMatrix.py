import numpy as np
class SuperMatrix():
    def __init__(self, matrix) -> None:
        self.matrix = matrix
        self.size = np.shape(self.matrix)
        self.delimeter = None

    def sarrus_resolve(self, extended_matrix):
        if extended_matrix is None:
            extended_matrix = np.array(extended_matrix)
        extended_matrix = np.append(extended_matrix, extended_matrix[:, 0:2], axis=1)
        delimeter = 0
#        print(f"extended_matrix = \n{extended_matrix}")
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
#        print(delimeter)
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

    def cramer_method(self):
        shape = np.shape(self.matrix)[1]-1
        coef_matrix = np.array(self.matrix[:, :shape])
        val_matrix = np.array(self.matrix[:, shape])
        delimeters = []
        for index in range(shape):
            sub_matrix = np.array(coef_matrix[:])
            sub_matrix[:, index] = val_matrix
            delimeters.append(self.sarrus_resolve(sub_matrix))
        matrix_delimeter = self.sarrus_resolve(coef_matrix)
        values = [unknown / matrix_delimeter for unknown in delimeters]
        #print(f"matrix_delimeter = {matrix_delimeter}\n delimeters = {delimeters}")
        print(delimeters)
        print(matrix_delimeter)
        return values

    def sum_matrix(self, sub_matrix):
        if np.shape(sub_matrix.matrix) == self.size:
            return sub_matrix.matrix + self.matrix



matrix = SuperMatrix(np.array([
    [1,-3,2,-3],
    [5,6,-1,13],
    [4,-1,3,8],
    ]))

print(matrix.cramer_method())
