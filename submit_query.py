from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

import time
import os

def make_action(driver):
    """
    Creates a selenium ActionChains object to
    automate low level interactions on loaded website

    Parameters:
    driver: selenium.webdriver object used in another functions.
    Defined by function open_blast() in a open_browser.py file
    """
    action = ActionChains(driver)

    return action

def paste_sequence(driver, query):
    """
    Fills defined and located textarea with sequence (string),
    provided by user.

    Parameters:
    driver: selenium.webdriver object used in another functions.
    Defined by function open_blast() in a open_browser.py file.

    query: sequence query provided by user.
    """

    search_sequence = driver.find_element_by_name("QUERY")
    search_sequence.send_keys(query)
    search_sequence.send_keys(Keys.RETURN)

    return

def paste_organism(driver, action, organism):
    """
    Fills defined and located textarea with organism name (string),
    provided by user. Next, it waits for hints, and choses the first one.

    Parameters:
    driver: selenium.webdriver object used in another functions.
    Defined by function open_blast() in a open_browser.py file.

    action: selenium.actionchains object which allows to interact
    with a browser

    organism: organism name provided by user.
    """

    search_organism = driver.find_element_by_id("qorganism")
    search_organism.send_keys(organism)

    list_elem = driver.find_element_by_xpath("//input[@name='NUM_ORG']")

    time.sleep(1)

    action.send_keys(Keys.ARROW_DOWN).perform()
    action.send_keys(Keys.ENTER).perform()

    return

"""
Functions below are responsible for:
    - checkbox select to show result in a new window
    - opening more algorithm parameters
    - changing max target sequences to 5000
    - submitting BLAST button
    - Quit

Parameters:
driver: selenium.webdriver object used in another functions.
Defined by function open_blast() in a open_browser.py file.

action: selenium.actionchains object which allows to interact
with a browser
"""

def open_options(driver, action):

    algo_param = driver.find_element_by_id("algPar")
    algo_param.click()

def select_options(driver, action):

    select_numbers = Select(driver.find_element_by_id("NUM_SEQ"))
    select_numbers.select_by_value("1000")

def click_button(driver):

    blast_btn = driver.find_element_by_class_name("blastbutton")
    blast_btn.click()
