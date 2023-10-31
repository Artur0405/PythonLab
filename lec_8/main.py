# import random

# class Matrix():
#     def __init__(self, m = 3, n = 3):
#         self.m = m
#         self.n = n 

#         matrix = list()
    
#         for i in range(m):
#             row = list()
#             for j in range(n):
#                 row.append(random.randint(1,100))
#             matrix.append(row)


#     def get_metrix(matrix):
#         for i in matrix:
#             print(i)

#     def mean_of_matrix(matrix):
#         for i in range(len(matrix)):
#             matrix[i] = sum(matrix[i])
            
#         return sum(matrix)/ len(matrix)
    
#     def sum_of_row(row):
#         return sum(matrix[row])
    
#     def average_of_column(column):
#         result = 0
#         for i in range(len(matrix)):
#             result += matrix[i][column]
    
#         return result / len(matrix)
    
#     def get_sub_matrix(col1, col2, row1, row2):
#         pass