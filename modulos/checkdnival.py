def checkdni():
    valido = False
    while valido != True:
        try:
            dni = int(input("DNI: "))
            if dni < 100000000 and dni > 0:
                valido = True
            else:
                valido = False
                print("Valor no valido, Solo se aceptan numeros positivos hasta 100000000") 
        except ValueError:
            valido = False
            print("Valor no valido, Solo se aceptan numeros positivos hasta 100000000") 
        
    return dni
        