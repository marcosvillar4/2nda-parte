import os
import modulos.votacionwrite as votwrite
import modulos.sufragios as suf

vottotal = []


absolute_path = os.path.dirname(__file__)
relative_path = "csv"
cadena = suf.registro()
for i in range (1, cadena):
    votwrite.csvwrite(absolute_path, vottotal)
   

os.system("PAUSE")