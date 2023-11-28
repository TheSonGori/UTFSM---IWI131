# Tarea 2:
# Realizada por Javiera Gutierrez Abarca
# Ramo: IWI131 - PARALELO 211
print("VALOR NUTRICIONAL DE LO QUE CONSUME GROGU")
nevarronummies = float(input("Nevarro Nummies consumidas (en unidades):"))
spacesoup = float(input("Space Soup consumida (en [ml]:"))
carnederana = float(input("Carne de rana consumida (en [g]):"))
sp_e = spacesoup/285
cr_e = carnederana/100
'''
Las variables spacesoup y carne de rana se dividen por lo equivale una porcion de estas, 285 ml y 100 g respectivamente
dandonos un numero decimal el cual sera multiplicado mas adelante.
'''
grasas_consumidas_nn = (nevarronummies * 1.90)
grasas_consumidas_total = grasas_consumidas_nn
grasas_consumidas_sp = (sp_e * 10.0)
grasas_consumidas_total = grasas_consumidas_total + grasas_consumidas_sp
grasas_consumidas_cr = (cr_e * 0.30)
grasas_consumidas_total = grasas_consumidas_total + grasas_consumidas_cr
carbo_consumidas_nn = (nevarronummies * 6.00)
carbo_consumidas_total = carbo_consumidas_nn
carbo_consumidas_sp = (sp_e * 12.0)
carbo_consumidas_total = carbo_consumidas_total + carbo_consumidas_sp
carbo_consumidas_cr = (cr_e * 0.00)
carbo_consumidas_total = carbo_consumidas_total + carbo_consumidas_cr
prot_consumidas_nn = (nevarronummies * 0.80)
prot_consumidas_total = prot_consumidas_nn
prot_consumidas_sp = (sp_e * 11.0)
prot_consumidas_total = prot_consumidas_total + prot_consumidas_sp
prot_consumidas_cr = (cr_e * 16.0)
prot_consumidas_total = prot_consumidas_total + prot_consumidas_cr
'''
Ahora creamos una variable para cada calculo de los nutrientes por separado (grasas, carbohitrados y proteinas) y los 
alimentos tambien van por separado (ejemplo: grasas_consumidas_nn, carbo_consumidas_nn y prot_consumidas_nn)
y otra variable que vaya acumulando los resultados de cada operacion de los nutrientes por separado
(grasas_consumidas_total, carbo_consumidas_total y prot_consumidas_total).

Para  calcular la cantidad de nutrientes ingeridos las multiplicaciones estan determinadas por una variable de 
algun alimento que ya este en decimales (ya sea nevarronummies, sp_e o cr_e) por lo que equivale el nutriente que se
quiera multiplicar.

Ej: Quiero saber las cant de grasas de una Carne de Rana en 250 [g]
Primero se dividiria 250 por la cantidad que vale una porcion: 250/100 = 2.5  (dandome el decimal deseado) 
Segundo se sabe que por cada 100 [g] (una porcion) hay 0.30 [g] de grasas, entonces ahora para saber la cantidad de 
grasas que hay en 250 [g] tendria que multiplicar 2.5 por 0.30: 2.5 * 0.30 = 0.75 [g]
Entonces en 250 [g] hay 0.75 [g] de grasas.
 
'''
grasas = round(grasas_consumidas_total, 2)
carbo = round(carbo_consumidas_total, 2)
prot = round(prot_consumidas_total, 2)
cal = round((grasas * 9) + (carbo * 4) + (prot * 4))
cal = int(cal)
'''
Para calcular las calorias totales consumidas por Grogu se multiplica individualmente los nutirientes con su 
equivalente en calorias. 

Ej: 1[g] de proteina se sabe que equivale a 4 [calorias] por lo tanto para saber cuanto son 15 [g] de proteinas
se multiplica 15 [g] por 4 [calorias] = 15 * 4 = 60 [calorias]

El resultado que nos de estara redondeado a la "," 
luego el resultado se pasa numero entero con int() y este es el que saldra en pantalla.
'''
print("Grogu ha consumido:")
print(grasas, "[g] de grasas")
print(carbo, "[g] de carbohidratos")
print(prot, "[g] de proteinas")
print("dando un total de:")
print(cal, "[calorias]")
'''
3 Casos de prueba 

1 Caso =
Nevarro Nummies: 2.8 
Space Soup: 300
Carne de rana: 278
16.68 [g] de grasas
29.43 [g] de carbohidratos
58.3 [g] de proteinas
Total calorias: 501 [calorias]

2 Caso = 
Nevarro Nummies: 8.4
Space Soup: 580
Carne de rana: 640
38.23 [g] de grasas
74.82 [g] de carbohidratos
131.51 [g] de proteinas
Total calorias: 1169 [calorias]

3 Caso =
Nevarro Nummies: 2.4
Space Soup: 300
Carne de rana: 125
15.46 [g] de grasas
27.03 [g] de carbohidratos
33.5 [g] de proteinas
Total calorias: 381 [calorias]
'''