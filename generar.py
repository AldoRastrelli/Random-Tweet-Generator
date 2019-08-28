import contadores

FAVORITOS = 'tweets_favoritos.txt'

def generar(cuentas):
    """Genera un tweet aleatorio considerando las cuentas ingresadas por parámetro, lo imprime
    y pregunta si desea guardarlo o no. Si es asi, lo guarda en {FAVORITOS}."""

    if not cuentas:
        print('Ninguna de las cuentas ingresadas se encuentran en archivo.')
        return
        
    probabilidad_cuentas_seleccionadas = contadores.probabilidad_palabras(cuentas)
    nuevo_tweet = contadores.generar_tweet(probabilidad_cuentas_seleccionadas)

    print(f'\n"""\n{nuevo_tweet}\n"""')

    if guardar_tweet():
        
        try:
            archivo = open(FAVORITOS,'a')
        except IOError:
            print('El archivo de Tweets Favoritos no se encuentra o está dañado.')
            return
    
        archivo.write(f'{nuevo_tweet}\n')
        archivo.close()
        print('Tweet agregado a favoritos.')

def guardar_tweet():
    """Pregunta al usuario si quiere guardar el tweet y devuelve True or False"""

    guardar = input('¿Desea agregar este tweet a favoritos? [s/n] ')

    while guardar not in ('s','n'):
        guardar = input('Entrada no válida. ¿Desea agregar este tweet a favoritos? [s/n] ').lower()

    return guardar == 's'