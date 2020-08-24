from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from open_browser import open_blast
from submit_query import submit_values
from redirect_page import redirect_page
from check_file import check_file
from download_seq import download_sequences

import time
import os

input_query = str(input("Please submit your sequence: \n"))
input_organism = str(input("\nPlease submit your organism name: \n"))

def main():
    web_browser = open_blast()
    submit_values(web_browser, input_query, input_organism)
    redirect_page(web_browser)
    download_sequences(web_browser)


if __name__ == '__main__':
    main()
