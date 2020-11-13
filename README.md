# Google-Meet-Bot
A bot that attends google meetings. It can exit from the meeting when the number of participants drops down a value or if a certain word or phrase has been called during the meeting(eg: your name)

## Requirements
* Python 3.7 or above : https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe (Link for python 3.9.0)
   
* Open cmd as administrator and run the following command to install Selenium   
      
```
pip install selenium
```
or
```
python -m pip install selenium
```

* Google Chrome

* Chrome Driver: Find out which version of Google Chrome you have by going to Help->About Google Chrome. Then go to https://sites.google.com/a/chromium.org/chromedriver/downloads and download the same driver as the Google Chrome version you are using. You’ll want chromedriver_win32.zip. Extract chromedriver_win32.zip and it will give you a file called chromedriver.exe. Now, Paste chromedriver.exe C:\Windows


## Running the program
* Make sure that 2-step verification process is off for your google account

* Update "conf.py" using your text editor and make the changes as per your requirement

* Execute "gMeet.py" and avoid making any mouse-clicks on the browser when the program is running.

* While running the program for the first time, the program might get interupted because of google-security issues(this should happen only the first time). Resolve the issues manually when they pop during the program's execution. Once done, execute the program again
