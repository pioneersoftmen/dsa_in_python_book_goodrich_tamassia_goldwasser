class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = [[0] * columns for _ in range(rows)]


    def add(self, matrix):
        if self.rows != matrix.rows or self.columns != matrix.columns:
            raise ValueError("Matrix dimensions must match.")
        
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.grid[i][j] = self.grid[i][j] + matrix.grid[i][j]
            
        return result
    
    def multiply(self, matrix):
        if self.columns != matrix.rows:
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix.")
        
        result = Matrix(self.rows, matrix.columns)
        for i in range(self.rows):
            for j in range(matrix.columns):
                dot_product = sum(self.grid[i][k] * matrix.grid[k][j] for k in range(self.columns))
                result.grid[i][j] = dot_product

        return result
    
    def __repr__(self):
        return '\n'.join([''.join(map(str, row)) for row in self.grid])