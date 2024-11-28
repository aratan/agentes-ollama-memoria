# agent.py
# -*- coding: utf-8 -*-
from ollama import Client as OllamaClient
from colorama import Fore, Style

ollama_client = OllamaClient()

def llamar_ollama(model, prompt):
    """Realiza una llamada a la API de Ollama y maneja errores."""
    try:
        response = ollama_client.generate(model=model, prompt=prompt)
        return response['response']
    except Exception as e:
        print(Fore.RED + f"Error al llamar a la API de Ollama: {e}" + Style.RESET_ALL)
        return None

def generar_embeddings(texto):
    """Genera embeddings usando el modelo mxbai-embed-large de Ollama."""
    try:
        response = ollama_client.embeddings(model='mxbai-embed-large', prompt=texto)
        print(Fore.GREEN + "Embeddings generados con éxito." + Style.RESET_ALL)
        return response
    except Exception as e:
        print(Fore.RED + f"Error al generar embeddings con Ollama: {e}" + Style.RESET_ALL)
        return None

def generar_respuesta(prompt, data):
    """Genera una respuesta utilizando el prompt y el documento recuperado."""
    prompt_completo = f"Usa estos datos: {data}. Responde en este prompt: {prompt}"
    respuesta = llamar_ollama(model="aratan/razon", prompt=prompt_completo)
    if respuesta:
        print(Fore.GREEN + "Respuesta generada con éxito." + Style.RESET_ALL)
    return respuesta

def hacer_pregunta(data):
    """Genera una pregunta basada en los datos proporcionados."""
    prompt = "¿Es hombre o mujer?"
    prompt_completo = f"{prompt} {data}"
    respuesta = llamar_ollama(model="aratan/razon", prompt=prompt_completo)
    if respuesta:
        print(Fore.GREEN + "Pregunta generada con éxito." + Style.RESET_ALL)
    return respuesta

