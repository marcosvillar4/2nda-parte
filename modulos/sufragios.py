def sufragios():
        
        print("Ingrese el numero de sufragios que desea cargar: ")
        esc = 0                 # escape para evitar errores
        try:
            cadena = int(input())       # chequeamos que el valor sea un numero entero
            if cadena > 0:
                return True, cadena     # chequeamos que el valor sea positivos, si es positivo devuelve la cadena
            else:
                return False, esc       # si es negativo devuelve escape y repite el ciclo
        except ValueError:
            return False, esc
             
def registro():
        error = False
        error1 = False      

        while error != True:            # Check para error   
            
            while error1 != True:
                error1, cadena = sufragios()        # Llamamos a la funcion sufragios 
                if error1 == False:
                    print("Caracter no valido, el numero puede tener solamente numeros que sean mayores a 0")
                elif error1 == True:
                    return cadena
                    

        return cadena
