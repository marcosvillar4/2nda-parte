def csvwrite(path, vottotal):
    import csv
    import platform
    import modulos.checkdatos as datos
    
    header = ["DNI, REGION, CARGO, PARTIDO"]
    fin = ["FIN"]

    rows = datos.vervoto(vottotal, path)

    if platform.system() == 'Windows':
        csvfile = path + "\csv\\votos.csv"
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/votos.csv'
 
    with open (csvfile, "w") as votos:
        writer = csv.writer(votos)
        writer.writerow(header)
        writer.writerows(rows)
        writer.writerow(fin)
