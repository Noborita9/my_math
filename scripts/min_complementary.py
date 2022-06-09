matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        ]
def get_min_complementary(matrix,column, row):
    matrix.pop(row)
    for mat in matrix:
        mat.pop(column)
        print(mat)


def main():
    row = 0
    column = 1
    get_min_complementary(matrix, column, row)


if __name__ == '__main__':
    main()
