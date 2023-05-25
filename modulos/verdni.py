dnitot = []                 # Declaramos Nombre variable y lista
ciclo = ""

def check(dnitotal):                                # Validacion de caracteristicas
    try:
        dni = int(input("DNI:"))
        errornum = 0            # Validamos que el valor sea un numero entero
    except ValueError:
        print("Valor no valido")            # Si devuelve un error, definimos DNI como -10 para que la proxima validacion falle y corra el chequeo de nuevo
        dni = -10
        errornum = 1
    try:
        dnitotal.index(dni)                   # Buscamos el valor del dni en la lista
        valido = False                        # Si lo encuentra definimos valido como falso para repetir el chequeo con otro dni
        dniappend = 0                           # Definimos el dniappend como 0 para evitar errores
        errorrep = 1                        
    except:
        if dni < 100000000 and dni > 0:        # Chequeamos que el valor sea menor a 100000000 y sea positivo
            valido = True                   
            dniappend = dni
            errorrep = 0
        else:
            valido = False                  # Si el valor es negativo, falla el chequeo
            dniappend = 0
            errorrep = 0
            errornum = 1

    return valido, dniappend, errornum, errorrep

resp = False



def dni():

    while resp != True:
        resp, dniappend, errornum, errorrep = check(dnitot)
        if errornum == 1:
            print("DNI no valido, solo se pueden usar numeros enteros positivos") 
        if errorrep == 1:
            print("DNI no valido, DNI ya voto")
    dnitot.append(dniappend)               # Sumamos el DNI validado a la lista

    resp = False

    return dnitot