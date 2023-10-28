import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from lexem import tokenize_input
from bparser import Parser

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
        return

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
