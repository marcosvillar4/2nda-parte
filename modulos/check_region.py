
def check(path):
    import csv
    import platform                     # Importamos csv y platform

    provincias = []                 # Creamos una lista para todas las provincias

    if platform.system() == 'Windows':
        csvfile = path + "\csv\\provincias.csv"             # Fix para windows y linux
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/provincias.csv'

    with open (csvfile, "r", ) as regiones:         # Leemos los valores de provincias.csv y los imprimimos
        reader = csv.reader(regiones)
        for row in reader:
            print(row)
            provincias.append(int(row[1]))          # a provincias le sumamos el valos de la posicion 1 de la linea actual (id)

    print("Seleccione el id de la provincia correspondiente: ")
    valido = False
    while valido != True:                   # chequeamos que la respuesta sea valida
        try:
            resp = int(input("ID: "))           # chequeamos que la respuesta sea un numero (id)
        except: 
            valido = False
        try:
            provincias.index(resp)              # buscamos el numero en la lista de id de provincias
            valido = True
        except:
            valido = False
            print("Valor no valido")               # si vuelve un error del index, el valor no esta presente, osea la respuesta no esta en el rango de numeros

    return resp

    

        


