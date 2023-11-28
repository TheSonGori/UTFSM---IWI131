def disparo(tablero, barcos, fila, columna):
    tablero_mas_barcos = list(tablero)
    for x in range(len(barcos)):
        largo = barcos[x][0]
        posicion = barcos[x][1]
        filx = barcos[x][2]
        columnx = barcos[x][3]

        if posicion == 1: #vertical
            i = 0
            while i < largo:
                tablero_mas_barcos[filx][columnx] = 'B'
                filx += 1
                i += 1
        elif posicion == 2: #horizontal
            j = 0
            while j < largo:
                tablero_mas_barcos[filx][columnx] = 'B'
                columnx += 1
                j += 1

    if tablero_mas_barcos[fila][columna] == 'B':
        tablero[fila][columna] = 'O'
    elif tablero_mas_barcos[fila][columna] == '-':
        tablero[fila][columna] = ' '
        
    eliminar = True
    filas = 0
    columnas = 0
    
    while eliminar:
        eliminar = False
        if filas == 9 or columnas == 9:
            eliminar = False
        elif tablero[filas][columnas]=='B':
            tablero[filas][columnas]='-'
            eliminar=True
        elif tablero[filas][columnas]=='-' or tablero[filas][columnas]==' ':
            eliminar=True
    for x in tablero:
        print(x)
        
tablero =[
	['-','-','-','-','-','-','-','-','-'],
	['-','-','-','-','-','-','-','-','-'],
	['-','-','-','-','-','-','-','-','-'],
	['-','-','-','-','-','-','-','-','-'],
	['-','-','-','-','-','-','-','-','-'],
	['-','-','-','-','-','-','-','-','-'],
	['-','-','-','-','-','-','-','-','-'],
	['-','-','-','-','-','-','-','-','-'],
	['-','-','-','-','-','-','-','-','-']
	]
barcos = [[2, 1, 2, 2], [3, 2, 7, 2], [3, 1, 3, 0], [4, 1, 0, 4], [5, 2, 5, 3]]

  
            
            


                

