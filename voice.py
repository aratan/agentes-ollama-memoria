# voice.py
# -*- coding: utf-8 -*-
from gtts import gTTS
import pygame
import tempfile
import time
from colorama import Fore, Style

def reproducir_respuesta_en_voz(respuesta):
    """Convierte la respuesta en audio y la reproduce usando pygame."""
    try:
        # Generar audio usando gTTS
        tts = gTTS(respuesta, lang='es', slow=False)  # Establece slow a False para aumentar la velocidad
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            audio_path = fp.name

        # Inicializar pygame mixer y reproducir el audio
        pygame.mixer.init()
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()

        # Esperar hasta que termine la reproducción
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.quit()
        print(Fore.GREEN + "Respuesta reproducida en voz con éxito." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error al reproducir la respuesta en voz: {e}" + Style.RESET_ALL)
