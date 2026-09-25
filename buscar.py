from collections import deque
import heapq

# algoritmo BFS
def bfs(mapa_obj, inicio, meta):
    # la cola (deque) guarda tuplas de (posición_actual, camino)
    cola = deque([(inicio, [])]) 
    visitados = set()
    visitados.add(inicio)
    
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    
    while cola:
        (x, y), camino = cola.popleft()
        
        # si llegamos a la salida
        if (x, y) == meta:
            return camino
            
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < mapa_obj.grilla.shape[0] and 0 <= ny < mapa_obj.grilla.shape[1]:
                # evitar obstáculos (1) y el fuego (2)
                if mapa_obj.grilla[nx, ny] not in [1, 2] and (nx, ny) not in visitados:
                    visitados.add((nx, ny))
                    # añadimos el nuevo paso al camino
                    cola.append(((nx, ny), camino + [(nx, ny)]))
                    
    return []

# algoritmo Dijkstra
def dijkstra(mapa_obj, inicio, meta):
    # la cola de prioridad guarda (costo_acumulado, posicion_actual, camino)
    cola_prioridad = [(0, inicio, [])]
    costos_visitados = {inicio: 0}

    # aqui implementamos los movimientos, incluyendo la accion de esperar (0, 0)
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)] 
    
    while cola_prioridad:
        costo_actual, (x, y), camino = heapq.heappop(cola_prioridad)
        
        # si llegamos a la salida
        if (x, y) == meta:
            return camino
            
        # si encontramos un camino más costoso hacia una celda ya visitada, se ignora
        if costo_actual > costos_visitados.get((x, y), float('inf')):
            continue
            
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < mapa_obj.grilla.shape[0] and 0 <= ny < mapa_obj.grilla.shape[1]:
                # evitar obstaculos y el fuego
                if mapa_obj.grilla[nx, ny] not in [1, 2]:
                    
                    # calculamos el costo de esta celda
                    costo_paso = mapa_obj.calcular_costo_celda(nx, ny)
                    nuevo_costo = costo_actual + costo_paso
                    
                    # si es un camino menos costoso, se guarda la ruta
                    if nuevo_costo < costos_visitados.get((nx, ny), float('inf')):
                        costos_visitados[(nx, ny)] = nuevo_costo
                        heapq.heappush(cola_prioridad, (nuevo_costo, (nx, ny), camino + [(nx, ny)]))
                        
    return []

# formula de heuristica
def heuristica(pos_actual, meta):
    # usaremos la formula de la heuristica euclidiana
    h = ((pos_actual[0] - meta[0])**2 + (pos_actual[1] - meta[1])**2)**(1/2)
    return h

# algoritmo A* 
def a(mapa_obj, inicio, meta):
    cola_prioridad = [(0, 0, inicio, [])]
    costos_visitados = {inicio: 0}
    
    # aqui implementamos los movimientos, incluyendo la accion de esperar (0, 0)
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)] 
    
    while cola_prioridad:
        f_score, costo_g, (x, y), camino = heapq.heappop(cola_prioridad)
        
        # si alcanzamos la salida
        if (x, y) == meta:
            return camino
            
        if costo_g > costos_visitados.get((x, y), float('inf')):
            continue
            
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < mapa_obj.grilla.shape[0] and 0 <= ny < mapa_obj.grilla.shape[1]:
                # evitamos los muros y el fuego del mapa
                if mapa_obj.grilla[nx, ny] not in [1, 2]:
                    
                    # g(n): costo acumulado
                    costo_paso = mapa_obj.calcular_costo_celda(nx, ny)
                    nuevo_costo_g = costo_g + costo_paso
                    
                    if nuevo_costo_g < costos_visitados.get((nx, ny), float('inf')):
                        costos_visitados[(nx, ny)] = nuevo_costo_g
                        
                        # h(n): costo por heuristica
                        h_n = heuristica((nx, ny), meta)
                        
                        # f(n) = g(n) + h(n), costo final al llegar a la casilla n
                        nuevo_f_score = nuevo_costo_g + h_n
                        
                        heapq.heappush(cola_prioridad, (nuevo_f_score, nuevo_costo_g, (nx, ny), camino + [(nx, ny)]))
                        
    return []

def greedy(mapa_obj, inicio, meta):
    cola_prioridad = [(heuristica(inicio, meta), inicio, [])]
    visitados = set()
    visitados.add(inicio)
    
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)] 
    
    while cola_prioridad:
        h_score, (x, y), camino = heapq.heappop(cola_prioridad)
        
        if (x, y) == meta:
            return camino
            
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < mapa_obj.grilla.shape[0] and 0 <= ny < mapa_obj.grilla.shape[1]:
                # evitamos muros y el fuego del mapa
                if mapa_obj.grilla[nx, ny] not in [1, 2] and (nx, ny) not in visitados:
                    visitados.add((nx, ny))
                    
                    # h(n): costo por heuristica
                    h_n = heuristica((nx, ny), meta)
                    
                    heapq.heappush(cola_prioridad, (h_n, (nx, ny), camino + [(nx, ny)]))
                    
    return []