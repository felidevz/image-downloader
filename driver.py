from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
import time


class ChromeDriver:
    def __init__(self, executable_path: str) -> None:
        """Creates a new instance of the ChromeDriver."""
        self._service = ChromeService(executable_path=executable_path)
        self._options = ChromeOptions()
        self._options.add_argument('start-maximized')
        self._driver = Chrome(service=self._service, options=self._options)

    def load_content(self, url: str, scrolls: int) -> str:
        """
        Driver opens given URL address, scrolls down for load images
        and returns HTML page code as `string`.
        If page is loading infinite number of images then use `scrolls` parameter.
        """
        self._driver.get(url)
        time.sleep(2)

        scrolls_count = 0
        old_height = None
        new_height = self._driver.execute_script('return document.body.scrollHeight')
        while old_height != new_height and scrolls_count < scrolls:
            old_height = new_height

            self._driver.execute_script(
                "window.scrollTo({top: %d, left: 0, behavior: 'smooth'});" % old_height
            )
            time.sleep(2)

            new_height = self._driver.execute_script('return document.body.scrollHeight')
            scrolls_count += 1
        return self._driver.page_source
