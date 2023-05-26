
def vervotodni(listatot):
    import modulos.checkdnival as dni
    listdniactual = []
    votoactual = []

    def find(lista, valor):
        try:
            lista.index(valor)
            check(lista)
            return 
        except ValueError:
            return 0
    
    def check(lista):
        listdniactual
        listdniactual.append(lista[2])

    def indexcheck(valactual, listdni):
        if listdni.count(valactual) != 1:
            return True
        else:
            return False

    
    valor = str(dni.checkdni())
    region = input("Region: ")
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
    votoactual.append(region)
    votoactual.append(cat)
    print (f"Su voto es {votoactual}")

    listatot.append(votoactual)
    cantlist = len(listatot)

    for nrolistactual in range(0,cantlist):
        listactual = listatot[nrolistactual]
        find(listactual, valor)

    rep = False
    for indexpos in range(0, len(listdniactual)):
        valactual = listdniactual[indexpos]
        rep = indexcheck(valactual, listdniactual)
        if rep == True:
            print("Voto no valido, DNI ya voto para esta categoria")
            listatot.pop()
            break
        
    print(listatot)

    return listatot
