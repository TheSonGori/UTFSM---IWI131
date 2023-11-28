#Hecho por Javiera Gutierrez Abarca
#IWI-131 Paralelo 211

print("BIENVENIDO AL BANCO DE PYTHONIA")
print("Nuevo simulador de creditos hipotecarios")
print("Ingrese sus datos...")

valor = int(input("Valor propiedad en UF(1500-13000):"))
if (1500<=valor<=13000) == True:
    pie = int(input("Ingrese % del Pie (20%-45%):"))
    if (20<=pie<=45) == True:
        plazo = int(input("Ingrese Plazo (20, 25, 30):"))
        if (plazo==20 or plazo==25 or plazo==30) == True:
            vivienda = int(input("Tipo de vivienda Casa(1) o Departamento(2):"))
            if (1==vivienda or vivienda==2) == True:
                estado = int(input("Estado de vivienda Nueva(1) o Usada(2):"))
                if (1==estado or estado==2) == True:
                    pie_p = pie / 100
                    if vivienda == 1:  # Casa
                        if estado == 1:  # Nueva
                            if plazo == 20:
                                calculo = valor - (valor * pie_p)
                                interes = calculo * 25 / 100
                                seguros = (0.5 + 0.8) * 12 * 20
                                suma = interes + calculo
                                credito = suma + seguros
                                dividendo = credito / (12 * 20)
                                print("Total del credito a pagar", round(credito, 2), "UF")
                                print("Dividendo mensual de", round(dividendo, 2), "UF")

                            elif plazo == 25:
                                calculo = valor - (valor * pie_p)
                                interes = calculo * 30 / 100
                                seguros = (0.5 + 0.8) * 12 * 25
                                suma = interes + calculo
                                credito = suma + seguros
                                dividendo = credito / (12 * 25)
                                print("Total del credito a pagar", round(credito, 2), "UF")
                                print("Dividendo mensual de", round(dividendo, 2), "UF")

                            elif plazo == 30:
                                calculo = valor - (valor * pie_p)
                                interes = calculo * 35 / 100
                                seguros = (0.5 + 0.8) * 12 * 30
                                suma = interes + calculo
                                credito = suma + seguros
                                dividendo = credito / (12 * 30)
                                print("Total del credito a pagar", round(credito, 2), "UF")
                                print("Dividendo mensual de", round(dividendo, 2), "UF")

                        elif estado == 2:  # Usada
                            if plazo == 20:
                                calculo = valor - (valor * pie_p)
                                interes = calculo * 22 / 100
                                seguros = (0.5) * 12 * 20
                                suma = interes + calculo
                                credito = suma + seguros
                                dividendo = credito / (12 * 20)
                                print("Total del credito a pagar", round(credito, 2), "UF")
                                print("Dividendo mensual de", round(dividendo, 2), "UF")

                            elif plazo == 25:
                                calculo = valor - (valor * pie_p)
                                interes = calculo * 27 / 100
                                seguros = (0.5) * 12 * 25
                                suma = interes + calculo
                                credito = suma + seguros
                                dividendo = credito / (12 * 25)
                                print("Total del credito a pagar", round(credito, 2), "UF")
                                print("Dividendo mensual de", round(dividendo, 2), "UF")

                            elif plazo == 30:
                                calculo = valor - (valor * pie_p)
                                interes = calculo * 31 / 100
                                seguros = (0.5) * 12 * 30
                                suma = interes + calculo
                                credito = suma + seguros
                                dividendo = credito / (12 * 30)
                                print("Total del credito a pagar", round(credito, 2), "UF")
                                print("Dividendo mensual de", round(dividendo, 2), "UF")

                    elif vivienda == 2:  # Departamento
                        if estado == 1:  # Nueva
                            if plazo == 20:  # 28%
                                calculo = valor - (valor * pie_p)
                                interes = calculo * 28 / 100
                                seguros = (0.5 + 0.8 + 0.3) * 12 * 20
                                suma = interes + calculo
                                credito = suma + seguros
                                dividendo = credito / (12 * 20)
                                print("Total del credito a pagar", round(credito, 2), "UF")
                                print("Dividendo mensual de", round(dividendo, 2), "UF")

                            elif plazo == 25:  # 33%
                                calculo = valor - (valor * pie_p)
                                interes = calculo * 33 / 100
                                seguros = (0.5 + 0.8 + 0.3) * 12 * 25
                                suma = interes + calculo
                                credito = suma + seguros
                                dividendo = credito / (12 * 25)
                                print("Total del credito a pagar", round(credito, 2), "UF")
                                print("Dividendo mensual de", round(dividendo, 2), "UF")

                            elif plazo == 30:  # 41%
                                calculo = valor - (valor * pie_p)
                                interes = calculo * 41 / 100
                                seguros = (0.5 + 0.8 + 0.3) * 12 * 30
                                suma = interes + calculo
                                credito = suma + seguros
                                dividendo = credito / (12 * 30)
                                print("Total del credito a pagar", round(credito, 2), "UF")
                                print("Dividendo mensual de", round(dividendo, 2), "UF")

                        elif estado == 2:  # Usada
                            if plazo == 20:
                                calculo = valor - (valor * pie_p)
                                interes = calculo * 26 / 100
                                seguros = (0.5 + 0.3) * 12 * 20
                                suma = interes + calculo
                                credito = suma + seguros
                                dividendo = credito / (12 * 20)
                                print("Total del credito a pagar", round(credito, 2), "UF")
                                print("Dividendo mensual de", round(dividendo, 2), "UF")

                            elif plazo == 25:
                                calculo = valor - (valor * pie_p)
                                interes = calculo * 32 / 100
                                seguros = (0.5 + 0.3) * 12 * 25
                                suma = interes + calculo
                                credito = suma + seguros
                                dividendo = credito / (12 * 25)
                                print("Total del credito a pagar", round(credito, 2), "UF")
                                print("Dividendo mensual de", round(dividendo, 2), "UF")

                            elif plazo == 30:
                                calculo = valor - (valor * pie_p)
                                interes = calculo * 37 / 100
                                seguros = (0.5 + 0.3) * 12 * 30
                                suma = interes + calculo
                                credito = suma + seguros
                                dividendo = credito / (12 * 30)
                                print("Total del credito a pagar", round(credito, 2), "UF")
                                print("Dividendo mensual de", round(dividendo, 2), "UF")

                else:
                    print('Tipo de estado invalido')
            else:
                print('Tipo de vivienda invalido')
        else:
            print('Plazo invalido')
    else:
        print("Pie fuera de rango")
else:
    print("Valor fuera de rango")

'''
if vivienda == 1 o 2: # este gato indica si es casa o depto

        if estado == 1 o 2: # este gato indica en que estado es el de la casa o depto
        
            if plazo == 20 o 25 o 30: [Indica el Plazo]
            
                calculo = valor - ( valor * pie_p )
                # Recordemos que pie_p es el porcentaje del pie en decimales y valor es el valor de la vivienda
                
                interes = calculo * (x) / 100
                # Ahora el calculo anterior lo multiplicaremos por x que x es el porcentaje de interes acorde al ano y 
                al estado de la casa o depto. ej: Tipo Casa, Estado Nueva, 20 anos = 25% de interes a cobrar.
                el x esta divido en 100 para pasarlo a decimales.
                
                seguros = (a + b + c) * 12 * [Plazo]
                # Los seguros dependen del estado y el tipo de vivienda. 
                 a = 0.5 Para todos los tipos de viviendas. 
                 b = 0.8 Solo aplica para viviendas nuevas ya sea depto o casa.
                 c = 0.3 Solo aplica para Deptos.
                
                suma = interes + calculo
                
                credito = suma + seguros
                
                dividendo = credito / ( 12 * [Plazo] )
                
                print("Total del credito a pagar", round(credito,2), "UF")
                print("Dividendo mensual de", round(dividendo,2), "UF")
                # Todos los resultados seran redondeados a 2 decimales
       
Casos de pruebas:      
              
Caso 1:
Valor propiedad en UF(1500-13000):12000
Ingrese % del Pie (20%-45%):33
Ingrese Plazo (20, 25, 30):25
Tipo de vivienda Casa(1) o Departamento(2):2
Estado de vivienda Nueva(1) o Usada(2):1
Total del credito a pagar 11173.2 UF
Dividendo mensual de 37.24 UF

Caso 2:
Valor propiedad en UF(1500-13000):2000
Ingrese % del Pie (20%-45%):30
Ingrese Plazo (20, 25, 30):20
Tipo de vivienda Casa(1) o Departamento(2):1
Estado de vivienda Nueva(1) o Usada(2):2
Total del credito a pagar 1828.0 UF
Dividendo mensual de 7.62 UF

Caso 3:
Valor propiedad en UF(1500-13000):4320
Ingrese % del Pie (20%-45%):21
Ingrese Plazo (20, 25, 30):30
Tipo de vivienda Casa(1) o Departamento(2):1
Estado de vivienda Nueva(1) o Usada(2):1
Total del credito a pagar 5075.28 UF
Dividendo mensual de 14.1 UF

'''