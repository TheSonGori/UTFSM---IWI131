#Hecho por Javiera Gutierrez Abarca
#IWI131 - PARALELO 211

from math import sqrt

#Solicitud de datos de la primera sucursal
sucursal1 = input("Nombre sucursal 1: ")
s_x1 = int(input("Coordenada X: "))
s_y1 = int(input("Coordenada Y: "))

#Solicitud de datos de la segunda sucursal
sucursal2 = input("Nombre sucursal 2: ")
s_x2 = int(input("Coordenada X: "))
s_y2 = int(input("Coordenada Y: "))

#Solicitud de datos de la tercera sucursal
sucursal3 = input("Nombre sucursal 3: ")
s_x3 = int(input("Coordenada X: "))
s_y3 = int(input("Coordenada Y: "))

print("") #lo uso a lo largo del codigo para que se vea mas ordenado cuando salga en pantalla.

#Banderas
flag = True
desea = True

#Contadores
sumapedido = 0
montofinal = 0
s1 = 0
s2 = 0
s3 = 0

while desea:
    while flag:
        plato = int(input("Ingrese numero del plato: "))
        if plato == -1:
            montofinal += sumapedido

            print("Total del pedido: ", "$",sumapedido)

            x = int(input("Ingrese coordenada X del cliente: "))
            y = int(input("Ingrese coordenada Y del cliente: "))

            #la variable se vuelve a igualar a 0, porque si no seguira sumando y acumulando los valores de los pedidos
            #pasados y no dando el que buscamos.
            #por eso esta la variable montofinal que va acumulando el monto recaudado final entre todos los pedidos.
            sumapedido = 0

            # Calculo distancias (usando la formula)
            d_s1 = ((x - (s_x1))**2) + ((y - (s_y1))**2)
            d_s2 = ((x - (s_x2))**2) + ((y - (s_y2))**2)
            d_s3 = ((x - (s_x3))**2) + ((y - (s_y3))**2)
            c_s1 = sqrt(d_s1)
            c_s2 = sqrt(d_s2)
            c_s3 = sqrt(d_s3)


            #este if, elif y else busca la distancia menor entre las 3 y ademas lleva un acumulador para saber
            #cuantos pedidos lleva esa sucursal.
            if c_s1 < c_s2 and c_s1 < c_s3:
                print("El pedido sera entregado por", sucursal1)
                s1 += 1

            elif c_s2 < c_s1 and c_s2 < c_s3:
                print("El pedido sera entregado por", sucursal2)
                s2 += 1

            else:
                print("El pedido sera entregado por", sucursal3)
                s3 += 1

            pedido = input("Desea registrar otro pedido?: ")
            print("")

            #si el usario coloca "si", en la pregunta el primer y segundo ciclo seguiran activos.
            if pedido == "si":
                desea = True
                flag = True

            else:
                #Si pedido resulta ser no o cualquier caracter distinto a "si", los ciclos se tornaran a False
                #e imprimira las estadisticas finales.
                desea = False
                flag = False

        else:
            if plato == 1:
                sumapedido += 4000

            elif plato == 2:
                sumapedido += 3000

            elif plato == 3:
                sumapedido += 3500

print("")
print("#### Estadisticas Finales ####")
print("Monto total recaudado", "$", montofinal)
print(sucursal1, "entrego", s1, "pedido/s")
print(sucursal2, "entrego", s2, "pedido/s")
print(sucursal3, "entrego", s3, "pedido/s")

#montofinal es la suma de todos los totales de los pedidos.
#Cada print tiene la variable asignada para su nombre y su contador de pedidos.

'''
Casos probados en el programa;
Caso 1:
Nombre sucursal 1: Erwin
Coordenada X: 3
Coordenada Y: -4
Nombre sucursal 2: Levi
Coordenada X: 4
Coordenada Y: 6
Nombre sucursal 3: Hange
Coordenada X: 8
Coordenada Y: -3

Ingrese numero del plato: 2
Ingrese numero del plato: 1
Ingrese numero del plato: -1
Total del pedido:  $ 7000
Ingrese coordenada X del cliente: 4
Ingrese coordenada Y del cliente: -5
El pedido sera entregado por Erwin
Desea registrar otro pedido?: si

Ingrese numero del plato: 1
Ingrese numero del plato: -1
Total del pedido:  $ 4000
Ingrese coordenada X del cliente: -2
Ingrese coordenada Y del cliente: 4
El pedido sera entregado por Levi
Desea registrar otro pedido?: no


#### Estadisticas Finales ####
Monto total recaudado $ 11000
Erwin entrego 1 pedido/s
Levi entrego 1 pedido/s
Hange entrego 0 pedido/s


Caso 2:
Nombre sucursal 1: Joseph
Coordenada X: 7
Coordenada Y: 4
Nombre sucursal 2: Jotaro
Coordenada X: -7
Coordenada Y: -9
Nombre sucursal 3: Josuke
Coordenada X: -6
Coordenada Y: 4

Ingrese numero del plato: 2
Ingrese numero del plato: 1
Ingrese numero del plato: 3
Ingrese numero del plato: -1
Total del pedido:  $ 10500
Ingrese coordenada X del cliente: 0
Ingrese coordenada Y del cliente: 0
El pedido sera entregado por Josuke
Desea registrar otro pedido?: si

Ingrese numero del plato: 1
Ingrese numero del plato: 2
Ingrese numero del plato: -1
Total del pedido:  $ 7000
Ingrese coordenada X del cliente: 4
Ingrese coordenada Y del cliente: -1
El pedido sera entregado por Joseph
Desea registrar otro pedido?: si

Ingrese numero del plato: 3
Ingrese numero del plato: 2
Ingrese numero del plato: -1
Total del pedido:  $ 6500
Ingrese coordenada X del cliente: 3
Ingrese coordenada Y del cliente: 0
El pedido sera entregado por Joseph
Desea registrar otro pedido?: no


#### Estadisticas Finales ####
Monto total recaudado $ 24000
Joseph entrego 2 pedido/s
Jotaro entrego 0 pedido/s
Josuke entrego 1 pedido/s

Caso 3:
Nombre sucursal 1: Gojo
Coordenada X: 0
Coordenada Y: 0
Nombre sucursal 2: Nanami
Coordenada X: 4
Coordenada Y: -6
Nombre sucursal 3: Geto
Coordenada X: -3
Coordenada Y: 4

Ingrese numero del plato: 2
Ingrese numero del plato: 1
Ingrese numero del plato: -1
Total del pedido:  $ 7000
Ingrese coordenada X del cliente: 3
Ingrese coordenada Y del cliente: 2
El pedido sera entregado por Gojo
Desea registrar otro pedido?: si

Ingrese numero del plato: 2
Ingrese numero del plato: 1
Ingrese numero del plato: -1
Total del pedido:  $ 7000
Ingrese coordenada X del cliente: 5
Ingrese coordenada Y del cliente: -4
El pedido sera entregado por Nanami
Desea registrar otro pedido?: no


#### Estadisticas Finales ####
Monto total recaudado $ 14000
Gojo entrego 1 pedido/s
Nanami entrego 1 pedido/s
Geto entrego 0 pedido/s

'''



