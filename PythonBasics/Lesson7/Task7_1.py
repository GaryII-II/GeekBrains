# Artificial Intelligence
# Igor Ivanov
# Lesson 7
# Task 1. Class Matrix for print and add matrix

My_matrix = [[2, 1, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]
             ]


class Matrix:

    def __init__(self, in_matrix):
        self.in_matrix = in_matrix

    def __str__(self):
        result = ''
        for line in self.in_matrix:
            result += (' '.join([str(item).center(6) for item in line])+'\n')

        return result

    def __add__(self, other):
        sum_matrix = []
        for line1, line2 in zip(self.in_matrix, other.in_matrix):
            sum_matrix.append([item1 + item2 for item1, item2 in zip(line1, line2)])
        return Matrix(sum_matrix)


matrix1 = Matrix(My_matrix)
matrix2 = Matrix(My_matrix)
print(matrix1)
matrix1 += matrix2
print(matrix1)
