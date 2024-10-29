import tkinter as tk
from tkinter import messagebox

class VistaAnalizador:

    def __init__(self, controlador):
        self.controlador = controlador
        
        
        # Configuración de la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("EmotiSense")
        self.ventana.geometry("400x200")
        self.ventana.resizable(False, False)
        
        # Campo de entrada de texto
        self.etiqueta_texto = tk.Label(self.ventana, text="Ingresa un texto:")
        self.etiqueta_texto.pack()

        self.entrada_texto = tk.Entry(self.ventana, width=50, borderwidth=5, relief="groove" )
        self.entrada_texto.pack()

        # Botón para analizar
        self.boton_analizar = tk.Button(self.ventana, text="Analizar Sentimiento", command=self.analizar_sentimiento)
        self.boton_analizar.pack()

        # Etiqueta para mostrar el resultado
        self.etiqueta_resultado = tk.Label(self.ventana, text="Resultado: ")
        self.etiqueta_resultado.pack()
        
    def obtener_texto(self):
        #Obtiene el texto del campo de entrada.
        return self.entrada_texto.get()

    def mostrar_resultado(self, resultado):
        #Muestra el resultado del análisis en la interfaz.
        self.etiqueta_resultado.config(text=f"Resultado: {resultado}")

    def analizar_sentimiento(self):
        #Maneja el evento del botón de análisis.
        texto = self.obtener_texto()
        if texto:
            self.controlador.analizar(texto)
        else:
            messagebox.showerror("Error", "El campo de texto está vacío")
    
    def iniciar(self):
        #Inicia el bucle principal de la ventana.
        self.ventana.mainloop()
        