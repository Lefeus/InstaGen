import os

### TODO:
### Zapis ostatniej sesji (chodzi o menu)

### Import bibliotek
try:
    import urllib.request
    import datetime
    import sys
    import time
    import asyncio
    import random
    import json
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
except ImportError:
    print("Installing")
    os.system("pip install -r requirements.txt")
    print("Relaunch WieszakWare")

init(autoreset=True)

############################################################################################################################

### Informacje
__info__ = {
    "appname": "InstaGen",
    "version": "TEST 1.0.2",
    "logspath": os.path.join(os.getcwd(), "logs", "logs.log"),
    ".ui-file-path": os.path.join(os.getcwd(), "ui", "ui_main.ui"),
    "input-path": lambda filename: os.path.join(".input", f"{filename}"),
    "property_0": "#FUTURE24",
    "property_1": "W^Z8gM60oMZ0*UgxY!mzqhtHc#TSFaWojlm8Wru^X3axY7gLr3",
    "property_2": "v8g@tf11CKO12EHZgQhL3gG7#c5O7bf*28Z8BKN1",
    "property_3": "8364-8263-1823-9172-1735",
    "property_4": "1103-0002-7772-0000-1728",
    "special-password": "wieszakware-future24"
}

############################################################################################################################

conf = json.load(open("config.json"))

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
        self.RESET = Style.RESET_ALL
        
        self.AllowDebug = True

    def info(self, text: str = None) -> None:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ INFO ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Info + "[ INFO ] >" + " " + f"{text}")


    def warning(self, text: str = None) -> None:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ WARNING ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Warning + "[ WARNING ] >" + " " + f"{text}")


    def debug(self, text: str = None) -> None:
        if not(self.AllowDebug):
            return
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ DEBUG ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Debug + "[ DEBUG ] >" + " " + f"{text}")


    def critical(self, text: str = None) -> None:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ CRITICAL ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Critical + "[ CRITICAL ] >" + " " + f"{text}")


    def error(self, text: str = None) -> None:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ CRITICAL ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Error + "[ ERROR ] >" + " " + f"{text}")


    def ok(self, text: str = None) -> None:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ OK ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Ok + "[ OK ] >" + " " + f"{text}")

    
    def success(self, text: str = None) -> None:
        try:
            with open(file=f"{__info__['logspath']}", mode="a+") as logfile:
                logfile.write(f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + "[ SUCCESS ] >" + " " + f"{text}" + "\n")
                logfile.close()
        except Exception as e:
            print(self.Error + f"There was an error | Exception Found: [ {e} ] | ERROR: dir not exists / file not exists | Fix: [ Create 'logs' folder ]")
        print(self.Time + f"[ {datetime.datetime.now().strftime('%H:%M:%S')} ]" + " " + self.Success + "[ SUCCESS ] >" + " " + f"{text}")


p = Print()




###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################

class Features():
    def __init__(self):
        super(Features, self).__init__()
        self.none = None
        
    ### Stwórz konto instagram
    async def CREATOR(self, Account_Number: int, Phone_Number: str, Name: str, Username: str, Password: str, Proxy: str, use_proxy: bool = False):


        binaries = os.path.join(os.getcwd(), ".chromebinaries", "chrome.exe")
        CHROMEDRIVER = os.path.join(os.getcwd(), "Drivers", "chromedriver.exe")

        p.warning("This generator requires \"high quality\" proxies!")

        if use_proxy == False:
            options = {
                ### Proxy
                'proxy': {
                    #'http': 'http://wieszakware:4wieszakware@45.140.13.119:9132',
                    #'https': 'http://wieszakware:4wieszakware@45.140.13.119:9132',
                    #'http': 'http://116.202.13.106:8080',
                    #'https': 'http://116.202.13.106:8080',
                    #'http': 'http://wieszakware-rotate:4wieszakware@p.webshare.io:80',
                    #'https': 'http://wieszakware-rotate:4wieszakware@p.webshare.io:80',
                    'no_proxy': 'localhost,127.0.0.1' # excludes
                }  
            }
        elif use_proxy == True:
            oneproxy_service = Proxy.replace("\n", "")
            options = {
                'proxy': {
                    'http': f'{conf["proxytype"]}://{oneproxy_service}',
                    'https': f'{conf["proxytype"]}://{oneproxy_service}',
                    #'no_proxy': 'localhost,127.0.0.1' # excludes
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
        opt.add_argument("--silient")
        # opt.add_argument("--headless")
        opt.binary_location = binaries
           
            
            
        driver = webdriver.Chrome(CHROMEDRIVER, options=opt, seleniumwire_options=options)

        p.debug("Attempting to start webdriver")

        try:
            driver.get("http://instagram.com")
            p.success(f"Webdriver Started with proxy [ {Proxy} ]")
        except Exception as e:
            p.critical(f"Unable to start webdriver, please contact on Discord [ {e} ]")

        agent = driver.execute_script("return navigator.userAgent")
        p.debug(f"Current user agent: [ {agent} ]")

        try:
            ippp = urllib.request.Request("http://ipinfo.io/json")
            ippp.set_proxy(str(Proxy), 'http')
            response = urllib.request.urlopen("http://ipinfo.io/json")
            #print(response.read().decode('utf8'))
            #p.info(f"Getting IP address info: [ {response.read().decode()} ]")
            p.info(f"Successfully yoinked ip")
        except Exception as e:
            p.warning(f"Unable to get your ip address")

        #time.sleep(4)
        p.debug("Attempting to confirm cookies")
        
        try:
            #Confirm Cookies
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.RnEpo.Yx5HN._4Yzd2 > div > div > button.aOOlW.HoLwm"))).click()
            p.ok(f"Cookies confirmed [ Cookies list: ( {driver.get_cookies()} ) ]")
        except Exception as e:
            p.critical(f"Unable to confirm cookies. | Cookies already confirmed.")
        #time.sleep(5)
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
            p.info("Attempting to insert Phone Number")
            p.info("Attempting to insert Name")
            p.info("Attempting to insert Username")
            p.info("Attempting to insert Password")
            p.info("Attempting to click signup button")
            
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
            
            while True:
                try:
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-root > section > main > div > div > div:nth-child(1) > div.P8adC > form > div:nth-child(9) > div > button"))).click()
                    p.ok("Continue button clicked")
                    break
                except Exception as e:
                    try:
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[7]/div/button"))).click()
                        p.ok("Continue button clicked")
                        break
                    except:
                        p.critical(f"Unable to register on {driver.current_url}")
                        p.error("Unable to click continue button")
                        
        except Exception as e:
            p.critical(f"Unable to register on {driver.current_url}")

        await asyncio.sleep(4)
        
        #Birthday verification
        
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

        with open(os.path.join(os.getcwd(), ".created", "unknown.txt"), "a") as append:
            append.write(f"___________________________Unknown Accounts [It may be accounts not created successfully but working perfectly] {datetime.datetime.now().strftime('[%m/%d/%Y] - %H.%M.%S')}_______________________________\n")
            append.write("This can happen when you are using vpn\n")
            append.write("Accounts in this file are in queue to create or created with error because instagram is very weird\n")
            append.write("Phone Number: " + Phone_Number + "\n")
            append.write("Name        :" + Name + "\n")
            append.write("Username    :" + Username + "\n")
            append.write("Password    :" + Password)
            append.close()

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
        with open(os.path.join(os.getcwd(), ".created", "accounts.txt"), "a") as append:
            append.write(f"___________________________Account Created {datetime.datetime.now().strftime('[%m/%d/%Y] - %H.%M.%S')}_______________________________\n")
            append.write("Phone Number: " + Phone_Number + "\n")
            append.write("Name        :" + Name + "\n")
            append.write("Username    :" + Username + "\n")
            append.write("Password    :" + Password)
            append.close()
        await asyncio.sleep(3)
        try:
            p.debug("Attempting to accept cookies...")
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div[3]/div/div[1]/div/div[2]/div[1]/span"))).click()
            p.info("Selected cookies (minimal)")
            p.ok(f"[ Cookies list: ( {driver.get_cookies()} ) ]")
        except Exception as e:
            p.debug(e)
            p.info("Cookies already selected")
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys("wieszakyt")
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

        



###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################

class APP(QMainWindow):
     def __init__(self):
        super(APP, self).__init__()
        loadUi(__info__[".ui-file-path"], self)

        self.show()

        self.setWindowTitle(f'{__info__["appname"]} | {__info__["version"]}')

        ########################################################################################################



        self.stackedWidget.setCurrentWidget(self.page_accgen)



        self.btn_accgen.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_accgen))

        self.btn_likebot.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_likebot))

        self.btn_followbot.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_followbot))

        self.btn_COOMING_SOON.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_COOMING_SOON))

        self.btn_settings.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_settings))



#######################################################################GetInputs#######################################################################################
        def getall(self):
            _useproxy = True if self.checkuseproxy.isChecked() == True else False
            _accnum = set()
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
                    pass
                # ó duże
                for x in string.ascii_letters + "ąęóśłżźćĄĘŻŹŚŁ":
                    if phonenum.__contains__(x):
                        p.error(err)
                        return False
                return True

            def getphonenum():
                global accepted_actions
                phonenum = str(self.insertphonenum.toPlainText())
                
                if(checkPhone(phonenum, "Mobile Phone Number is required!.", "Mobile Phone number can't contain letters") == True):
                    p.ok("Phone Number Accepted")
                    accepted_actions += 1
                    _phone.add(phonenum)
                    return True
            




            def getacctogen():
                global accepted_actions
                acctogen = str(self.insertnumberacc.toPlainText())
                if acctogen == "":
                    p.warning("Number of accounts to generate is required!")
                    pass
                # Jak powyżej
                elif acctogen.__contains__("a"):
                    p.error("Method not allowed")
                    return False
                else:
                    p.ok("Number of accounts accepted")
                    accepted_actions += 1
                    _accnum.add(acctogen)
                    return True

            def getpassword():
                global accepted_actions
                accpassword = str(self.insertpassword.toPlainText())
                if accpassword == "":
                    p.debug(f'Getting password from {__info__["input-path"]("passwords.txt")}')
                    passfilesize = os.path.getsize(__info__["input-path"]("passwords.txt"))
                    if passfilesize == 0:
                        p.critical(f'GetPassword returned an error: [ {__info__["input-path"]("passwords.txt")} file is empty ]')
                    else:
                        with open(__info__["input-path"]("passwords.txt")) as inputpassword:
                            templist_1 = set()
                            for line in inputpassword:
                                templist_1.add(line.replace("\n", ""))
                            _password.add(random.choice(list(templist_1)))
                            accepted_actions += 1
                            p.success("Password Choosen Successfully")      
                elif len(accpassword) <= 4:
                    p.error("Password lenght must be more than 4")
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
                        p.success(f"Generated {un}")
                        accepted_actions += 1
                    else:
                        with open(__info__["input-path"]("usernames.txt")) as inputusername:
                            templist_2 = set()
                            for line in inputusername:
                                templist_2.add(line.replace("\n", ""))
                            _username.add(random.choice(list(templist_2)))
                            accepted_actions += 1
                            p.success("Username Choosen Successfully")      
                elif len(accusername) <= 4:
                    p.error("Username lenght must be more than 4")
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
                    p.error("name lenght must be more than 2")
                elif len(accname) <= 25:
                    accepted_actions += 1
                    p.success("Name Accepted")
                    _name.add(accname)
                else:
                    p.warning("Something went wrong with checking your name. | Name too long")




            getacctogen()
            getphonenum()
            getname()
            getusername()
            getpassword()


            p.info("Accepted Actions :> " + Fore.GREEN + "[ " + str(accepted_actions) + " ]")
            if accepted_actions == 6:
                p.info(f"Data: [ ACCNumber: {list(_accnum)[0]} ] [ PhoneNum: {list(_phone)[0]} ] [ Name: {list(_name)[0]} ] [ Username: {list(_username)[0]} ] [ Password: {list(_password)[0]} ] [ Proxy: {_proxy} ]")
                asyncio.run(Features().CREATOR(Account_Number=int(list(_accnum)[0]), Phone_Number=list(_phone)[0], Name=list(_name)[0], Username=list(_username)[0], Password=list(_password)[0], Proxy=_proxy, use_proxy=_useproxy))
            else:
                pass
            
            
            
  
        #data.clear()

#######################################################################Generator#######################################################################################
        self.btn_startfuture24.clicked.connect(lambda: getall(self))

#######################################################################################################################################################################










class InstaBot:
    def __init__(self) -> None:    
        self.none = None



logo = fr""" ██▓ ███▄    █   ██████ ▄▄▄█████▓ ▄▄▄        ▄████ ▓█████  ███▄    █ 
▓██▒ ██ ▀█   █ ▒██    ▒ ▓  ██▒ ▓▒▒████▄     ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▒██▒▓██  ▀█ ██▒░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
░██░▓██▒  ▐▌██▒  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
░██░▒██░   ▓██░▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒░▒▓███▀▒░▒████▒▒██░   ▓██░
░▓  ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
 ▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░    ░      ▒   ▒▒ ░  ░   ░  ░ ░  ░░ ░░   ░ ▒░
 ▒ ░   ░   ░ ░ ░  ░  ░    ░        ░   ▒   ░ ░   ░    ░      ░   ░ ░ 
 ░           ░       ░                 ░  ░      ░    ░  ░         ░ 
                                                                     """
    
        

if __name__ == "__main__":
    print(Style.BRIGHT + logo)
    p.info(f"Welcome to {__info__['appname']} | Enjoy A Lot Of Features For Free With WieszakWare #FUTURE24 Special Edition")
    p.info(f"Application Version: [ {__info__['version']} ]")
    p.info(f"For more info / help visit our webisite! | 'https://wieszakware.rf.gd'")
    p.warning("Application is not stable for now! | Some features will not work!")
    p.info("If you have any questions please contact me on DM | Wieszak#0384")
    while checkproperties() == False:
        pass
    else:

        try:
            app = QApplication(sys.argv)
            window = APP()
            p.success(f"Successfully executed with status code [ 200 ]")
            try:
                sys.exit(app.exec_())
            except:
                p.info("Exiting")
        except Exception as e:
            p.critical(f"Critical Error Detected | Code: STOPCODE | Exception Found: {e}")