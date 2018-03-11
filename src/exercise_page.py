class ExercisePage:
    def __init__(self, driver, exercise_name):
        self._driver = driver
        self._href_prefix = "/skill/de/{}".format(exercise_name)

    def _get_lesson_css(self, lesson_name):
        return "a[href='{}/{}']".format(self._href_prefix, lesson_name)

    def click_lesson(self, lesson_name):
        self._driver.find_element_by_css_selector(self._get_lesson_css(lesson_name)).click()
