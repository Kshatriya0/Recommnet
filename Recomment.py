from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip
import time

def clickComment():
    
    driver.find_element(By.NAME, 'mainFrame').send_keys(Keys.SPACE)
    time.sleep(2)
    driver.switch_to.frame("mainFrame")
    driver.find_element(By.XPATH, '//*[@id="btn_comment_2"]').click()
    time.sleep(2)

def Login(myId, myPw):
    driver.find_element(By.CLASS_NAME, 'u_cbox_inbox').click()
    main_window = driver.current_window_handle
    for handle in driver.window_handles:
        if handle != main_window:
            driver.switch_to.window(handle)
            break

    id = driver.find_element(By.ID, "id")
    pyperclip.copy(myId)
    pw = driver.find_element(By.ID, "pw")


    #commentBox.send_keys('안녕하세요')
    #time.sleep(1)
    #driver.find_element(By.CLASS_NAME, 'u_cbox_txt_upload').click()

url = "https://blog.naver.com/iknow433/223705744432"
driver = webdriver.Chrome() 
driver.get(url)
time.sleep(3)

myId = "iknow433"
myPw = "6746Kmv+"

clickComment()
Login(myId, myPw)
time.sleep(2)