import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(executable_path=r"D:\Python&Selenium\selenium\chromedriver.exe")
    driver.get("https://demo.oxwall.com/")
    yield driver
    driver.quit()

@pytest.fixture()
def wait():
    return WebDriverWait(driver=driver, timeout=10)

@pytest.fixture()
def login(driver):
    sing_in_btn = driver.find_element(By.XPATH, "//span[.='Sign In']")
    sing_in_btn.click()

    name_field = driver.find_element(By.NAME, "identity")
    name_field.clear()
    name_field.send_keys("demo")

    pass_field = driver.find_element(By.NAME, "password")
    pass_field.clear()
    pass_field.send_keys("demo")

    submit_btn = driver.find_element(By.NAME, "submit")
    submit_btn.click()
