from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)
driver.maximize_window()

def click(xpath):
   # """ Waits for an element to be clickable and clicks it."""
    wait.until(ec.element_to_be_clickable((By.XPATH, xpath))).click()

# Navigate to the login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Login
wait.until(ec.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Click "Admin" in the sidebar menu
admin_module = wait.until(ec.element_to_be_clickable((By.XPATH, "//span[text()='Admin']")))
admin_module.click()

# Wait for Admin page to load
wait.until(ec.presence_of_element_located((By.XPATH, "//h6[text()='Admin']")))
print("✅ Successfully navigated to the Admin page.")

# Menu Navigation and Actions:
# User Management
click("//span[text()='User Management ']")
click("//a[text()='Users']")

# Job
click("//span[text()='Job ']")
click("//a[text()='Job Titles']")
click("//span[text()='Job ']")
click("//a[text()='Pay Grades']")
click("//span[text()='Job ']")
click("//a[text()='Employment Status']")
click("//span[text()='Job ']")
click("//a[text()='Job Categories']")
click("//span[text()='Job ']")
click("//a[text()='Work Shifts']")

# Organization
click("//span[text()='Organization ']")
click("//a[text()='General Information']")
click("//span[text()='Organization ']")
click("//a[text()='Locations']")
click("//span[text()='Organization ']")
click("//a[text()='Structure']")

# Qualification
click("//span[text()='Qualifications ']")
click("//a[text()='Skills']")
click("//span[text()='Qualifications ']")
click("//a[text()='Education']")
click("//span[text()='Qualifications ']")
click("//a[text()='Licenses']")
click("//span[text()='Qualifications ']")
click("//a[text()='Languages']")
click("//span[text()='Qualifications ']")
click("//a[text()='Memberships']")

# Nationalities
click("//a[text()='Nationalities']")

# Corporate Branding
click("//a[text()='Corporate Branding']")

# Configuration
click("//span[text()='Configuration ']")
click("//a[text()='Email Configuration']")
click("//span[text()='Configuration ']")
click("//a[text()='Email Subscriptions']")
click("//span[text()='Configuration ']")
click("//a[text()='Localization']")
click("//span[text()='Configuration ']")
click("//a[text()='Language Packages']")
click("//span[text()='Configuration ']")
click("//a[text()='Modules']")
click("//span[text()='Configuration ']")
click("//a[text()='Social Media Authentication']")
click("//span[text()='Configuration ']")
click("//a[text()='Register OAuth Client']")
click("//span[text()='Configuration ']")
click("//a[text()='LDAP Configuration']")

# Logout
click("//span[@class='oxd-userdropdown-tab']")
click("//a[text()='Logout']")
driver.quit()
