from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

import time
import os

def fill_values(driver, query, organism):
    """ Sending desired queries into textboxes, matching algorithm for 10000 sequences search and submitting blast algorithn

    :param driver: webdriver defined by function open_blast() in a open_browser.py file
    :param query: input provided by user with a DNA sequence
    :param organism: input provided by user with an organism name
    """

    #Enable actions
    action = ActionChains(driver)

    # Find and import Query
    search_sequence = driver.find_element_by_name("QUERY")
    search_sequence.send_keys(query)
    search_sequence.send_keys(Keys.RETURN)

    # Find and import organism
    search = driver.find_element_by_id("qorganism")
    search.send_keys(organism)
    element = driver.find_element_by_xpath("//input[@name='NUM_ORG']")

    time.sleep(1)

    action.send_keys(Keys.ARROW_DOWN).perform()
    action.send_keys(Keys.ENTER).perform()

    # Find and expand blast algorithm options
    algo_param = driver.find_element_by_id("algPar")
    algo_param.click()

    # Find and choose searching target
    select = Select(driver.find_element_by_id("NUM_SEQ"))
    select.select_by_value("5000")

    # Run
    blast = driver.find_element_by_class_name("blastbutton")
    blast.click()

    return(driver)


def refresh_page(driver):
    """ There will be here error with which this function will handle with"""
    driver.refresh()


def submit_query(driver, query, organism):
    """Function made for handling BLAST main web-page in case of some CGI Text Error """

    try:
        fill_values(driver, query, organism)

    except:
        refresh_page()
        fill_values(driver, query, organism)
