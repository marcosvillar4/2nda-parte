
def vervoto(listatot, path):
    import modulos.checkdnival as dni           #Importamos las funciones nescesarias
    import modulos.check_region as region
    import modulos.partidos as partidos
    listcanactual = []                          # Listas temporal para los datos
    listregactual = []
    votoactual = []                              
    
    indexdni = 0

    valido = False  
    error = False                               # Variables para errores

    def find(lista, valor, indexdni):            
        try:
            lista.index(valor)                  # Buscamos el dni en la lista actual
            checkcan(lista)                     # Llamamos a checkcan 
            indexdni = indexdni + 1             
            checkreg(lista)
            return indexdni
        except ValueError:
            return indexdni
    
    def checkcan(lista):
        listcanactual
        listcanactual.append(lista[2])          # Creamos una lista con todos los valores de candidatos votados para un cierto dni

    def checkreg(lista):
        listregactual
        listregactual.append(lista[1])          # Creamos una lista con todos los valores de candidatos votados para un cierto dni

    def countcheck(valactual, listdni):
        if listdni.count(valactual) != 1:       # Chequeamos que no se repita ningun numero en la lista de candidatos dni
            return True                         # Devolvemos true si encuentra el valor actual mas de 1 vez
        else:
            return False                        # Devolvemos false si lo encuentra 1 vez
    
    
    valor = str(dni.checkdni())                 # Llamamos a checkdni para validar el dni y lo pasamos a str para operar
    reg = str(region.check(path))               # Llamamos a check de region para validar la region y lo pasamos a str para operar
    print("Categoria (1/ presidente y vicepresidente, 2/diputado, 3/senador, 4/gobernador y vicegobernador)")

    val = False

    while val != True:
        try:
            cat = str(input("Categoria: ")) 
            if cat != "1" and cat != "2" and cat != "3" and cat != "4":             # Validamos la categoria
                val = False
                print("Valor no valido")
            else:
                val = True
        except ValueError:
            print("Valor no valido")
            val = False

    par = str(partidos.check(path))              # Llamamos a check de partidos para validar el partido

    votoactual.append(valor)
    votoactual.append(reg)
    votoactual.append(cat)                      # sumamos todos los valores a la lista temporal voto actual
    votoactual.append(par)
    print (f"Su voto es {votoactual}")

    listatot.append(votoactual)                 # Sumamos el voto actual a la lista total
    cantlist = len(listatot)                    # conseguimos cuantos votos hay

    for nrolistactual in range(0,cantlist):
        listactual = listatot[nrolistactual]            # leemos cada lista dentro de la lista 
        indexdni = find(listactual, valor, indexdni)            # LLamamamos a la funcion find

    
    
    for regindexpos in range (0, len(listregactual)):           # Check para las regiones
        if len(listregactual) == 1:                         # Si solo hay una region registrada para el dni pasamos los chequeos automaticamente
            valido = True
        if listregactual[regindexpos] == listregactual[0]:      # Chequeamos cada ciclo del for que el valor de la posicion actual sea igual al primer valor
            valido = True
        elif listregactual[regindexpos] != listregactual[0]:    # Si dentro de algun ciclo el valor es diferente, definimos valido como falso
            valido = False

        if valido == False:
            print("Voto no valido, usted ya voto en otra region")           # si la no es valido printeamos un mensaje y definimos error como verdadero
            error = True
            break
    
    rep = False
    for indexpos in range(0, len(listcanactual)):                           # chequeamos para cada item de la lista de candidato
        valactual = listcanactual[indexpos]                             # Separamos el valor de la poscicion actual
        rep = countcheck(valactual, listcanactual)                      # Llamamos a la funcion countcheck
        if rep == True:                                                 # Chequeamos que rep sea true
            print("Voto no valido, DNI ya voto para esta categoria")        # Si rep es true imprimimos un mensaje de error y definimos error como true
            error = True
            break
        
    if error == True:               # chequeamos si error es true
        listatot.pop()              # Si error es true, sacamos el ultimo valor de la lista total de votos, este siempre va a ser el voto actual, revertiendo cualquier cambio
            
    return listatot,error           # Devolvemos la lista para el writer y el error para el while de sufragios de main
