
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#----------------------------------------- Choosing mode ---------------------------------------------------------------

options = webdriver.ChromeOptions()

while True:
    user_mode_set = input("Run code with opening browser/y or without/n?\nNote: Running code in headless mode(without "
                          "opening browser) will execute code faster because of less usage of memory.\ny/n: ").lower()

    if user_mode_set == "n":
        options.add_argument("--headless=new")
        break
    elif user_mode_set == "y":
        break
    else:
        print("Type y or n")

#-----------------------------------------Finding Lyrics Block ---------------------------------------------------------

creator, song = input("Name of creator(artist, band ect): ").lower(), input("Name of composition: ").lower()
print("Servers are processing input data. Please wait...")

chrome_driver_path = "chromedriver/chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s, options=options)
URL_GOOGLE = "https://www.google.com/"
driver.get(URL_GOOGLE)
search = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search.click()
search.send_keys(f"{creator} - {song} lyrics")
search.send_keys(Keys.ENTER)
find_lyrics = driver.find_element(By.XPATH,
'//*[@id="kp-wp-tab-default_tab:kc:/music/recording_cluster:lyrics"]/div[1]/div/div/div[2]/div/div/div/div/div[1]/div[2]')
lyric_list = find_lyrics.text.splitlines()
number_of_lines = len(lyric_list)
driver.quit()
print("Step completed. Starting to work with each line of text.")

#print(lyric_list)#   This two lines are just for optional checking if the lyrics were formated to list,
#input("step stopper")# type anything or just press Enter


#-------------------------------------- Text to image AI Block ---------------------------------------------------------

checklist = []# list to check line of text converted into image
for line in lyric_list:
    if user_mode_set == "n":
        options.add_argument("--headless=new")
    s = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=s, options=options)

    URL_AI = "https://dream.ai/create"
    driver.get(URL_AI)

    print(f"Waiting for AI to generate image based on line '{line}'")
    search = driver.find_element(By.XPATH, '//*[@id="blur-overlay"]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/input')
    search.click()
    search.send_keys(line)
    x1 = driver.find_element(By.XPATH, '//*[@id="blur-overlay"]/div/div/div[1]/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div')
    x1.click()
    x2 = driver.find_element(By.XPATH, '//*[@id="blur-overlay"]/div/div/div[1]/div[2]/button')
    x2.click()
    time.sleep(40)# can be decreased or increased due to quality of connection
    x3 = driver.find_element(By.CSS_SELECTOR, '#blur-overlay > div > div > div.PaneContainers__PaneDisplayContainer-sc-9ic5sr-1.DreamOutput__PaneDisplayContainer-sc-q3wcit-0.iPZNUi.jRFaEk > div.DreamOutput__DreamOutputContainer-sc-q3wcit-3.jmCaAz > div > div > div:nth-child(1) > div > div > div > div:nth-child(3)')
    x3.click()

    time.sleep(10)# just to ensure that image will be downloaded
    print(f"Image based on line '{line}' was downloaded.")
    driver.quit()

print(f"Executed {len(lyric_list)} items.")
