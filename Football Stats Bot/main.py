import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 
from selenium import webdriver
import time

website= 'https://www.adamchoi.co.uk/overs/detailed'
driver=webdriver.Chrome()
driver.get(website)

all_matches = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches.click()
time.sleep(3)

dropdown=Select(driver.find_element(By.ID,'country'))
dropdown.select_by_visible_text('USA')
time.sleep(3)


matches = driver.find_elements(By.TAG_NAME, 'tr')

date = []
home_team = []
goals = []
away_team = []

for match in matches:
    date.append(match.find_element(By.XPATH, './td[1]').text)
    home = match.find_element(By.XPATH, './td[2]').text
    home_team.append(home)
    goals.append(match.find_element(By.XPATH, './td[3]').text)
    away_team.append(match.find_element(By.XPATH, './td[4]').text)
#     print(home)
driver.quit()


# Exporting to CSV 
df = pd.DataFrame({'Date': date, 'Home-team': home_team, 'Goals': goals, 'Away-team': away_team})
df.to_csv('Football.csv', index=False)


