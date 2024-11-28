# embedding.py
# -*- coding: utf-8 -*-
import logging
from ollama import Client as OllamaClient

# Configuración del logger
logging.basicConfig(level=logging.INFO)

def generar_embeddings_ollama(texto):
    """Genera embeddings usando el modelo mxbai-embed-large de Ollama."""
    try:
        ollama_client = OllamaClient()

        # Llamada a la función embeddings con el formato correcto
        response = ollama_client.embeddings(
            model='mxbai-embed-large',
            prompt=texto
        )

        logging.info("Embeddings generados con éxito.")
        return response

    except Exception as e:
        logging.error(f"Error al generar embeddings con Ollama: {e}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    texto = "Llamas are members of the camelid family"
    embeddings = generar_embeddings_ollama(texto)
    print("Embeddings:\n", embeddings)
