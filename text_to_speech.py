from gtts import gTTS
import pygame
import os

def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    filename = "temp_tts.mp3"
    tts.save(filename)
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass
    pygame.mixer.music.unload()
    os.remove(filename)
