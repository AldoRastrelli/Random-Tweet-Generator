TWEETS = 'tweets.csv'

def trending(cantidad):
    """ Devuelve los hashtags más usados en la base de tweets, del más usado al menos usado. Si se le pasa número N por parámetro,
    devuelve el top N (los N hashtags más usados). De lo contrario, devuelve todos"""
    
    try: 
        tweets = open(TWEETS)
    except IOError:
        print('El archivo de origen no se encuentra o está dañado')
        return

    trending = {}
    top_trending = []
    
    contar_hashtags(tweets,trending)
    tweets.close()

    hashtags = list(trending.items())
    hashtags.sort(key = lambda x: x[1], reverse = True)

    if not cantidad.isdigit():
        cantidad = len(hashtags)
    else:
        cantidad = int(cantidad)

    for i in range(cantidad):
        print(hashtags[i][0])
        
def contar_hashtags(archivo,diccionario):
    """Devuelve un diccionario con cada hashtag del archivo como clave y su cantidad de
    apariciones como valor"""

    for linea in archivo:
        for palabra in linea.split():
            if palabra[0] == '#':
                if palabra in diccionario:
                    diccionario[palabra] +=1
                    continue
                diccionario.update({palabra:1})
