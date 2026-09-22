import numpy as np

class Mapa:
    def __init__(self, tipo_mapa):
        #tipos de mapa en generar_mapa
        self.tipo_mapa = tipo_mapa
        self.grilla = self.generar_mapa()

        #calcular la densidad de las celdas por la cantidad de personas
        self.densidad_celdas = np.zeros_like(self.grilla) 
        
    def generar_mapa(self):
        #aca se elige y generan los mapas distintos
        if self.tipo_mapa == 1:
            # alta densidad
            mapa_1 = np.array([
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 1, 0, 0, 0, 1, 0, 3, 1],
                [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1], 
                [1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            ])
            pass
        elif self.tipo_mapa == 2:
            # media densidad
            pass
        elif self.tipo_mapa == 3:
            # baja densidad
            pass
            
    def propagar_fuego(self):
        # logica del fuego
        pass
        
    def calcular_costo_celda(self, x, y):
        #costo de celdas como 0= vacio, 1= obstaculo, 2= fuego, 3= salida
        pass