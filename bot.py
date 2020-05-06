from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
import time,sys

def new_chat(username):
    new_chat=driver.find_element_by_xpath('//div[@class="gQzdc"]')
    new_chat.click()
    new_user=driver.find_element_by_xpath('//div[@class="_2S1VP copyable-text selectable-text"]')
    new_user.send_keys(username)
    time.sleep(2)
    try:
        user=driver.find_element_by_xpath('//span[@title="{}"]'.format(username))
        user.click()
        message = driver.find_element_by_xpath('//div[@class="_1Plpp"]')
        message.send_keys('Hi, I\'m kutty\'s bot')
        sendbtn = driver.find_element_by_xpath('//button[@class="_35EW6"]')
        sendbtn.click()
        
        filepath = "set a path of your file located "
        files = driver.find_element_by_xpath('//div[@title="Attach"]')
        files.click()
        images = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        images.send_keys(filepath)
        time.sleep(2)
        image_send_btn = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
        image_send_btn.click()

    except ElementClickInterceptedException:
        print('This person is not in your contact')
    except Exception as e:
        driver.close()
        print(e)
        sys.exit()

if __name__=='__main__':
    options=webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=C:/Users/"System Name"/AppData/Local/Google/Chrome/User Data/Default')
    options.add_argument('--profile-directory=Default')

    driver=webdriver.Chrome(executable_path='D:/software/chromedriver/chromedriver.exe', options=options)
    driver.maximize_window()
    driver.get('https://web.whatsapp.com/')
    time.sleep(15)

    print(time.time())
    while (True):
        if (time.localtime(time.time()).tm_hour == 10 and time.localtime(time.time()).tm_min == 28):
            break


    username_list = ['XXX']
    for username in username_list:
        try:
            user=driver.find_element_by_xpath('//span[@title="{}"]'.format(username))
            user.click()
            message = driver.find_element_by_xpath('//div[@class="_1Plpp"]')
            message.send_keys('Hi, I\'m kutty\'s bot')
            sendbtn = driver.find_element_by_xpath('//button[@class="_35EW6"]')
            sendbtn.click()
            
            filepath = "set a path of your file located "
            files = driver.find_element_by_xpath('//div[@title="Attach"]')
            files.click()
            images = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
            images.send_keys(filepath)
            time.sleep(2)
            image_send_btn = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
            image_send_btn.click()

        except NoSuchElementException as nc:
            new_chat(username)


