características = [
('kawaii',10), ('leal',20), ('acusete',-10), ('avaro',-15), ('respetuoso',20),
('otaku',25),('lolero',25),('furro',-50),('vtuver',25),('mechero',-30)
]
amigos = [('Sneki',('leal','kawaii','vtuver')),
          ('Otaku-taku',('otaku','avaro','lolero','leal')),
          ('Maiga',('paciente','otaku','leal')),
          ('Mojojojo',('mechero','kawaii','Furro','lolero')),
          ('Seiya',('leal','acusete')),
          ('Vegeta',('otaku','avaro')),
          ('Kalila',('lolero','kawaii')),
          ('Grogu',('avaro','kawaii','lolero','otaku')),
          ('Freezer',('acusete','furro','otaku','lolero'))
]

def obtener_valor_característica(características, buscada):
    for caracter, puntos in características: #Desempaqueta la lista
        if caracter == buscada:
            return puntos
    return 0

def puntaje_amigo(amigo, características):
    nombre, caracteres = amigo #Desempaqueta la tupla
    calculo = 0
    for x in caracteres:
        busqueda = obtener_valor_característica(características,x.lower()) #.lower() porque hay un furro con la f mayuscula
        calculo += busqueda
    return calculo

#Encontrar a los amigos que conformaran su equipo
def lolcito(caracteres):  #Revisa si el amigo es lolero
    for lol in caracteres:
        if lol.lower() == 'lolero':
            return True
    return False

leagueoflegends = []
resultado_amigos = []  #Puntaje de todos los amigos dados segun el orden de la lista amigos

for x in range(len(amigos)):
    caracteres = amigos[x][1]  #Extrae las caracteristicas
    amigo = amigos[x]
    juegalol = lolcito(caracteres)
    resultado = puntaje_amigo(amigo,características)  #llamado funcion para calcualr el puntaje de todos los amigos
    resultado_amigos.append(resultado)
    if juegalol == True:
        leagueoflegends.append(amigo)

puntajes = []
for l in range(len(leagueoflegends)): #Busca encontrar los 2 mejores jugadores
    amigx = leagueoflegends[l]
    nombre = leagueoflegends[l][0]
    puntaje = puntaje_amigo(amigx,características)
    puntajes.append(puntaje)

puntajes.sort() #Menor a Mayor
puntajes.reverse()  #Mayor a Menor

for y in range(len(leagueoflegends)):
    datos = leagueoflegends[y]
    puntos = puntaje_amigo(datos,características)
    if puntos == puntajes[0]:  #El primero con mejor puntaje
        nombre_uno = leagueoflegends[y][0]
        puntaje_uno = puntos
    elif puntos == puntajes[1]: #El segundo con mejor puntaje
        nombre_dos = leagueoflegends[y][0]
        puntaje_dos = puntos

print('Equipo seleccinado:')
print(nombre_uno+',', puntaje_uno, 'puntos')
print(nombre_dos+',', puntaje_dos, 'puntos')
#print(resultado_amigos)