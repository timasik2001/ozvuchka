import pystray
import PIL.Image
import threading
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup;
from gtts import gTTS
from playsound import playsound
from time import *

with open("chat_url.txt", "r", encoding="utf-8") as file:
    chat_url = str(file.read())
chrome_options = Options()
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)
driver.get(chat_url)
message_list = []
toggle = False
ru_loop = False
en_loop = False
uk_loop = False
pl_loop = False
ja_loop = False

def ru_voice():
    while toggle:
        while ru_loop:
            htmlSource = driver.page_source
            soup = BeautifulSoup(htmlSource, "html.parser")
            parsedMessages = soup.find_all("span", class_="text-fragment")
            if len(parsedMessages) != len(message_list):
                len_difference = len(parsedMessages) - len(message_list)
                for i in range(len_difference, 0, -1):
                    message = str(parsedMessages[-i])[62:]
                    message = message[:-7]
                    tts = gTTS(text=message, lang="ru")
                    try:
                        tts.save("tmp.mp3")
                        playsound("tmp.mp3")
                        os.remove('tmp.mp3')
                    except AssertionError:
                        os.remove('tmp.mp3')
                    message_list.append(message)
        sleep(1)
    return None

def en_voice():
    while toggle:
        while en_loop:
            htmlSource = driver.page_source
            soup = BeautifulSoup(htmlSource, "html.parser")
            parsedMessages = soup.find_all("span", class_="text-fragment")
            if len(parsedMessages) != len(message_list):
                len_difference = len(parsedMessages) - len(message_list)
                for i in range(len_difference, 0, -1):
                    message = str(parsedMessages[-i])[62:]
                    message = message[:-7]
                    tts = gTTS(text=message, lang="en")
                    try:
                        tts.save("tmp.mp3")
                        playsound("tmp.mp3")
                        os.remove('tmp.mp3')
                    except AssertionError:
                        os.remove('tmp.mp3')
                    message_list.append(message)
        sleep(1)
    return None

def uk_voice():
    while toggle:
        while uk_loop:
            htmlSource = driver.page_source
            soup = BeautifulSoup(htmlSource, "html.parser")
            parsedMessages = soup.find_all("span", class_="text-fragment")
            if len(parsedMessages) != len(message_list):
                len_difference = len(parsedMessages) - len(message_list)
                for i in range(len_difference, 0, -1):
                    message = str(parsedMessages[-i])[62:]
                    message = message[:-7]
                    tts = gTTS(text=message, lang="uk")
                    try:
                        tts.save("tmp.mp3")
                        playsound("tmp.mp3")
                        os.remove('tmp.mp3')
                    except AssertionError:
                        os.remove('tmp.mp3')
                    message_list.append(message)
        sleep(1)
    return None

def pl_voice():
    while toggle:
        while pl_loop:
            htmlSource = driver.page_source
            soup = BeautifulSoup(htmlSource, "html.parser")
            parsedMessages = soup.find_all("span", class_="text-fragment")
            if len(parsedMessages) != len(message_list):
                len_difference = len(parsedMessages) - len(message_list)
                for i in range(len_difference, 0, -1):
                    message = str(parsedMessages[-i])[62:]
                    message = message[:-7]
                    tts = gTTS(text=message, lang="pl")
                    try:
                        tts.save("tmp.mp3")
                        playsound("tmp.mp3")
                        os.remove('tmp.mp3')
                    except AssertionError:
                        os.remove('tmp.mp3')
                    message_list.append(message)
        sleep(1)
    return None

def ja_voice():
    while toggle:
        while ja_loop:
            htmlSource = driver.page_source
            soup = BeautifulSoup(htmlSource, "html.parser")
            parsedMessages = soup.find_all("span", class_="text-fragment")
            if len(parsedMessages) != len(message_list):
                len_difference = len(parsedMessages) - len(message_list)
                for i in range(len_difference, 0, -1):
                    message = str(parsedMessages[-i])[62:]
                    message = message[:-7]
                    tts = gTTS(text=message, lang="ja")
                    try:
                        tts.save("tmp.mp3")
                        playsound("tmp.mp3")
                        os.remove('tmp.mp3')
                    except AssertionError:
                        os.remove('tmp.mp3')
                    message_list.append(message)
        sleep(1)
    return None

ru_thread = threading.Thread(target=ru_voice)
en_thread = threading.Thread(target=en_voice)
uk_thread = threading.Thread(target=uk_voice)
pl_thread = threading.Thread(target=pl_voice)
ja_thread = threading.Thread(target=ja_voice)



def ru_button():
    global toggle
    global ru_loop
    global en_loop
    global uk_loop
    global pl_loop
    global ja_loop
    if en_loop or uk_loop or pl_loop or ja_loop:
        en_loop = False
        uk_loop = False
        pl_loop = False
        ja_loop = False
        ru_loop = True
        if not ru_thread.is_alive():
            return ru_thread.start()
        else:
            return None
    elif not toggle:
        toggle = True
        ru_loop = True
        return ru_thread.start()
    elif ru_loop:
        return None
    
def en_button():
    global toggle
    global ru_loop
    global en_loop
    global uk_loop
    global pl_loop
    global ja_loop
    if ru_loop or uk_loop or pl_loop or ja_loop:
        ru_loop = False
        uk_loop = False
        pl_loop = False
        ja_loop = False
        en_loop = True
        if not en_thread.is_alive():
            return en_thread.start()
        else:
            return None
    elif not toggle:
        toggle = True
        en_loop = True
        return en_thread.start()
    elif en_loop:
        return None

def uk_button():
    global toggle
    global ru_loop
    global en_loop
    global uk_loop
    global pl_loop
    global ja_loop
    if ru_loop or en_loop or pl_loop or ja_loop:
        ru_loop = False
        en_loop = False
        pl_loop = False
        ja_loop = False
        uk_loop = True
        if not uk_thread.is_alive():
            return uk_thread.start()
        else:
            return None
    elif not toggle:
        toggle = True
        uk_loop = True
        return uk_thread.start()
    elif uk_loop:
        return None

def pl_button():
    global toggle
    global ru_loop
    global en_loop
    global uk_loop
    global pl_loop
    global ja_loop
    if ru_loop or en_loop or uk_loop or ja_loop:
        ru_loop = False
        en_loop = False
        uk_loop = False
        ja_loop = False
        pl_loop = True
        if not pl_thread.is_alive():
            return pl_thread.start()
        else:
            return None
    elif not toggle:
        toggle = True
        pl_loop = True
        return pl_thread.start()
    elif pl_loop:
        return None

def ja_button():
    global toggle
    global ru_loop
    global en_loop
    global uk_loop
    global pl_loop
    global ja_loop
    if ru_loop or en_loop or uk_loop or pl_loop:
        ru_loop = False
        en_loop = False
        uk_loop = False
        pl_loop = False
        ja_loop = True
        if not ja_thread.is_alive():
            return ja_thread.start()
        else:
            return None
    elif not toggle:
        toggle = True
        ja_loop = True
        return ja_thread.start()
    elif ja_loop:
        return None

def exit_button(icon):
    global toggle
    global ru_loop
    global en_loop
    global uk_loop
    global pl_loop
    global ja_loop
    toggle = False
    ru_loop = False
    en_loop = False
    uk_loop = False
    pl_loop = False
    ja_loop = False
    driver.quit()
    return icon.stop()




def run_icon():
    image = PIL.Image.open("bogdan.png")
    icon = pystray.Icon("ITStart", image, menu=pystray.Menu(
        pystray.MenuItem("ru", ru_button),
        pystray.MenuItem("en", en_button),
        pystray.MenuItem("uk", uk_button),
        pystray.MenuItem("pl", pl_button),
        pystray.MenuItem("ja", ja_button),
        pystray.MenuItem("exit", exit_button),
    ))
    return icon.run()





main_thread = threading.Thread(target=run_icon)
main_thread.start()
