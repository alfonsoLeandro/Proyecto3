import numpy as np

# Aplicar eliminación gaussiana en módulo 2
def gauss_elimination_mod2(A, b):
    """ Resuelve el sistema de ecuaciones A * x = b en módulo 2 """
    # Evitando problemas
    if A.shape[0] != A.shape[1]:
        print("ERROR: La matriz no es cuadrada")
        return
    if len(b.shape) > 1 or b.shape[0] != A.shape[0]:
        print("El vector constante tiene tamaño incorrecto")
        return
    # n es la cantidad de incognitas en el sistema
    n = len(b)
    # x es el vector solucion
    x = np.zeros(n, dtype=int)

    for i in range(n):
        # Encontrar pivote en la columna i
        if A[i, i] == 0:
            for j in range(i + 1, n):
                if A[j, i] == 1:
                    # Intercambiar filas
                    A[[i, j]] = A[[j, i]]
                    b[[i, j]] = b[[j, i]]
                    break

        # Realizar operaciones de fila
        for j in range(i + 1, n):
            if A[j, i] == 1:
                A[j] = (A[j] + A[i]) % 2
                b[j] = (b[j] + b[i]) % 2

    # Sustitución hacia atrás para encontrar la solución
    for i in range(n - 1, -1, -1):
        if A[i, i] == 1:
            x[i] = b[i]
            for j in range(i + 1, n):
                x[i] = (x[i] + A[i, j] * x[j]) % 2

    return x
