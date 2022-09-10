import requests
import threading
import random
import os

from colorama import Fore, init

init(convert=True)


def check():

    os.system(f"title https://github.com/realCosmicHub")
    usersf = open("users.txt")
    user = random.choice(usersf.read().splitlines())
    usersf.close()

    r = requests.get(f'https://www.twitch.tv/{user}')
    if r.status_code == 200:
        print(Fore.RED + f"Taken | {Fore.RESET}{user}\n")
    else:
        print(Fore.GREEN + f"Available {Fore.RESET}| {user}\n")
        t = open('valid.txt', 'a')
        t.write(f'{user}\n')



def start():

    os.system(f"title https://github.com/realCosmicHub")
    r = input("Amount of users to check: ")
    for i in range(int(r)):
        x = threading.Thread(target=check)
        x.start()

start()