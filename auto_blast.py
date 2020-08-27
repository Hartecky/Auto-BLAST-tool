import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from open_browser import open_blast
from submit_query import fill_values, refresh_page, submit_query
from redirect_page import redirect_page

"""
Main function containing the all others
"""

def auto_blast(seq_entry, org_entry):

    web_browser = open_blast()
    submit_query(web_browser, seq_entry, org_entry)
    redirect_page(web_browser)
