# Description: This program multiplies two matrices and prints the result. 
# Reason for creating this was to help me understand how matrix multiplication works prior to my exam.
# Author: Harry Wills
# 2024-10-28

class CalculateMatrix:
    def __init__(self, matrix1, matrix2):
        self.first_matrix = matrix1
        self.second_matrix = matrix2
    
    def run(self):
        print("Matrix 1:")
        for row in self.first_matrix:
            print(" ".join(map(str, row))) 

        print("Matrix 2:")
        for row in self.second_matrix:
            print(" ".join(map(str, row)))
        
        # Check if multiplication is possible
        if len(self.first_matrix[0]) != len(self.second_matrix):
            return "The number of columns in the first matrix and the number of rows in the second matrix are not equal."
        
        multiplied_matrix = []
        # Iterate through rows of first matrix
        for i in range(len(self.first_matrix)): 
            # Build the row for the new matrix
            row = []

            # Iterate through columns of second matrix
            for j in range(len(self.second_matrix[0])): 
                # Multiply and sum corresponding numbers
                result = sum(self.first_matrix[i][k] * self.second_matrix[k][j] for k in range(len(self.first_matrix[0]))) 
                row.append(result)
            multiplied_matrix.append(row)

        return multiplied_matrix

def main():
    matrix1 = [
        [1, 2], 
        [3, 4]
    ]
    matrix2 = [
        [5, 6], 
        [7, 8]
    ]

    matrix_multiplier = CalculateMatrix(matrix1, matrix2)
    result = matrix_multiplier.run()
    print("\nResult:")
    for row in result:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()