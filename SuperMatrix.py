import numpy as np
class SuperMatrix():
    def __init__(self, matrix=np.array([])) -> None:
        self.matrix = matrix
        self.size = np.shape(self.matrix)

    def ask_size(self):
        finish = False
        layer = 0
        while not finish:
            text = input(f"Ingrese los numeros de la capa {layer}. Ej:(4,1,3,2)\n~~> ")
            numbers = np.array([int(num) for num in text.split(',')])
            self.matrix = np.append(self.matrix, [numbers], axis=0)
            isFinish = input("Quieres agregar otra capa?[Y/n]\n~~> ")
            if isFinish in ["n", "N"]:
                finish = True

    def get_size(self):
        self.size = np.shape(self.matrix)
        return self.size


matrix = SuperMatrix()
matrix.ask_size()
matrix_size = matrix.get_size()
print(matrix.matrix)
print(matrix_size)
