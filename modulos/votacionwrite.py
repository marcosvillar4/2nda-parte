def csvwrite(path, vottotal):
    import csv
    import platform
    import modulos.checkdatos as datos
    
    header = ["DNI, REGION, CARGO, PARTIDO"]
    fin = ["FIN"]

    rows = datos.vervotodni(vottotal)

    if platform.system() == 'Windows':
        csvfile = path + "\csv\partidos.csv"
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/partidos.csv'
 
    with open (csvfile, "w") as votos:
        writer = csv.writer(votos)
        writer.writerow(header)
        writer.writerows(rows)
        writer.writerow(fin)
