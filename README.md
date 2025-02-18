# recaptcha-v3-login-bruteforce
Python and Node.js scripts designed for ethical brute-force password testing on web login forms protected by reCAPTCHA v3. This project demonstrates techniques for automated credential testing and reCAPTCHA circumvention for security analysis on authorized accounts. Use responsibly and only for authorized security assessments.

This project consists of two scripts:

*   `main.py`: A Python script using Selenium and requests to attempt login with a list of passwords, bypassing reCAPTCHA using a Node.js script.
*   `nodeToRecaptcha.js`: A Node.js script using Puppeteer to generate a reCAPTCHA token.

## Prerequisites

Before running these scripts, ensure you have the following installed:

*   **Python 3.x**
    *   Libraries: `selenium`, `requests`, `beautifulsoup4`
        ```bash
        pip install selenium requests beautifulsoup4
        ```
    *   ChromeDriver: Download the appropriate ChromeDriver for your Chrome version and operating system from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads). Place the `chromedriver` executable in a known location or in your system's PATH.
*   **Node.js**
    *   Libraries: `puppeteer`
        ```bash
        npm install puppeteer
        ```

## Setup

1.  **ChromeDriver Path:** In `main.py`, update the `service = Service(...)` line with the correct path to your ChromeDriver executable.

    ```python
    service = Service('/path/to/your/chromedriver') # Replace '/path/to/your/chromedriver'
    ```

2.  **Password List:** Create a text file named `value1.txt` (or change the filename in `main.py`) in the same directory as `main.py`.  Each line in this file should contain a password you want to try.

    ```
    password_attempt_1
    password_attempt_2
    password_attempt_3
    ...
    ```

3.  **Website URL:** In both `main.py` and `nodeToRecaptcha.js`, replace `https://www.academico.uni.edu.pe/alumno/entra` with the URL of the login page you want to target.

    **`main.py`:**
    ```python
    driver.get('YOUR_TARGET_URL') # Replace 'YOUR_TARGET_URL'
    response = session.get("YOUR_TARGET_URL") # Replace 'YOUR_TARGET_URL'
    response = session.post("YOUR_TARGET_URL", data=form_data) # Replace 'YOUR_TARGET_URL'
    ```

    **`nodeToRecaptcha.js`:**
    ```javascript
    await page.goto('YOUR_TARGET_URL'); // Replace 'YOUR_TARGET_URL'
    ```

4.  **reCAPTCHA Site Key:** In `nodeToRecaptcha.js`, replace `'6LfnkXYiAAAAAO2v5wKACcHdcZyJjtopTvIHJM1D'` with the actual reCAPTCHA site key from the target website's login page. Inspect the HTML source of the login page to find the `sitekey` within the reCAPTCHA widget's parameters.

    ```javascript
    grecaptcha.ready(function () {
        grecaptcha.execute('YOUR_RECAPTCHA_SITE_KEY', { action: 'contact' }).then(function (token) { // Replace 'YOUR_RECAPTCHA_SITE_KEY'
            // ...
        });
    });
    ```

5.  **Form Input Names and Values:**
    *   Inspect the HTML source of the login page to identify the names of the input fields for:
        *   Username/Code (`codUni` in the example)
        *   Password (`clave` in the example)
        *   CSRF Token (`_token` in the example)
        *   reCAPTCHA Response (`recaptcha_response` in the example - this is usually hidden and populated by JavaScript)
        *   Form submission type (`tipo` in the example)

    *   Update the `form_data` dictionary in `main.py` with the correct input names and any static values (like `tipo: 'acceso'`).

    ```python
    form_data = {
        'tipo': 'YOUR_TIPO_INPUT_NAME', # Replace 'YOUR_TIPO_INPUT_NAME' if different
        '_token': token_value,
        'codUni': 'YOUR_USERNAME', # Replace 'YOUR_USERNAME' with your actual username input field name if different
        'clave': password,
        'recaptcha_response': recaptcha_value
    }
    ```
## Running the Scripts

1.  **Run `main.py`:** Execute the Python script from your terminal.

    ```bash
    python main.py
    ```
