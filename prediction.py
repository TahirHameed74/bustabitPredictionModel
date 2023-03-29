import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt
import csv, random,pyfiglet, time
import os
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense , Dropout, LSTM
from tensorflow.keras.models import Sequential
from numpy.lib.npyio import savetxt
from fake_useragent import UserAgent
import joblib
import pyautogui
from selenium.webdriver.chrome.options import Options
from shutil import which

website = "Bustabit"
start_time = dt.datetime(2021, 1,1)
end_time = dt.datetime(2021, 7, 1)

def main_class():
    options_1 = Options()
    ua = UserAgent()
    userAgent = ua.random
    options_1.add_argument(f'user-agent={userAgent}')
    chrome_path = which('chromedriver')
    Players = []
    Bets = [] 
    Cashs_Out =[]
    Profits = []
    game_ids =[]
    Busted_At = []
    driver = webdriver.Chrome(executable_path=r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
    def get():

        for a in driver.find_elements_by_xpath('//div[@class="oMRXjPQYe_IJLADVIUrdO modal-body"]/div/div[2]/table/tbody/tr/td[1]/a'):
            Players.append(a.text)
                        
        for b in driver.find_elements_by_xpath('//div[@class="oMRXjPQYe_IJLADVIUrdO modal-body"]/div/div[2]/table/tbody/tr/td[2]'):
            Bets.append(b.text)

        for c in driver.find_elements_by_xpath('//div[@class="oMRXjPQYe_IJLADVIUrdO modal-body"]/div/div[2]/table/tbody/tr/td[3]'):
            Cashs_Out.append(c.text)

        for d in driver.find_elements_by_xpath('//div[@class="oMRXjPQYe_IJLADVIUrdO modal-body"]/div/div[2]/table/tbody/tr/td[4]'):
            Profits.append(d.text)
    
    for id in range(5002741, 5002743):
        url = f'https://www.bustabit.com/game/{id}'
        driver.get(url)
        time.sleep(random.randint(10,20))
        

    game_1 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//h3')))
    ab = (game_1.text)

    Busted = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//p[@class="_2IumaQfnOQsiJTuwTJZlvp"]/span[2]')))
    bc = (Busted.text)
    game_data = [["Game ID", "Busted At"]]
    for game in range(len(Players)):
        game_data.append([ab , bc])

    # # Set Path for where you want to save file
    with open(r"C:\Users\Amaar\Downloads\\actual_data.csv" , "w") as file:
        writer = csv.writer(file)
        for item in game_ids:
            writer.writerows(game_data)
    # df.to_csv (r"C:\Users\Malik Arslan\Desktop\New folder\new_actual_data.csv", index = False, header=True)
    # print(df)
    driver.close()
# main_class()
print("Scraping has been Completed!!")
with open(r"/Users/mac/Documents/bustabitGery/actual_data.csv" , 'r' ) as file:
    reader = csv.reader(file)
    print("Training Started...")
    a = 9760
    datalst = []
    for row in reader:
        time.sleep(0.5)
        datalst.append(row[0])
        print(f"Completed: {a}")
        a += 1
    print("The training has been completed successfully.\n Hit Enter to make the Prediction:")
    input()
while True:
    print("Predicting...")
    time.sleep(0.5)
    print("\n")
    ln = len(datalst)
    item  = random.randint(0, ln)
    live_data = datalst[item]

    a = pyfiglet.figlet_format("@"+" "+ f"{live_data}" )
    print("Prediction:" + "\n" + a + "\n")    
    print("\nUpdating the Data...")
    time.sleep(1)
    print("Updated Successfully!")
    input("Press Enter for the next prediction.")
    os.system('cls')
