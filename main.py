# main.py
# -*- coding: utf-8 -*-
import ollama
import chromadb
import os
import sys
from colorama import Fore, Style
from maindb import generar_incrustaciones_y_almacenar, recuperar_documento_relevante
from agent import generar_respuesta, hacer_pregunta
from voice import reproducir_respuesta_en_voz

# Función para cargar documentos de todos los archivos .txt en un directorio
def cargar_documentos(directorio):
    documentos = []
    try:
        for filename in os.listdir(directorio):
            if filename.endswith('.txt'):
                with open(os.path.join(directorio, filename), 'r', encoding='utf-8') as file:
                    documentos.extend(file.readlines())
        print(Fore.GREEN + "Documentos cargados desde el directorio." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error al cargar documentos: {e}" + Style.RESET_ALL)
    return [doc.strip() for doc in documentos]  # Limpia espacios en blanco

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python main.py <prompt>")
        sys.exit(1)

    prompt = sys.argv[1]

    # Definir el directorio donde se encuentran los archivos de texto
    directorio = "datos"  # Cambia esta ruta según sea necesario

    # Paso 1: Cargar documentos desde todos los archivos .txt en el directorio
    documentos = cargar_documentos(directorio)

    # Paso 2: Generar incrustaciones y almacenar
    collection = generar_incrustaciones_y_almacenar(documentos)

    if collection:
        # Paso 3: Recuperar documento más relevante
        data = recuperar_documento_relevante(collection, prompt)

        # Paso 4: Pasar los datos al agente para generar una respuesta
        if data:
            respuesta = generar_respuesta(prompt, data)
            print(Fore.CYAN + "Respuesta generada:\n" , respuesta)
            print( Style.RESET_ALL, '*****************')
            agente = hacer_pregunta(data)
            print(Fore.CYAN, agente)
            # Paso 5: Reproducir la respuesta en voz
            reproducir_respuesta_en_voz(respuesta)
            reproducir_respuesta_en_voz(agente)
