from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from check_file import check_file
import os
import time

def download_sequences(driver):
    """Download all avalaible sequences returned in a query search provided by function submit_values() in a submit_query.py file

    :param driver: webdriver defined by function open_blast() in a open_browser.py file
    """

    # Prepare space and remove unnecessary files
    if os.path.isfile('C:\\Users\\amplicon\\Downloads\\downloaded_sequences.txt'):
        os.remove('C:\\Users\\amplicon\\Downloads\\downloaded_sequences.txt')
    else:
        pass

    # On a redirected page find and choose download option
    download_button = driver.find_element_by_id("btnDwnld")
    download_button.click()

    download_fasta = driver.find_element_by_id("dwFSTAl")
    download_fasta.click()

    make_check = check_file()

    # Function call to check downloading file existing
    if make_check is True:
        os.rename('C:\\Users\\amplicon\\Downloads\\seqdump.txt', \
            'C:\\Users\\amplicon\\Downloads\\downloaded_sequences.txt')
    else:
        driver.quit()
        return(False)
