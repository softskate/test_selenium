from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


email = 'tzpythondemo@domconnect.ru'
password = 'kR092IEz'

browser = webdriver.Chrome()
browser.get('https://px6.me/')
sign_in_btn = browser.find_element(By.CSS_SELECTOR, '.pull-right > :nth-child(2) > .btn')
sign_in_btn.click()

form_login = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'form-login'))
)
email_input = form_login.find_element(By.NAME, 'email')
pass_input = form_login.find_element(By.ID, 'login-password')
submit = browser.find_element(By.CSS_SELECTOR, ':nth-child(7) > button')

email_input.send_keys(email)
pass_input.send_keys(password)

captcha = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'iframe'))
)
browser.switch_to.frame(captcha)
checkbox = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'recaptcha-anchor'))
)
while True:
    checked = checkbox.get_attribute('aria-checked')
    if checked == 'true':
        break
    sleep(.5)

browser.switch_to.default_content()
submit.click()

user_proxy_table = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'table.user_proxy_table'))
)
proxies = user_proxy_table.find_elements(By.CSS_SELECTOR, 'tr[id^="el-"]')
for proxy_row in proxies:
    host, date = proxy_row.find_elements(By.TAG_NAME, 'td')[2:4]
    host = host.find_element(By.CSS_SELECTOR, 'li > div.right > b').text
    date = date.find_element(By.CSS_SELECTOR, 'li > div.right').text
    print(f'{host} - {date}')

browser.close()
