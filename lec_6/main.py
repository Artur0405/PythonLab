import random

def get_metrix(matrix):
    for i in matrix:
        print(i)

def generate_random_matrix(row: int,column: int):
    result_matrix = list()
    
    for m in range(row):
        row = list()
        for n in range(column):
            row.append(random.randint(1,100))
        result_matrix.append(row)
    
    return result_matrix


def get_column_sum(matrix: list, column :int):
    result = 0
    for i in range(len(matrix)):
        result += matrix[i][column]
    
    return result

def get_row_average(matrix: list, row: int):
    return sum(matrix[row])/len(matrix[row])


matrix = generate_random_matrix(3,3)

get_metrix(matrix)
print(get_column_sum(matrix, 1))
print(get_row_average(matrix, 2))