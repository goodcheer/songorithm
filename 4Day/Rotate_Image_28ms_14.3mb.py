class Solution:
    def rotate(self, matrix: list) -> None:
        row = len(matrix)
        rotate_matrix = []
        for i in zip(*matrix[::-1]):
            rotate_matrix.append(list(i))
        for j in range(row):
            matrix[j] = rotate_matrix[j]

if __name__ == '__main__':
    inst = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    inst.rotate(matrix)
    print(matrix)