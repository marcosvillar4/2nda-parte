import os
import modulos.votacionwrite as votwrite
import modulos.sufragios as suf

vottotal = []


absolute_path = os.path.dirname(__file__)
relative_path = "csv"
cadena = suf.registro()
i = 0
while i != cadena:
    error = votwrite.csvwrite(absolute_path, vottotal)
    if error == True:
        i = i
    else: 
        print("Voto Valido")
        i = i + 1
    error = False
    print(i)
        
   

os.system("PAUSE")