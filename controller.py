
from model import AnalizadorSentimiento
from view import VistaAnalizador

class Controlador:
    def __init__(self):
        self.modelo = AnalizadorSentimiento()
        self.vista = VistaAnalizador(self)

    def analizar(self, texto):
        """Maneja el análisis de sentimiento."""
        self.modelo.texto = texto
        resultado = self.modelo.analizar_sentimiento(texto)
        self.vista.mostrar_resultado(resultado)

    def iniciar(self):
        """Inicia la aplicación."""
        self.vista.iniciar()
