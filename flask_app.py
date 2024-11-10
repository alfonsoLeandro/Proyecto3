import numpy as np
from flask import Flask, jsonify, render_template
from flask_cors import CORS

from main import obtener_solucion

app = Flask(__name__)
CORS(app)

size = 3
matriz_actual = np.random.randint(0, 2, size=(size, size))

@app.route('/')
def index():
    # Create the initial grid
    grid = matriz_actual
    # Convert grid to array for easy rendering
    grid_array = grid_to_array(grid)
    return render_template('index.html', grid=grid_array, n=len(grid))


@app.route('/toggle/<int:i>/<int:j>')
def toggle(i, j):
    grid = toggle_lights(matriz_actual, i, j)
    grid_array = grid_to_array(grid)
    return render_template('grid.html', grid=grid_array, n=len(grid))

@app.route("/solucion")
def mostrar_solucion():
    return jsonify(obtener_solucion(matriz_actual))


# Convert a 2D grid into a 1D array for the HTML rendering
def grid_to_array(grid):
    return grid.flatten()


# Update the grid when a button is pressed
def toggle_lights(grid, i, j):
    n = grid.shape[0]
    print('hijota', i,j)
    # List of neighbors (including itself)
    neighbors = [
        (i, j),  # itself
        (i - 1, j) if i > 0 else None,  # up
        (i + 1, j) if i < n - 1 else None,  # down
        (i, j - 1) if j > 0 else None,  # left
        (i, j + 1) if j < n - 1 else None  # right
    ]
    print('vecinos', neighbors)

    for vecino in neighbors:
        if vecino is not None:
            grid[vecino[0], vecino[1]] = 1 - grid[vecino[0], vecino[1]]  # Toggle the light
    return grid

def run_app():
    app.run()
