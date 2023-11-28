#Pregunta 2
def categorizar_sismos(archivo_sismos):
    arch = open(archivo_sismos)
    diccionario = {} #{categoria:[(magnitud,fecha,hora,lugar)...]}

    for linea in arch:
        linea = linea.strip().split(";")

        magnitud = linea[-2]
        lugar = linea[-1]
        fecha_tiempo_hora = linea[0]
        separar_t = fecha_tiempo_hora.split("T")
        fecha = separar_t[0] #aaaa-mm-dd
        hora_tiempo = separar_t[1]
        hora = hora_tiempo[:5]

        if float(magnitud) >= 2:
            numero_flotante = float(magnitud)
            numero_entero = int(numero_flotante)
            if numero_entero not in diccionario:
                diccionario[numero_entero] = []
            agregar = (magnitud,fecha,hora,lugar) #(magnitud,fecha,hora,lugar)
            diccionario[numero_entero].append(agregar)
    arch.close()

    oracion = "Fecha: {fecha_f}; Hora: {hora_f}; Lugar: {lugar_f}; Magnitud: {mag_f}."

    for llave in diccionario:

        numero = str(llave)
        x = diccionario[llave]
        x.sort()
        x.reverse()
        crear = open("mag" + numero + ".txt", "w")  # magN.txt
        crear.write(oracion.format(fecha_f=x[0][1], hora_f=x[0][2], lugar_f=x[0][-1], mag_f=x[0][0]) + "\n")
        crear.write(oracion.format(fecha_f=x[1][1], hora_f=x[1][2], lugar_f=x[1][-1], mag_f=x[1][0]) + "\n")
        crear.write(oracion.format(fecha_f=x[2][1], hora_f=x[2][2], lugar_f=x[2][-1], mag_f=x[2][0]) + "\n")
        crear.close()

    return len(diccionario)

print(categorizar_sismos('sismos.txt'))