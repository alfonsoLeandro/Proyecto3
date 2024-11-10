# Proyecto 3 Algebra

## Letra del proyecto
https://webasignatura.ucu.edu.uy/pluginfile.php/794522/mod_resource/content/1/Tarea_Lights_Out___%C3%81lgebra_aplicada_.pdf

## Integrantes
Leandro Alfonso
Santiago Avelino
Sebastian Quintana

## Ejecucion
Previo a la ejecución es necesario instalar los requerimientos, detallados en `requirements.txt` corriendo el siguiente comando

```pip install -m requirements.txt```

Finalmente correr el proyecto, a través del archivo principal ejecutando el siguiente comando

```python main.py```

Esto imprimirá la matriz inicial (hardcodeada), la misma matriz aplanada (en forma de vector) y por último el vector solución.
Finalmente imprime logs de flask, y la dirección donde se puede acceder a la aplicación de flask (http://localhost:5000)

## Aplicación Flask
La aplicación disponibiliza una página donde se puede jugar "lights out", en ella se verá una grilla de 3x3 donde se
ubican las luces que debemos apagar y prender para participar del juego, un botón debajo "Ver solución" 
que indica que luces deben ser presionadas para llegar a la solución (todas las luces apagadas) y un botón tipo 
refresh en la esquina superior izquierda, para generar una nueva matriz.