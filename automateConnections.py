from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#login.py should contain your LinkedIn credentials
import login 
import time

# Setup Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/login")

#Login to LinkedIn
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
username.send_keys(login.username)
password.send_keys(login.password)

loginButton = driver.find_element(By.XPATH, "//button[@type='submit']")
loginButton.click()
time.sleep(5)

# Search for profiles by industry keyword
searchBar = driver.find_element(By.CSS_SELECTOR, ".search-global-typeahead__collapsed-search-button")
searchBar.click()
time.sleep(2)
searchInput = driver.find_element(By.CSS_SELECTOR, "input.search-global-typeahead__input")
searchInput.send_keys("Software Engineer")
searchInput.send_keys(Keys.RETURN)
time.sleep(5)

# Navigate to the "People" tab
peopleTab = driver.find_element(By.XPATH, "@type='button' and @aria-label='People'")
peopleTab.click()
time.sleep(3)

# Click on "Connect" for each profile in the search results
profiles = driver.find_elements(By.XPATH, "//button[contains(@class, 'artdeco-button--secondary')]")
