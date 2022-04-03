import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        user = "bk"
        pwd = "123"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://bk07.pythonanywhere.com/admin")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div/form/div[1]/input").send_keys(user)
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div/form/div[2]/input[1]").send_keys(pwd)
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div/form/div[3]/input").click()
        time.sleep(3)
        driver.get("http://bk07.pythonanywhere.com/catalog/")
        time.sleep(3)
        # Click on Books
        BookList = driver.find_element_by_xpath(
            "/html/body/div/div/div[1]/ul/li[5]/a").click()
        time.sleep(3)

        try:
            elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/h1")
            text = elem.text
            time.sleep(2)
            assert text == "Book List"

        except NoSuchElementException:
            self.fail("Logout Failed - user may not exist")
            assert False
        time.sleep(3)


def tearDown(self):
    self.driver.close()


if _name_ == "_main_":
    unittest.main()