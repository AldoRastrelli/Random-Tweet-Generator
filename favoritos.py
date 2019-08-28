FAVORITOS = 'tweets_favoritos.txt'

def favoritos(cantidad_favoritos_a_imprimir):
    """Imprime los tweets guardados en favoritos del más reciente al más viejo, con la cantidad
    indicada por parámetro. Si la cantidad es vacía, los imprime todos"""
    
    try:
        favoritos = open(FAVORITOS,'r')
    except IOError:
        print('El archivo de origen no se encuentra o está dañado')
        return

    lineas = leer_lineas(favoritos)
    favoritos.close()
    
    cantidad_lineas = contar_lineas(lineas)
    

    if not cantidad_favoritos_a_imprimir:
        lineas_a_leer = cantidad_lineas
    else:
        lineas_a_leer = int(cantidad_favoritos_a_imprimir)
                
    if lineas_a_leer > cantidad_lineas:
        hasta = 0
    else:
        hasta = cantidad_lineas - lineas_a_leer
    
    for i in range(cantidad_lineas-1,hasta-1,-1):
        print(f'- {lineas[i]}')

def leer_lineas(archivo):
    """Lee linea por linea del archivo y lo guarda en una lista"""

    lineas = []
    linea = archivo.readline()
    while linea != "":
        lineas.append(linea)
        linea = archivo.readline()
    return lineas

def contar_lineas(lista_lineas):
    """Devuelve la cantidad de lineas que tiene el archivo"""
    
    return len(lista_lineas)
            