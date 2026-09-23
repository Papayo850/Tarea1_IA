import numpy as np
from mapa import Mapa
from agente import Agente
from buscar import bfs, dijkstra

def ejecutar_simulacion(tipo_mapa, algoritmo_str, num_iteraciones=80):
    resultados_supervivencia = []
    resultados_tiempos = []

    print(f"Iniciando pruebas: Mapa {tipo_mapa} | Algoritmo: {algoritmo_str}")

    for iteracion in range(num_iteraciones):
        entorno = Mapa(tipo_mapa=tipo_mapa)
        
        # cantidad de personas
        agentes = [
            Agente(id_agente=1, x_inicial=1, y_inicial=1),
            Agente(id_agente=2, x_inicial=4, y_inicial=8),
            Agente(id_agente=3, x_inicial=1, y_inicial=8)
        ]
        
        meta = (1, 9)  # coordenada de salida
        
        simulacion_activa = True
        
        # bucle de turnos
        while simulacion_activa:
            # propagar el fuego cada k turnos
            entorno.propagar_fuego()
            
            entorno.densidad_celdas = np.zeros_like(entorno.grilla)
            for ag in agentes:
                if ag.vivo and not ag.evacuado:
                    entorno.densidad_celdas[ag.x, ag.y] += 1

            todos_terminaron = True
            
            # turno de cada agente
            for agente in agentes:
                if agente.vivo and not agente.evacuado:
                    todos_terminaron = False
                    
                    # verificar si el fuego alcanzó al agente
                    if entorno.grilla[agente.x, agente.y] == 2:
                        agente.morir()
                        continue
                        
                    # decidir ruta segun el algoritmo
                    ruta = []
                    if algoritmo_str == "BFS":
                        ruta = bfs(entorno, (agente.x, agente.y), meta)
                    elif algoritmo_str == "Dijkstra":
                        ruta = dijkstra(entorno, (agente.x, agente.y), meta)
                        
                    # mover al agente al primer paso de la ruta
                    if ruta and len(ruta) > 0:
                        siguiente_paso = ruta[0] if ruta[0] != (agente.x, agente.y) else ruta[1] if len(ruta) > 1 else (agente.x, agente.y)
                        agente.mover(siguiente_paso[0], siguiente_paso[1])
                        
                        # verificar si llegó a la salida
                        if (agente.x, agente.y) == meta:
                            agente.salvarse()

            if todos_terminaron:
                simulacion_activa = False

        # recolección de datos de los resultados finales
        sobrevivientes = [ag for ag in agentes if ag.evacuado]
        tasa = len(sobrevivientes) / len(agentes)
        resultados_supervivencia.append(tasa)
        
        if sobrevivientes:
            # el tiempo del último sobreviviente
            tiempo_maximo = max([ag.turnos_tomados for ag in sobrevivientes])
            resultados_tiempos.append(tiempo_maximo)

    # calculo de estadísticas finales
    tasa_promedio = np.mean(resultados_supervivencia) * 100
    
    if resultados_tiempos:
        tiempo_media = np.mean(resultados_tiempos) # tiempo media de turnos
        tiempo_std = np.std(resultados_tiempos)    # desviacion estandar
        tiempo_min = np.min(resultados_tiempos)    # tiempo minimo de turnos
        tiempo_max = np.max(resultados_tiempos)    # tiempo maximo de turnos
    else:
        tiempo_media = tiempo_std = tiempo_min = tiempo_max = 0

    # printeo de los resultados en la terminal
    print(f"Resultados tras {num_iteraciones} iteraciones:")
    print(f"Tasa de supervivencia media: {tasa_promedio:.2f}%")
    print(f"Tiempos del último sobreviviente -> Media: {tiempo_media:.2f}, Std: {tiempo_std:.2f}, Min: {tiempo_min}, Max: {tiempo_max}\n")

if __name__ == "__main__":
    ejecutar_simulacion(tipo_mapa=1, algoritmo_str="BFS", num_iteraciones=80)
    ejecutar_simulacion(tipo_mapa=1, algoritmo_str="Dijkstra", num_iteraciones=80)