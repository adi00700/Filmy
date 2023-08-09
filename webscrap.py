import numpy as np
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import sys
import os
from dotenv import load_dotenv
from datetime import datetime



opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
        # Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 1,
            "profile.default_content_setting_values.notifications": 1
        })

browser = webdriver.Chrome(executable_path='/Users/harshitkalra/Desktop/ml/chromedriver', options=opt)
browser.get("https://www.hotstar.com/in/movies/list/popular-movies/t-5739_25_4")
time.sleep(7)
mov_list = []
genre_list = []
for j in range(20):
    time.sleep(3)
    browser.execute_script(f"window.scrollTo(0, {250*j})")
    movie = browser.find_elements_by_xpath("//span[contains(@class, 'content-title ellipsise')]")
    genre = browser.find_elements_by_xpath("//span[contains(@class, 'subtitle')]")
    for i in range(len(movie)):
        content = browser.execute_script('return arguments[0].textContent;', movie[i])
        g = browser.execute_script('return arguments[0].textContent;', genre[i])
        if content not in mov_list:
            mov_list.append(content)
            genre_list.append(g)

mov_list = np.array(mov_list)
genre_list = np.array(genre_list)
df = pd.DataFrame({'Movies':mov_list, 'Genre':genre_list})
df.to_csv("Mov.csv")
print(len(mov_list))
print(len(genre_list))
time.sleep(3)
