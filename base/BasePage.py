import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import logging

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    def get_element_text(self, locator):
        return self.get_element(locator).text

    def get_elements(self, locator):
        return self.driver.find_elements(By.XPATH, locator)

    def click(self, locator):
        self.get_element(locator).click()

    def get_elements_text(self, locator):
        return list(map(self.get_element_text(), self.get_elements(locator)))

    def safe_click(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, locator))).click()

    def getActions(self):
        action = ActionChains(self.driver)
        return action

    def move_to_element(self, locator):
        ele = self.get_element(locator)
        self.getActions().move_to_element(ele).perform()

    def double_click(self, locator):
        ele = self.get_element(locator)
        self.getActions().double_click(ele)

    def enter_text(self, locator, value):
        self.get_element(locator).send_keys(value)

    def get_page_title(self):
        return self.driver.title

    def scroll_into_view(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.get_element(locator))

    def actions_click(self, locator):
        self.getActions().move_to_element(self.get_element(locator)).click().perform()

    def is_element_visible(self, locator):
        return self.get_element(locator).is_displayed()

    def wait_for_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located((By.XPATH, locator)))

    def wait_for_element_clickable(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, locator)))

    def clear(self,locator):
        self.wait_for_element_clickable(locator)
        ele = self.get_element(locator)
        time.sleep(2)
        self.getActions().move_to_element(ele).double_click(ele).send_keys(Keys.DELETE).perform()

    def log_info(self, str):
        logging.basicConfig(level=logging.DEBUG)
        logging.debug(str)

    def click_element_using_js(self,locator):
        self.driver.execute_script("arguments[0].click();", self.get_element(locator))