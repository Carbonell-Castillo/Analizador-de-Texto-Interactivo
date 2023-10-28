class DB:
    def __init__(self):
        self.claves = {}
        ##Asignar errores token, lexema, fila y columna
        self.errores ={"token":[], "lexema":[], "fila":[], "columna":[]}
        
    
    def agregarError(self, token, lexema, fila, columna):
        self.errores["token"].append(token)
        self.errores["lexema"].append(lexema)
        self.errores["fila"].append(fila)
        self.errores["columna"].append(columna)

    def agregarClave(self, clave):
        self.claves[clave] = []

    def imprimirErrores(self):
        print("-"*50)
        print("Errores")
        for i in range(len(self.errores["token"])):
            print(self.errores["token"][i], self.errores["lexema"][i], self.errores["fila"][i], self.errores["columna"][i])
    def agregarValor(self, pos, valor):
        clave = list(self.claves.keys())[pos]
        self.claves[clave].append(valor)

    ##obtener cantidad de claves
    def cantidadClaves(self):
        return len(self.claves)
    
    def conteo(self):
        clave = list(self.claves.keys())[0]
        return len(self.claves[clave])
    
    def contarSi(self, clave, valor):
        return self.claves[clave].count(valor)

    #imprimir calves
    def imprimirClaves(self):
        print("-"*50)
        print("Claves")
        for clave in self.claves:
            print(clave)
            
    def imprimirRegistros(self):
        print("-"*50)
        print("Valores")
        for clave in self.claves:
            print(clave, self.claves[clave])
