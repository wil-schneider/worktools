import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "YOUR_AVOS_URL"
avosUsername = "YOUR_AVOS_USERNAME"
avosPassword = "YOUR_AVOS_PASSWORD"


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get(url)

driver.implicitly_wait(3)

login_username_text_box = driver.find_element(By.NAME, value="j_username")
login_password_text_box = driver.find_element(By.NAME, value="j_password")
login_button = driver.find_element(By.XPATH, "//input[@value='Log In']")


login_username_text_box.send_keys(avosUsername)
login_password_text_box.send_keys(avosPassword)
login_button.click()

driver.implicitly_wait(3)

link_to_active_processes = driver.find_element(By.XPATH, "//*[@title='View active processes']")

link_to_active_processes.click()

query_expression_text_box = driver.find_element(By.ID, value="query_expression")
query_expression_text_box.send_keys("""contains(  getProcessProperty("Title") ,'' )""")
for i in range(3):
    query_expression_text_box.send_keys(Keys.LEFT)

