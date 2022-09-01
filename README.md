# WieszakWare InstaGen
### A new powerfull tool for automatic creation of [Instagram](https://www.instagram.com/) accounts.

Before asking for help please read FAQ.  
Do you want to get touch in touch with us?  
Join our [discord server](https://discord.gg/KCqrbVgSBF)!

### FAQ  
**Q:** What is InstaGen?  
**A:** InstaGen is open source automation tool for creating instagram accounts.

**Q:** Is it a virus?  
**A:** No it isn't, and if you don't trust us, you can look at [source code](https://github.com/WieszakWare/InstaGen) of our program or even run/compile from [source](#how-to-runcompile-from-source)!

**Q:** Why is `x` not working?  
**A:** Soon we are going to release a tutorial explaining everything, or if you found a bug you can create bug report in [issues section](https://github.com/WieszakWare/InstaGen/issues).

**Q:** Hey you can change this and this and...  
**A:** If you would like to change/patch something in InstaGen, you can always fork this project and create pull request.

**Q:** Is Linux/MacOS supported?  
**A:** For now we are not planning to add Linux/MacOS support, but we included intrustion on how to run from source for MacOS and linux too, so if you want you should be able to try, but we do not promise that code will be working on those platforms.

**Q:** Can I republish/modify this project?  
**A:** This project is licensed under [GPL V2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt).

### How to run/compile from source.
Don't trust our pre-compiled binaries?  
Here we will teach you how you can run from source code.  
Note for Linux users: As your case is a little bit diffrent documentation (or kinda lack of it) has been moved to [Running under Linux Section](#running-under-linux).  
Also as we mentioned in [FAQ](#faq), we are creating instagen for windows and MacOS/Linux is not supported. While we give instruction on how run it, we can't be 100% if it is going to run under those platforms. And we are not planning on adding support any time soon.

#### Downloading Python (Windows/MacOS)
InstaGen is using Python 3.10.4.  
You can download it from [official python website.](https://www.python.org/downloads/release/python-3104/).  
Also make sure you have `Add Python 3.10.4 to PATH` checked at the bottom.  
Now to make sure you have installed python,  
- **On Windows**: Press Windows button and search for `cmd` or `Command Prompt`.
- **On MacOS**: Idk, I don't use it just open your terminal.
And type `python --version` or `python3.10 --version`. if you see output saying that python version is 3.10.4 it means that you have sucessfully installed python, if not then it means that you have screwd something up. And please don't create issues or beg for help with installing python, just google the tutorial.

#### Downloading code and preparing envrioment (Windows/MacOS)
Now to download source code go to [code tab](https://github.com/WieszakWare/InstaGen). Under the green `Code \/` menu, you can click `Download ZIP`. Now unzip the contest and for simplify documentation I will have path pointent to your desktop.
MACOS NOTE: In [Drivers](https://github.com/WieszakWare/InstaGen/tree/master/Drivers) folder, replace chrome driver with Chrome Driver for MacOS, you can download it from [official chrome webiste](https://chromedriver.chromium.org/) and replace gecko driver witb Firefox Driver for MacOS, you can download it from [official firefox github page](https://github.com/mozilla/geckodriver/releases).  
Once you have unziped you can execute the following commands:  
NOTE: Replcae the path to InstaGen with your own path, and replace python with python3 or python3.10 if it is the command you have python bind to.  
For Windows:
```
cd C:\Users\USER_USERNAME\Desktop\InstaGen
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
venv\Scripts\deactivate
```
For MacOS:
```
cd ~/Desktop/InstaGen
python -m venv venv
venv/bin/activate
pip install -r requirements.txt
venv/bin/deactivate
```

#### Running code (Windows/MacOS)
Now everytime you want to launch InstaGen from source you have to type following command.
Windows:
```
cd C:\Users\USER_USERNAME\Desktop\InstaGen && venv\Scripts\activate && python main.py && venv\Scripts\deactivate
```
MacOS:
```
cd ~/Desktop/InstaGen && venv/bin/activate && python main.py && venv/bin/deactivate
```


### Running under Linux
As it's pain in the ass compyling and supporting all linux distributions you will have to do some work for yourself.

#### Downloading Python (Linux)
Here I can't help because there just so many package managers, so this I am leaving up to you to find out how to install Python 3.10.4 on your specific distribution.

#### Downloading code and preparing envrioment (Linux)
Now to download source code go to [code tab](https://github.com/WieszakWare/InstaGen). Under the green `Code \/` menu, you can click `Download ZIP`. Now unzip the contest and for simplify documentation I will have path pointent to your desktop.
NOTE: In [Drivers](https://github.com/WieszakWare/InstaGen/tree/master/Drivers) folder, replace chrome driver with Chrome Driver for Linux, you can download it from [official chrome webiste](https://chromedriver.chromium.org/) and replace gecko driver witb Firefox Driver for Linux, you can download it from [official firefox github page](https://github.com/mozilla/geckodriver/releases).  
Once you have unziped you can execute the following commands:  
NOTE: Replcae the path to InstaGen with your own path, and replace python with python3 or python3.10 if it is the command you have python bind to. 
```
cd ~/Desktop/InstaGen
python -m venv venv
venv/bin/activate
pip install -r requirements.txt
venv/bin/deactivate
```

#### Running code (Linux)
Now everytime you want to launch InstaGen from source you have to type following command.
```
cd ~/Desktop/InstaGen && venv/bin/activate && python main.py && venv/bin/deactivate
```

WieszakWare 2022, Licensed under [GPL V2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt)  
[YouTube Wieszak](https://youtube.com/c/WieszakXD)  
[Instagram @wieszakyt](http://instagram.com/wieszakyt)
