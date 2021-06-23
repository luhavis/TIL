import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


chrome_options = Options()



chrome_options.add_argument("headless")
chrome_options.add_argument("window-size=1920x1080")
chrome_options.add_argument("--start-fullscreen")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36")

URL = ""

driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=chrome_options)
wait = WebDriverWait(driver, 5)

driver.get(URL)

driver.get_screenshot_as_file("test2.png")