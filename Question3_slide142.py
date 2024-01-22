def rotate_matrix(matrix):
    n = len(matrix)
    # Xoay từ phần tử ngoài cùng ra trong
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            # Lưu giữ phần tử trên cạnh trên
            top = matrix[first][i]

            # Di chuyển phần tử từ cạnh trái đến cạnh trên
            matrix[first][i] = matrix[last - (i - first)][first]

            # Di chuyển phần tử từ cạnh dưới đến cạnh trái
            matrix[last - (i - first)][first] = matrix[last][last - (i - first)]

            # Di chuyển phần tử từ cạnh phải đến cạnh dưới
            matrix[last][last - (i - first)] = matrix[i][last]

            # Di chuyển phần tử từ cạnh trên đến cạnh phải
            matrix[i][last] = top

# Hàm in ra màn hình ma trận
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Example Usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Original Matrix:")
print_matrix(matrix)
rotate_matrix(matrix)
print("\nMatrix after 90-degree rotation:")
print_matrix(matrix)