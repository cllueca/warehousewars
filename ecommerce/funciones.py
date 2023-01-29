# Funcion que convierte las querys a la BBDD en diccionarios, para acceder de manera mas facil al valor de cada campo en las templates
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def comprobarContraseña(pwd, pwdConf):
    if(len(pwd) < 8):
        return -2 # longitud corta

    if(len(pwd) != len(pwdConf)):
        return -1 # false, diferente tamaño
    
    if(pwd != pwdConf):
        return 2 # false
    
    return 1 # true