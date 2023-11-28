#Item 2a
def votos_partido(votos, partido):
    i = 0
    z = 0
    cont_votos = 0
    voto_signopeso = votos + '$'  #Se le agrega un signo peso para que sea mas facil extraer el ultimo voto
    while i < len(voto_signopeso):
        if voto_signopeso[i] == '$':
            comprobar = voto_signopeso[z :i]
            z = i + 1
            if comprobar == partido:
                cont_votos += 1
        i += 1
    return cont_votos
