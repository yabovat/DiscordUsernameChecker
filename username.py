import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()

# Navigate to url
driver.get("https://discord.com/login?redirect_to=%2Fchannels%2F%40me")

# Wait for 3 seconds to load the webpage completely 
time.sleep(11) 

username = "<Enter Username Here>"
password = "<Enter Password Here>"
driver.find_element(By.XPATH, '//*[@id="uid_5"]').send_keys(username) # Enter Username
driver.find_element(By.XPATH, '//*[@id="uid_7"]').send_keys(password) # Enter Password

# Click the login button
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/button[2]').click()
time.sleep(7) 

# Click the settings button
driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[1]/section/div[2]/div[2]/button[3]').click()
time.sleep(5) 

# Click the edit username button
driver.find_element(By.XPATH, '//*[@id="my-account-tab"]/div/div[1]/div[2]/div/div[2]/div/div[2]/button').click()
time.sleep(6)

# Click new username input button
driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div[1]/div[4]/div[2]/div/div/form/div[1]/div[1]/div/div/input').click()
time.sleep(5)

# Clear the current username                           
driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div[1]/div[4]/div[2]/div/div/form/div[1]/div[1]/div/div/input').send_keys([Keys.BACKSPACE] * 1000) #clear username

yeahIsAvailable = "Username is available. Nice!" # username is available alert

# Append the list of usernames you would like to check to the following array of strings:
usernames = [] 
usernames.append("avaiableusername")
usernames.append("oo.")
usernames.append(".oo")
usernames.append("_x")
usernames.append("x_")
usernames.append(".x")
usernames.append("x.")
usernames.append("_c")
usernames.append("c_")
usernames.append(".c")
usernames.append("c.")
usernames.append("_v")
usernames.append("v_")
usernames.append(".v")
usernames.append("v.")
usernames.append("_n")
usernames.append("n_")
usernames.append(".n")
usernames.append("n.")
usernames.append("_m")
usernames.append("m_")
usernames.append(".m")
usernames.append("m.")

for str in usernames:
    driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div[1]/div[4]/div[2]/div/div/form/div[1]/div[1]/div/div/input').send_keys(str) # input username
    time.sleep(3) # wait for validaiton from discord
    isUsernameAvail = driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div[1]/div[4]/div[2]/div/div/form/div[1]/div[2]/div/div').text # alert XPATH
    if isUsernameAvail == yeahIsAvailable: #check isUsernameAvailable? if yeahIsAvailable print username 
        print(str)
    driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div[1]/div[4]/div[2]/div/div/form/div[1]/div[1]/div/div/input').send_keys([Keys.BACKSPACE] * 1000) #clear username

print("test complete")

###############################  N O T E S  ############################### 

# Bibliography:
# find button with xpath
# https://www.geeksforgeeks.org/python-selenium-find-button-by-text/

# entering info
# https://www.guru99.com/accessing-forms-in-webdriver.html

# more info
# https://www.selenium.dev/documentation/webdriver/elements/interactions/#click

# can't click becuase element obscured
# https://stackoverflow.com/questions/49921128/selenium-cant-click-element-because-other-element-obscures-it

# more button click
# https://stackoverflow.com/questions/21350605/python-selenium-click-on-button

# clear text 
# https://stackoverflow.com/questions/7732125/clear-text-from-textarea-with-selenium

# Attributes you can use for locators
# https://stackoverflow.com/questions/30002313/finding-elements-by-class-name-with-selenium-in-python

# Get print text from div
# https://stackoverflow.com/questions/57936583/python-selenium-i-cant-get-print-text-from-div

# array of strings python
# https://sparkbyexamples.com/python/create-array-of-strings-in-python/

# for loops python
# https://discovery.cs.illinois.edu/learn/Simulation-and-Distributions/For-Loops-in-Python/