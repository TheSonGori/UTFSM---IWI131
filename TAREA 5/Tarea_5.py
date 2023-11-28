#TAREA HECHA POR JAVIERA GUTIERREZ ABARCA
#IWI131 - PARALELO 211

#Funcion para poder sacar la raiz cubica
def raiz_cubica(numero):
    return numero**(1/3)

#Funcion para la media aritmetica
def media_aritmetica(a, b, c):
    c = (a + b + c)/3
    ma = round(c)
    return ma

#Funcion para la media geometrica
def media_geometrica(p, q, t):
    c = p * q * t
    r = raiz_cubica(c)
    mg = round(r)
    return mg

#Funcion para la media vuelta + usando funcion de media aritmetica
def media_vuelta(x, y, z):
    c = z * ((media_aritmetica(x, y, z))**2)
    r = raiz_cubica(c)
    mv = round(r)
    return mv

'''
Las 3 media estan redondeadas al 
'''


#Funcion para ver si aprueba con algun metodo calculado anteriormente y si no aprueba con ningun metodo se retorna 0
def aprobacion (nf_aritmetica, nf_geometrica, nf_vuelta):
    if nf_aritmetica >= 55:  #mayor o igual a 55
        return 1
    elif nf_geometrica >= 55:  #mayor o igual a 55
        return 2
    elif nf_vuelta >= 55:  #mayor o igual a 55
        return 3
    else:
        return 0  #Si ninguna de las anteriores es mayor o igual a 55, se retorna 0


pedir_notas = True
while pedir_notas:
    ramo = input("Ingrese el nombre del ramo: ")

    if ramo == "salir":
        pedir_notas = False
        print("Fin del programa - Desarrollado por Kiwi :D!")
    else:
        n1 = int(input("Ingrese la 1era nota: "))
        n2 = int(input("Ingrese la 2era nota: "))
        n3 = int(input("Ingrese la 3era nota: "))

        # llamado funciones
        nf_aritmetica = media_aritmetica(n1, n2, n3)
        nf_geometrica = media_geometrica(n1, n2, n3)
        nf_vuelta = media_vuelta(n1, n2, n3)

        print("Su nota final según la Media Aritmética es:", nf_aritmetica)
        print("Su nota final según la Media Geométrica es:", nf_geometrica)
        print("Su nota final según la Media Vuelta es:", nf_vuelta)

        # llamado funcion para ver si aprueba con algunas de las medias
        nf_aprobacion = aprobacion(nf_aritmetica, nf_geometrica, nf_vuelta)

        if nf_aprobacion == 0:
            print("Lamentablemente no puedes aprobar", ramo, "con ninguna de las fórmulas :'c")
            print("")

        elif nf_aprobacion == 1:
            print("Si la NF del ramo se calcula usando la Media Aritmética, entonces apruebas", ramo, ":D")
            print("")


        elif nf_aprobacion == 2:
            print("Si la NF del ramo se calcula usando la Media Geométrica, entonces apruebas", ramo, ":D")
            print("")

        elif nf_aprobacion == 3:
            print("Si la NF del ramo se calcula usando la Media Vuelta, entonces apruebas", ramo, ":D")
            print("")


#print("") lo uso para que cuando se imprima por pantalla se vea mas ordenado


'''
CASO 1:

Ingrese el nombre del ramo: Programacion
Ingrese la 1era nota: 75
Ingrese la 2era nota: 50
Ingrese la 3era nota: 45
Su nota final según la Media Aritmética es: 57
Su nota final según la Media Geométrica es: 55
Su nota final según la Media Vuelta es: 53
Si la NF del ramo se calcula usando la Media Aritmética, entonces apruebas Programacion :D

Ingrese el nombre del ramo: Matematicas
Ingrese la 1era nota: 45
Ingrese la 2era nota: 53
Ingrese la 3era nota: 68
Su nota final según la Media Aritmética es: 55
Su nota final según la Media Geométrica es: 55
Su nota final según la Media Vuelta es: 59
Si la NF del ramo se calcula usando la Media Aritmética, entonces apruebas Matematicas :D

Ingrese el nombre del ramo: salir
Fin del programa - Desarrollado por Kiwi :D!



CASO 2:

Ingrese el nombre del ramo: Extension de Dominio
Ingrese la 1era nota: 78
Ingrese la 2era nota: 65
Ingrese la 3era nota: 48
Su nota final según la Media Aritmética es: 64
Su nota final según la Media Geométrica es: 62
Su nota final según la Media Vuelta es: 58
Si la NF del ramo se calcula usando la Media Aritmética, entonces apruebas Extension de Dominio :D

Ingrese el nombre del ramo: salir
Fin del programa - Desarrollado por Kiwi :D!



CASO 3:

Ingrese el nombre del ramo: FIS100
Ingrese la 1era nota: 50
Ingrese la 2era nota: 60
Ingrese la 3era nota: 72
Su nota final según la Media Aritmética es: 61
Su nota final según la Media Geométrica es: 60
Su nota final según la Media Vuelta es: 64
Si la NF del ramo se calcula usando la Media Aritmética, entonces apruebas FIS100 :D

Ingrese el nombre del ramo: HRW133
Ingrese la 1era nota: 40
Ingrese la 2era nota: 55
Ingrese la 3era nota: 30
Su nota final según la Media Aritmética es: 42
Su nota final según la Media Geométrica es: 40
Su nota final según la Media Vuelta es: 38
Lamentablemente no puedes aprobar HRW133 con ninguna de las fórmulas :'c

Ingrese el nombre del ramo: salir
Fin del programa - Desarrollado por Kiwi :D!

'''