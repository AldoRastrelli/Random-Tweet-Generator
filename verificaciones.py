def verificar_cuentas(lista,cuentas):
    """verifica que las cuentas ingresadas por comando estén en el archivo de tweets. Si es así, se las agrega a una lista
    de usuarios a devolver. Si el usuario pasado no está en el archivo, se avisa al usuario y no se lo agrega a la lista a devolver."""
    
    lista_usuarios = []
    for usuario in lista:
        if usuario not in cuentas:
            print(f'El usuario {usuario} no se encontró en archivo.')
            continue
        lista_usuarios.append(usuario)

    return lista_usuarios

def es_usuario_pedido(cuentas_pedidas,usuario):
    """verifica que el usuario pedido se encuentre entre las
    cuentas presentes en el archivo"""

    return usuario in cuentas_pedidas

def es_cantidad_valida(parametro):
    """devuelve True si el parametro es un dígito o una cadena vacía, y False si no lo es"""

    return parametro == "" or parametro.isdigit()
    