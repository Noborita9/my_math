matrix = [
        [1,1,1,4],
        [-2,-1,-1,3],
        [1,-1,-2,0]
        ]
matrix1= [
        [3,1,6,3,2,1],
        [4,5,1,6,1,6],
        [2,4,1,5,6,1],
        [7,8,4,5,3,5],
        [6,6,1,9,1,2],
        ]


def get_matrix_size(matrix):
    height = len(matrix)
    length = len(matrix[0])
    return {'height': int(height), 'length': int(length)}


def replace_lines(matrix, size, counter, rnum):
    line_number = size['height']-counter
    first_line = matrix[rnum][rnum]
    second_line = matrix[line_number][rnum]
    if first_line * second_line + first_line *second_line != 0:
        second_line *= -1
    new_line = []
    for index, number in enumerate(matrix[rnum]):
        new_line.append(number*second_line + matrix[line_number][index]* first_line)
    matrix[line_number] = new_line
    counter -= 1
    if counter != 0:
        replace_lines(matrix, size, counter, rnum)
    else:
        rnum += 1
        if rnum == size['height']-1:
            return
        counter =0
        replace_lines(matrix, size, counter+line_number-rnum, rnum)


def get_values(matrix, size, value_list, counter):
    unknown = matrix[size['height']-1-counter][size['length']-2-counter]
    equivalence = matrix[size['height']-1-counter][size['length']-1]
    value_holder= 0
    indexes = -1
    for number in range(counter):
        value_holder += (matrix[size['height']-1-counter][size['length']-1-counter+number] * value_list[indexes])
        indexes -= 1
    equivalence -= value_holder
    new_value = equivalence / unknown
    value_list.append(new_value)
    counter += 1
    if counter == size['length']-1:
        return
    else:
        get_values(matrix, size, value_list, counter)



def resolve_matrix(matrix):
    size = get_matrix_size(matrix)
    replace_lines(matrix, size, size['height']-1, 0)
    value_list = [matrix[size['height']-1][size['length']-1] / matrix[size['height']-1][size['length']-2]]
    get_values(matrix, size, value_list, 1)
    return value_list


def main():
    value_list =resolve_matrix(matrix)

    for index, number in enumerate(reversed(value_list)):
        print(f"x{index+1}: {number}")

if __name__ == '__main__':
    main()
