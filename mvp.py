import random
from collections import deque
import os

#algunas variables globales
personaje_elegido = None        
posiciones = {}
fin_juego = False
cache_caminos = {}


estructura_laberinto = [
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
# Guardamos posición de la meta
meta = (0, 15)

#recorrer espacios libres            
libres = []
for i in range(len(estructura_laberinto)):
    for j in range(len(estructura_laberinto[i])):
        if estructura_laberinto[i][j] == "   ":
            libres.append((i,j))
    
#colocar quesos
#cantidad = 3
#quesos = set(random.sample(libres, cantidad))
#for (f, c) in quesos:
#    estructura_laberinto[f][c] = " 🧀"
quesos = set()
    
#Las funciones
def mostrar_tablero( tablero):
    os.system('cls')
    for fila in tablero:
        print(" ".join(fila))

def movimientos_validos( posicion, es_raton = True):
    fila, col = posicion
    direcciones = [(-1,0), (1,0), (0,-1), (0,1)]
    posibles = []
    
    for df, dc in direcciones:
        nf, nc = fila + df, col + dc
        if (0 <= nf < len(estructura_laberinto) and
            0 <= nc < len(estructura_laberinto[0])):
            casilla = estructura_laberinto[nf][nc]
            
            if es_raton: 
                if casilla in ["   "," $ "]:
                    posibles.append((nf, nc))
                    
            else:  #gato
                if casilla in ["   "," $ ", " 🐁"]:
                    posibles.append((nf, nc))
    return posibles
    
def camino_mas_corto( inicio, destino):
    clave = (inicio, destino)
    
    if clave in cache_caminos:
        return cache_caminos[clave]
    
    cola = deque([(inicio, [inicio])])
    visitados = set([inicio])
    
    while cola:
        actual, camino = cola.popleft()
        if actual == destino:
            return camino
    
        # Usamos libres como referencia de movimiento válido
        for mov in [(actual[0]-1, actual[1]), (actual[0]+1, actual[1]), 
                    (actual[0], actual[1]-1), (actual[0], actual[1]+1)]:
            
            if mov in libres or mov == destino:  # solo explora casillas libres
                if mov not in visitados:
                    visitados.add(mov)
                    cola.append((mov, camino + [mov]))
                    
    cache_caminos[clave] = None           
    return None  # no hay camino
    
def posiciones_jugadores( fija = False):
    global posiciones
    if fija:
        gato_pos = (1, 1)
        raton_pos = (len(estructura_laberinto)-2, len(estructura_laberinto[0])-2)
        
    else:
        # Posiciones aleatorias iniciales
        gato_pos = random.choice(libres)
        raton_pos = random.choice(libres)

        # Evitar que salgan en la misma casilla
        while raton_pos == gato_pos:
            raton_pos = random.choice(libres)

    posiciones = {
        " 🐈": gato_pos,
        " 🐁": raton_pos
    }
    
    fila_g, col_g = gato_pos
    fila_r, col_r = raton_pos

    estructura_laberinto[fila_g][col_g] = " 🐈"
    estructura_laberinto[fila_r][col_r] = " 🐁"
    
def escoger_personaje():
        print("Bienvenido al juego del LABERINTO!!\n ~Ahora te pedite que escojas un personaje~\n")
        print("\t1)-El raton\n")
        print("\t2)-El gato\n")
        while True:
            opcion = input("Escoja una de las opciones '1' = raton , '2' = gato : ")
            
            if not opcion.isdigit():
                print("Debes ingresar un valor válido.")
                continue  # vuelve al inicio del loop
            
            opcion = int(opcion)
            
            if opcion == 1:
                personaje_elegido = " 🐁"
                break
            
            elif opcion == 2:
                personaje_elegido = " 🐈"
                break
            
            else:
                print("Ingrese una de las dos opciones por favor.")
        return personaje_elegido 
    
def esta_adyacente( pos1, pos2):
    fila1, col1 = pos1
    fila2, col2 = pos2
    
    # distancia Manhattan de 1 = adyacente
    return abs(fila1 - fila2) + abs(col1 - col2) == 1

def objetivo_raton():
    #if quesos:
    #    queso_mas_cercano = None
    #    menor_distancia = 50  # un número grande al inicio
    #    for q in quesos:
    #        camino = camino_mas_corto(posiciones[" 🐁"], q)
    #        if camino and len(camino) < menor_distancia:
    #            menor_distancia = len(camino)
    #            queso_mas_cercano = q
    #    return queso_mas_cercano
    #else:
    return meta

def siguiente_mov_raton():
    camino = camino_mas_corto(posiciones[" 🐁"], meta)
    if camino and len(camino) > 1:
        return camino[1]
    return posiciones[" 🐁"]
    
def mover_a_nueva_posicion( personaje, nueva_pos):
        global fin_juego
        
        # limpiar posición anterior
        fila, col = posiciones[personaje]
        if personaje == " 🐁":
            estructura_laberinto[fila][col] = "   "
        elif personaje == " 🐈":
            # si en la posición anterior había un queso, mantenerlo
            if (fila, col) in quesos:
                estructura_laberinto[fila][col] = " 🧀"
            else:
                estructura_laberinto[fila][col] = "   "

        # mover personaje a nueva posición
        nf, nc = nueva_pos
        
        estructura_laberinto[nf][nc] = personaje
        posiciones[personaje] = (nf, nc)
            
def jugar(personaje):
    global cache_caminos
    turno = "jugador"
    
    while not fin_juego:
        #Mostrar laberinto
        mostrar_tablero(estructura_laberinto)
        
        if turno == "jugador":
            personaje = personaje_elegido
            fila, col = posiciones[personaje]

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
            if (nueva_fila, nueva_col) in movimientos_validos((fila, col), es_raton=True):
                mover_a_nueva_posicion(personaje, (nueva_fila, nueva_col))
            else:
                print("Movimiento inválido, no puedes ir allí todavía.")
                                
            
            turno = "IA"  # cambiar turno
        else: 
            if personaje_elegido == " 🐁":
                personaje_ia = " 🐈"
                es_raton_ia = False
            else:
                personaje_ia = " 🐁"
                es_raton_ia = True
    
            pos_actual = posiciones[personaje_ia]
            
            # Elegir el mejor movimiento usando minimax
            nueva_pos = elegir_mejor_movimiento(pos_actual, es_raton_ia, prof=5)
            mover_a_nueva_posicion(personaje_ia, nueva_pos)

            #saber donde esta ahora cada uno
            pos_raton = posiciones[" 🐁"]
            pos_gato = posiciones[" 🐈"]

            # Verificar el fin del juego
            if personaje_elegido == " 🐁":
                if esta_adyacente(pos_gato, pos_raton) or pos_raton == pos_gato:
                    print("¡El gato atrapó al ratón! 😱 GAME OVER")
                    break
                if pos_raton == meta:
                    print("¡El ratón llegó a la meta! 🎉")
                    break
            else:
                if pos_raton == meta:
                    print("El ratón llegó a la meta, GAME OVER.")
                    break
                if esta_adyacente(pos_gato, pos_raton) or pos_raton == pos_gato:
                    print("¡El gato atrapó al ratón! 😱, GANASTE!")
                    break
                    
            turno = "jugador"  # cambiar turno

def distancia_manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def heuristica( raton, gato, meta):
        # Distancia Manhattan del ratón a la meta
        dist_meta = distancia_manhattan(raton, meta)

        # Distancia Manhattan del gato al ratón
        dist_gato_raton = distancia_manhattan(gato, raton)
        
        valor = dist_gato_raton * 5 - dist_meta * 3 

        return valor

#def heuristica_gato(raton, gato):
    # Un valor alto es bueno para el gato (que busca minimizar)
    #dist_gat_raton = distancia_manhattan(gato, raton)
    #return dist_gat_raton * 10

def minimax( raton, gato, profundidad, max_turno, meta, alfa, beta):
    gato_atrapa = (raton == gato)
    raton_llega_meta = (raton == meta)
    
    #print(max_turno)
    if gato_atrapa:
        # Si la IA es el ratón, esto es muy malo (-1000), si es el gato, muy bueno (+1000)
        return -1000
 
    if raton_llega_meta:
        # Si la IA es el ratón, esto es muy bueno (+1000), si es el gato, muy malo (-1000)
        return 1000

    if profundidad == 0:
        return heuristica(raton, gato, meta)
    
    if max_turno:  # turno max
        mejor_valor = -float("inf")
        for mov in movimientos_validos(raton, es_raton = True):
            valor = minimax(mov, gato, profundidad - 1, False, meta, alfa, beta)
            mejor_valor = max(mejor_valor, valor)
            alfa = max(alfa, mejor_valor)
            if beta <= alfa:
                break
        return mejor_valor
    
    else: # turno min
        peor_valor = float("inf")
        for mov in movimientos_validos(gato, es_raton = False):
            valor = minimax(raton, mov, profundidad-1, True, meta, alfa, beta)
            peor_valor = min(peor_valor, valor)
            beta = min(beta,peor_valor)
            if beta <= alfa:
                break
        return peor_valor

def elegir_mejor_movimiento( posicion, es_raton_ia, prof=5):
    """
    Devuelve el mejor movimiento para ratón o gato usando minimax.
    """
    posibles = movimientos_validos(posicion, es_raton = es_raton_ia)
    if not posibles:
        return posicion  # no hay movimiento posible

    alfa = -float("inf")
    beta = float("inf")
    mejor_mov = posicion
    
    if es_raton_ia: # IA = ratón (maximizador)
        mejor_valor = -float("inf")
        gato = posiciones[" 🐈"]
       
        for mov in posibles:
            valor = minimax(mov, gato, prof-1, False, meta, alfa, beta)
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_mov = mov
    
    else: # IA = gato (minimizador)
        peor_valor = float("inf")
        mejor_mov = posicion
        gato = posiciones[" 🐈"]
        raton = posiciones[" 🐁"]
        
        for mov in posibles:
            valor = minimax(raton, mov, prof-1, True, meta, alfa, beta)
            if valor < peor_valor:
                peor_valor = valor
                mejor_mov = mov
    return mejor_mov

# Colocar jugadores en el laberinto
posiciones_jugadores()

# Elegir personaje
personaje_elegido = escoger_personaje()

# Comenzar el por turnos
jugar(personaje_elegido)
        
