from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
#from selenium.webdriver.firefox.options import Options

option = webdriver.ChromeOptions()
#options.headless = True
wait=120
option.add_argument('--disable-blink-features=AutomationControlled')
with webdriver.Chrome('chromedriver', options=option) as driver:
    # Initial load and "Välkommen..."
    driver.get("https://bokapass.nemoq.se/Booking/Booking/Index/stockholm")
    time.sleep(10)
    #WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.NAME, "StartNextButton")))
    #driver.find_element(By.NAME, "StartNextButton").click()

    # Accept GDPR
    #WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.ID, "AcceptInformationStorage")))
    #driver.find_element(By.ID, "AcceptInformationStorage").click()
    #driver.find_element(By.NAME, "Next").click()

    # "Bor du i Sverige?"
    #WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.ID, "ServiceCategoryCustomers_0__ServiceCategoryId")))
    ## "Ja, jag bor i Sverige"
    #driver.find_element(By.ID, "ServiceCategoryCustomers_0__ServiceCategoryId").click()
    #driver.find_element(By.NAME, "Next").click()

    # Check first available timeslot
    while(1):
        driver.get("https://bokapass.nemoq.se/Booking/Booking/Index/stockholm")
        WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.ID, "SectionId")))
        dropdown = driver.find_element(By.ID, "SectionId")
        ## ...in Sthlm city
        #dropdown.find_element(By.XPATH, "//option[. = 'Sthlm City']").click()
        driver.find_element(By.NAME, "TimeSearchFirstAvailableButton").click()

        # Finally check when first available time is
        WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.timetable")))
        tbl = driver.find_element(By.ID, "datepicker").get_attribute('value')
        print(tbl)

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(20)