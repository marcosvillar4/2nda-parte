def checkdni():
    valido = False
    while valido != True:                       # Chequeamos que el valor no haya sido validado
        try:
            dni = int(input("DNI: "))           # Chequeamos que el valor entregado sea un numero entero
            if dni < 100000000 and dni > 0:     # Chequeamos que el valor sea positivo y menor a 100000000
                valido = True
            else:
                valido = False
                print("Valor no valido, Solo se aceptan numeros positivos hasta 100000000") 
        except ValueError:                                                                      # Si el valor no es valido, el ciclo se repite
            valido = False
            print("Valor no valido, Solo se aceptan numeros positivos hasta 100000000") 
        
    return dni
        