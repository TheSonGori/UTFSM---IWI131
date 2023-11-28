def disparo(tablero, barcos, fila, columna):
    for x in range(len(barcos)):
        largo = barcos[x][0]
        posicion = barcos[x][1]
        filx = barcos[x][2]
        columnx = barcos[x][3]

        if posicion==1: #vertical
            v = 0
            while v < largo:
                if filx== fila and columnx==columna:
                    tablero[fila][columna] = 'O'
                filx += 1
                v += 1
            if tablero[fila][columna] != 'O':
                tablero[fila][columna] = ' '

        elif posicion==2: #horizontal
            h = 0
            while h < largo:
                if filx== fila and columnx==columna:
                    tablero[fila][columna] = 'O'
                columnx+= 1
                h += 1
            if tablero[fila][columna] != 'O':
                tablero[fila][columna] = ' '

def destruidos(tablero, barcos):
    for r in range(len(barcos)):
        largo = barcos[r][0]
        posicion = barcos[r][1]
        filx = barcos[r][2]
        columnx = barcos[r][3]

        if posicion == 1:  # vertical
            v = 0
            casi = 0
            inicio = filx  # para no perder de donde inicia el barco
            while v < largo:
                if tablero[filx][columnx] == 'O':
                    filx += 1
                elif tablero[filx][columnx] != 'O':
                    casi = 1000
                v += 1
            if casi != 1000:
                cambio = 0
                while cambio < largo:
                    tablero[inicio][columnx] = 'X'
                    inicio += 1
                    cambio += 1

        elif posicion == 2:  # horizontal
            h = 0
            casi = 0
            inicio = columnx
            while h < largo:
                if tablero[filx][columnx] == 'O':
                    columnx += 1
                elif tablero[filx][columnx] != 'O':
                    casi = 1000
                h += 1
            if casi != 1000:
                cambio = 0
                while cambio < largo:
                    tablero[filx][inicio] = 'X'
                    inicio += 1
                    cambio += 1
    cont = 0
    for contador in range(len(barcos)):
        largo = barcos[contador][0]
        posicion = barcos[contador][1]
        filx = barcos[contador][2]
        columnx = barcos[contador][3]

        if posicion == 1:  # vertical
            v = 0
            finalmente = 0
            while v < largo:
                if tablero[filx][columnx] == ' ' or tablero[filx][columnx] == '-':
                    finalmente = 1000
                filx += 1
                v += 1
            if finalmente == 0:
                cont += 1

        elif posicion == 2:  # horizontal
            h = 0
            finalmente = 0
            while h < largo:
                if tablero[filx][columnx] == ' ' or tablero[filx][columnx] == '-':
                    finalmente = 1000
                columnx += 1
                h += 1
            if finalmente == 0:
                cont += 1
    return cont

# OPCIONAL:
# Cambie el valor de esta variable a 1 si desea ver
# la ubicación de los barcos antes de comenzar.
# Esto puede ser útil para probar sus funciones.
mostrar_solucion = 0



##################################################
#                                                #
#  NO MODIFIQUE EL CÓDIGO A PARTIR DE ESTE PUNTO #
#                                                #
##################################################

import random as rd

# Función que muestra el tablero con el formato deseado para la pantalla
def show(tablero):
    print("\n  123456789")
    for i in range(9):
        fila_texto = " "
        for j in tablero[i]:
            fila_texto += str(j)
        print(chr(65+i)+fila_texto)

# Creación del tablero (inicialmente únicamente con "-" en todas las posiciones)
tablero = []
board = []
for i in range(9):
    fila = []
    for j in range(9):
        fila.append("-")
    tablero.append(fila)
    board.append(list(fila))

# Creación de los barcos con orientación y posición aleatorias
barcos = []
length = [2,3,3,4,5]
for i in range(5):
    l = length[i]
    orientation = rd.randint(1,2)
    if orientation == 1:
        flag = True
        while flag:
            row = rd.randint(0,9-l)
            column = rd.randint(0,8)
            empty = True
            for j in range(l):
                empty = empty and board[row+j][column] != "X"
            if empty:
                flag = False
        for j in range(l): board[row+j][column] = "X"
    else:
        flag = True
        while flag:
            row = rd.randint(0,8)
            column = rd.randint(0,9-l)
            if "X" not in board[row][column:column+l]:
                flag = False
        for j in range(l): board[row][column+j] = "X"
    barcos.append([l,orientation,row,column])
print(barcos)
# Se muestra la solución al inicio en caso de que se haya seleccionado esta opción
if mostrar_solucion == 1:
    print("Solución:")
    show(board)
    print("\n\n")

# Ciclo principal del programa donde se reciben los disparos, se validan y se llama a la función disparo()
print("¡Bienvenido a Solitary Battleship!")
destroyed = 0
while destroyed < 5:
    not_valid = True
    while not_valid:
        turn = input("\n¿Que casilla desea disparar? (Ejemplo: A1): ")
        not_valid = False
        if len(turn) != 2:
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        elif not("A" <= turn[0] and turn[0] <= "I"):
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        elif not("1" <= turn[1] and turn[1] <= "9"):
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        else:
            fila = "ABCDEFGHI".index(turn[0])
            columna = int(turn[1])-1
            if tablero[fila][columna] != "-":
                not_valid = True
                print("Ya ha disparado a esta casilla.")
    disparo(tablero, barcos, fila, columna)
    destroyed = destruidos(tablero, barcos)
    show(tablero)
    print("\n"+str(destroyed)+" barcos destruidos.")
    # Fin del juego
    if destroyed == 5:
        print("Felicidades, juego terminado.")
