import os

### TODO:
### Zapis ostatniej sesji (chodzi o menu)

### Import bibliotek

import urllib.request
import datetime
import sys
import time
import asyncio
import random
import threading
import multiprocessing
from progressbar import *
import json
import pyautogui
import psutil
import rich.table
import rich
from configparser import ConfigParser
import ctypes
#from tqdm import tqdm
#from joblib import Parallel, delayed
import math
import shutil
import subprocess
from colorama import Fore, Back, Style, init
import string
from getpass import getpass
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QMainWindow
from seleniumwire import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

init(autoreset=True)


# Convert to EXE
# TODO: pyarmor pack -e " --onefile --icon ext/#instagram.ico" main.py
# TODO: pyinstaller --onefile --icon ext/#instagram.ico main.py



### TODO: Download Seleniumwire Cert-------------------
### XXX GITPYTHON MODULE


if os.path.exists(f"{os.path.join(os.getenv('temp'), '.seleniumwire')}") == True:
    pass
else:
    if os.path.exists(os.path.join(os.getcwd(), "missing-files-instagen-exe")):
        try:
            os.rename(os.path.join(os.getcwd(), "missing-files-instagen-exe"), ".seleniumwire")   
        except:
            print(Fore.RED + "[ UNABLE TO RENAME ] Unable to rename directory! Please close any opened editors in this folder [ like visual studio / pycharm ]")
        try:
            shutil.move(os.path.join(os.getcwd(), ".seleniumwire"), fr"{os.getenv('temp')}")
        except:
            print(Fore.RED + "Unable to move file to %temp%")
            time.sleep(999)
            sys.exit()
    else:
        ctypes.windll.kernel32.SetConsoleTitleW(f'''WieszakWare InstaGen | Download''')
        print(Style.BRIGHT + fr"""

                        ▓█████▄  ▒█████   █     █░███▄    █  ██▓     ▒█████   ▄▄▄      ▓█████▄ 
                        ▒██▀ ██▌▒██▒  ██▒▓█░ █ ░█░██ ▀█   █ ▓██▒    ▒██▒  ██▒▒████▄    ▒██▀ ██▌
                        ░██   █▌▒██░  ██▒▒█░ █ ░█▓██  ▀█ ██▒▒██░    ▒██░  ██▒▒██  ▀█▄  ░██   █▌
                        ░▓█▄   ▌▒██   ██░░█░ █ ░█▓██▒  ▐▌██▒▒██░    ▒██   ██░░██▄▄▄▄██ ░▓█▄   ▌
                        ░▒████▓ ░ ████▓▒░░░██▒██▓▒██░   ▓██░░██████▒░ ████▓▒░ ▓█   ▓██▒░▒████▓ 
                        ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒ ░ ▒░   ▒ ▒ ░ ▒░▓  ░░ ▒░▒░▒░  ▒▒   ▓▒█░ ▒▒▓  ▒ 
                        ░ ▒  ▒   ░ ▒ ▒░   ▒ ░ ░ ░ ░░   ░ ▒░░ ░ ▒  ░  ░ ▒ ▒░   ▒   ▒▒ ░ ░ ▒  ▒ 
                        ░ ░  ░ ░ ░ ░ ▒    ░   ░    ░   ░ ░   ░ ░   ░ ░ ░ ▒    ░   ▒    ░ ░  ░ 
                        ░        ░ ░      ░            ░     ░  ░    ░ ░        ░  ░   ░    
                        ░                                                              ░           
""")
        print(Fore.LIGHTCYAN_EX + f"[ SETUPWARNING.EXE ] WIESZAKWARE SETUP STARTED | WELCOME {os.getlogin()}")
        actiondownloadgit = input("[ INPUT ] Is git-scm installed on your computer? [ TYPE 'No' FOR AUTO DOWNLOAD or type 'Yes' if you have git installed on your pc ] :>").capitalize()
        if actiondownloadgit == "No":
            print(Fore.LIGHTBLACK_EX + "[ LOG ] Installing git for Windows")
            try:
                print(Fore.LIGHTBLACK_EX + "[ LOG ] Stutus: Downloading file")
                response = urllib.request.urlopen(url="https://github.com/git-for-windows/git/releases/download/v2.37.3.windows.1/Git-2.37.3-64-bit.exe", timeout=80)
                time.sleep(2)
                with open("downloaded_git.exe", "wb+") as writegit:
                    try:
                        writegit.write(response.read())
                        print(Fore.GREEN + "[ GIT ] Git Downloaded please install git!")
                    except Exception as e:
                        print(Fore.RED + "[ ERROR ] Unable to write git | Exception: {}".format(e))
                    writegit.close()
                print(Fore.LIGHTBLACK_EX + "[ LOG ] Stutus: File Downloaded Successfully!")
                print("[ GIT ] Version: 2.37.3")
                #response.read().decode(response.headers.get_content_charset())
            except:
                print(Fore.RED + "[ ERROR ] Unable to download file! | Check internet connection.")
            print("[ LOG ] Waiting for download!")
            time.sleep(3)
            print("[ LOG ] Successfull!")
            print(Fore.BLUE + "[ INFO ] Attemting to get cursor position")
            print(Fore.LIGHTMAGENTA_EX + "[ CURSOR ] Position [ {} ]".format(pyautogui.position()))
            try:
                os.startfile(os.path.join(os.getcwd(), "downloaded_git.exe"))
                print(Fore.GREEN + "[ SYSTEM ] GIT SETUP STARTED")
            except Exception as e:
                print(Fore.RED + f"Unable to start git setup | Exception found: [ {e} ]")
            print(Fore.LIGHTRED_EX + "[ system32/system/win.exe ] GRANT ADMINISTRATOR PERMISSIONS TO GIT.EXE | JUST CLICK YES")
            print(Fore.YELLOW + "[ WARNING ] Install git and RELAUNCH wieszakware!")
            print(Fore.LIGHTYELLOW_EX + "[ RELAUNCH ] RELAUNCH")
            time.sleep(999)
            sys.exit()
            
            #onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
            #selectfile = input("Select GIT file to install git!")
 
        else:

            print(Fore.LIGHTCYAN_EX + "[ ACTION / DOWNLOAD ] DOWNLOADING REPOSITORY! MAKE SURE YOU GAVE GIT INSTALLED!")
            try:
                dotseleniumwire = subprocess.call('git clone https://github.com/WieszakWare/missing-files-instagen-exe', shell=True)
            except:
                print(Fore.RED + "Please install git from: [ https://git-scm.com/download/ ]")
            
            print(Fore.RED  + "[ RELAUNCH ] Relaunch program")
            time.sleep(10000)
            pass













############################################################################################################################

### Informacje
__info__ = {
    "appname": "InstaGen",
    "version": "Release 1.0.7",
    "logspath": os.path.join(os.getcwd(), "logs", "logs.log"),
    ".ui-file-path": os.path.join(os.getcwd(), "ui", "ui_main.ui"),
    "input-path": lambda filename: os.path.join("input", f"{filename}"),
    "property_0": "#FUTURE24",
    "property_1": "W^Z8gM60oMZ0*UgxY!mzqhtHc#TSFaWojlm8Wru^X3axY7gLr3",
    "property_2": "v8g@tf11CKO12EHZgQhL3gG7#c5O7bf*28Z8BKN1",
    "property_3": "8364-8263-1823-9172-1735",
    "property_4": "1103-0002-7772-0000-1728",
    "special-password": "wieszakware-future24"
}

ctypes.windll.kernel32.SetConsoleTitleW(f"{__info__['appname']} | {__info__['version']}")

############################################################################################################################


# TODO: ConfigParser - 2 plik configowy - GUI
conf = json.load(open("config.json"))

parser = ConfigParser()
parser.read('settings.config')

#print(bool(parser.get('Settings', 'use_proxy')))



def checkproperties():
    # Sprawdzenie czy wszystko działa
    counter = 0
    valid = 0
    invalid = 0
    for x in range(5):
        if conf["x-super-properties"][x] == __info__[f"property_{x}"]:
            counter += 1
            valid += 1
        else:
            counter += 1
            invalid += 1
    if valid == 5:
        print(Style.BRIGHT + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ] " + Fore.GREEN + F'[ ACCEPTED ] All properties valid! ( Valid properties: [ {valid} ] ) ( Invalid properties: [ {invalid} ] ) ( All:  {counter})')
    else:
        ### Hasło nieprawidłowe
        print(Style.BRIGHT + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ] " + Fore.RED + F'[ NOT ACCEPTED PASSWORD REQUIRED ] Enter Special Password! ( Valid properties: [ {valid} ] ) ( Invalid properties: [ {invalid} ] ) ( All:  {counter})')
        specialpassword = getpass(">>>")
        max_retries = 0
        used_retries = 0
        if specialpassword ==  __info__["special-password"]:
            print(Style.BRIGHT + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ] " + Fore.GREEN + F'[ PASSWORD ACCEPTED ] Valid Password')
            return True
        else:
            print(Style.BRIGHT + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ] " + Fore.RED + F'[ PASSWORD NOT ACCEPTED ] Invalid Password')
            return False
            
            





############################################################################################################################



class Print():

    def __init__(self):
        super(Print, self).__init__()
        self.Time = Style.BRIGHT
        self.Warning = Fore.YELLOW
        self.Error = Fore.LIGHTRED_EX
        self.Critical = Fore.RED
        self.Debug = Fore.LIGHTMAGENTA_EX
        self.Info = Fore.LIGHTBLUE_EX
        self.Ok = Fore.GREEN
        self.Success = Fore.LIGHTGREEN_EX
        self.HARDWAREINFO = Fore.LIGHTBLACK_EX
        self.RESET = Style.RESET_ALL
        
        self.AllowDebug = True

    def info(self, text: str = None, end: str = None) -> None:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ INFO ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Info + "[ INFO ] >" + " " + f"{text}", end=end)


    def warning(self, text: str = None, end: str = None) -> None:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ WARNING ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Warning + "[ WARNING ] >" + " " + f"{text}", end=end)


    def debug(self, text: str = None, end: str = None, allowdebug: bool = True) -> None:
        if allowdebug == False:
            return
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ DEBUG ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Debug + "[ DEBUG ] >" + " " + f"{text}", end=end)


    def critical(self, text: str = None, end: str = None) -> None:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ CRITICAL ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Critical + "[ CRITICAL ] >" + " " + f"{text}", end=end)


    def error(self, text: str = None, end: str = None) -> None:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ CRITICAL ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Error + "[ ERROR ] >" + " " + f"{text}", end=end)


    def ok(self, text: str = None, end: str = None) -> None:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ OK ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Ok + "[ OK ] >" + " " + f"{text}", end=end)

    
    def success(self, text: str = None, end: str = None) -> None:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ SUCCESS ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Success + "[ SUCCESS ] >" + " " + f"{text}", end=end)

    def hardwareinfo(self, text: str = None, end: str = None) -> None:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ HWINFO ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.HARDWAREINFO + "[ HWINFO ] >" + " " + f"{text}", end=end)


p = Print()




###########################################################################################################
###########################################################################################################


class Features():
    def __init__(self):
        super(Features, self).__init__()
        self.none = None
        
    ### XXX Stwórz konto instagram - Phone 
    async def CREATOR_PHONE(self, Account_Number: int, Phone_Number: str, Name: str, Username: str, Password: str, Proxy: str, use_proxy: bool = False):
        p.debug("Attemting to find chrome binaries...")
        global binaries
        try:
            p.ok("Binaries Located")
            if os.path.exists(os.getcwd(), ".chromebinaries", "chrome.exe"):
                p.ok("Binaries Located [ .chromebinaries ]")
                binaries = os.path.join(os.getcwd(), ".chromebinaries", "chrome.exe")
            else:
                p.error("Unable to locate .chromebinaries folder.")
                p.ok("Searching for google chrome installed on your computer")
                p.success("Google Chrome Found")
                binaries = None
        except:
            p.critical("Unexpected Error | Please contact support")

        CHROMEDRIVER = os.path.join(os.getcwd(), "Drivers", "chromedriver.exe")

        p.warning("This generator requires high quality proxies!")

        if use_proxy == False:
            options = {
                ### Proxy
                'proxy': {
                    'no_proxy': 'localhost,127.0.0.1'
                }  
            }
        elif use_proxy == True:
            oneproxy_service = Proxy.replace("\n", "")
            options = {
                'proxy': {
                    'http': f'{parser.get("Settings", "proxytype")}://{oneproxy_service}',
                    'https': f'{parser.get("Settings", "proxytype")}://{oneproxy_service}',
                }  
            }
            p.debug(options)

        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('excludeSwitches', ['enable-logging'])
        #opt.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.3.6')
        #opt.add_argument("--start-minimized")
        opt.add_argument('--no-sandbox')
        opt.add_argument("--ignore-certificate-errors")
        opt.add_argument("--incognito")
        opt.add_argument("--silent") # TODO: --silient -> --silent
        # opt.add_argument("--headless")
        try:
            p.ok("Binaries Located")
            if binaries == None:
                pass
            else:
                opt.binary_location = binaries
        except:
            p.error("Unable to locate .chromebinaries folder.")
            p.ok("Searching for google chrome installed on your computer")
           
            
            
        driver = webdriver.Chrome(CHROMEDRIVER, options=opt, seleniumwire_options=options)

        p.debug("Attempting to start webdriver")

        try:
            driver.get("http://instagram.com")
            p.success(f"Webdriver Started with proxy [ {Proxy} ]")
        except Exception as e:
            p.critical(f"Unable to start webdriver, please contact on Discord [ {e} ]")

        agent = driver.execute_script("return navigator.userAgent")
        p.debug(f"Current user agent: [ {agent} ]")

        p.debug("Attempting to confirm cookies")
        
        try:
            #Confirm Cookies
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.RnEpo.Yx5HN._4Yzd2 > div > div > button.aOOlW.HoLwm"))).click()
            p.ok(f"Cookies confirmed [ Cookies list: ( {driver.get_cookies()} ) ]")
        except Exception as e:
            p.critical(f"Unable to confirm cookies. | Cookies already confirmed.")

        p.debug("Attempting to redirect to signup page")

        await asyncio.sleep(2.2)

        while True:
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-root > section > main > article > div.rgFsT > div:nth-child(2) > div > p > a > span"))).click()
                await asyncio.sleep(2)
                if driver.current_url == "https://www.instagram.com/accounts.signup":
                    p.success(F"Successfully redirected to signup page [{driver.current_url}]")
                break
            except Exception as e:
                try:
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-root > section > main > div > div > div:nth-child(2) > div > p > a"))).click()
                    await asyncio.sleep(2)
                    if driver.current_url == "https://www.instagram.com/accounts.signup":
                        p.success(F"Successfully redirected to signup page [{driver.current_url}]")
                    break
                except Exception as e2:
                    p.critical(f"Unable to redirect to signup page")
                    await asyncio.sleep(2)

        await asyncio.sleep(2.2)

        #time.sleep(6)
        try:
            ### Uzupełnianie inputów

            p.debug(f"Attempting to register on {driver.current_url}")
            #p.info(f"Current Window Handle: [ {driver.current_window_handle} ]")
            #Register
            #phone
            p.info("Attempting to insert Phone Number/Name/Username/Password")
            
            try:
                driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[3]/div/label/input").send_keys(Phone_Number)
                p.success("Phone Number inserted successfully")
            except Exception as e:
                p.error(f"Unable to insert phone number")
            try:
                driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[4]/div/label/input").send_keys(Name)
                p.success("Name inserted successfully")
            except Exception as e:
                p.error(f"Unable to insert name")
            try:
                driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[5]/div/label/input").send_keys(Username)
                p.success("Username inserted successfully")
            except Exception as e:
                p.error(f"Unable to insert username")
            try:
                driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[6]/div/label/input").send_keys(Password)
            except Exception as e:
                p.error(f"Unable to insert password")

            p.info("Attempting to click signup button")
            
            while True:
                try:
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-root > section > main > div > div > div:nth-child(1) > div.P8adC > form > div:nth-child(9) > div > button"))).click()
                    p.ok("Sign-up button clicked")
                    break
                except Exception as e:
                    try:
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[7]/div/button"))).click()
                        p.ok("Sign-up button clicked")
                        break
                    except:
                        p.critical(f"Unable to register on {driver.current_url}")
                        #p.error("Unable to click sign-up button")
                        
        except Exception as e:
            p.critical(f"Unable to register on {driver.current_url}")

        await asyncio.sleep(4)
        
        #Birthday verification

        if(driver.current_url ==  "https://www.instagram.com/accounts/emailsignup/"):
            #p.critical("Unexpected error ocurred")
            if(Proxy != None):
                p.critical(f"1. Instagram doesn't allow proxy ({Proxy}) to proceed with register.")
            else:
                #p.critical(f"We don't know how to fix it.")
                pass
            if not(p.AllowDebug):
                driver.quit()
                exit()
        
        ### Urodziny
        try:
            # Month
            driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select").click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[{random.randrange(1, 12)}]"))).click()

            # Day
            driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select").click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[{random.randrange(1, 30)}]"))).click()

            # Year
            driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select").click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[27]"))).click()

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[6]/button"))).click()
        except Exception as e:
            p.critical("Unexpected error ocurred")
            p.critical("Possible problems and fixes:")
            p.critical("1. Phone is used to frequently and couldn't proceed")
            p.critical("2. Instagram Generator generated used username, you should restart app")
            p.critical("3. You used proxy where Instagram is acting weird")
            p.debug(e)
            if not(p.AllowDebug):
                driver.quit()
                exit()



        #XPATH CONFIRMATION CODE - /html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/input
        p.info(f"Enter Confirmation code sent to [ {Phone_Number} ]")

        #confirmationcode = input("Confirmation Code :> ")
        #while confirmationcode == None:
        #    await asyncio.sleep(1)
        #    pass
        p.info("Please enter your confirmation code")
        await asyncio.sleep(5)
        p.debug("Came to loop")
        try:
            while driver.find_element(By.CSS_SELECTOR, "#react-root > section > main > div > div > div:nth-child(1) > div > div > div > form > div.TfHme > div > label > input").is_displayed():
                p.debug("Not passed, trying again")
                await asyncio.sleep(2)
        except:
            pass
        p.debug("Exited loop")
        # Zapis konta

        jsonaccount = {
            "Phone Number:": f"{Phone_Number}",
            "Name:": f"{Name}",
            "Username:": f"{Username}",
            "Password:": f"{Password}"
        }


        with open(os.path.join(os.getcwd(), "created", "accounts.json"), "a", encoding="utf-8") as savedata:
            json.dump(jsonaccount, savedata, indent=4)
            savedata.write("\n")
            savedata.close()
        await asyncio.sleep(3)
        try:
            p.debug("Attempting to accept cookies...")
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div[3]/div/div[1]/div/div[2]/div[1]/span"))).click()
            p.info("Selected cookies (minimal)")
            p.ok(f"[ Cookies list: ( {driver.get_cookies()} ) ]")
        except Exception as e:
            p.debug(e, allowdebug=False)
            p.info("Cookies already selected")
        try:
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys("wieszakyt")
        except:
            p.error("Unable to search")
        await asyncio.sleep(1)
        driver.quit()
    
        #else:
        #    p.info("Attempting to insert confirmation code.")
        #
        #    p.debug(f"Inserting [ {confirmationcode} ]")
        #
        #    try:
        #        driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/div/div/form/div[1]/div/label/input").send_keys(confirmationcode)
        #    except:
        #        p.critical("Unable to insert confirmation code")
        #
        #    driver.close()

        #driver.find_element(By.CSS_SELECTOR, "#react-root > section > main > div > div > div:nth-child(1) > div.P8adC > form > div:nth-child(4) > div > label > input").send_keys("Phone number")
        #driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[4]/div/label/input").send_keys("Name")
        #driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[5]/div/label/input").send_keys("Username")
        #driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[6]/div/label/input").send_keys("Password")

        












    async def CREATOR_EMAIL(self, Email_Address: str, Name: str, Username: str, Password: str, Proxy: str, use_proxy: bool = False):
        p.debug("Attemting to find chrome binaries...")
        global binaries
        try:
            p.ok("Binaries Located")
            if os.path.exists(os.getcwd(), ".chromebinaries", "chrome.exe"):
                p.ok("Binaries Located [ .chromebinaries ]")
                binaries = os.path.join(os.getcwd(), ".chromebinaries", "chrome.exe")
            else:
                p.error("Unable to locate .chromebinaries folder.")
                p.ok("Searching for google chrome installed on your computer")
                p.success("Google Chrome Found")
                binaries = None
        except:
            p.critical("Unexpected Error | Please contact support")

        CHROMEDRIVER = os.path.join(os.getcwd(), "Drivers", "chromedriver.exe")

        p.warning("This generator requires high quality proxies!")

        if use_proxy == False:
            options = {
                ### Proxy
                'proxy': {
                    'no_proxy': 'localhost,127.0.0.1'
                }  
            }
        elif use_proxy == True:
            oneproxy_service = Proxy.replace("\n", "")
            options = {
                'proxy': {
                    'http': f'{parser.get("Settings", "proxytype")}://{oneproxy_service}',
                    'https': f'{parser.get("Settings", "proxytype")}://{oneproxy_service}',
                }  
            }
            p.debug(options)

        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('excludeSwitches', ['enable-logging'])
        #opt.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.3.6')
        #opt.add_argument("--start-minimized")
        opt.add_argument('--no-sandbox')
        opt.add_argument("--ignore-certificate-errors")
        opt.add_argument("--incognito")
        opt.add_argument("--silent") # TODO: --silient -> --silent
        # opt.add_argument("--headless")
        try:
            p.ok("Binaries Located")
            if binaries == None:
                pass
            else:
                opt.binary_location = binaries
        except:
            p.error("Unable to locate .chromebinaries folder.")
            p.ok("Searching for google chrome installed on your computer")
           
            
            
        driver = webdriver.Chrome(CHROMEDRIVER, options=opt, seleniumwire_options=options)

        p.debug("Attempting to start webdriver")

        try:
            driver.get("http://instagram.com")
            p.success(f"Webdriver Started with proxy [ {Proxy} ]")
        except Exception as e:
            p.critical(f"Unable to start webdriver, please contact on Discord [ {e} ]")

        agent = driver.execute_script("return navigator.userAgent")
        p.debug(f"Current user agent: [ {agent} ]")

        p.debug("Attempting to confirm cookies")
        
        try:
            #Confirm Cookies
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.RnEpo.Yx5HN._4Yzd2 > div > div > button.aOOlW.HoLwm"))).click()
            p.ok(f"Cookies confirmed [ Cookies list: ( {driver.get_cookies()} ) ]")
        except Exception as e:
            p.critical(f"Unable to confirm cookies. | Cookies already confirmed.")

        p.debug("Attempting to redirect to signup page")

        await asyncio.sleep(2.2)

        while True:
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-root > section > main > article > div.rgFsT > div:nth-child(2) > div > p > a > span"))).click()
                await asyncio.sleep(2)
                if driver.current_url == "https://www.instagram.com/accounts.signup":
                    p.success(F"Successfully redirected to signup page [{driver.current_url}]")
                break
            except Exception as e:
                try:
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-root > section > main > div > div > div:nth-child(2) > div > p > a"))).click()
                    await asyncio.sleep(2)
                    if driver.current_url == "https://www.instagram.com/accounts.signup":
                        p.success(F"Successfully redirected to signup page [{driver.current_url}]")
                    break
                except Exception as e2:
                    p.critical(f"Unable to redirect to signup page")
                    await asyncio.sleep(2)

        await asyncio.sleep(2.2)

        #time.sleep(6)
        try:
            ### Uzupełnianie inputów

            p.debug(f"Attempting to register on {driver.current_url}")
            #p.info(f"Current Window Handle: [ {driver.current_window_handle} ]")
            #Register
            #phone
            p.info("Attempting to insert Email/Name/Username/Password")
            
            try:
                driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[3]/div/label/input").send_keys(Email_Address)
                p.success("Email Adrress inserted successfully")
            except Exception as e:
                p.error(f"Unable to insert Email Adrress")
            try:
                driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[4]/div/label/input").send_keys(Name)
                p.success("Name inserted successfully")
            except Exception as e:
                p.error(f"Unable to insert name")
            try:
                driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[5]/div/label/input").send_keys(Username)
                p.success("Username inserted successfully")
            except Exception as e:
                p.error(f"Unable to insert username")
            try:
                driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[6]/div/label/input").send_keys(Password)
            except Exception as e:
                p.error(f"Unable to insert password")

            p.info("Attempting to click signup button")
            
            while True:
                try:
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-root > section > main > div > div > div:nth-child(1) > div.P8adC > form > div:nth-child(9) > div > button"))).click()
                    p.ok("Sign-up button clicked")
                    break
                except Exception as e:
                    try:
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[7]/div/button"))).click()
                        p.ok("Sign-up button clicked")
                        break
                    except:
                        p.critical(f"Unable to register on {driver.current_url}")
                        #p.error("Unable to click sign-up button")
                        
        except Exception as e:
            p.critical(f"Unable to register on {driver.current_url}")

        await asyncio.sleep(4)
        
        #Birthday verification

        if(driver.current_url ==  "https://www.instagram.com/accounts/emailsignup/"):
            p.critical("Unexpected error ocurred")
            if(Proxy != None):
                p.critical(f"1. Instagram doesn't allow proxy ({Proxy}) to proceed with register.")
            else:
                p.critical(f"We don't know how to fix it.")
            if not(p.AllowDebug):
                driver.quit()
                exit()
        
        ### Urodziny
        try:
            # Month
            driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select").click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[{random.randrange(1, 12)}]"))).click()

            # Day
            driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select").click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[{random.randrange(1, 30)}]"))).click()

            # Year
            driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select").click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[27]"))).click()

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[6]/button"))).click()
        except Exception as e:
            p.critical("Unexpected error ocurred")
            p.critical("Possible problems and fixes:")
            p.critical("1. Email is used to frequently and couldn't proceed")
            p.critical("2. Instagram Generator generated used username, you should restart app")
            p.critical("3. You used proxy where Instagram is acting weird")
            p.debug(e)
            if not(p.AllowDebug):
                driver.quit()
                exit()



        #XPATH CONFIRMATION CODE - /html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/input
        p.info(f"Enter Confirmation code sent to your email address: [ {Email_Address} ]")

        #confirmationcode = input("Confirmation Code :> ")
        #while confirmationcode == None:
        #    await asyncio.sleep(1)
        #    pass
        p.info("Please enter your confirmation code")

        await asyncio.sleep(5)

        p.debug("Waiting for confirmation code.")

        try:
            while driver.find_element(By.CSS_SELECTOR, "#react-root > section > main > div > div > div:nth-child(1) > div.qF0y9.Igw0E.IwRSH.eGOV_.acqo5._4EzTm > form > div > div:nth-child(1) > input").is_displayed():
                p.debug("Not passed, trying again", end="\r", allowdebug=True)
                await asyncio.sleep(2)
            else:
                p.success("Code Received!")
        except:
            pass
        p.debug("Exited loop")
        # Zapis konta

        jsonaccount = {
            "Email Address:": f"{Email_Address}",
            "Name:": f"{Name}",
            "Username:": f"{Username}",
            "Password:": f"{Password}"
        }

        

        with open(os.path.join(os.getcwd(), "created", "accounts.json"), "a", encoding="utf-8") as savedata:
            json.dump(jsonaccount, savedata, indent=4)
            savedata.write("\n")
            savedata.close()
        await asyncio.sleep(3)
        try:
            p.debug("Attempting to accept cookies...")
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div[3]/div/div[1]/div/div[2]/div[1]/span"))).click()
            p.info("Selected cookies (minimal)")
            p.ok(f"[ Cookies list: ( {driver.get_cookies()} ) ]")
        except Exception as e:
            p.debug(e)
            p.info("Cookies already selected")
        try:
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys("wieszakyt")
        except:
            p.error("Unable to search")
        await asyncio.sleep(1)
        driver.quit()












##################################################################################################################################################################################################


class APP(QMainWindow):
     def __init__(self):
        super(APP, self).__init__()
        loadUi(__info__[".ui-file-path"], self)

        self.show()

        self.setWindowTitle(f'{__info__["appname"]} | {__info__["version"]}')

        self.setWindowIcon(QtGui.QIcon('ext/#instagram.png'))

##################################################################################################################################################################################################

        # NOTE: Widżety

        self.stackedWidget.setCurrentWidget(self.page_accgen_phone)



        self.btn_accgen_phone.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_accgen_phone))

        self.btn_accgen_email.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_accgen_email))


        self.btn_likebot.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_likebot))

        self.btn_followbot.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_followbot))

        self.btn_settings.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_settings))


##################################################################################################################################################################################################
# TODO Cooming soon! Button Icons insead of labels.
# self.printButton.setIcon(QtGui.QIcon('printer.tif'))







##################################################################################################################################################################################################
# NOTE Auto Check Use Proxy ACCGEN - PHONE, Settings

        
        
                
        
      


        def checkboxrefresh(self):
            try:
                checkboxstate = parser.getboolean('Settings', 'use_proxy')
                p.ok(f"Default checkbox value: [ settings.config ], [ {bool(checkboxstate)} ] ")
                self.checkuseproxy.setChecked(bool(checkboxstate))
                self.sett_checkbtn_getproxystatus.setChecked(bool(checkboxstate))
                self.accgenemail_checkbox_proxy.setChecked(bool(checkboxstate))
                self.sett_textedit_proxytype.setPlainText(parser.get("Settings", "proxytype"))
                return bool(checkboxstate)
            except Exception as e:
                p.error(f"Unable to get checkbox state. Please check settings.config file and try again. | {e}")


        def settingsupdate(self):
            p.debug("Updating Settings")
            p.debug("Refreshing checkbox")
            parser.set("Settings", "use_proxy", "yes") if self.sett_checkbtn_getproxystatus.isChecked() == True else parser.set("Settings", "use_proxy", "no")
            p.debug("Attemting to get proxytype")
            if self.sett_textedit_proxytype.toPlainText() == "":
                p.error("ProxyType field is empty")
            if self.sett_textedit_proxytype.toPlainText() == "http":
                p.ok("Proxy type [ http ] accepted")
                parser.set("Settings", "proxytype", "http")
            elif self.sett_textedit_proxytype.toPlainText() == "socks4":
                p.ok("Proxy type [ socks4 ] accepted")
                parser.set("Settings", "proxytype", "socks4")
            elif self.sett_textedit_proxytype.toPlainText() == "socks5":
                p.ok("Proxy type [ socks5 ] accepted")
                parser.set("Settings", "proxytype", "socks5")
            else:
                p.warning("This proxytype is not allowed!")
            with open('settings.config', 'w+') as configfile:
                parser.write(configfile)
            try:
                p.success(f"Checkbox refreshed successfully!")
                checkboxrefresh(self)
            except Exception as e:
                p.error(f"Unable to refresh checkbox! | Exception Found: [ {e} ]")

            
            
            try:
                pass
                #self.sett_textedit_proxytype
            except:
                pass

            
            

        self.sett_btn_updatesettings.clicked.connect(lambda: settingsupdate(self))
        
      

##################################################################################################################################################################################################
# NOTE: Automaticly refresh checkboxes
        checkboxrefresh(self)
##################################################################################################################################################################################################

        # NOTE Functions to accgen email / phone

        def getall_email(self):
            _useproxy = True if self.checkuseproxy.isChecked() == True else False
            _email = set()
            _name = set()
            _username = set()
            _password = set()
            global accepted_actions
            accepted_actions = 0
            

            def loadproxy():
                global accepted_actions
                proxylist = set()
                proxyfilesize = os.path.getsize(__info__["input-path"]("proxies.txt"))
                if _useproxy == True:
                    if proxyfilesize != 0:
                        with open(__info__["input-path"]("proxies.txt")) as getproxy:
                            for line in getproxy:
                                proxylist.add(line)
                        p.ok(f'{__info__["input-path"]("proxies.txt")}')
                        accepted_actions += 1
                        return str(random.choice(list(proxylist)))
                    else:
                        p.critical(f'Proxy list is empty! | Please insert proxies in {__info__["input-path"]("proxies.txt")}')
                else:
                    p.warning("Use Proxies turned off")
                    accepted_actions += 1
                    return None
                        

                                
                

            _proxy = loadproxy()

            def checkEmail(email: str, warn, warn2):
                if email == "":
                    p.warning(warn)
                    return False

                if email.__contains__("@") == False:
                    p.warning(warn2)
                    return False


                else:
                    return True


            def getemail():
                global accepted_actions
                email = str(self.accgenemail_textedit_email.toPlainText())
                
                if(checkEmail(email, "Email Address is required", "Email Address must contains [ @ ]") == True):
                    p.success("Email Address Accepted")
                    accepted_actions += 1
                    _email.add(email)
                    return True
            





            def getpassword():
                global accepted_actions
                accpassword = str(self.accgenemail_textedit_password.toPlainText())
                if accpassword == "":
                    p.debug(f'Getting password from {__info__["input-path"]("passwords.txt")}')
                    passfilesize = os.path.getsize(__info__["input-path"]("passwords.txt"))
                    if passfilesize == 0:
                        p.warning(f'GetPassword returned anerror : [ {__info__["input-path"]("passwords.txt")} file is empty ]')
                        p.info("Generating password...")
                        un = ""
                        for x in range(48):
                            un = un + random.choice(string.ascii_letters + string.digits)
                        _password.add(un)
                        p.success(f"Password Generated: [ {un} ]")
                        accepted_actions += 1
                        # TODO: Generowanie haseł
                    else:
                        with open(__info__["input-path"]("passwords.txt")) as inputpassword:
                            templist_1 = set()
                            for line in inputpassword:
                                templist_1.add(line.replace("\n", ""))
                            _password.add(random.choice(list(templist_1)))
                            accepted_actions += 1
                            p.success("Password Choosen Successfully")      
                elif len(accpassword) <= 4:
                    p.error("Password length must be more than 4")
                elif len(accpassword) <= 50:
                    accepted_actions += 1
                    p.success("Password Accepted")
                    _password.add(accpassword)
                    
                else:
                    p.warning("Something went wrong with checking your password. | Please contact support.")



            def getusername():
                global accepted_actions
                accusername = str(self.accgenemail_textedit_username.toPlainText())
                if accusername == "":
                    p.debug(f'Getting username from {__info__["input-path"]("usernames.txt")}')
                    usernamesfilesize = os.path.getsize(__info__["input-path"]("usernames.txt"))
                    if usernamesfilesize == 0:
                        p.warning(f'GetUsername returned an error: [ {__info__["input-path"]("usernames.txt")} file is empty ]')
                        p.info("Generating username...")
                        un = ""
                        for x in range(24):
                            un = un + random.choice(string.ascii_letters + string.digits)
                        _username.add(un)
                        p.success(f"Username Generated: [ {un} ]")
                        accepted_actions += 1
                    else:
                        with open(__info__["input-path"]("usernames.txt"), "r") as inputusername:
                            templist_2 = set()
                            for line in inputusername:
                                templist_2.add(line.replace("\n", ""))
                            _username.add(random.choice(list(templist_2)))
                            accepted_actions += 1
                            with open(__info__["input-path"]("usernames.txt"), "w") as writeun:
                                writeun.write("")
                            with open(__info__["input-path"]("usernames.txt"), "a") as appendun:
                                for x in inputusername.readlines():
                                    if not(x.startswith(_username[0])):
                                        appendun.write(x)
                            # TODO: Usunięcie nicku z listy po użyciu.
                            p.success("Username Choosen Successfully & Deleted From List")      
                elif len(accusername) <= 4:
                    p.error("Username length must be more than 4") # TODO: lenght -> length (cały plik)
                elif len(accusername) <= 25:
                    accepted_actions += 1
                    p.success("Username Accepted")
                    _username.add(accusername)
                else:
                    p.warning("Something went wrong with checking your username. | Username too long")

            def getname():
                global accepted_actions
                accname = str(self.accgenemail_textedit_name.toPlainText())
                if accname == "":
                    p.debug(f'Getting name from {__info__["input-path"]("names.txt")}')
                    namesfilesize = os.path.getsize(__info__["input-path"]("names.txt"))
                    if namesfilesize == 0:
                        p.critical(f'GetName returned an error: [ {__info__["input-path"]("names.txt")} file is empty ]')
                    else:
                        with open(__info__["input-path"]("names.txt")) as inputname:
                            templist_2 = set()
                            for line in inputname:
                                templist_2.add(line.replace("\n", ""))
                            _name.add(random.choice(list(templist_2)))
                            accepted_actions += 1
                            p.success("Name Choosen Successfully")      
                elif len(accname) <= 2:
                    p.error("name length must be more than 2")
                elif len(accname) <= 25:
                    accepted_actions += 1
                    p.success("Name Accepted")
                    _name.add(accname)
                else:
                    p.warning("Something went wrong with checking your name. | Name too long")




            getemail()
            getname()
            getusername()
            getpassword()


            p.info("Accepted Actions :> " + Fore.GREEN + "[ " + str(accepted_actions) + " ]")
            if accepted_actions == 5:
                p.info(f"Data: [ Email Address: {list(_email)[0]} ] [ Name: {list(_name)[0]} ] [ Username: {list(_username)[0]} ] [ Password: {list(_password)[0]} ] [ Proxy: {_proxy} ]")
                asyncio.run(Features().CREATOR_EMAIL(Email_Address=list(_email)[0], Name=list(_name)[0], Username=list(_username)[0], Password=list(_password)[0], Proxy=_proxy, use_proxy=_useproxy))
            else:
                pass



        def getall_phone(self):
            _useproxy = True if self.checkuseproxy.isChecked() == True else False
            _phone = set()
            _name = set()
            _username = set()
            _password = set()
            global accepted_actions
            accepted_actions = 0
            

            def loadproxy():
                global accepted_actions
                proxylist = set()
                proxyfilesize = os.path.getsize(__info__["input-path"]("proxies.txt"))
                if _useproxy == True:
                    if proxyfilesize != 0:
                        with open(__info__["input-path"]("proxies.txt")) as getproxy:
                            for line in getproxy:
                                proxylist.add(line)
                        p.ok(f'{__info__["input-path"]("proxies.txt")}')
                        accepted_actions += 1
                        return str(random.choice(list(proxylist)))
                    else:
                        p.critical(f'Proxy list is empty! | Please insert proxies in {__info__["input-path"]("proxies.txt")}')
                else:
                    p.warning("Use Proxies turned off")
                    accepted_actions += 1
                    return None
                        

                                
                

            _proxy = loadproxy()

            def checkPhone(phonenum, warn, err):
                if phonenum == "":
                    p.warning(warn)
                    return False

                for x in string.ascii_letters + "ąęóśłżźćĄĘŻŹŚÓŁ":
                    if phonenum.__contains__(x):
                        p.error(err)
                        return False
                return True

            def getphonenum():
                global accepted_actions
                phonenum = str(self.insertphonenum.toPlainText())
                
                if(checkPhone(phonenum, "Mobile Phone Number is required!", "Mobile Phone number can't contain letters") == True):
                    p.success("Phone Number Accepted")
                    accepted_actions += 1
                    _phone.add(phonenum)
                    return True
            





            def getpassword():
                global accepted_actions
                accpassword = str(self.insertpassword.toPlainText())
                if accpassword == "":
                    p.debug(f'Getting password from {__info__["input-path"]("passwords.txt")}')
                    passfilesize = os.path.getsize(__info__["input-path"]("passwords.txt"))
                    if passfilesize == 0:
                        p.warning(f'GetPassword returned anerror : [ {__info__["input-path"]("passwords.txt")} file is empty ]')
                        p.info("Generating password...")
                        un = ""
                        for x in range(48):
                            un = un + random.choice(string.ascii_letters + string.digits)
                        _password.add(un)
                        p.success(f"Password Generated: [ {un} ]")
                        accepted_actions += 1
                        # TODO: Generowanie haseł
                    else:
                        with open(__info__["input-path"]("passwords.txt")) as inputpassword:
                            templist_1 = set()
                            for line in inputpassword:
                                templist_1.add(line.replace("\n", ""))
                            _password.add(random.choice(list(templist_1)))
                            accepted_actions += 1
                            p.success("Password Choosen Successfully")      
                elif len(accpassword) <= 4:
                    p.error("Password length must be more than 4")
                elif len(accpassword) <= 50:
                    accepted_actions += 1
                    p.success("Password Accepted")
                    _password.add(accpassword)
                    
                else:
                    p.warning("Something went wrong with checking your password. | Please contact support.")



            def getusername():
                global accepted_actions
                accusername = str(self.insertusername.toPlainText())
                if accusername == "":
                    p.debug(f'Getting username from {__info__["input-path"]("usernames.txt")}')
                    usernamesfilesize = os.path.getsize(__info__["input-path"]("usernames.txt"))
                    if usernamesfilesize == 0:
                        p.warning(f'GetUsername returned an error: [ {__info__["input-path"]("usernames.txt")} file is empty ]')
                        p.info("Generating username...")
                        un = ""
                        for x in range(24):
                            un = un + random.choice(string.ascii_letters + string.digits)
                        _username.add(un)
                        p.success(f"Username Generated: [ {un} ]")
                        accepted_actions += 1
                    else:
                        with open(__info__["input-path"]("usernames.txt"), "r") as inputusername:
                            templist_2 = set()
                            for line in inputusername:
                                templist_2.add(line.replace("\n", ""))
                            _username.add(random.choice(list(templist_2)))
                            accepted_actions += 1
                            with open(__info__["input-path"]("usernames.txt"), "w") as writeun:
                                writeun.write("")
                            with open(__info__["input-path"]("usernames.txt"), "a") as appendun:
                                for x in inputusername.readlines():
                                    if not(x.startswith(_username[0])):
                                        appendun.write(x)
                            # TODO: Usunięcie nicku z listy po użyciu.
                            p.success("Username Choosen Successfully & Deleted From List")      
                elif len(accusername) <= 4:
                    p.error("Username length must be more than 4") # TODO: lenght -> length (cały plik)
                elif len(accusername) <= 25:
                    accepted_actions += 1
                    p.success("Username Accepted")
                    _username.add(accusername)
                else:
                    p.warning("Something went wrong with checking your username. | Username too long")

            def getname():
                global accepted_actions
                accname = str(self.insertname.toPlainText())
                if accname == "":
                    p.debug(f'Getting name from {__info__["input-path"]("names.txt")}')
                    namesfilesize = os.path.getsize(__info__["input-path"]("names.txt"))
                    if namesfilesize == 0:
                        p.critical(f'GetName returned an error: [ {__info__["input-path"]("names.txt")} file is empty ]')
                    else:
                        with open(__info__["input-path"]("names.txt")) as inputname:
                            templist_2 = set()
                            for line in inputname:
                                templist_2.add(line.replace("\n", ""))
                            _name.add(random.choice(list(templist_2)))
                            accepted_actions += 1
                            p.success("Name Choosen Successfully")      
                elif len(accname) <= 2:
                    p.error("name length must be more than 2")
                elif len(accname) <= 25:
                    accepted_actions += 1
                    p.success("Name Accepted")
                    _name.add(accname)
                else:
                    p.warning("Something went wrong with checking your name. | Name too long")




            getphonenum()
            getname()
            getusername()
            getpassword()


            p.info("Accepted Actions :> " + Fore.GREEN + "[ " + str(accepted_actions) + " ]")
            if accepted_actions == 5:
                p.info(f"Data: [ PhoneNum: {list(_phone)[0]} ] [ Name: {list(_name)[0]} ] [ Username: {list(_username)[0]} ] [ Password: {list(_password)[0]} ] [ Proxy: {_proxy} ]")
                mainthread = multiprocessing.Process(target=(threading.Thread(target=(asyncio.run(Features().CREATOR_PHONE(Account_Number=None, Phone_Number=list(_phone)[0], Name=list(_name)[0], Username=list(_username)[0], Password=list(_password)[0], Proxy=_proxy, use_proxy=_useproxy))), daemon=True, name="Creating Account")), daemon=True)
                mainthread.join()
                mainthread.start()
            else:
                pass
########################################################################################################################################################################################################################################################################################################################################################################
            
            
    

#######################################################################Generator#######################################################################################
        # NOTE: Przycisk od ACCGEN By phone number
        self.btn_startfuture24.clicked.connect(lambda: getall_phone(self))
        self.accgenemail_pushbutton_start.clicked.connect(lambda: getall_email(self))

#######################################################################################################################################################################










class InstaBot:
    def __init__(self) -> None:    
        self.none = None



logo = fr"""
                        ██▓ ███▄    █   ██████ ▄▄▄█████▓ ▄▄▄        ▄████ ▓█████  ███▄    █ 
                        ▓██▒ ██ ▀█   █ ▒██    ▒ ▓  ██▒ ▓▒▒████▄     ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
                        ▒██▒▓██  ▀█ ██▒░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
                        ░██░▓██▒  ▐▌██▒  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
                        ░██░▒██░   ▓██░▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒░▒▓███▀▒░▒████▒▒██░   ▓██░
                        ░▓  ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
                        ▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░    ░      ▒   ▒▒ ░  ░   ░  ░ ░  ░░ ░░   ░ ▒░
                        ▒ ░   ░   ░ ░ ░  ░  ░    ░        ░   ▒   ░ ░   ░    ░      ░   ░ ░ 
                        ░           ░       ░                 ░  ░      ░    ░  ░         ░ 
"""
    
# TODO: Wytabowałem logo aby łatwiej zobaczyć logo

if __name__ == "__main__":
    print(Style.BRIGHT + logo)
    p.info(f"Welcome to {__info__['appname']} | Enjoy A Lot Of Features For Free With WieszakWare InstaGen!")
    p.info(f"Application Version: [ {__info__['version']} ]")
    p.info(f"For more info / help visit our webisite! | 'https://wieszakware.epizy.com'")
    p.warning("Application is not stable for now! | Some features will not work!")
    p.debug("Prepairing Files | WieszakWare Files")
    p.debug("Proccessing Files | WieszakWare InstaGen")
    p.debug("Loading UI | UI By WieszakWare")
    p.info("If you have any questions please contact me on DM | Wieszak#6385")
    p.info("WieszakWare InstaGen By [ Wieszak#6385 [ https://wieszakware.epizy.com ] ] x [ Bombelek#2206 ]")
    #print("")
    #__loader = [math.factorial(load) for load in tqdm(range(random.randrange(3000, 9000)))]
    #print("")
    #__loader = Parallel(n_jobs=10)(delayed(math.factorial)(load) for load in tqdm(range(random.randrange(1000, 2000)), colour="yellow"))
    #print("")
    p.success("WieszakWare InstaGen Loaded Successfully!")
    
    while checkproperties() == False:
        pass
    else:

        #try:
            app = QApplication(sys.argv)
            window = APP()
            p.success(f"Successfully executed | WieszakWare InstaGen")
            p.hardwareinfo(f"Logical CPU: [ {[psutil.cpu_count()]} ]")
            p.hardwareinfo(f"CPU Frequency: {[psutil.cpu_freq()]}")
            p.hardwareinfo(f"CPU Times: {[psutil.cpu_times()[0]]}")
            conf["use_proxy"] = True

            try:
                sys.exit(app.exec_())
            except:
                p.debug("Exiting | WieszakWare InstaGen")
        #except Exception as e:
            #p.critical(f"WieszakWare Critical Error Detected | Code: STOPCODE | Exception Found: {e}")
