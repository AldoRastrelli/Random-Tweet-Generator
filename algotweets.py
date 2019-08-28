import sys
from generar import generar
from favoritos import favoritos
from trending import trending
import contadores
import verificaciones

TWEETS = 'tweets.csv'

def main():
    """Desarrollo principal del programa"""

    lista_comandos = sys.argv
    if len(sys.argv) == 1:
        mensaje_ayuda()
        return

    comando = sys.argv[1].lower()

    if comando == 'generar':
        
        cuentas = lista_comandos[2:]
        cuentas_en_archivo = contadores.cuentas_en_archivo()

        if not cuentas:
            lista_cuentas = cuentas_en_archivo
        else:
            lista_cuentas = verificaciones.verificar_cuentas(cuentas,cuentas_en_archivo)
        
        generar(lista_cuentas)

    elif comando == 'favoritos':
        
        try:
            cantidad_favoritos_a_imprimir = lista_comandos[2]
        except IndexError:
            cantidad_favoritos_a_imprimir = ""
        
        if verificaciones.es_cantidad_valida(cantidad_favoritos_a_imprimir):
            favoritos(cantidad_favoritos_a_imprimir)
        else:
            print('La cantidad ingresada no es válida.')
            return
        
    elif comando == 'trending':
        
        try:
            cantidad_hashtags_a_imprimir = lista_comandos[2]
        except IndexError:
            cantidad_hashtags_a_imprimir = ""
        
        if verificaciones.es_cantidad_valida(cantidad_hashtags_a_imprimir):
            trending(cantidad_hashtags_a_imprimir)
        else:
            print('La cantidad ingresada no es válida.')
            return

    else:
        print('\nOops!\n')
        mensaje_ayuda()
        return

def mensaje_ayuda():
    """Imprime mensaje explicando el funcionamiento del programa"""

    print('Hi there! Debes ingresar un comando para jugar con RandomTweets.\nLos comandos son:\nA) Generar\nB) Favoritos\nC) Trending')

    accion = input('\nIngresa A, B o C para más información o cualquier otra tecla para salir: ').upper()        
    while accion in ('A','B','C'):
        if accion == 'A':
            print('\nA) GENERAR:')
            print(f'\nIngresa una o más cuentas ({ ", ".join(list(contadores.cuentas_en_archivo()))}) y se generará un tweet aleatorio con esas cuentas. Si no ingresas ninguna, se generará un tweet con todas las cuentas juntas.')
            print(f'Ejemplo: $python3 algotweets.py generar {contadores.cuentas_en_archivo().pop()}')
            accion = input('\nIngresa A, B o C para más información o cualquier otra tecla para salir: ').upper()        
            continue
        elif accion == 'B':
            print('\nB) FAVORITOS:')
            print('\nFavoritos te deja ver los tweets que guardaste, luego de generarlos. Se muestran del último al primero.')
            print('\n[!] Podés ingresar una cantidad de tweets a ver en pantalla, o no colocar nada y en ese caso se imprimirán todos los tweets guardados.')
            print('Ejemplo: $python3 algotweets.py favoritos 10')
            print('O también: $python3 algotweets.py favoritos')
            accion = input('\nIngresa A, B o C para más información o cualquier otra tecla para salir: ').upper()        
            continue
        else:
            print('\nC) TRENDING:')
            print('\nTrending te deja ver los hashtags más usados en la base de tweets disponible.')
            print('\n[!] Podés ingresar una cantidad de hashtags a ver en pantalla y se imprimiran los más populares')
            print('Si no ingresas cantidad, se imprimirán todos los hashtags disponibles.')
            print('Ejemplo: $python3 algotweets.py trending 10')
            print('O también: $python3 algotweets.py trending')
            accion = input('\nIngresa A, B o C para más información o cualquier otra tecla para salir: ').upper()        
            continue
    return

main()