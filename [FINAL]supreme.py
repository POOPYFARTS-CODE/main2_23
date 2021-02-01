from selenium import webdriver
from selenium import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import sys
import time

link = input('Enter The Link')

def checkStock():
  try:
    options = webdriver.ChromeOptions()# options for driver
    options.add_argument('--ignore-certificate-errors')#argumen added
    options.add_argument('--ignore-ssl-errors')#argumen added 
    driver = webdriver.Chrome("E:/chromedriver_win32 (3)/chromedriver.exe", chrome_options= options )#initiaizing driver
    driver.get(link)#userapp
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'swatch')))#wait till element specified is located
    username = driver.find_element_by_class_name('swatch')#sizes element parent
    options = username.find_elements_by_tag_name('label')#element conatins sizes
    optionList = []#sizes array
    for option in options:
      optionList.append(option.get_attribute('innerHTML'))
    for sizes in range(len(optionList)-2):
        print("Size "+ str(optionList[sizes][:20]) + " for is available.")
  finally:
     driver.quit() 


def selectSize():
  input_user = input('Please Select your Size:')
  return(input_user)

def final_stage():
  # size_ = selectSize()
  driver = webdriver.Chrome("chromedriver.exe" )
  driver.get(link)
  time.sleep(5)
  element1 = driver.find_element_by_xpath("//LABEL[@for='swatch-0-l']")
  element1.click()
  time.sleep(5)
  element2 = driver.find_element_by_xpath("/html/body/div[4]/main/div[1]/div/div[2]/div[1]/div[2]/div/div/div[1]/div[2]/form/div[5]/input")
  element2.click()
  time.sleep(10)
  element3 = driver.find_element_by_xpath("//BUTTON[@class='btn btn-go-to-cart'][text()='Go to cart']")
  time.sleep(5)
  element3.click()
  element4 = driver.find_element_by_xpath('/html/body/div[4]/main/div/div/div/form/div[2]/div[3]/input')
  element4.click()
  time.sleep(5)
  email_duda = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[1]/div[2]/div[1]/div/div/input')
  email_duda.send_keys('example@example.com')
  name1 = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div[1]/div[1]/div/input')
  name1.send_keys('John')
  name2 = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/input')
  name2.send_keys('Doe')
  addres = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/input')
  addres.send_keys('1234 blah blah')
  addres2 = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div[1]/div[4]/div/input')
  addres2.send_keys('1234 Random Addres')
  addres3 = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div[1]/div[5]/div/input')
  addres3.send_keys('Placer Hills')
  time.sleep(5)
  dropdown = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div[1]/div[7]/div/select/option[4]').click()
  pin = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div[1]/div[8]/div/input')
  pin.send_keys('791111')
  phone = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div[1]/div[9]/div/input')
  phone.send_keys('9234567890')
  continue_ = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[2]/button')
  continue_.click()
  time.sleep(5)
  continue_1 = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[2]/button')
  continue_1.click()
  time.sleep(5)
  check_box = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/div/form/div[1]/div[2]/div[2]/fieldset/div[4]/div[1]/input')
  check_box.click()
  time.sleep(10)
  # driver.switch_to.frame('card-fields-number-g27wkebc2yd00000-scope-www.streetwearofficial.com')
  # card_number = driver.find_element_by_tag_name('/html/body/form/input[1]')
  # card_number.send_keys('367257981963732')
  # name_on_c = driver.find_element_by_xpath('name')
  # name_on_c.send_keys('John Doe')
  # expiry = driver.find_element_by_xpath('expiry')
  # expiry.send_keys('11 24')
  # cvv = driver.find_element_by_xpath('verification_value')
  # cvv.send_keys('1234')
  # time.sleep(5)
  btnlast = driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/div/form/div[3]/div[1]/button')
  btnlast.click()
  time.sleep(10)
  password = driver.find_element_by_xpath('//*[@id="password"]')
  password.send_keys("Blah Blah bruh")
  time.sleep(10)




checkStock()
selectSize()
final_stage()


  #            *     ,MMM8&&&.            *
  #                 MMMM88&&&&&    .
  #                MMMM88&&&&&&&
  #    *           MMM88&&&&&&&&
  #                MMM88&&&&&&&&
  #                'MMM88&&&&&&'
  #                  'MMM8&&&'      *
  #         |\___/|
  #         )     (             .              '
  #        =\     /=
  #          )===(       *
  #         /     \
  #         |     |
  #        /       \
  #        \       /
  # _/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_
  # |  |  |  |( (  |  |  |  |  |  |  |  |  |  |
  # |  |  |  | ) ) |  |  |  |  |  |  |  |  |  |
  # |  |  |  |(_(  |  |  |  |  |  |  |  |  |  |
  # |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  # |  |  |  |  |  |  |  |  |  |  |  |  |  |  |