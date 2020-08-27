from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from download_seq import download_sequences, check_file
import time

def redirect_page(driver):
    """
    Waits until page redirection will finish. Then it responsible for sending information to download_sequences() function if the page will load with avalaible sequences, or to stop running program if there will be no results.

    :param driver: webdriver defined by function open_blast() in a open_browser.py file
    """

    try:
        WebDriverWait(driver, 90).until(lambda driver: driver.find_element_by_id("tabDescr"))
        download_sequences(driver)
        driver.quit()
    except:
        res = WebDriverWait(driver,60).until(lambda driver: driver.find_element_by_id("noResInfo"))
        res_info = res.is_displayed()

        if res_info is True:
            driver.quit()
