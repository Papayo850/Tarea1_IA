class Agente:
    def __init__(self, id_agente, x_inicial, y_inicial):
        self.id_agente = id_agente
        self.x = x_inicial
        self.y = y_inicial
        self.evacuado = False # estado de si escapo o no
        self.vivo = True      # estado de vivo o muerto (osea si lo toco el fuego o no)
        self.turnos_tomados = 0

    def obtener_movimientos_posibles(self):
        return {
            "arriba": (self.x - 1, self.y),
            "abajo": (self.x + 1, self.y),
            "izquierda": (self.x, self.y - 1),
            "derecha": (self.x, self.y + 1),
            "esperar": (self.x, self.y)
        }

    def mover(self, nueva_x, nueva_y):
        if self.vivo and not self.evacuado:
            self.x = nueva_x
            self.y = nueva_y
            self.turnos_tomados += 1
            
    def morir(self): 
        # si el fuego lo alcanza, muere
        self.vivo = False
        
    def salvarse(self):
        # si llega a la casilla 3 (salida), escapa
        self.evacuado = True