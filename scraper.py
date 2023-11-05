import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def compare_texts(t1, t2, filename):
	t1 = t1.split("\n")
	t2 = t2.split("\n")
	if len(t1) != len(t2):
		print(filename + ': Different number of English and German textfields')
		return
	same_file = open(filename + "_same.txt", "w", encoding="utf-8")
	diff_file = open(filename + "_diff.txt", "w", encoding="utf-8")
	for i in range(len(t1)):
		if t1[i] == t2[i]:
			same_file.write(t1[i] + "\n")
		else:
			diff_file.write(t1[i] + " - " + t2[i] + "\n")

def select_ger(driver):
	lan_select = driver.find_element(By.XPATH, "//app-navbar//select")
	lan_select.click()
	lan_select.send_keys(Keys.DOWN)
	lan_select.send_keys(Keys.ENTER)
	time.sleep(2)

def select_en(driver):
	lan_select = driver.find_element(By.XPATH, "//app-navbar//select")
	lan_select.click()
	lan_select.send_keys(Keys.UP)
	lan_select.send_keys(Keys.ENTER)
	time.sleep(2)

def scrape_page(driver, url, filename):
	driver.get(url)

	time.sleep(2)

	en_text = driver.find_element(By.XPATH, "/html/body").text
	select_ger(driver)
	ger_text = driver.find_element(By.XPATH, "/html/body").text
	select_en(driver)

	compare_texts(en_text, ger_text, filename)

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()

scrape_page(driver, 'https://petropolis.progmasters.hu/', 'home')
scrape_page(driver, 'https://petropolis.progmasters.hu/posts', 'posts')
scrape_page(driver, 'https://petropolis.progmasters.hu/postsCategory/DOGS-Dogs', 'postsCategory')
scrape_page(driver, 'https://petropolis.progmasters.hu/registration-needed', 'registration-needed')
scrape_page(driver, 'https://petropolis.progmasters.hu/donation', 'donation')
scrape_page(driver, 'https://petropolis.progmasters.hu/login', 'login')
scrape_page(driver, 'https://petropolis.progmasters.hu/register', 'register')

driver.quit()


