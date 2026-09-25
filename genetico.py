import random

def genetico(mapa_obj, inicio, meta, tam_poblacion=150, generaciones=150, max_pasos=40):
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]
    
    # generar población inicial
    poblacion = []
    for _ in range(tam_poblacion):
        individuo = [random.choice(movimientos) for _ in range(max_pasos)]
        poblacion.append(individuo)
        
    def calcular_fitness(individuo):
        x, y = inicio
        costo_total = 0
        camino_recorrido = [(x, y)]
        llego = False
        
        for dx, dy in individuo:
            nx, ny = x + dx, y + dy
            
            # verificamos los limites del mapa
            if 0 <= nx < mapa_obj.grilla.shape[0] and 0 <= ny < mapa_obj.grilla.shape[1]:
                # si choca con un muro o fuego, queda penalizado con mayor costo
                if mapa_obj.grilla[nx, ny] in [1, 2]:
                    costo_total += 1000  # penalizacion alta 
                else:
                    x, y = nx, ny 
                    costo_total += mapa_obj.calcular_costo_celda(x, y)
            else:
                costo_total += 1000

            camino_recorrido.append((x, y))
                
            if (x, y) == meta:
                llego = True
                break

        # formula heuristica
        distancia_meta = ((x - meta[0])**2 + (y - meta[1])**2)**0.5

        bono_meta = 10000 if llego else 0
        fitness = bono_meta - (distancia_meta * 10) - costo_total
        
        return fitness, camino_recorrido

    mejor_camino_global = []
    
    # ciclo evolutivo
    for gen in range(generaciones):
        # evaluar a toda la población y ordenarlos por orden descendente: los de mayor fitness primero
        evaluaciones = [(calcular_fitness(ind), ind) for ind in poblacion]
        evaluaciones.sort(key=lambda item: item[0][0], reverse=True) 
        
        mejor_fitness, mejor_camino = evaluaciones[0][0]
        mejor_camino_global = mejor_camino
        
        # si el mejor individuo ya llegó a la meta, detenemos la evolución temprano
        if len(mejor_camino) > 0 and mejor_camino[-1] == meta:
            return mejor_camino
            
        # selección y reproducción (nueva generación)
        # elitismo: los 2 mejores pasan intactos a la siguiente generación
        nueva_poblacion = [evaluaciones[0][1], evaluaciones[1][1]] 
        
        while len(nueva_poblacion) < tam_poblacion:
            # elegimos padres aleatorios entre los mejores de la generación
            padres_potenciales = [item[1] for item in evaluaciones[:10]]
            padre1 = random.choice(padres_potenciales)
            padre2 = random.choice(padres_potenciales)
            
            # cruce: cortamos las secuencias y las unimos
            punto_corte = random.randint(1, max_pasos - 2)
            hijo = padre1[:punto_corte] + padre2[punto_corte:]
            
            # mutación: 5% de probabilidad de que un paso cambie al azar
            for i in range(max_pasos):
                if random.random() < 0.05:
                    hijo[i] = random.choice(movimientos)
                    
            nueva_poblacion.append(hijo)
            
        poblacion = nueva_poblacion
        
    return mejor_camino_global