class LoginPage:
    def __init__(self, driver):
        self._driver = driver
        self._css_signin_btn = 'sign-in-btn'
        self._css_user_field = 'top_login'
        self._css_pass_field = 'top_password'
        self._css_login_btn = 'login-button'

    def click_signin(self):
        self._driver.find_element_by_id(self._css_signin_btn).click()

    def click_login(self):
        self._driver.find_element_by_id(self._css_login_btn).click()

    def type_username(self, username):
        self._driver.find_element_by_id(self._css_user_field).send_keys(username)

    def type_password(self, password):
        self._driver.find_element_by_id(self._css_pass_field).send_keys(password)
