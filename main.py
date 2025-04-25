from textblob import TextBlob
from googletrans import Translator

translator = Translator()

def analizar_sentimiento(frase):
    try:
        traduccion = translator.translate(frase, dest='en')  # Traducimos al inglés
        #print(f"Traducción: {traduccion.text}")  # Puedes quitar esta línea si no quieres mostrar la traducción
        blob = TextBlob(traduccion.text)
        polaridad = blob.sentiment.polarity

        if polaridad > 0:
            return "Sentimiento positivo 😊"
        elif polaridad < 0:
            return "Sentimiento negativo 😠"
        else:
            return "Sentimiento neutral 😐"
    except Exception as e:
        return f"Error al analizar: {e}"

# Bucle de prueba
while True:
    texto = input("Escribe una frase (o 'salir' para terminar): ")
    if texto.lower() == 'salir':
        break
    resultado = analizar_sentimiento(texto)
    print(resultado)
