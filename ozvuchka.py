import pystray
import PIL.Image
import threading
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from gtts import gTTS
from playsound import playsound
from time import *

class Button:
    
    def __init__(self, lang):
        self.lang = lang

    def press(self):
        global voiceLanguage
        global toggle
        toggle = True
        voiceLanguage = self.lang
        if not t1.is_alive():
            t1.start()

def voice():
    global voiceLanguage
    global toggle
    global driver
    with open("chat_url.txt", "r", encoding="utf-8") as file:
        chat_url = file.read()
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(chat_url)
    message_list = []
    while toggle:
        htmlSource = driver.page_source
        soup = BeautifulSoup(htmlSource, "html.parser")
        parsedMessages = soup.find_all("span", class_="text-fragment")
        if len(parsedMessages) != len(message_list):
            len_difference = len(parsedMessages) - len(message_list)
            for i in range(len_difference, 0, -1):
                message = str(parsedMessages[-i])[62:]
                message = message[:-7]
                tts = gTTS(text=message, lang=voiceLanguage)
                try:
                    tts.save("tmp.mp3")
                    playsound("tmp.mp3")
                    os.remove('tmp.mp3')
                except AssertionError:
                    os.remove('tmp.mp3')
                message_list.append(message)
        sleep(1)

def exit_button(icon):
    global toggle
    global driver
    toggle = False
    if t1.is_alive():
        t1.join()
    try:
        driver.quit()
    except NameError:
        pass
    return icon.stop()

def run_icon():
    image = PIL.Image.open("bogdan.png")
    icon = pystray.Icon("ITStart", image, menu=pystray.Menu(
        pystray.MenuItem("ru", Button("ru").press),
        pystray.MenuItem("en", Button("en").press),
        pystray.MenuItem("uk", Button("uk").press),
        pystray.MenuItem("pl", Button("pl").press),
        pystray.MenuItem("ja", Button("ja").press),
        pystray.MenuItem("exit", exit_button),
    ))
    return icon.run()

t1 = threading.Thread(target=voice)
run_icon()
