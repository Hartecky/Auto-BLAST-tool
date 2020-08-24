from selenium import webdriver

def open_blast():
    """Opens Nucleotide Blast web page

    :return driver: web driver for MS Edge browser used in another functions
    """
    page_title = 'Nucleotide BLAST: Search nucleotide databases using a nucleotide query'
    # Path to webdriver API file
    PATH = "C:\\Users\\amplicon\\Desktop\\msedgedriver.exe"
    driver = webdriver.Edge(PATH)

    # Desired website
    driver.get("https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome")

    return(driver)
