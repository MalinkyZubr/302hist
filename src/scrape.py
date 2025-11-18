import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import undetected_chromedriver as uc
from selenium_stealth import stealth
from selenium.webdriver.common.by import By



HOME_ADDRESS = "https://historicalnewspapers.lib.purdue.edu/?a=cl&cl=CL1&sp=PE&e=-------en-20--1--txt-txIN--------1"
options = Options()
#options.add_argument("--headless")
driver = uc.Chrome(options=options)
stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True
        )

driver.implicitly_wait(5)

driver.get(HOME_ADDRESS)
input("Enter anything when captcha complete")
print(driver.title)

driver.find_element(By.ID, 'datebrowserrichardtoplevelcalendar')

# close the browser
driver.quit()