def csvwrite(path, vottotal):
    import csv
    import platform                     # importamos las funciones nescesarias
    import modulos.checkdatos as datos

    header = ["DNI, REGION, CARGO, PARTIDO"]        # definimos un header y un fin para el csv
    fin = ["FIN"]

    rows, error = datos.vervoto(vottotal, path)         # Llamamos la funcion vervoto de checkdatos.py

    if platform.system() == 'Windows':
        csvfile = path + "\csv\\votos.csv"
    elif platform.system() == 'Linux':                  # fix de carpeta para compatibilidad con linux y windows
        csvfile = path + '/csv/votos.csv'
 
    with open (csvfile, "w") as votos:                  # Escribimos el csv
        writer = csv.writer(votos)
        writer.writerow(header)     
        writer.writerows(rows)
        writer.writerow(fin)
    return error