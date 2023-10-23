#analizador sintatico
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index=0

    def consume(self):
        token = self.tokens[self.index]
        self.index += 1
        return token
    
    def peek(self):
        return self.tokens[self.index]
    
    def parse(self):
        while self.index < len(self.tokens):
            if self.peek().name == "IMPRIMIR":
                self.imprimir()

    def imprimir(self):
        self.consume() #imprimir generar los errones
        if self.consume().name != "PARENTESISIZQUIERDO":
            print("Error: Se esperaba un parentesis izquierdo")
            return
        token = self.consume()
        if token.name != "STRING":
            print("Error: Se esperaba un string")
            return
        if self.consume().name != "PARENTESISDERECHO":
            print("Error: Se esperaba un parentesis derecho")
            return
        if self.consume().name != "PUNTOYCOMA":
            print("Error: Se esperaba un punto y coma")
            return
        print(token.value)