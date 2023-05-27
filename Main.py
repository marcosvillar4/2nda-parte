import os
from modulos import votacionwrite as votwrite

vottotal = []
resp = ""

absolute_path = os.path.dirname(__file__)
relative_path = "csv"
while resp != "N" and resp != "NO" and resp != "FIN":
    votwrite.csvwrite(absolute_path, vottotal)
    resp = ""
    while resp != "N" and resp != "NO" and resp != "FIN" and resp != "S" and resp != "SI":
        print("Desea agregar otro voto?")
        resp = str.upper(str(input("Respuesta: ")))

