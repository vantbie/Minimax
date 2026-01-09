import random
#import msvcrt  # en Windows para leer teclas sin ENTER
from collections import deque
import os

class laboratorio:
    
    def __init__(self):
        #inicializamos los jugadores
        self.personaje_elegido = None
        self.posiciones = {}
        self.fin_juego = False
        
    def laberinto(self):
        self.estructura_laberinto = [
            ["\t # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " $ ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # "],
            ["\t # ", "   ", "   ", "   ", "   ", "   ", " # ", " # ", "   ", "   ", "   ", "   ", " # ", " # ", " # ", "   ", " # ", " # ", " # ", "   ", "   ", "   ", "   ", "   ", " # ", " # ", "   ", "   ", "   ", "   ", "   ", " # "],
            ["\t # ", "   ", "   ", " # ", " # ", "   ", "   ", "   ", "   ", " # ", " # ", "   ", "   ", "   ", " # ", "   ", " # ", " # ", " # ", "   ", " # ", " # ", "   ", "   ", " # ", " # ", "   ", "   ", "   ", "   ", "   ", " # "],
            ["\t # ", "   ", "   ", " # ", " # ", "   ", "   ", "   ", "   ", " # ", " # ", "   ", "   ", "   ", "   ", "   ", " # ", " # ", "   ", "   ", " # ", " # ", "   ", "   ", " # ", "   ", "   ", "   ", "   ", "   ", "   ", " # "],
            ["\t # ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " # ", " # ", "   ", "   ", " # ", " # ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " # "],
            ["\t # ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " # ", " # ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " # "],
            ["\t # ", "   ", " # ", " # ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " # ", " # ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " # ", " # ", "   ", "   ", " # "],
            ["\t # ", "   ", " # ", " # ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " # ", " # ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " # ", " # ", "   ", "   ", " # "],
            ["\t # ", "   ", " # ", " # ", "   ", "   ", " # ", " # ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " # ", " # ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " # ", " # ", "   ", "   ", " # "],
            ["\t # ", "   ", "   ", "   ", "   ", "   ", " # ", " # ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " # ", " # ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " # ", " # ", "   ", "   ", " # "],
            ["\t # ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " # ", " # ", " # ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " # ", " # ", "   ", "   ", " # "],
            ["\t # ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " # ", " # ", " # ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " # "],
            ["\t # ", "   ", "   ", "   ", "   ", " # ", " # ", " # ", "   ", "   ", " # ", " # ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " # ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " # "],
            ["\t # ", "   ", " # ", " # ", " # ", " # ", " # ", " # ", "   ", "   ", " # ", " # ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " # ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " # "],
            ["\t # ", "   ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", "   ", "   ", "   ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", "   ", "   ", " # "],
            ["\t # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # ", " # "]
        ]
        # Guardar posición de la meta
        self.meta = (0, 15)  # la fila y columna de la "$"
        # Asegurarse que la celda tiene el "$"
        self.estructura_laberinto[self.meta[0]][self.meta[1]] = " $ "
    
    def mostrar_tablero(self, tablero):
        os.system('cls')  # o 'clear' en Linux/Mac
        for fila in tablero:
            print(" ".join(fila))
            
    def recorrer_casillas(self):
        self.libres = []
        for i in range(len(self.estructura_laberinto)):
            for j in range(len(self.estructura_laberinto[i])):
                if self.estructura_laberinto[i][j] == "   ":
                    self.libres.append((i,j))
    
    def colocar_quesos(self, cantidad=5):
        self.quesos = set(random.sample(self.libres, cantidad))
        for (f, c) in self.quesos:
            self.estructura_laberinto[f][c] = " 🧀"

    def movimientos_validos(self, posicion, es_raton = True):
        fila, col = posicion
        direcciones = [(-1,0), (1,0), (0,-1), (0,1)]
        posibles = []
        for df, dc in direcciones:
            nf, nc = fila + df, col + dc
            if (0 <= nf < len(self.estructura_laberinto) and
                0 <= nc < len(self.estructura_laberinto[0])):
                casilla = self.estructura_laberinto[nf][nc]
                if es_raton:
                    # solo permitir moverse a la meta si no quedan quesos
                    if casilla in ["   ", " 🧀"]:
                        posibles.append((nf, nc))
                    elif casilla == " $ " and not self.quesos:
                        posibles.append((nf, nc))
                else:  # gato
                    if casilla in ["   ", " $ "]:  # gato no toca quesos
                        posibles.append((nf, nc))
        return posibles
    
    def camino_mas_corto(self, inicio, destino):
        cola = deque([(inicio, [inicio])])
        visitados = set([inicio])
        
        while cola:
            actual, camino = cola.popleft()
            if actual == destino:
                return camino
            
            # Usamos self.libres como referencia de movimiento válido
            for mov in [(actual[0]-1, actual[1]), (actual[0]+1, actual[1]), 
                        (actual[0], actual[1]-1), (actual[0], actual[1]+1)]:
                
                if mov in self.libres or mov == destino:  # solo explora casillas libres
                    if mov not in visitados:
                        visitados.add(mov)
                        cola.append((mov, camino + [mov]))
        return None  # no hay camino
    
    def posiciones_jugadores(self, fija = False):
        if fija:
        # Posiciones predeterminadas (útil para debug)
            gato_pos = (1, 1)     # ejemplo
            raton_pos = (len(self.estructura_laberinto)-2, len(self.estructura_laberinto[0])-2)
        else:
            # Posiciones aleatorias iniciales
            gato_pos = random.choice(self.libres)
            raton_pos = random.choice(self.libres)

            # Evitar que salgan en la misma casilla
            while raton_pos == gato_pos:
                raton_pos = random.choice(self.libres)

        #self.posicion_gato = gato_pos
        #self.posicion_raton = raton_pos
            
        # Diccionario general
        self.posiciones = {
            " 🐈": gato_pos,
            " 🐁": raton_pos
        }
        
        fila_g, col_g = gato_pos
        fila_r, col_r = raton_pos

        self.estructura_laberinto[fila_g][col_g] = " 🐈"
        self.estructura_laberinto[fila_r][col_r] = " 🐁"
    
    def escoger_personaje(self):
        print("Bienvenido al juego del LABERINTO!!\n ~Ahora te pedite que escojas un personaje~\n")
        print("\t1)-El raton (pequeño pero muy veloz)\n")
        print("\t2)-El gato (GRANDE pero un poco lento)\n")
        while True:
            opcion = input("Escoja una de las opciones '1' = raton , '2' = gato : ")
            
            if not opcion.isdigit():
                print("Debes ingresar un valor válido.")
                continue  # vuelve al inicio del loop
            
            opcion = int(opcion)
            
            if opcion == 1:
                self.personaje_elegido = " 🐁"
                break
            elif opcion == 2:
                self.personaje_elegido = " 🐈"
                break
            else:
                print("Ingrese una de las dos opciones por favor.")

    def esta_adyacente(self, pos1, pos2):
        fila1, col1 = pos1
        fila2, col2 = pos2
        # distancia Manhattan de 1 = adyacente
        return abs(fila1 - fila2) + abs(col1 - col2) == 1
    
    def mover_a(self, personaje, nueva_pos):
        # limpiar posición anterior
        fila, col = self.posiciones[personaje]
        if personaje == " 🐁":
            self.estructura_laberinto[fila][col] = "   "
        elif personaje == " 🐈":
            # si en la posición anterior había un queso, mantenerlo
            self.estructura_laberinto[fila][col] = " 🧀" if (fila, col) in self.quesos else "   "

        # mover personaje a nueva posición
        nf, nc = nueva_pos
        if personaje == " 🐁" and nueva_pos in self.quesos:
            self.quesos.remove(nueva_pos)  # ratón come el queso
        self.estructura_laberinto[nf][nc] = personaje
        self.posiciones[personaje] = (nf, nc)

        # Verificar si el ratón llegó a la meta
        if personaje == " 🐁" and (nf, nc) == self.meta:
            if self.quesos:
                print("Debes agarrar todos los quesos antes de llegar a la meta!")
            else:
                print("¡El ratón llegó a la meta con todos los quesos! 🎉")
                self.fin_juego = True  # Terminar juego
            
        
    def jugar(self):
        turno = "jugador"  # o "IA"
        
        while not self.fin_juego:
            # Mostrar laberinto
            self.mostrar_tablero(self.estructura_laberinto)
            print("\n")
            
            self.fin_juego = False
            
            if turno == "jugador":
                personaje = self.personaje_elegido
                fila, col = self.posiciones[personaje]

                direccion = input("Tu turno (w/a/s/d): ").lower()
                if direccion == "w":
                    nueva_fila, nueva_col = fila-1, col
                elif direccion == "s":
                    nueva_fila, nueva_col = fila+1, col
                elif direccion == "a":
                    nueva_fila, nueva_col = fila, col-1
                elif direccion == "d":
                    nueva_fila, nueva_col = fila, col+1
                elif direccion == "salir":
                    print("Juego terminado")
                    break
                else:
                    print("Dirección inválida")
                    continue

                # Verificar movimiento válido
                if (nueva_fila, nueva_col) in self.movimientos_validos((fila, col), es_raton=True):
                    self.mover_a(personaje, (nueva_fila, nueva_col))
                else:
                    print("Movimiento inválido, no puedes ir allí todavía.")
                                    
                
                turno = "IA"  # cambiar turno
            else:  # turno de la IA
                if self.personaje_elegido == " 🐁":
                    personaje_ia = " 🐈"
                    es_raton = False
                else:
                    personaje_ia = " 🐁"
                    es_raton = True

                pos_actual = self.posiciones[personaje_ia]
                nueva_pos = self.elegir_mejor_movimiento(pos_actual, es_raton, prof=2)
                self.mover_a(personaje_ia, nueva_pos)

                
                # turno de la IA
                pos_raton = self.posiciones[" 🐁"]
                pos_gato = self.posiciones[" 🐈"]

                # Verificar fin de juego
                if self.personaje_elegido == " 🐁":
                    if self.esta_adyacente(pos_gato, pos_raton) or pos_raton == pos_gato:
                        print("¡El gato atrapó al ratón! 😱 GAME OVER")
                        break

                    # Ratón llegó a la meta con todos los quesos
                    if pos_raton == self.meta and not self.quesos:
                        print("¡El ratón llegó a la meta con todos los quesos! 🎉")
                        break

                    # Si ratón llega a la meta pero aún quedan quesos, solo aviso
                    if pos_raton == self.meta and self.quesos:
                        print("Debes agarrar todos los quesos antes de salir!")
                else:
                    if self.posiciones[" 🐁"] == self.meta:
                        print("El raton llegó a la meta, GAME OVER.")
                        break
                    elif self.esta_adyacente(pos_gato, pos_raton):
                        print("¡El gato atrapó al ratón! 😱, GANASTE!")
                        break
                    elif pos_raton == pos_gato:
                        print("El gato atrapó al raton! 😱 GANASTE.")
                        break
                     
                turno = "jugador"  # cambiar turno

    
        
    def heuristica(self, raton, gato, meta):
        # Camino más corto del ratón a la meta
        camino_meta = self.camino_mas_corto(raton, meta)
        dist_meta = len(camino_meta) - 1 if camino_meta else 50  

        # Camino más corto del gato al ratón
        camino_gato = self.camino_mas_corto(gato, raton)
        dist_gato = len(camino_gato) - 1 if camino_gato else 50

        # Espacios libres alrededor del ratón
        libres_raton = len(self.movimientos_validos(raton))

        # Base: evitar al gato importa más que ir a la meta
        valor = (dist_gato * 4) - dist_meta   # 💡 aumenté el peso de dist_gato

        # Penalización extra si el ratón está muy cerca del gato
        if dist_gato <= 2:
            valor -= 10   # 👈 fuerte castigo por acercarse demasiado

        # Penalizar si están alineados (línea de visión)
        if raton[0] == gato[0] or raton[1] == gato[1]:
            valor -= 7    # 👈 castigo medio

        # Penalizar si tiene pocas opciones de escape
        if libres_raton <= 1:
            valor -= 5

        return valor
    
    def minimax(self, raton, gato, profundidad, max_turno, meta):
        if raton == gato:  # gato atrapó al ratón
            return -1
        if raton == meta:  # ratón llega a la meta
            return 1
        if profundidad == 0:
            return self.heuristica(raton, gato, meta)
        
        if max_turno:  # turno del ratón
            mejor_valor = -float("inf")
            for mov in self.movimientos_validos(raton):
                valor = self.minimax(mov, raton, profundidad-1, False, meta)
                mejor_valor = max(mejor_valor, valor)
            return mejor_valor
        
        else:  # turno del gato
            peor_valor = float("inf")
            for mov in self.movimientos_validos(gato):
                valor = self.minimax(mov, gato, profundidad-1, False, meta)
                peor_valor = min(peor_valor, valor)
            return peor_valor

    def elegir_mejor_movimiento(self, posicion, es_raton, prof=5):
        """
        Devuelve el mejor movimiento para ratón o gato usando minimax.
        """
        if es_raton:  # ratón busca la salida
            camino = self.camino_mas_corto(posicion, self.meta)
        else:  # gato busca al ratón
            raton = self.posiciones[" 🐁"]
            camino = self.camino_mas_corto(posicion, raton)

        if camino and len(camino) > 1:
            return camino[1]  # el siguiente paso
        return posicion  # si no hay camino, quedarse quieto
    


# Crear instancia
juego = laboratorio()

# Inicializar laberinto
juego.laberinto()

# Obtener lista de casillas libres
juego.recorrer_casillas()

juego.colocar_quesos(cantidad=3)
# Colocar jugadores en el laberinto
juego.posiciones_jugadores()  # si querés posiciones fijas para debug: juego.posiciones_jugadores(fija=True)

# Elegir personaje
juego.escoger_personaje()

# Comenzar el juego por turnos
juego.jugar()

        
