from abc import ABC, abstractmethod
from textblob import TextBlob

class Sentimiento(ABC):
    
    @abstractmethod
    def analizar_sentimiento(self, texto):
        pass

class AnalizadorSentimiento(Sentimiento):
    def __init__(self):
        self._texto = ""
        self._resultado = None
    
    @property
    def texto(self):
        return self._texto
    
    @texto.setter
    def texto(self, texto):
        self._texto = texto
    
    @property
    def resultado(self):
        return self._resultado
    
    '''def traducir_texto(self, texto):
        blob=TextBlob(texto)
        texto_traducido = blob.translate(to="en")
        return str(texto_traducido)'''
    
    def analizar_sentimiento(self, texto):
        #texto_traducido = self.traducir_texto(texto)
        blob = TextBlob(texto)
        polaridad = blob.sentiment.polarity
        
        if polaridad > 0:
            self._resultado = "Positivo"
        elif polaridad < 0:
            self._resultado = "Negativo"
        else:
            self._resultado = "Neutro"
        
        return self._resultado  # Devuelve el resultado
