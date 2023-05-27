def check(path):
    import csv                      # Importamos csv y platform 
    import platform

    partidoslist = []                   # Creamos una lista para todos los partidos

    if platform.system() == 'Windows':
        csvfile = path + "\csv\\partidos.csv"           # Fix para linux
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/partidos.csv'

    with open (csvfile, "r", ) as partidos:             # Leemos el archivo partidos.csv para la lista de partidos
        reader = csv.reader(partidos)
        for row in reader:
            print(row)
            partidoslist.append(int(row[1]))
    
    print("Seleccione el id del partido que quiere votar: ")
    valido = False
    while valido != True:                           # Chequeamos que el valor sea valido
        try:
            resp = int(input("ID: "))               # Chequeamos que el valor sea un numero
        except: 
            valido = False
        try:
            partidoslist.index(resp)                # Buscamos el valor en la lista de partidos
            valido = True
        except:
            valido = False
            print("Valor no valido")                # si no lo encuentra tira un error, usamos esto para definirlo como no valido

    return resp
