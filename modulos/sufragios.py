def sufragios():
        
        print("Ingrese el numero de sufragios que desea cargar: ")
        esc = 0
        try:
            cadena = int(input())
            if cadena > 0:
                return True, cadena
            else:
                return False, esc
        except ValueError:
            return False, esc
        
def registro():
        error = False
        error1 = False

        while error != True:
        
            while error1 != True:
                error1, cadena = sufragios()
                if error1 == False:
                    print("Caracter no valido, el numero puede tener solamente numeros que sean mayores a 0")
                elif error1 == True:
                    break

        return cadena

registro()