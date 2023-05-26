import os
import modulos.votacionwrite as votwrite

vottotal = []

absolute_path = os.path.dirname(__file__)
relative_path = "csv"

votwrite.csvwrite(absolute_path, vottotal)

