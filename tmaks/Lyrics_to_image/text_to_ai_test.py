from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()


user_mode_set = input("y, n: ")
chrome_driver_path = "chromedriver/chromedriver.exe"
lyric_list = input("write a few words or expressions separated by ~").split("~")

for line in lyric_list:
    if user_mode_set == "n":
        options.add_argument("--headless=new")
    s = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=s, options=options)


    URL_AI = "https://dream.ai/create"
    driver.get(URL_AI)

    search = driver.find_element(By.XPATH, '//*[@id="blur-overlay"]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/input')
    search.click()
    search.send_keys(line)
    x1 = driver.find_element(By.XPATH, '//*[@id="blur-overlay"]/div/div/div[1]/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div')
    x1.click()
    x2 = driver.find_element(By.XPATH, '//*[@id="blur-overlay"]/div/div/div[1]/div[2]/button')
    x2.click()
    print(f"Waiting for AI to generate image based on '{line}'")
    time.sleep(30)
    x3 = driver.find_element(By.CSS_SELECTOR, '#blur-overlay > div > div > div.PaneContainers__PaneDisplayContainer-sc-9ic5sr-1.DreamOutput__PaneDisplayContainer-sc-q3wcit-0.iPZNUi.jRFaEk > div.DreamOutput__DreamOutputContainer-sc-q3wcit-3.jmCaAz > div > div > div:nth-child(1) > div > div > div > div:nth-child(3)')
    x3.click()

    time.sleep(6)# just to ensure that image will be downloaded
    print(f"Image based on '{line}' was downloaded")
    driver.quit()
