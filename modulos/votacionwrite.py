def csvwrite(path, vottotal):
    import csv
    import platform
    import verdni
    
    header = ["DNI, REGION, CARGO, PARTIDO"]
    fin = ["FIN"]
    voto = []

    if platform.system() == 'Windows':
        csvfile = path + "\csv\partidos.csv"
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/partidos.csv'

    dni = verdni.dni

    voto.append()

    



    with open (path, "w", ) as votos:
        writer = csv.writer(votos)
        writer.writerow(header)
        writer.writerows()
        writer.writerow(fin)
