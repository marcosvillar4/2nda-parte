
def vervoto(listatot, path):
    import modulos.checkdnival as dni           #Import check valores de dni
    import modulos.check_region as region
    listcanactual = []                          # Lista temporal para candidatos votados
    listregactual = []
    votoactual = []                          # Lista temporal para el voto actual
    
    indexdni = 0

    valido = False  
    error = False  

    def find(lista, valor, indexdni):             # Buscamos el dni en la lista
        try:
            lista.index(valor)
            checkcan(lista)
            indexdni = indexdni + 1
            checkreg(lista)
            return indexdni
        except ValueError:
            return indexdni
    
    def checkcan(lista):
        listcanactual
        listcanactual.append(lista[2])  # Buscamos el valor representante del candidato

    def checkreg(lista):
        listregactual
        listregactual.append(lista[1])

    def indexcheck(valactual, listdni):
        if listdni.count(valactual) != 1:
            return True
        else:
            return False
    
    
    valor = str(dni.checkdni())
    reg = str(region.check(path))
    print("Categoria (1/ presidente, 2/vice, 3/senador, 4/diputado)")

    val = False

    while val != True:
        try:
            cat = str(input("Categoria: "))
            if cat != "1" and cat != "2" and cat != "3" and cat != "4":
                val = False
                print("Valor no valido")
            else:
                val = True
        except ValueError:
            print("Valor no valido")
            val = False

    votoactual.append(valor)
    votoactual.append(reg)
    votoactual.append(cat)
    print (f"Su voto es {votoactual}")

    listatot.append(votoactual)
    cantlist = len(listatot)

    for nrolistactual in range(0,cantlist):
        listactual = listatot[nrolistactual]
        indexdni = find(listactual, valor, indexdni)

    
    
    for regindexpos in range (0, len(listregactual)):
        if len(listregactual) == 1:
            valido = True
        if listregactual[regindexpos] == listregactual[0]:
            valido = True
        elif listregactual[regindexpos] != listregactual[0]:
            valido = False

        if valido == False:
            print("Voto no valido, usted ya voto en otra region")
            error = True
            break
    
    rep = False
    for indexpos in range(0, len(listcanactual)):
        valactual = listcanactual[indexpos]
        rep = indexcheck(valactual, listcanactual)
        if rep == True:
            print("Voto no valido, DNI ya voto para esta categoria")
            error = True
            break
        
    if error == True:
        listatot.pop()
            
    return listatot
