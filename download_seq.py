from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

import os
import time

def check_file(file_to_check, path_1):
    """
    Checks if a file 'seqdump.txt' is in a directory,
    otherwise it waits untill it will appear.

    Parameters:
    file_to_check: file name with a path, which we want to
    download. The while loop is waiting for confirmed presence
    of a provided file.

    path_1: Downloads directiory path with a file name to be renamed.

    """

    while not os.path.exists(file_to_check):
        time.sleep(1)

    if os.path.isfile(file_to_check):
        os.rename(file_to_check, path_1)
    else:
        raise ValueError("%s is not a file" % file_to_check)


def download_button(driver):
    """
    Downloads all avalaible sequences returned in a query
    search provided by function submit_values() in a submit_query.py file.
    Runs only if redirect_page() will find avalaible sequences in a blast search.

    Parameters:
    driver: selenium.webdriver object used in another functions.
    Defined by function open_blast() in a open_browser.py file

    """
    # On a redirected page find and choose download option
    download_button = driver.find_element_by_xpath("//*[@id='btnDwnld']")
    download_button.click()

    return

def download_sequences(driver, option, output_name):

    # Destination paths
    file_path_1 = os.path.expanduser("~")+"\\Downloads\\"+str(output_name)
    file_path_2 = os.path.expanduser("~")+"\\Downloads\\seqdump.txt"
    download_folder = os.path.expanduser("~")+"\\Downloads"

    if output_name is None:
        file_path_1 = os.path.expanduser("~")+"\\Downloads\\"+"output.txt"
    else:
        pass


    if str(option).lower() == 'aligned':

        download_all = driver.find_element_by_xpath("//*[@id='dwFSTAl']")
        download_all.click()

        # Function call to check downloading file existing
        check_file(file_path_2, file_path_1)

    elif str(option).lower() == 'complete':

        download_aligned = driver.find_element_by_xpath("//*[@id='dwFST']")
        download_aligned.click()

        # Function call to check downloading file existing
        check_file(file_path_2, file_path_1)

    else:

        download_aligned = driver.find_element_by_xpath("//*[@id='dwFSTAl']")
        download_aligned.click()

        # Function call to check downloading file existing
        check_file(file_path_2, file_path_1)

    return
