class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def __str__(self):
        matrix = ""
        for i in range(len(self.mat)):
            prmat = [str(el) for el in self.mat[i]]
            prmat = "   ".join(prmat)
            matrix = matrix + prmat + "\n"
        return matrix

    def __add__(self, other):
        summat = []
        for i in range(len(self.mat)):
            sumrow = list(map(lambda x, y: x + y, self.mat[i], other.mat[i]))
            summat.append(sumrow)
        return f"Сумма матриц:\n{Matrix(summat)}"

    #Или так:
    #def __add__(self, other):
     #   summat = []
      #  for i in range(len(self.mat)):
       #     sumrow = []
            #for j in range(len(self.mat[i])):
             #   row = int(self.mat[i][j]) + int(other.mat[i][j])
              #  sumrow.append(row)
        #    summat.append(sumrow)
        #return f"Сумма указанных матриц:\n{Matrix(summat)}"


mat_1 = Matrix([[1, 2, 0], [3, 4, 0], [5, 6, 0]])
print(mat_1)
mat_2 = Matrix([[2, 1, 0], [4, 3, 1], [2, 1, 2]])
print(mat_2)
print(mat_1 + mat_2)
