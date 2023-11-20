# Analizador de Texto Interactivo

Este proyecto consiste en un analizador de texto interactivo que realiza tanto el análisis léxico como el análisis sintáctico de un conjunto de instrucciones simples. La aplicación cuenta con una interfaz de usuario desarrollada en `tkinter` y ofrece funcionalidades básicas como la ejecución de comandos y la visualización de resultados.

## Estructura del Proyecto

### 1. Archivo `app.py`

El archivo `app.py` define la interfaz de usuario principal utilizando la biblioteca `tkinter`. Aquí, se encuentran los elementos gráficos y la lógica para la interacción del usuario.

```python
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from lexem import tokenize_input
from bparser import Parser
import webbrowser
```

Se importan las bibliotecas necesarias, incluyendo aquellas para la interfaz gráfica, el análisis léxico, y el manejo del navegador.

```python
class MainWindow:
    def __init__(self, root):
        # Inicialización de la interfaz gráfica y creación de widgets
```

Se define la clase principal `MainWindow`, encargada de gestionar la ventana principal de la aplicación.

### 2. Archivo `lexem.py`

En `lexem.py`, se realiza el análisis léxico del texto. Define la estructura básica de un token y la función principal para el análisis léxico.

```python
from collections import namedtuple
Token = namedtuple('Token', ['name', 'value', 'line', 'column'])
```

Se define una estructura `Token` que describe la estructura básica de un token en el lenguaje.

```python
reservados = {...}
```

Se listan las palabras reservadas y símbolos especiales del lenguaje.

```python
def tokenize_input(input_str):
    # Implementación de la función principal para el análisis léxico
```

La función `tokenize_input` realiza el análisis léxico del texto y devuelve una lista de tokens.

### 3. Archivo `db.py`

El archivo `db.py` gestiona una estructura de datos que simula una base de datos y el manejo de errores.

```python
class DB:
    def __init__(self):
        # Inicialización de la "base de datos" y registro de errores
```

Se inicializa una "base de datos" con un conjunto de claves y un registro de errores.

```python
def agregarError(self, token, lexema, fila, columna):
    # Función para registrar un error en la base de datos
```

La función `agregarError` permite registrar un error en la base de datos.

```python
def agregarClave(self, clave):
    # Función para añadir una clave a la base de datos
```

La función `agregarClave` permite añadir una clave a la base de datos.

```python
def imprimirErrores(self):
    # Función para mostrar los errores registrados en la base de datos
```

La función `imprimirErrores` muestra los errores registrados en la base de datos.

### 4. Archivo `analizador.py`

En `analizador.py`, se encuentra la implementación del analizador sintáctico, que procesa la lista de tokens generada por el análisis léxico.

```python
from printer import Printer
from db import DB
import webbrowser
```

Se importan módulos externos, incluyendo `Printer` para construir el texto de salida y `DB` para manejar la base de datos.

```python
class Parser:
    def __init__(self, tokens):
        # Inicialización del analizador sintáctico
```

Se define la clase `Parser`, responsable del análisis sintáctico.

```python
def consume(self):
    # Función para avanzar al siguiente token en la lista de tokens
```

La función `consume` se utiliza para avanzar al siguiente token.

```python
def peek(self):
    # Función para obtener el token actual sin avanzar el índice
```

La función `peek` permite obtener el token actual sin avanzar el índice.

```python
def parse(self):
    # Función principal para el análisis sintáctico
```

La función `parse` recorre los tokens y decide cómo procesar cada uno según su tipo.

```python
def revertir(self):
    # Función para retroceder al token anterior si es necesario
```

La función `revertir` permite retroceder al token anterior si es necesario.

```python
def obtenerTexto(self):
    # Función para obtener el texto generado hasta el momento
```

La función `obtenerTexto` devuelve el texto generado hasta el momento.

```python
def imprimir(self):
    # Implementación para procesar la instrucción "IMPRIMIR"
```

La función `imprimir` se encarga de procesar la instrucción "IMPRIMIR".

## Uso de la Aplicación

1. Ejecute el archivo `app.py` para iniciar la interfaz de usuario.
2. Ingrese las instrucciones en el área de texto y haga clic en el botón "Ejecutar".
3. Visualice los resultados y mensajes en la interfaz.

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).
