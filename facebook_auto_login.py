from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


user=input('Enter User Id of your Fb Account :')  # Take user id and password as input from the user
password=input('Enter the password :')

print(user)
print(password)

cd='C:\\chromedriver\\chromedriver.exe' #path to the driver

browser= webdriver.Chrome(cd)
browser.get('https://www.facebook.com/')


user_box = browser.find_element_by_id("email")       # For detecting the user id box
user_box.send_keys(user)                                               # Enter the user id in the box 

password_box = browser.find_element_by_id("pass")    # For detecting the password box
password_box.send_keys(password)                                          # For detecting the password in the box

login = browser.find_element_by_id("u_0_b")      # For detecting the Login button
login.click()
