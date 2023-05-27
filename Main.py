import os
import modulos.votacionwrite as votwrite        # Importamos funciones importantes 
import modulos.sufragios as suf

vottotal = []               # Creamos lista con toda la info

absolute_path = os.path.dirname(__file__)
relative_path = "csv"                       # Funciones para no tener problemas con las carpetas
cadena = suf.registro()                     # Llamamos a la funcion registro en sufragios.py
i = 0
while i != cadena:                          # While para repetir 
    error = votwrite.csvwrite(absolute_path, vottotal)      # Llamamos a la funcion csvwrite para iniciar la escritura de votos.csv
    if error == True:
        i = i           # Si encuentra un error, no se suma nada a la cadena
    else: 
        print("Voto Valido")
        i = i + 1               # si todo va bien sumamos 1 a la cantidad actual de votos procesados
    error = False

os.system("PAUSE")

