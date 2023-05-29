import os
import platform
# Importamos funciones importantes
import modulos.votacionwrite as votwrite
import modulos.sufragios as suf

vottotal = []               # Creamos lista con toda la info

absolute_path = os.path.dirname(__file__)
# Funciones para no tener problemas con las carpetas
relative_path = "csv"
# Llamamos a la funcion registro en sufragios.py
cadena = suf.registro()
i = 0
while i != cadena:                          # While para repetir
    # Llamamos a la funcion csvwrite para iniciar la escritura de votos.csv
    error = votwrite.csvwrite(absolute_path, vottotal)
    if error == True:
        i = i           # Si encuentra un error, no se suma nada a la cadena
    else:
        print("Voto Valido")
        i = i + 1               # si todo va bien sumamos 1 a la cantidad actual de votos procesados
    error = False
if platform.system() == 'Windows':
    os.system("PAUSE")
