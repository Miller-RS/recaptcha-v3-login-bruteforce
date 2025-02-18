const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({ headless: true });
    const page = await browser.newPage();

    await page.goto('YOUR_TARGET_URL'); // Replace with the actual page you want to test

    // Inject the reCAPTCHA script
    await page.addScriptTag({
        url: 'https://www.google.com/recaptcha/api.js?render=YOUR_RECAPTCHA_SITE_KEY'
    });

    // Execute the reCAPTCHA code
    await page.evaluate(() => {
        return new Promise((resolve) => {
            grecaptcha.ready(function () {
                grecaptcha.execute('YOUR_RECAPTCHA_SITE_KEY', { action: 'contact' }).then(function (token) {
                    var recaptchaResponse = document.getElementsByClassName('recaptchaResponse');
                    for (var i = 0; i < recaptchaResponse.length; i++) {
                        recaptchaResponse[i].value = token;
                    }
                    resolve(token);
                });
            });
        });
    }).then((token) => {
        console.log('ReCAPTCHA token:', token);
    });

    await browser.close();
})();
