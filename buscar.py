from collections import deque
import heapq

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