import numpy as np

import escalerizacion_gaussiana
import flask_app

matriz_inicial = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 1, 0, 0, 0, 1, 1, 1]
])

def aplanar_matriz(matriz):
    # Evitando problemas
    if matriz.shape[0] != matriz.shape[1]:
        print("ERROR: La matriz no es cuadrada")
        return
    n = matriz.shape[0] # Obtener el tamaño de la matriz n x n
    vector = np.zeros(n*n, dtype=int)

    for i in range(n):
        for j in range(n):
            # Calcular la posición en el vector para el elemento (i, j)
            index = i * n + j  # Esto es equivalente a la división entera
            vector.put(index, matriz[i][j])

    return np.array(vector)


def generar_matriz_ecuaciones(n):
    """Genera una matriz A de tamaño nxn para representar un sistema de ecuaciones de Lights Out"""
    A = np.zeros((n*n, n*n), dtype=int)

    # Rellenar la matriz A con las interacciones entre las luces
    for i in range(n):
        for j in range(n):
            index = i * n + j  # Este es el índice en el vector (aplanado)

            # Interacciones de la luz en (i, j)
            A[index, index] = 1  # La luz actual (en su posición)

            # Vecinos (arriba, abajo, izquierda, derecha) si existen
            if i > 0:  # Fila superior
                A[index, (i - 1) * n + j] = 1
            if i < n - 1:  # Fila inferior
                A[index, (i + 1) * n + j] = 1
            if j > 0:  # Columna izquierda
                A[index, i * n + (j - 1)] = 1
            if j < n - 1:  # Columna derecha
                A[index, i * n + (j + 1)] = 1
    return A


def obtener_solucion(matriz):
    n = matriz.shape[0]
    sistema_ecuaciones = generar_matriz_ecuaciones(n)

    aplanada = aplanar_matriz(matriz)

    solucion = escalerizacion_gaussiana.gauss_elimination_mod2(sistema_ecuaciones, aplanada)
    return solucion


if __name__ == '__main__':
    # 1- definir matriz de un juego
    # 2- aplanar para obtener vector del modelo matematico
    # 3- hallar matriz/sistema de ecuaciones
    # 4- hallar matriz solucion
    n = matriz_inicial.shape[0]
    sistema_ecuaciones = generar_matriz_ecuaciones(n)

    print('inicial:', matriz_inicial)
    aplanada = aplanar_matriz(matriz_inicial)
    print('aplanada:', aplanada)

    solucion = escalerizacion_gaussiana.gauss_elimination_mod2(sistema_ecuaciones, aplanada)
    print('solucion', solucion)
    flask_app.run_app()