#Pregunta 1
def sismos_por_pais(archivo_sismos):
    arch = open(archivo_sismos)
    estados_unidos = open("estados_eeuu.txt")
    eeuu = []
    for estado in estados_unidos:
        estado = estado.strip().split("\n")
        eeuu.append(estado)
    estados_unidos.close()

    diccionario = {} #{lugar:cantidad_de_sismos}
    for linea in arch:
        linea = linea.strip().split(";")
        magnitud = linea[-2]
        lugar = linea[-1]
        if float(magnitud) >= 2:
            transformar = [lugar]
            if transformar in eeuu:
                lugar = 'EEUU'
            if lugar not in diccionario:
                diccionario[lugar] = 0
            diccionario[lugar] += 1

    arch.close()
    sismos = [] #[()]
    for llave in diccionario:
        cantidad = diccionario[llave]
        pais = llave
        sismos.append((cantidad,pais))
    sismos.sort()
    sismos.reverse()
    return sismos

#print(sismos_por_pais('sismos.txt'))