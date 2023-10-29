from printer import Printer
from db import DB
import webbrowser
#analizador sintatico
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index=0
        self.printer = Printer()
        self.db = DB()
        self.errorSintactico=False

    def consume(self):
        token = self.tokens[self.index]
        self.index += 1
        return token
    
    #revertir consume
    def revertir(self):
        self.index -= 1

    def peek(self):
        return self.tokens[self.index]
    
    def parse(self):
        while self.index < len(self.tokens):
            if self.peek().name == "IMPRIMIR":
                self.imprimir()
            elif self.peek().name == "IMPRIMIRLN":
                self.imprimirln()
            elif self.peek().name == "CLAVES":
                self.claves()
            elif self.peek().name == "REGISTROS":
                self.registros()
            elif self.peek().name == "CONTEO":
                self.conteo()
            elif self.peek().name == "PROMEDIO":
                self.promedio()
            elif self.peek().name == "CONTARSI":
                self.contarSi()
            elif self.peek().name == "DATOS":
                self.datos()
            elif self.peek().name == "SUMAR":
                self.sumar()
            elif self.peek().name == "MAX":
                self.max()
            elif self.peek().name == "MIN":
                self.min()
            elif self.peek().name == "EXPORTARREPORTE":
                self.exportarReporte()
            else:
                if self.errorSintactico==True:
                    print("Error: Token desconocido")

                    self.revertir()
                    self.revertir()
                    self.printer.addLine("Error: Token desconocido")
                    self.db.agregarError("Sintactico", self.peek().value, self.peek().line, self.peek().column)
                    self.consume()
                    self.errorSintactico=False
                else:
                    self.printer.addLine("Error: Token desconocido")
                    self.db.agregarError("Sintactico", self.peek().value, self.peek().line, self.peek().column)
                    self.consume()
        
        texto = self.printer.print()
        for line in texto.split("\n"):
            print("\033[32m" +">>"+ line + "\033[0m")

    #regresar texto
    def obtenerTexto(self):
        return self.printer.print()
    def imprimir(self):
        self.consume()  # imprimir generar los errores
        if self.consume().name != "PARENTESISIZQUIERDO":
            print("Error: Se esperaba un paréntesis izquierdo")
            self.printer.addLine("Error: Se esperaba un paréntesis izquierdo")
            self.errorSintactico=True
        else:
            token = self.consume()
            if token.name != "STRING":
                print("Error: Se esperaba un string")
                self.printer.addLine("Error: Se esperaba un string")
                self.errorSintactico=True
            elif self.consume().name != "PARENTESISDERECHO":
                print("Error: Se esperaba un paréntesis derecho")
                self.printer.addLine("Error: Se esperaba un paréntesis derecho")
                self.errorSintactico=True
            elif self.consume().name != "PUNTOYCOMA":
                print("Error: Se esperaba un punto y coma")
                self.printer.addLine("Error: Se esperaba un punto y coma")
                self.errorSintactico=True
            else:
                self.printer.add(token.value)


    def imprimirln(self):
        self.consume() # imprimirLN
        if self.consume().name != "PARENTESISIZQUIERDO":
            print("Error: Se esperaba un parentesis izquierdo")
            self.printer.addLine("Error: Se esperaba un parentesis izquierdo")
            self.errorSintactico=True
        else:
            token = self.consume()
        if token.name != "STRING":
            print("Error: Se esperaba un string")
            self.printer.addLine("Error: Se esperaba un string")
            self.errorSintactico=True
            
        if self.consume().name != "PARENTESISDERECHO":
            print("Error: Se esperaba un parentesis derecho")
            self.printer.addLine("Error: Se esperaba un parentesis derecho")
            self.errorSintactico=True
            
        if self.consume().name != "PUNTOYCOMA":
            print("Error: Se esperaba un punto y coma")
            self.printer.addLine("Error: Se esperaba un punto y coma")
            self.errorSintactico=True
        else:
            self.printer.addLine(token.value)

    def claves(self):
        self.consume()
        if self.consume().name != "IGUAL":
            print("Error: Se esperaba un igual")
            self.printer.addLine("Error: Se esperaba un igual")
            self.errorSintactico=True
            
        if self.consume().name != "CORCHETEIZQUIERDO":
            print("Error: Se esperaba un corchete izquierdo")
            self.printer.addLine("Error: Se esperaba un corchete izquierdo")
            self.errorSintactico=True
            
        ##confimar lsitado de calves
        if self.peek().name != "STRING":
            print("Error: Se esperaba un string")
            self.printer.addLine("Error: Se esperaba un string")
            self.errorSintactico=True
            
        
        valor1= self.consume().value
        self.db.agregarClave(valor1)
        while self.peek().name == "COMA":
            self.consume()
            if self.peek().name != "STRING":
                self.printer.addLine("Error: Se esperaba un string")
                print("Error: Se esperaba un string")
                self.errorSintactico=True
            else:
                valor2 = self.consume().value
                self.db.agregarClave(valor2)
        if self.consume().name != "CORCHETEDERECHO":
            print("Error: Se esperaba un corchete derecho")
            self.printer.addLine("Error: Se esperaba un corchete derecho")
            self.errorSintactico=True
            
        
    def registros(self):
        print("entro a registros")
        self.consume()
        if self.consume().name != "IGUAL":
            print("Error: Se esperaba un igual")
            self.printer.addLine("Error: Se esperaba un igual")
            self.errorSintactico=True
            
        if self.consume().name != "CORCHETEIZQUIERDO":
            print("Error: Se esperaba un corchete izquierdo")
            self.printer.addLine("Error: Se esperaba un corchete izquierdo")
            self.errorSintactico=True
            
        
        while self.peek().name == "LLAVEIZQUIERDA":
            self.consume()
            contador=0
            if self.peek().name != "STRING" and self.peek().name != "NUMBER":
                print("Error: Se esperaba un valor de clave")
                self.printer.addLine("Error: Se esperaba un valor de clave")
                self.errorSintactico=True
            else:
            
                valor = self.consume().value
            
                self.db.agregarValor(contador, valor)
                contador+=1

                while self.peek().name == "COMA":
                    self.consume()
                    if self.peek().name != "STRING" and self.peek().name != "NUMBER":
                        print("Error: Se esperaba un valor de clave")
                        self.printer.addLine("Error: Se esperaba un valor de clave")
                        self.db.agregarErrorself.errorSintactico=True
                        return
                    valor = self.consume().value
                    self.db.agregarValor(contador, valor)
                    contador+=1

            if self.peek().name != "LLAVEDERECHA":
                print("Error: Se esperaba una llave derecha")
                self.printer.addLine("Error: Se esperaba una llave derecha")
                self.errorSintactico=True
                
            self.consume() 
        self.consume()
        self.db.imprimirRegistros()
        self.db.imprimirClaves()
            

    def conteo(self):
        print("Entro conteo")
        self.consume()
        if self.consume().name != "PARENTESISIZQUIERDO":
            print("Error: Se esperaba un parentesis izquierdo")
            self.printer.addLine("Error: Se esperaba un parentesis izquierdo")
            self.errorSintactico=True
            
        if self.consume().name != "PARENTESISDERECHO":
            print("Error: Se esperaba un parentesis derecho")
            self.printer.addLine("Error: Se esperaba un parentesis derecho")
            self.errorSintactico=True
            
        if self.consume().name != "PUNTOYCOMA":
            print("Error: Se esperaba un punto y coma")
            self.printer.addLine("Error: Se esperaba un punto y coma")
            self.errorSintactico=True
        else:
            self.printer.addLine(str(self.db.conteo()))
        print(self.db.conteo())

    def promedio(self):
        print("Entro promedio")
        self.consume()
        if self.consume().name != "PARENTESISIZQUIERDO":
            print("Error: Se esperaba un parentesis izquierdo")
            self.printer.addLine("Error: Se esperaba un parentesis izquierdo")
            self.errorSintactico=True
            
        if self.peek().name != "STRING":
            print("Error: Se esperaba un string")
            self.printer.addLine("Error: Se esperaba un string")
            self.errorSintactico=True
        else:
            clave = self.consume().value
        if self.consume().name != "PARENTESISDERECHO":
            print("Error: Se esperaba un parentesis derecho")
            self.printer.addLine("Error: Se esperaba un parentesis derecho")
            self.errorSintactico=True
            
        if self.consume().name != "PUNTOYCOMA":
            print("Error: Se esperaba un punto y coma")
            self.printer.addLine("Error: Se esperaba un punto y coma")
            self.errorSintactico=True
        else:
            self.printer.addLine(str(sum(self.db.claves[clave])/len(self.db.claves[clave])))
        
    def contarSi(self):
        
        print("Entro contar si")
        self.consume()
        if self.consume().name != "PARENTESISIZQUIERDO":
            print("Error: Se esperaba un parentesis izquierdo")
            self.printer.addLine("Error: Se esperaba un parentesis izquierdo")
            self.errorSintactico=True
        if self.peek().name != "STRING":
            print("Error: Se esperaba un string")
            self.printer.addLine("Error: Se esperaba un string")
            self.errorSintactico=True
        else:
            clave = self.consume().value
        if self.consume().name != "COMA":
            print("Error: Se esperaba una coma")
            self.printer.addLine("Error: Se esperaba una coma")
            self.errorSintactico=True
            
        if self.peek().name != "STRING" and self.peek().name != "NUMBER":
            print("Error: Se esperaba un valor de clave")
            self.printer.addLine("Error: Se esperaba un valor de clave")
            self.errorSintactico=True
        else:
            valor = self.consume().value

        if self.consume().name != "PARENTESISDERECHO":
            print("Error: Se esperaba un parentesis derecho")
            self.printer.addLine("Error: Se esperaba un parentesis derecho")
            self.errorSintactico=True
    
        if self.consume().name != "PUNTOYCOMA":
            print("Error: Se esperaba un punto y coma")
            self.printer.addLine("Error: Se esperaba un punto y coma")
            self.errorSintactico=True
        else:
        
            self.printer.addLine(str(self.db.contarSi(clave, valor)))


    def max(self):
        print("Entro max")
        self.consume()
        if self.consume().name != "PARENTESISIZQUIERDO":
            print("Error: Se esperaba un parentesis izquierdo")
            self.printer.addLine("Error: Se esperaba un parentesis izquierdo")
            self.errorSintactico=True
        if self.peek().name != "STRING":
            print("Error: Se esperaba un string")
            self.printer.addLine("Error: Se esperaba un string")
            self.errorSintactico=True
        else:
            clave = self.consume().value
        if self.consume().name != "PARENTESISDERECHO":
            print("Error: Se esperaba un parentesis derecho")
            self.printer.addLine("Error: Se esperaba un parentesis derecho")
            self.errorSintactico=True
        if self.consume().name != "PUNTOYCOMA":
            print("Error: Se esperaba un punto y coma")
            self.printer.addLine("Error: Se esperaba un punto y coma")
            self.errorSintactico=True
        else:
            self.printer.addLine(str(max(self.db.claves[clave])))

    def min(self):
        print("Entro min")
        self.consume()
        if self.consume().name != "PARENTESISIZQUIERDO":
            print("Error: Se esperaba un parentesis izquierdo")
            
        if self.peek().name != "STRING":
            print("Error: Se esperaba un string")
        else:
            clave = self.consume().value
        if self.consume().name != "PARENTESISDERECHO":
            print("Error: Se esperaba un parentesis derecho")
            
        if self.consume().name != "PUNTOYCOMA":
            print("Error: Se esperaba un punto y coma")
        else: 
            self.printer.addLine(str(min(self.db.claves[clave])))


    #imprimir todos los datos de la base de datos
    def datos(self):
        print("Entro datos")
        self.consume()
        if self.consume().name != "PARENTESISIZQUIERDO":
            print("Error: Se esperaba un parentesis izquierdo")
            self.printer.addLine("Error: Se esperaba un parentesis izquierdo")
            self.errorSintactico=True
            
        if self.consume().name != "PARENTESISDERECHO":
            print("Error: Se esperaba un parentesis derecho")
            self.printer.addLine("Error: Se esperaba un parentesis derecho")
            self.errorSintactico=True
            
        if self.consume().name != "PUNTOYCOMA":
            print("Error: Se esperaba un punto y coma")
            self.printer.addLine("Error: Se esperaba un punto y coma")
            self.errorSintactico=True
        else:
            stringClaves=""
            for clave in self.db.claves:
                stringClaves=stringClaves+str(clave) + " "
            self.printer.addLine(stringClaves)
            #crear un while hasta la cantidad de claves    
            for i in range(self.db.conteo()):
                resultado=""
                for clave in self.db.claves:
                    resultado=resultado+str(self.db.claves[clave][i]) + " "
                self.printer.addLine(resultado)
            

    def sumar(self):
        print("Entro sumar")
        self.consume()
        if self.consume().name != "PARENTESISIZQUIERDO":
            print("Error: Se esperaba un parentesis izquierdo")
            self.printer.addLine("Error: Se esperaba un parentesis izquierdo")
            self.errorSintactico=True
        if self.peek().name != "STRING":
            print("Error: Se esperaba un string")
            self.printer.addLine("Error: Se esperaba un string")
            self.errorSintactico=True
        else:
            clave = self.consume().value
        if self.consume().name != "PARENTESISDERECHO":
            print("Error: Se esperaba un parentesis derecho")
            self.printer.addLine("Error: Se esperaba un parentesis derecho")
            self.errorSintactico=True
            
        if self.consume().name != "PUNTOYCOMA":
            print("Error: Se esperaba un punto y coma")
            self.printer.addLine("Error: Se esperaba un punto y coma")
            self.errorSintactico=True
        else:
            self.printer.addLine(str(sum(self.db.claves[clave])))

    def exportarReporteError(self):
        print("Entro exportar reporte")
        #imprimir errrores
    
    # Crea el contenido HTML que deseas exportar
        html_content = """
        <html>
        <head>
            <title>Reporte</title>
            <link rel="stylesheet" type="text/css" href="style.css">
        </head>
        <body>
            <div class="container">
                <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body text-center">
                            """
        html_content += """
                            <h5 class="card-title m-b-0">Reporte Errores</h5>
                        </d iv>
                        <div class="table-responsive">
                            <table class="table">
                                <thead class="thead-light">
                                    <tr>
                                        <th>
                                            <label class="customcheckbox m-b-20">
                                                <input type="checkbox" id="mainCheckbox">
                                                <span class="checkmark"></span>
                                            </label>
                                        </th>
        
                                        <th scope="col">Tipo Token</th>
                                        <th scope="col">Lexemaa</th>
                                        <th scope="col">Fila</th>
                                        <th scope="col">Columna</th>
                                        
                                   
                                    </tr>
                                </thead>
                                <tbody class="customtable">
                                """
        ##crea un ciclo for con todos los errores
        for i in range(len(self.db.errores["token"])):
            html_content += """             
                                    <tr>
                                        <th>
                                            <label class="customcheckbox">
                                                <input type="checkbox" class="listCheckbox">
                                                <span class="checkmark"></span>
                                            </label>
                                        </th>
                                        <td>"""+self.db.errores["token"][i]+"""</td>
                                        <td>"""+self.db.errores["lexema"][i]+"""</td>
                                        <td>"""+str(self.db.errores["fila"][i])+"""</td>
                                        <td>"""+str(self.db.errores["columna"][i])+"""</td>
                                    </tr>
                                    """
        html_content += """
                                    <!-- Agrega más filas de la tabla aquí -->
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    # Escribe el contenido HTML en un archivo HTML
        with open('reporte.html', 'w') as html_file:
            html_file.write(html_content)

    # Abre el archivo HTML en el navegador predeterminado
        webbrowser.open('reporte.html')


    def exportarReporte(self):
        print("Entro exportar reporte")
        #imprimir errrores
        for i in range(len(self.db.errores["token"])):
            print(self.db.errores["token"][i], self.db.errores["lexema"][i], self.db.errores["fila"][i], self.db.errores["columna"][i])
        self.consume()
        if self.consume().name != "PARENTESISIZQUIERDO":
            print("Error: Se esperaba un parentesis izquierdo")
            self.printer.addLine("Error: Se esperaba un parentesis izquierdo")
            self.errorSintactico=True
            return
        if self.peek().name != "STRING":
            print("Error: Se esperaba un string")
            self.printer.addLine("Error: Se esperaba un string")
            self.errorSintactico=True
            return
        clave = self.consume().value
        if self.consume().name != "PARENTESISDERECHO":
            print("Error: Se esperaba un parentesis derecho")
            self.printer.addLine("Error: Se esperaba un parentesis derecho")
            self.errorSintactico=True
            return
        if self.consume().name != "PUNTOYCOMA":
            print("Error: Se esperaba un punto y coma")
            self.printer.addLine("Error: Se esperaba un punto y coma")
            self.errorSintactico=True
            return
    
    # Crea el contenido HTML que deseas exportar
        html_content = """
        <html>
        <head>
            <title>Reporte</title>
            <link rel="stylesheet" type="text/css" href="style.css">
        </head>
        <body>
            <div class="container">
                <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body text-center">
                            """
        html_content += """
                            <h5 class="card-title m-b-0">"""+clave+"""</h5>
                        </d iv>
                        <div class="table-responsive">
                            <table class="table">
                                <thead class="thead-light">
                                    <tr>
                                        <th>
                                            <label class="customcheckbox m-b-20">
                                                <input type="checkbox" id="mainCheckbox">
                                                <span class="checkmark"></span>
                                            </label>
                                        </th>
                                    """
        for clave in self.db.claves:
            html_content += """ 
                                        <th scope="col">"""+str(clave)+"""</th>
                                        """
        html_content += """
                                    </tr>
                                </thead>
                                <tbody class="customtable">
                                """
        for i in range(self.db.conteo()):
            html_content += """ 
                                                <tr>
                                        <th>
                                            <label class="customcheckbox">
                                                <input type="checkbox" class="listCheckbox">
                                                <span class="checkmark"></span>
                                            </label>
                                        </th>
                                        """
            for clave in self.db.claves:
                html_content += """             

                                        <td>"""+str(self.db.claves[clave][i])+"""</td>
                                        """
            html_content += """
                                    </tr>
                                    """
        html_content += """
                                    <!-- Agrega más filas de la tabla aquí -->
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    # Escribe el contenido HTML en un archivo HTML
        name = clave+".html"
        with open(name, 'w') as html_file:
            html_file.write(html_content)

    # Abre el archivo HTML en el navegador predeterminado
        webbrowser.open(name)

# Llama a la función para exportar y abrir el reporte

