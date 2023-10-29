import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from lexem import tokenize_input
from bparser import Parser
import webbrowser

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Interfaz con Paneles")
        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        # Botón para seleccionar el panel
        boton_seleccionar = tk.Button(self.root, text="Ejecutar", command=self.ejecutar)
        boton_seleccionar.pack(pady=10)

        # Crear dos paneles de texto
        self.texto_panel1 = tk.Text(self.root, height=30, width=40)
        self.texto_panel2 = tk.Text(self.root, height=30, width=40)
        self.texto_panel1.pack(side=tk.LEFT, padx=20)
        self.texto_panel2.pack(side=tk.RIGHT, padx=20)

        # Inicialmente, el texto del "Panel 2" estará desactivado
        self.texto_panel2.config(state=tk.NORMAL)

    def opcion_seleccionada(self):
        self.texto_panel1.config(state=tk.NORMAL)
        self.texto_panel2.config(state=tk.DISABLED)

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Abrir", command=self.abrir_archivo)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.root.quit)

        view_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Reportes", menu=view_menu)
        view_menu.add_command(label="Reporte de Tokens", command=self.reporte_tokens)
        view_menu.add_command(label="Reporte de Errores", command=self.reporte_errores)
        view_menu.add_command(label="Arbol de derivacion")

    def reporte_tokens(self):
        tokens = tokenize_input(self.texto_panel1.get(1.0, tk.END))
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
        
                                        <th scope="col">Token</th>
                                        <th scope="col">Lexemaa</th>
                                        <th scope="col">Fila</th>
                                        <th scope="col">Columna</th>
                                        
                                   
                                    </tr>
                                </thead>
                                <tbody class="customtable">
                                """
        
        for i in tokens:
            html_content += """
                                    <tr>
                                        <th>
                                            <label class="customcheckbox">
                                                <input type="checkbox" class="listCheckbox">
                                                <span class="checkmark"></span>
                                            </label>
                                        </th>
                                        <td>"""+str(i.name)+"""</td>
                                        <td>"""+str(i.value)+"""</td>
                                        <td>"""+str(i.line)+"""</td>
                                        <td>"""+str(i.column)+"""</td>
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
        with open('reporteTokens.html', 'w') as html_file:
            html_file.write(html_content)

    # Abre el archivo HTML en el navegador predeterminado
        webbrowser.open('reporteTokens.html')

        for i in tokens:
            
            print(i.name, i.value, i.line, i.column)
        print("-"*50)


    def reporte_errores(self):
        tokens = tokenize_input(self.texto_panel1.get(1.0, tk.END))
        parser = Parser(tokens)
        parser.parse()
        parser.exportarReporteError()

    def abrir_archivo(self):
        # Abrir el archivo
        path = filedialog.askopenfilename(filetypes=[("Archivos bizdata", "*.bizdata")])
        if path:
            self.path = path
            with open(path, 'r') as file:
                content_data = file.read()
                self.texto_panel1.delete(1.0, tk.END)
                self.texto_panel1.insert(tk.END, content_data)
    def ejecutar(self):
        tokens = tokenize_input(self.texto_panel1.get(1.0, tk.END))
        parser = Parser(tokens)
        parser.parse()
        content_data = parser.obtenerTexto()
        self.texto_panel2.delete(1.0, tk.END)
        self.texto_panel2.insert(tk.END, content_data)
        
def main():
    ventana = tk.Tk()
    app = MainWindow(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    main()
