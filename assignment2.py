from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup Webdriver
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)

# Login
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

# Click "Admin" in the sidebar menu
driver.find_element(By.XPATH, "//span[text()='Admin']").click()
time.sleep(5)
print("✅ Successfully navigated to the Admin page.")

# Menu Navigation and Actions:
# User Management
driver.find_element(By.XPATH,"//span[text()='User Management ']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Users']").click()
time.sleep(5)

# Job
driver.find_element(By.XPATH,"//span[text()='Job ']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Job Titles']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Job ']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Pay Grades']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Job ']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Employment Status']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Job ']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Job Categories']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Job ']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Work Shifts']").click()
time.sleep(5)

# Organization
driver.find_element(By.XPATH,"//span[text()='Organization ']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='General Information']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Organization ']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Locations']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Organization ']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Structure']").click()
time.sleep(5)

# Qualification
driver.find_element(By.XPATH,"//span[text()='Qualifications ']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Skills']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Qualifications ']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Education']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Qualifications ']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Licenses']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Qualifications ']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Languages']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Qualifications ']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Memberships']").click()
time.sleep(5)

# Nationalities
driver.find_element(By.XPATH,"//a[text()='Nationalities']").click()
time.sleep(5)

# Corporate Branding
driver.find_element(By.XPATH,"//a[text()='Corporate Branding']").click()
time.sleep(5)

# Configuration
driver.find_element(By.XPATH,"//span[text()='Configuration ']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Email Configuration']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Configuration ']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Email Subscriptions']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Configuration ']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Localization']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Configuration ']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Language Packages']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Configuration ']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Modules']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Configuration ']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Social Media Authentication']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Configuration ']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Register OAuth Client']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Configuration ']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='LDAP Configuration']").click()
time.sleep(5)

# Logout
driver.find_element(By.XPATH,"//span[@class='oxd-userdropdown-tab']").click()
driver.find_element(By.XPATH,"//a[text()='Logout']").click()
driver.quit()
