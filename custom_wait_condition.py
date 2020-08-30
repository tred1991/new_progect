from selenium.webdriver.common.by import By
from selenium import webdriver

dr = webdriver.Chrome(executable_path=r"D:\Python&Selenium\selenium\chromedriver.exe")

# def present_posts_displayed(driver):
#     posts = dr.find_elements(By.CSS_SELECTOR, ".ow_newsfeed_content ow_smallmargin")
#     number_old_posts = len(posts)
#     if len(posts) == number_old_posts + 1:
#         return posts
#     else:
#         return False


class present_posts_displayed:

    def __init__(self, locator, number):
        self.locator = locator
        self.number = number

    def __call__(self, driver):
        posts = driver.find_elements(*self.locator)
        if len(posts) == self.number:
            return posts
        else:
            return False