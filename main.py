from lexem import tokenize_input
from bparser import Parser
entrada = open("entrada.bizdata", "r").read()
tokens = tokenize_input(entrada)

print("-"*50)
for i in tokens:
    print(i.name, i.value, i.line, i.column)
print("-"*50)
parser = Parser(tokens)
parser.parse()

parser.exportarReporteError()

