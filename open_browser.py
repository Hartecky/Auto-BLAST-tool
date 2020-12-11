from selenium import webdriver

"""
First function creates the instance of MS Edge Webdriver
and keeps it in a 'driver' variable.

Second function opens website provided in webpage
variable inside function.

Parameters:
driver: selenium.webdriver object used in another functionse.
"""

def get_driver():

    driver = webdriver.Edge(executable_path=r'C:/msedgedriver.exe')
    return(driver)

def open_website(driver):

    # Desired website
    webpage = 'https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome'

    driver.get(webpage)


