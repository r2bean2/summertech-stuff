matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
while True:
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0
    number_options = [str(i) for i in range(1, max_number + 1)]