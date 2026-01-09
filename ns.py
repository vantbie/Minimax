import random

class TicTacToe:
    def __init__(self):
       # Inicializar tablero vacío (usando ' ' para casillas vacías)
       self.tablero = [" " for _ in range(9)]
       self.jugador_humano = "O"
       self.jugador_ia = "X"

    def imprimir_tablero(self):
       """Imprimir el estado actual del tablero"""
       for i in range(0, 9, 3):
           print(f"{self.tablero[i]} | {self.tablero[i+1]} | {self.tablero[i+2]}")
           if i < 6:
               print("---------")

    def movimientos_disponibles(self):
       """Devuelve la lista de movimientos disponibles (índices de casillas vacías)"""
       return [i for i, spot in enumerate(self.tablero) if spot == " "]
   
    def haz_un_movimiento(self, posicion, jugador):
       """Haz un movimiento en el tablero"""
       if self.tablero[posicion] == " ":
           self.tablero[posicion] = jugador
           return True
       return False
    
    def tablero_lleno(self):
       """Comprueba si el tablero está lleno"""
       return " " not in self.tablero
   
    def evaluar_ganador(self):
       """Comprueba si hay un ganador. Devuelve el símbolo de ganador o Ninguno."""
       # evalua las lineas
       for i in range(0, 9, 3):
           if self.tablero[i] == self.tablero[i + 1] == self.tablero[i + 2] != " ":
               return self.tablero[i]

       # evalua las columnas
       for i in range(3):
           if self.tablero[i] == self.tablero[i + 3] == self.tablero[i + 6] != " ":
               return self.tablero[i]

       # evalua las diagonales
       if self.tablero[0] == self.tablero[4] == self.tablero[8] != " ":
           return self.tablero[0]
       
       if self.tablero[2] == self.tablero[4] == self.tablero[6] != " ":
           return self.tablero[2]

       return None
   
    def game_over(self):
       """Chequea si el juego termino"""
       return self.evaluar_ganador() is not None or self.tablero_lleno()
    
    def minimax(self, profundidad, maximizar):
        """
        Implementación del algoritmo Minimax
            Devuelve la mejor puntuación posible para el estado actual del tablero.
        """
        # casos
        ganador = self.evaluar_ganador()
        if ganador == self.jugador_ia:
            return 1
        if ganador == self.jugador_humano:
            return -1
        if self.tablero_lleno():
            return 0
    
        # Si es el turno del jugador maximizador (IA), queremos maximizar la puntuación
        if maximizar:
            mejor_puntuacion = float("-inf")
            for mover in self.movimientos_disponibles():
                # Hace un movimiento calculador
                self.tablero[mover] = self.jugador_ia
                # Llamar recursivamente a minimax con la siguiente profundidad y el jugador minimizador
                marcador = self.minimax(profundidad + 1, False)
                # Resetear el movimiento
                self.tablero[mover] = " "
                # Actualiza la mejor puntuación
                mejor_puntuacion = max(marcador, mejor_puntuacion)
            return mejor_puntuacion
        else:
            # Si es el turno del jugador minimizador (humano), queremos minimizar la puntuación
            mejor_puntuacion = float("inf")
            for mover in self.movimientos_disponibles():
                # Hace un movimiento calculador
                self.tablero[mover] = self.jugador_humano
                # Llamar recursivamente a minimax con la siguiente profundidad y el jugador que maximiza
                marcador = self.minimax(profundidad + 1, True)
                # Resetear el movimiento
                self.tablero[mover] = " "
                # actualiza la mejor puntuacion
                mejor_puntuacion = min(marcador, mejor_puntuacion)
            return mejor_puntuacion
        
    def agarra_el_mejor_movimiento(self):
       """Encuentra el mejor movimiento para la IA usando minimax"""
       mejor_puntuacion = float("-inf")
       mejor_movimiento = None

       for mover in self.movimientos_disponibles():
           # Haz un movimiento calculador
           self.tablero[mover] = self.jugador_ia
           # Llamar recursivamente a minimax con la siguiente profundidad y el jugador minimizador
           marcador = self.minimax(0, False)
           # Resetea el movimiento
           self.tablero[mover] = " "

           # actualiza la mejor puntuacion
           if marcador > mejor_puntuacion:
               mejor_puntuacion = marcador
               mejor_movimiento = mover

       return mejor_movimiento
   
   
    def jugar(self):
       """Main del ciclo"""
       print("Bienvenido a Tic Tac Toe!")
       print("Tu usaras el 'O' y la maquina usara la'X'")
       print("Colaca las posiciones (0-8), aqui las puedes visualizar:")
       print("0 | 1 | 2")
       print("---------")
       print("3 | 4 | 5")
       print("---------")
       print("6 | 7 | 8")
       print("\n")
        
       turno_ia = random.choice([True, False])
       
       while not self.game_over():
        self.imprimir_tablero()

        if turno_ia:
            print("\nTurno de la maquina..")
            mover = self.agarra_el_mejor_movimiento()
            self.haz_un_movimiento(mover, self.jugador_ia)
        else:
            while True:
                try:
                    mover = int(input("\nEs tu turno (0-8): "))
                    if 0 <= mover <= 8 and self.haz_un_movimiento(mover, self.jugador_humano):
                        break
                    else:
                            print("Movimiento invalido! intentalo otra vez.")
                except ValueError:
                        print("Por favor coloca un numero que este entre el 1 y el 8!")

        turno_ia = not turno_ia
        
        #Game over
        self.imprimir_tablero()
        ganador = self.evaluar_ganador()
        if ganador == self.jugador_ia:
            print("\nLa maquina te a vencido!")
        elif ganador == self.jugador_humano:
            print("\Felicidades! Haz ganado!")
        else:
            print("\nEs un empate!")
    
if __name__ == "__main__":
   game = TicTacToe()
   game.jugar()