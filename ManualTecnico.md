### Manual Técnico

#### 1. Archivo `app.py`

El archivo `app.py` describe una interfaz de usuario basada en `tkinter` que permite interacción y procesamiento de texto.

```python
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from lexem import tokenize_input
from bparser import Parser
import webbrowser
```
Se importan las bibliotecas necesarias para la interfaz gráfica, el análisis léxico, y el manejo del navegador.

```python
class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Interfaz con Paneles")
        self.create_widgets()
        self.create_menu()
```
Se define la clase principal `MainWindow`. En su constructor se inicializan los widgets y el menú.

```python
def create_widgets(self):
        boton_seleccionar = tk.Button(self.root, text="Ejecutar", command=self.ejecutar)
        boton_seleccionar.pack(pady=10)
        ...
```
Dentro de `create_widgets`, se configura un botón y dos paneles de texto.

```python
def create_menu(self):
    ...
```
`create_menu` es el método que construye el menú de la aplicación.

```python
def reporte_tokens(self):
    tokens = tokenize_input(self.texto_panel1.get(1.0, tk.END))
    ...
```
`reporte_tokens` genera un informe basado en los tokens del texto del panel.

#### 2. Archivo `lexem.py`

En `lexem.py` se realiza el análisis léxico del texto.

```python
from collections import namedtuple
Token = namedtuple('Token', ['name', 'value', 'line', 'column'])
```
Se define una estructura `Token` que describe la estructura básica de un token en el lenguaje.

```python
reservados = {...}
```
Se listan todas las palabras reservadas y símbolos especiales del lenguaje.

```python
def tokenize_input(input_str):
    ...
```
`tokenize_input` es la función principal que realiza el análisis léxico del texto y devuelve una lista de tokens.

#### 3. Archivo `db.py`

El archivo `db.py` gestiona una estructura de datos que simula una base de datos y el manejo de errores.

```python
class DB:
    def __init__(self):
        ...
```
Se inicializa una "base de datos" con un conjunto de claves y un registro de errores.

```python
def agregarError(self, token, lexema, fila, columna):
    ...
```
`agregarError` permite registrar un error en la base de datos.

```python
def agregarClave(self, clave):
    ...
```
`agregarClave` permite añadir una clave a la base de datos.

```python
def imprimirErrores(self):
    ...
```
`imprimirErrores` muestra los errores registrados en la base de datos.

Claro, explicaré el código por partes:
### Archivo Analizador.py
#### Importaciones
```python
from printer import Printer
from db import DB
import webbrowser
```

Estas son importaciones de módulos externos. El módulo `Printer` se utiliza para construir y mantener un texto de salida, y `DB` se utiliza para manejar una base de datos ficticia en la que se pueden almacenar claves y valores. `webbrowser` se importa para abrir archivos HTML en el navegador más adelante.

### Clase `Parser`

```python
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.printer = Printer()
        self.db = DB()
        self.errorSintactico = False
```

Aquí se define la clase `Parser`. La instancia de esta clase se utiliza para analizar una lista de tokens. Algunos atributos importantes son:
- `self.tokens`: Almacena la lista de tokens a analizar.
- `self.index`: Un índice que rastrea la posición actual en la lista de tokens.
- `self.printer`: Una instancia de la clase `Printer` utilizada para construir el texto de salida.
- `self.db`: Una instancia de la clase `DB` utilizada para simular una base de datos que puede contener claves y valores.
- `self.errorSintactico`: Un indicador para rastrear errores sintácticos.

### Función `consume`

```python
def consume(self):
    token = self.tokens[self.index]
    self.index += 1
    return token
```

La función `consume` se utiliza para avanzar al siguiente token en la lista `tokens` y devolver el token actual.

### Función `peek`

```python
def peek(self):
    return self.tokens[self.index]
```

La función `peek` permite obtener el token actual sin avanzar el índice.

### Función `parse`

```python
def parse(self):
    while self.index < len(self.tokens):
        # Implementación de la lógica de análisis para diferentes tipos de tokens
```

La función `parse` es la función principal que recorre todos los tokens y decide cómo procesar cada uno de acuerdo con su tipo. En tu código, se han implementado casos para diferentes instrucciones, como "IMPRIMIR", "IMPRIMIRLN", "CLAVES", etc.

### Funciones `revertir` y `obtenerTexto`

```python
def revertir(self):
    self.index -= 1

def obtenerTexto(self):
    return self.printer.print()
```

`revertir` permite retroceder al token anterior si es necesario. `obtenerTexto` devuelve el texto generado hasta el momento.

### Función `imprimir`

```python
def imprimir(self):
    # Implementación para procesar la instrucción "IMPRIMIR"
```

La función `imprimir` se encarga de procesar la instrucción "IMPRIMIR". Verifica la sintaxis correcta de la instrucción y agrega el texto que se va a imprimir al resultado.

Las otras funciones, como `imprimirln`, `claves`, y las demás, siguen una estructura similar. Cada una procesa su propia instrucción y verifica la sintaxis correspondiente.

