from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the download directory
download_directory = "C:\\Users\\Cody9\\development\\sale_fetch"

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory": download_directory}
chrome_options.add_experimental_option("prefs", prefs)

# Set up Chrome WebDriver with options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the login page
driver.get('http://172.16.0.14/2021A/login.php')

# Fill in login credentials and submit the form
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')

username.send_keys('cody96bear@yahoo.com')
password.send_keys('Codyray@HP2023')

password.send_keys(Keys.RETURN)

# Navigate to "Sales" dropdown and select "Change Sales"
sales_dropdown = driver.find_element(By.XPATH, "//a[@id='nav-dropdown-3' and contains(text(), 'Sales')]")
sales_dropdown.click()

first_dropdown_option = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='dropdown-menu']/a[1]"))
)
# Click the "Change Sales" option
change_sales_option.click()

# Wait for the "Select Sale" button to appear
select_sale_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-success badge' and contains(text(), 'Select Sale')]"))
)

# Click the "Select Sale" button
select_sale_button.click()


# Navigate to "Output" dropdown and select "Reports"
output_dropdown = driver.find_element(By.XPATH, "//a[@id='nav-dropdown-3' and contains(text(), 'Output')]")
output_dropdown.click()

# Wait
first_output_option = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='dropdown-menu']/a[1]"))
)

# Click the "Reports" option
reports_option = driver.find_element(By.XPATH, "//a[@href='?page=reports' and contains(text(), 'Reports')]")
reports_option.click()

# Wait
element_on_reports_page = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='your-element-class-on-reports-page']"))
)

# Click the "Excel for QH Track" button
excel_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary button125 badge' and contains(text(), 'Excel for QH Track')]")
excel_button.click()


# Now, wait for the page to update before interacting with the next element
element_on_excel_page = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='your-element-class-on-excel-page']"))
)


# close the browser when done
driver.quit()
