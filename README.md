# Tarea 1: Escape de la Torre - Inteligencia Artificial

* Cristobal Valenzuela Escobar

## Descripción
Simulacion de evacuacion de un edificio en llamas. Evalúa la navegación dedistintos agentes a través de mapas con congestión para pasar y propagación de fuego, se ha utilizado los siguientes algoritmos para la simulacion:
- **Búsqueda No Informada:** BFS y Dijkstra
- **Búsqueda Informada:** A* y Greedy Best-First Search
- **Optimización Bioinspirada:** Algoritmo Genetico

## Requisitos previos
* Python 3.x
* Librería NumPy (`pip install numpy`)

## Cómo ejecutar el código
Para correr las simulaciones y el benchmarking comparativo de los 3 mapas (con 200 iteraciones por algoritmo) en la consola, ejecuta el archivo principal en la raíz del proyecto:

python main.py