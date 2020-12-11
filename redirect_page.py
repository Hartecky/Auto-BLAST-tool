from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from download_seq import *
import time

def redirect_page(driver):
    """
    Waits until page redirection will finish after submitting
    BLAST query. Then it is responsible for sending information
    to download_sequences() function if the page will load with
     avalaible sequences, or to stop running program if there will be no results.

    Parameters:
    driver: selenium.webdriver object used in another functions.
    Defined by function open_blast() in a open_browser.py file
    """

    try:
        WebDriverWait(driver, 90).until(lambda driver: driver.find_element_by_id("tabDescr"))
        driver.maximize_window()
        pass

    except:
        res = WebDriverWait(driver,90).until(lambda driver: driver.find_element_by_id("noResInfo"))
        res_info = res.is_displayed()

        if res_info is True:
            driver.quit()


