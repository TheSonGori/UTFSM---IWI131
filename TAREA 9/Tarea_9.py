vacunas = {
 "Sinovac":["11.111.111-1", "12.345.678-9"],
 "Pfizer": ["8.978.657-3"],
 "CanSino": ["13.789.456-k"]
}
dosis = {
 "11.111.111-1":[55,(2021,4,11),(2021,5,10)],
 "12.345.678-9":[47,(2021,6,3)],
 "8.978.657-3":[79,(2021,3,23)],
 "13.789.456-k":[40,(2021,5,18),(2021,6,10)]
}
#vacunas = {}
#dosis = {}
print("############################################################")
print("INGRESE FECHA")
dia = int(input("Día:\t"))
mes = int(input("Mes:\t"))
año = int(input("Año:\t"))
fecha = (año, mes, dia)

print("\n############################################################")
def revisar_dosis(rut, dosis):
    # Retornara 1 si solo tiene una dosis, 2 si tiene dos dosis y 0 si no esta registrado.
    if len(dosis) == 0:
        return 0
    else:
        for llave in dosis:
            if llave == rut:
                if len(dosis[llave]) == 3:
                    return 2
                elif len(dosis[llave]) == 2:
                    return 1
        return 0

def actualizar(fecha,rut,dosis):
    #Ingresa la segunda fecha a las personas que ya tenian primera dosis inyectada
    for llave in dosis:
        if llave == rut:
            dosis[llave].append(fecha)

def encontrar_vacuna(rut,vacunas):
    #Busca encontrar la Vacuna con la cual el paciente se vacuno en la primera dosis
    for llave in vacunas:
        lista = vacunas[llave]
        for run in lista:
            if run == rut:
                return llave

def nuevo_vacunado(tipo_de_vacuna, edad, rut, vacunas, dosis, fecha):
    if len(vacunas) == 0 and len(dosis) == 0:
        vacunas[tipo_de_vacuna] = [rut]
        dosis[rut] = [edad, fecha]
    else:
        for v in vacunas:
            if v == tipo_de_vacuna:
                vacunas[v].append(rut)
                dosis[rut] = [edad, fecha]
    if tipo_de_vacuna not in vacunas:
        vacunas[tipo_de_vacuna] = [rut]
        dosis[rut] = [edad, fecha]

covid = True
while covid:
    rut = input("RUT:\t")
    analizar = revisar_dosis(rut,dosis)

    if analizar == 2:
        print("Paciente ya cuenta con ambas dosis")

    elif analizar == 1:
        vac = encontrar_vacuna(rut,vacunas)
        print("Segunda dosis. Paciente debe ser inoculado con:", vac)
        actualizar(fecha,rut,dosis)

    else:
        edad = int(input("Edad:\t"))
        tipo_de_vacuna = input("Tipo vacuna:\t")
        nuevo_vacunado(tipo_de_vacuna, edad, rut, vacunas, dosis, fecha)

    continuar = input("¿Desea continuar? (s/n):\t")
    if continuar == "n":
        covid = False

print("\n############################################################")
print(("Edades con más personas con esquema de inoculación completo").upper())
top_tres = {}
for top in dosis:
    if len(dosis[top]) == 3:
        if top_tres == {}:
            top_tres[dosis[top][0]] = 1
        elif dosis[top][0] not in top_tres:
            top_tres[dosis[top][0]] = 1
        elif dosis[top][0] in top_tres:
            top_tres[dosis[top][0]] += 1
            
top_list = []
for x in top_tres:
    tupla = (top_tres[x],x)
    top_list.append(tupla)
top_list.sort()
top_list.reverse()

#Estos condicionales estan por si, los inocualdos compeltos no son suficientes!
if len(top_list)==0:
    print("Ningun paciente registrado tiene inoculacion completa")

elif len(top_list)==1:
    print(top_list[0][1], "años:", top_list[0][0], "personas")

elif len(top_list)==2:
    print(top_list[0][1], "años:", top_list[0][0], "personas")
    print(top_list[1][1], "años:", top_list[1][0], "personas")

else:
    print(top_list[0][1], "años:", top_list[0][0], "personas")
    print(top_list[1][1], "años:", top_list[1][0], "personas")
    print(top_list[2][1], "años:", top_list[2][0], "personas")