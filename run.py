# from core import parse_feature_file
#
# if __name__ == '__main__':
#     file_path = 'example.feat'
#     parsed_lines = parse_feature_file(file_path)

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# import pytest
#
# @pytest.fixture(scope="function")
# def setup_driver():
#     # Initialize Chrome WebDriver
#     driver = webdriver.Chrome(executable_path="path/to/chromedriver")
#     yield driver  # yield the setup (like return but for fixtures)
#     driver.quit()  # teardown: this runs after the test function finishes
#
# def test_search_in_google(setup_driver):
#     # Navigate to Google's homepage
#     setup_driver.get("https://www.google.com")
#
#     # Find the search box element and enter "Selenium"
#     search_box = setup_driver.find_element_by_name("q")
#     search_box.send_keys("Selenium")
#     search_box.send_keys(Keys.RETURN)
#
#     # Wait for search results to load
#     time.sleep(2)
#
#     # Verify if "Selenium" exists in the first search result
#     first_result = setup_driver.find_element_by_css_selector(".tF2Cxc").text
#     assert "Selenium" in first_result, f"Expected 'Selenium' to be in first result, but got {first_result}"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
print("Page title: ", driver.title)
print("Current URL: ", driver.current_url)
search_box = driver.find_element(By.ID, "APjFqb")
search_box.send_keys("Selenium")
search_box.send_keys(Keys.RETURN)
time.sleep(2)
driver.quit()