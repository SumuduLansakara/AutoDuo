class HomePage:
    def __init__(self, driver):
        self._driver = driver
        self._href_prefix = "/skill/de"

    def _get_exercise_css(self, exercise_name):
        return "a[href='{}/{}']".format(self._href_prefix, exercise_name)

    def click_exercise(self, exercise_name):
        self._driver.find_element_by_css_selector(self._get_exercise_css(exercise_name)).click()
