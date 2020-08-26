from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

import time

def redirect_page(driver):
    """It waits for the database search to finish, it is responsible for the information about the redirection to the result page

    :param driver: webdriver defined by function open_blast() in a open_browser.py file
    """
    # Wait until page redirect is complete
    try:
        WebDriverWait(driver, 90).until(lambda driver: driver.find_element_by_id("mainCont"))
    except:
        print("Time's up")
        driver.close()

    return(driver)
