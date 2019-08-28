import random
import csv
import verificaciones

FINAL = ""
CANTIDAD_MAXIMA_CARACTERES = 280
TWEETS= 'tweets.csv'

def cuentas_en_archivo():
    """Devuelve un conjunto con todas las cuentas que aparecen en el archivo,
    sin repeticiones"""

    try:
        tweets = open(TWEETS)
    except IOError:
        print('El archivo de origen se encuentra dañado o no existe.')
        return

    tweets_csv = csv.DictReader(tweets,delimiter = '\t',fieldnames=('usuario','tweet'))
    cuentas = set()

    for linea in tweets_csv:
        usuario = linea['usuario']
        if usuario not in cuentas:
            cuentas.add(usuario.lower())

    tweets.close()
    return cuentas

def contar_palabras_proximas(cuentas):
    """Devuelve un diccionario de diccionarios con las palabras como claves primeras,
    un diccionario segundo como valor. Dicho diccionario tiene a las palabras próximas como claves
    y a la cantidad de veces que la siguen como valor"""

    contador_proxima_palabra = {}

    try:
        tweets = open(TWEETS,'r')
    except IOError:
        print('El archivo de origen se encuentra dañado o no existe.')
        return
        
    tweets_csv = csv.DictReader(tweets,delimiter = '\t',fieldnames = ('usuario','tweet'))
    
    for linea in tweets_csv:

        usuario = linea['usuario']
        tweet = linea['tweet']

        if verificaciones.es_usuario_pedido(cuentas,usuario):
            actualizar_contador_palabra(tweet,contador_proxima_palabra)
            
    tweets.close()

    return contador_proxima_palabra

def contar_total_apariciones(diccionario):
    """Devuelve un diccionario con las palabras como claves y su cantidad de apariciones
    totales como valor"""

    total_apariciones = {}
    for palabra in diccionario:
        apariciones = 0
        for proxima in diccionario[palabra]:
            apariciones += diccionario[palabra][proxima]
        total_apariciones.update({palabra:apariciones})

    return total_apariciones

def probabilidad_palabras(cuentas):
    """Devuelve un diccionario con la probabilidad de cada palabra de suceder a su anterior"""

    contador_palabras = contar_palabras_proximas(cuentas)
    total_apariciones = contar_total_apariciones(contador_palabras)
    probabilidad_proxima_palabra = calcular_probabilidades(contador_palabras,total_apariciones)

    return probabilidad_proxima_palabra

def calcular_probabilidades(diccionario_contador_palabras,diccionario_totalidad_apariciones):
    """Calcula la probabilidad de cada palabra de suceder a su anterior
    y lo devuelve en forma de diccionario de diccionario tal que las primeras claves son equiprobables,
    y sus valores son diccionarios con claves segundas de palabras próximas y su probabilidad de
    sucederla"""

    probabilidades = {}

    for palabra in diccionario_contador_palabras:
        probabilidades.update({palabra:{}})

        for proxima in diccionario_contador_palabras[palabra]:
            probabilidades[palabra].update({proxima: 0})

            total = diccionario_totalidad_apariciones[palabra]
            eventos = diccionario_contador_palabras[palabra][proxima]
            probabilidad = eventos/total

            probabilidades[palabra][proxima] = probabilidad
            
    return probabilidades

def generar_tweet(diccionario_palabras):
    """Genera un tweet aleatorio y lo devuelve"""

    palabra = random.choice(list(diccionario_palabras.keys()))
    nuevo_tweet = ""

    while palabra != '' and (len(nuevo_tweet)+len(palabra)) <= CANTIDAD_MAXIMA_CARACTERES:

        opciones = []
        probabilidades = []
        nuevo_tweet += palabra + " "

        for clave in diccionario_palabras[palabra]:
            opciones.append(clave)
            probabilidades.append(diccionario_palabras[palabra][clave])

        probabilidades[0] = 1 - sum(probabilidades[1:])
        palabra = random.choices(opciones,probabilidades)[0] #devuelve lista de único elemento
    
    return nuevo_tweet


def actualizar_contador_palabra(tweet,contador_proxima_palabra):
    """Actualiza el diccionario pasado por parámetro con palabras nuevas y su cantidad
    de apariciones"""

    palabras_tweet = tweet.split()
    [contador_proxima_palabra.update({palabra:{}}) for palabra in palabras_tweet if palabra not in contador_proxima_palabra]

    for palabra in palabras_tweet:
            try:
                indice = palabras_tweet.index(palabra)
                proxima = palabras_tweet[indice+1]
            except IndexError:
                proxima = FINAL

            if proxima in contador_proxima_palabra[palabra]:
                contador_proxima_palabra[palabra][proxima] += 1
            else:
                contador_proxima_palabra[palabra].update({proxima:1})