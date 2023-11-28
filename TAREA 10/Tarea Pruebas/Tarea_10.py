#TAREA 10
def avistamientos_por_región(nombre_archivo):
    oracion = "En el mes {mes} de {año} hubo {porcentaje} % de avistamientos confirmados de un total de {informados}"
    archivo = open(nombre_archivo)
    regiones_completas = []
    for crear in archivo:
        lista = crear.strip().split(";")
        if lista[-1] != "otros":
            if lista[1] not in regiones_completas:
                regiones_completas.append(lista[1])
                datos_region = []
                analizar = open(nombre_archivo)
                for linea in analizar:
                    revisar = linea.strip().split(";")
                    if lista[1] == revisar[1]:
                        datos_region.append(revisar)
                organizar = []
                region = datos_region[0][1]
                creacion_archivo = open(region + ".txt", "w")
                for x in range(len(datos_region)):
                    fecha = datos_region[x][0]
                    calculo = (int(datos_region[x][3])*100)/int(datos_region[x][2])
                    redondear = round(calculo,2)
                    agregar = [redondear,oracion.format(mes=fecha[5:],año=fecha[:4],porcentaje=redondear,informados=datos_region[x][2])]
                    organizar.append(agregar)
                organizar.sort()
                organizar.reverse()
                if len(organizar)>=3:
                    creacion_archivo.write(organizar[0][1]+"\n")
                    creacion_archivo.write(organizar[1][1]+"\n")
                    creacion_archivo.write(organizar[2][1]+"\n")
                else:
                    for w in range(len(organizar)):
                        creacion_archivo.write(organizar[w][1]+"\n")
                creacion_archivo.close()
                analizar.close()
    archivo.close()
    return len(regiones_completas)

print(avistamientos_por_región("ovnis_chico.csv"))