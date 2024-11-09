import numpy as np

def gauss_elimination(a_matrix, b_matrix):
    # Evitando problemas
    if a_matrix.shape[0] != a_matrix.shape[1]:
        print("ERROR: La matriz no es cuadrada")
        return
    if b_matrix.shape[1] > 1 or b_matrix.shape[0] != a_matrix.shape[0]:
        print("El vector constante tiene tama~no incorrecto")
        return

    # Inicialización de variables
    n = len(b_matrix)
    m = n - 1
    i = 0
    x = np.zeros(n)
    new_line = "\n"

    # Creando la matriz ampliada usando numpy.concatenate
    augmented_matrix = np.concatenate((a_matrix, b_matrix,), axis=1, dtype=float)

    print(f"La matriz ampliada inicial es: {new_line}{augmented_matrix}")
    print()
    print("Llevando a una forma triangular superior:")

    # Aplicando escalerización Gaussiana:
    while i < n:
        # Pivoteo parcial.
        for p in range(i + 1, n):
            if abs(augmented_matrix[i, i] < abs(augmented_matrix[p, i])):
                augmented_matrix[[p, i]] = augmented_matrix[[i, p]]

        # Error por dividir entre cero.
        if augmented_matrix[i][i] == 0.0:
            print("Error por dividir entre cero")
            return
        for j in range(i + 1, n):
            scaling_factor = augmented_matrix[j][i] / augmented_matrix[i][i]
            augmented_matrix[j] = augmented_matrix[j] - (scaling_factor * augmented_matrix[i])
            # Para ver el proceso
            print(augmented_matrix)
            print()

        i = i + 1

        # Sustitución hacia atrás
        if augmented_matrix[m][m] == 0.0:
            print("Error: el sistema no es compatible determinado")
            return

        x[m] = augmented_matrix[m][n] / augmented_matrix[m][m]
        for k in range(n - 2, -1, -1):
            x[k] = augmented_matrix[k][n]
            for j in range(k + 1, n):
                x[k] = x[k] - augmented_matrix[k][j] * x[j]
            if augmented_matrix[k][k] == 0.0:
                print("Error: el sistema no es compatible determinado")
                return
            x[k] = x[k] / augmented_matrix[k][k]

    # Imprimiendo la solución
    print("El siguiente vector x resuelve el sistema:")
    for answer in range(n):
        print(f"x{answer + 1} is {x[answer]}")


# Para probar el código, ingresar aquí la matriz A del sistema y
# el vector constante b
if __name__ == '__main__':
    variable_matrix = np.array([[1, 1, 3], [0, 1, 3], [-1, 3, 0]])
    constant_matrix = np.array([[1], [3], [5]])
    gauss_elimination(variable_matrix, constant_matrix)
