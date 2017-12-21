import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.wikipedia.org/")
        self.assertIn("Wikipedia", driver.title)
        elem = driver.find_element_by_id("js-link-box-en")
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_id("searchInput")
        elem.send_keys("USA")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
