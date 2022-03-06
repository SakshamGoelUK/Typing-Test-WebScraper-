
from pynput.keyboard import Key,Controller
import pyautogui as py;
import time;
from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
global browser
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options,executable_path=ChromeDriverManager().install())
browser.get('https://monkeytype.com/')
keyboard = Controller()
startWord= browser.find_element_by_id('words')
startWord.click()
words = startWord.get_attribute('innerText').split('\n')
print(words)
y=0
for i in words:
    wordLength = len(i)

    x = 0
    for j in i:
            time.sleep(0.05)
            x += 1
            keyboard.press(j)
            keyboard.release(j)
            if(x == wordLength):
                keyboard.press(Key.space)
                keyboard.release(Key.space)
                y += 1



