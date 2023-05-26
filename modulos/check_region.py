
def check(path):
    import csv
    import platform

    provincias = []

    if platform.system() == 'Windows':
        csvfile = path + "\csv\\provincias.csv"
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/provincias.csv'

    with open (csvfile, "r", ) as regiones:
        reader = csv.reader(regiones)
        for row in reader:
            print(row)
            provincias.append(int(row[1]))
    
    print("Seleccione el id de la provincia correspondiente: ")
    valido = False
    while valido != True:
        try:
            resp = int(input("ID: "))
        except: 
            valido = False
        try:
            provincias.index(resp)
            valido = True
        except:
            valido = False
            print("Valor no valido")

    return resp

    

        


