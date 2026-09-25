import numpy as np

class Mapa: 
    def __init__(self, tipo_mapa, k_turnos_fuego=3): 
        # tipos de mapa en generar_mapa 
        self.tipo_mapa = tipo_mapa 
        self.grilla = self.generar_mapa()
        
        # calcular la densidad de las celdas por la cantidad de personas
        self.densidad_celdas = np.zeros_like(self.grilla) 
        
        self.k_turnos_fuego = k_turnos_fuego
        self.turno_actual = 0
        
    def generar_mapa(self):
        # aca se elige y generan los mapas distintos
        if self.tipo_mapa == 1:
            # densidad alta
            mapa_1 = np.array([
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 1, 0, 0, 0, 1, 0, 3, 1],
                [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1], 
                [1, 0, 2, 1, 1, 1, 1, 1, 0, 1, 1], # el 2 es el fuego inicial
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            ])
            return mapa_1
        elif self.tipo_mapa == 2:
            # densidad mediana
            mapa_2 = np.array([
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1, 0, 0, 0, 0, 3, 1],
                [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 0, 1, 2, 0, 0, 1], # fuego inicial en el centro
                [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            ])
            return mapa_2
        elif self.tipo_mapa == 3:
            # densidad baja
            mapa_3 = np.array([
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
                [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 1, 2, 0, 0, 0, 0, 1], # fuego en un pilar central
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            ])
            return mapa_3
            
    def propagar_fuego(self):
        # pasa un turno mas
        self.turno_actual += 1
        
        if self.turno_actual % self.k_turnos_fuego == 0:
            posiciones_fuego = np.argwhere(self.grilla == 2)
            nuevas_posiciones_fuego = []

            # el fuego se expande a las casillas adyacentes
            for fila, col in posiciones_fuego:
                vecinos = [(fila-1, col), (fila+1, col), (fila, col-1), (fila, col+1)]
                
                for f, c in vecinos:
                    # restriccion de limites con el mapa
                    if 0 <= f < self.grilla.shape[0] and 0 <= c < self.grilla.shape[1]:
                        if self.grilla[f, c] == 0:
                            nuevas_posiciones_fuego.append((f, c))

            # actualizamos las casillas para propagar el fuego
            for f, c in nuevas_posiciones_fuego:
                self.grilla[f, c] = 2
        
    def calcular_costo_celda(self, x, y):
        if self.grilla[x, y] == 1 or self.grilla[x, y] == 2:
            return float('inf')
            
        # pasillos libres 0 o salida 3
        cantidad_personas = self.densidad_celdas[x, y]
        costo_base = 1
        
        # si hay 0 personas, costo es 1, si hay 1 persona, costo es 2, si son 3 personas, entonces el costo es 10
        # el costo total se medira con la exponencial de 2 por la cantidad de personas, mas el costo base (que es 1)
        costo_total = costo_base + (cantidad_personas ** 2) 
        
        return costo_total

