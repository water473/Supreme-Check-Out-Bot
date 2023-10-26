from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
executable_path = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()


driver = webdriver.Chrome(executable_path, options=options)

driver.get("https://www.supremenewyork.com/shop/jackets/elf1deo3y")

time.sleep(5)
driver.quit()
#atc
search = driver.find_element_by_name("commit")
search.click()
print("Successful ATC")
#checkout now
try:
    checkout = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.LINK_TEXT, "checkout now"))
    )
    checkout.click()
except:
    driver.quit()


#first and last name
try:
    name = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="order_billing_name"]'))
    )
    name.send_keys("Dimitrios Mahairas")
except:
    driver.quit()



#email address
email = driver.find_element_by_xpath('//*[@id="order_email"]')
email.clear()
email.send_keys("dimitriosrko114@gmail.com")
print("submitting email")

#phone number
phone = driver.find_element_by_xpath('//*[@id="order_tel"]')
phone.clear()
phone.send_keys("4353453455")
print("submitting phone")
#address
address = driver.find_element_by_xpath('//*[@id="bo"]')
address.clear()
address.send_keys("1234 Huxley Avenue")
print("submitting shipping")

#zipcode
zipcode = driver.find_element_by_xpath('//*[@id="order_billing_zip"]')
zipcode.clear()
zipcode.send_keys("10471")


#card info
cardinfo = driver.find_element_by_xpath('//*[@id="rnsnckrn"]')
cardinfo.clear()
cardinfo.send_keys("1111111111111111")
print("submitting billing")

#cvv (security code)
securitycode = driver.find_element_by_xpath('//*[@id="orcer"]')
securitycode.clear()
securitycode.send_keys("734")


#expiry month
month = Select(driver.find_element_by_xpath('//*[@id="credit_card_month"]'))
month.select_by_visible_text("02")


#expiry year
year = Select(driver.find_element_by_xpath('//*[@id="credit_card_year"]'))
year.select_by_visible_text("2025")


#state 
state = Select(driver.find_element_by_xpath('//*[@id="order_billing_state"]'))
state.select_by_visible_text("NY")


#click accept terms and conditions
terms = driver.find_element_by_xpath('//*[@id="terms-checkbox"]/label/div/ins')
terms.click()


#process payment
try:
    process = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="pay"]/input'))
    )
    process.click()
except:
    driver.quit()

print("Proccessing Payment...")

time.sleep(3)

print("Checkout Successful")
time.sleep(5)



driver.quit()
print("Task Complete")