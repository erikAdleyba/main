from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from collections import *
import numpy as np
import pandas as pd
import random as rd

o = Options()
o.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=o)
wait = WebDriverWait(driver, 30)
driver.get('https://www.vseprosport.ru/news/today')
#driver.fullscreen_window()
time.sleep(10)

