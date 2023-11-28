def notreplace(emoji, significado, texto): #Esta Funcion busca replicar lo que hace la funcion .replace()
    texto_cambiado = ""
    i = 0
    mayuscula = significado.upper()

    while i < len(texto):
        if emoji == texto[i : i + len(emoji)]:
            texto_cambiado += mayuscula
            i += len(emoji)
        else:
            texto_cambiado += texto[i]
            i += 1
    return texto_cambiado

def reductor_significado(significado): #Busca reducir el significado | ejemplo de: <3*corazon$:-D*cara feliz$ a :-D*cara feliz$
    i = 0
    nuevo_significado = ''
    revisa = ''
    nuevo = ''
    while i < len(significado):
        revisa += significado[i]
        if significado[i] == '$':
            z = i +1
            nuevo = significado[z:]
            nuevo_significado = nuevo
            return nuevo_significado
        i += 1

def significado_necesario(significado): #La funcion deja el significado y emoji cortado en '$' | ejemplo: <3*corazon$
    i = 0
    significado_para_la_busqueda = ''
    while i < len(significado):
        significado_para_la_busqueda += significado [i]
        if significado [i] == '$':
            return significado_para_la_busqueda
        i += 1

def extraccion_emojis_y_significados(significado, texto): #Esta Funcion busca los emojis y los significados de estos
    flag = True
    while flag:
        extraccion_signo_peso = significado_necesario(significado) #se busca sacar el primer termino hasta el primer '$'
        significado = reductor_significado(significado) #Significado tendra un nuevo valor

        if extraccion_signo_peso == None:
            flag =False
            return texto

        i = 0
        busqueda_asterisco = ''
        significado_emoji = ''

        while i < len(extraccion_signo_peso):
            busqueda_asterisco += extraccion_signo_peso[i]

            if extraccion_signo_peso[i] == '*':
                emoji = busqueda_asterisco[0:i]

                for q in extraccion_signo_peso: #q es un caracter de palabra
                    if q not in emoji and q != '*' and q != '$':
                        significado_emoji += q

                llamado_funcion = notreplace(emoji, significado_emoji, texto)
                texto_nuevo = llamado_funcion
                texto = texto_nuevo

            i += 1

print("====================================================================================")
texto_usuario = input("Ingrese Texto: ")
significado_usuario = input("Ingrese significado/s: ")

funcion_llamado = extraccion_emojis_y_significados(significado_usuario,texto_usuario)
print('Texto traducido: ', funcion_llamado)
print("====================================================================================")