from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from custom_wait_condition import present_posts_displayed
from selenium.webdriver.support.wait import WebDriverWait
import time


def test_create_post(driver, login):

    wait = WebDriverWait(driver=driver, timeout=10)
    add_comment_field = wait.until(EC.presence_of_element_located(locator=(By.NAME, "status")))

    posts = driver.find_elements(By.CSS_SELECTOR, ".ow_newsfeed_content.ow_smallmargin")
    number_old_posts = len(posts)
    print(number_old_posts)

    add_comment_field.send_keys("test text added by Tania!!!")

    save_btn = driver.find_element(By.NAME, "save")
    save_btn.click()

    wait.until(present_posts_displayed(locator=(By.CSS_SELECTOR, ".ow_newsfeed_content.ow_smallmargin"),
                                       number=number_old_posts+1))

    assert driver.find_element(By.CSS_SELECTOR, ".ow_newsfeed_content.ow_smallmargin").text == "test text added by Tania!!!"