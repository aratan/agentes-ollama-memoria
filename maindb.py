# maindb.py
# -*- coding: utf-8 -*-
import ollama
import chromadb
from colorama import Fore, Style

def generar_incrustaciones_y_almacenar(documents):
    """Genera incrustaciones (embeddings) para los documentos y los almacena en una base de datos vectorial."""
    try:
        client = chromadb.Client()
        collection = client.create_collection(name="docs")

        # Genera y almacena embeddings
        for i, d in enumerate(documents):
            response = ollama.embeddings(model="mxbai-embed-large", prompt=d)
            embedding = response["embedding"]
            collection.add(
                ids=[str(i)],
                embeddings=[embedding],
                documents=[d]
            )
        print(Fore.GREEN + "Embeddings generados y almacenados con éxito." + Style.RESET_ALL)
        return collection
    except Exception as e:
        print(Fore.RED + f"Error al generar o almacenar embeddings: {e}" + Style.RESET_ALL)
        return None

def recuperar_documento_relevante(collection, prompt):
    """Genera un embedding para el prompt y recupera el documento más relevante."""
    try:
        # Generar embedding para el prompt
        response = ollama.embeddings(
            model="mxbai-embed-large",
            prompt=prompt
        )
        embedding = response["embedding"]

        # Consultar el documento más relevante
        results = collection.query(
            query_embeddings=[embedding],
            n_results=1
        )
        data = results['documents'][0][0]
        print(Fore.GREEN + f"Documento recuperado: {data}" + Style.RESET_ALL)
        return data
    except Exception as e:
        print(Fore.RED + f"Error al recuperar el documento: {e}" + Style.RESET_ALL)
        return None
