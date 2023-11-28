#Item 2b
def votos_partido(votos, partido):
    i = 0
    z = 0
    cont_votos = 0
    voto_signopeso = votos + '$'  #Se le agrega un signo peso para que sea mas facil extraer el ultimo voto
    while i < len(voto_signopeso):
        if voto_signopeso[i] == '$' :
            comprobar = voto_signopeso[z :i]
            z = i + 1
            if comprobar == partido:
                cont_votos += 1
        i += 1
    return cont_votos

def nombre_coalicion(coaliciones_puntoycoma, i, x):
    acortar = coaliciones_puntoycoma[x:i]
    z = 0
    nombre = ''
    while z < len(acortar):
        if acortar[z] == ':':
            return nombre
        else:
            nombre += acortar[z]
            z += 1

coaliciones = input('Ingrese coaliciones: ')
votos = input('Ingrese votos por partido: ')

#Quien de las coaliciones tiene mas votos
mayor = -1

#contadores
i = 0
x = 0

coaliciones_puntoycoma = coaliciones + ';'

while i < len(coaliciones_puntoycoma):
    suma = 0
    if coaliciones_puntoycoma[i] == ';':
        nombre = nombre_coalicion(coaliciones_puntoycoma, i, x)
        print('Coalicion: ', nombre)
        acortar_partidos = coaliciones_puntoycoma[x:i]
        x = i + 1
        n = 0
        while n <len(acortar_partidos):
            if acortar_partidos[n] == ':':
                n += 1
                partidos = acortar_partidos[n:]
                n += len(acortar_partidos)
            else:
                n += 1
        partidos = partidos + '-'

        t = 0
        y = 0

        while t <len(partidos):
            if partidos[t] == '-':
                partido_a_analizar = partidos[y:t]
                y = t + 1
                votos_analizar= votos_partido(votos, partido_a_analizar)
                print(partido_a_analizar, votos_analizar)
                suma += votos_analizar
            t += 1
        print('Total coalicion', nombre,': ', suma)

        if int(suma) > mayor:
            mayor = int(suma)
            votos_ganador = suma
            coalicion_ganadora = nombre
    i += 1
print('La coalicion ganadora es ', coalicion_ganadora, ' con ', votos_ganador, ' votos ')