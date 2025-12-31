class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()


'''
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]





Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
'''
'''
matrix[0][0] -> matrix[0][3]
matrix[0][1] -> matrix[1][3]
matrix[0][2] -> matrix[2][3]
matrix[0][3] -> matrix[3][3]
matrix[1][0] -> matrix[0][2]
matrix[1][1] -> matrix[1][2]
matrix[1][2] -> matrix[2][2]
matrix[1][3] -> matrix[3][2]
matrix[2][0] -> matrix[0][1]
matrix[2][1] -> matrix[1][1]
matrix[2][2] -> matrix[2][1]
matrix[2][3] -> matrix[3][1]
matrix[3][0] -> matrix[0][0]
matrix[3][1] -> matrix[1][0]
matrix[3][2] -> matrix[2][0]
matrix[3][3] -> matrix[3][0]
'''