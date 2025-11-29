class LoginLocators:
    CLICK_LOGIN_BTN = "//button[contains(., 'Click here to Login')]"

    GOOGLE_EMAIL_FIELD = "//input[@type='email' or @id='identifierId']"
    GOOGLE_EMAIL_NEXT = "//button[.//span[text()='Next']]"

    GOOGLE_PASSWORD_FIELD = "//input[@type='password' or @name='Passwd']"
    GOOGLE_PASSWORD_NEXT = "//button[@id='passwordNext']//button | //button[.//span[text()='Next']]"

    ACCOUNT_SELECT = "//div[contains(text(), '{email}')]"

    CONSENT_BUTTONS = [
        "//button[contains(., 'Continue')]",
        "//button[contains(., 'Allow')]",
        "//button[contains(., 'Approve')]"
    ]
