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

from appJar import gui

import time
import os

#input_query = str(input("Please submit your sequence: \n"))
#input_organism = str(input("\nPlease submit your organism name: \n"))


def search_blast():

    #if name == "Submit Auto-Blast":
    seq = app.getEntry("Sequence")
    org = app.getEntry("Organism")

    web_browser = open_blast()
    submit_values(web_browser, seq, org)
    redirect_page(web_browser)
    download_sequences(web_browser)
    web_browser.close()



def main():

    def press(name):
        if name == "Cancel":
            app.stop()
        elif name == "Clear":
            app.clearEntry("Sequence")
            app.clearEntry("Organism")
            app.setFocus("Sequence")

    def search_blast():

        #if name == "Submit Auto-Blast":
        seq = app.getEntry("Sequence")
        org = app.getEntry("Organism")

        web_browser = open_blast()
        submit_values(web_browser, seq, org)
        redirect_page(web_browser)
        download_sequences(web_browser)
        web_browser.close()

    app = gui("Auto-Blast Tool", "640x480")
    app.setBg("green")
    app.setFont(20)
    app.setResizable(False)
    app.addLabel("title", "Auto-Blast Tool")

    app.addLabelEntry("Sequence")
    app.addLabelEntry("Organism")

    app.addButton("Submit Auto-Blast", search_blast)
    app.addButtons(["Clear", "Cancel"], press)
    app.go()


if __name__ == '__main__':
    main()

'''
Example sequence for arabidopsis thaliana PetC Gene

GCCTTATCTGCTTCTCTCTCTCCAGTGGTCTCAAATCTCTCTGTGTGATCCCACTTGTCATCCTCCTCCACAACATAAAGCTTGAGACCATAACCCTTTAGCGTTTTCGGCTAAAGCTTTCGCTGACTACTACAACAATGGCGTCCTCATCCCTTTCCCCTGCTACTCAGGTTCACTCTTGATCGTTCGAATCGAAACAATCGGGTCTCTTCGTATAGGAATTTGGGTTTTTGAAAGTTTGGTTTTTTTTTTTGGTGGCAGCTTGGTTCTAGCAGAAGTGCTTTGATGGCGATGTCAAGTGGGTTGTTTGTGAAGCCAACGAAGATGAATCATCAAATGGTTAGAAAAGAGAAGATTGGATTGAGAATTTCTTGTCAAGCGTCGAGTATTCCAGCAGACAGAGTTCCAGATATGGAAAAGAGGAAGACTTTGAATCTTCTTCTTCTTGGGGCTCTTTCTCTACCTACTGGCTACATGCTTGTCCCTTACGCTACCTTCTTTGTTCCTCCTGGAACCGGAGGTGGAGGTGGTGGTACTCCAGCCAAGGATGCCCTTGGAAACGATGTAGTTGCAGCGGAATGGCTTAAGACTCATGGTCCCGGTGACCGAACCTTGACCCAAGGATTAAAGGGAGATCCGACTTACCTAGTTGTAGAGAACGACAAGACTCTAGCGACATACGGTATCAACGCAGTGTGCACTCATCTTGGATGTGTTGTGCCATGGAACAAAGCTGAGAACAAGTTTCTATGTCCTTGCCATGGATCCCAATACAACGCCCAAGGAAGAGTCGTTAGAGGTCCAGCCCCATTGTCGCTAGCGTTGGCTCACGCGGATATAGATGAAGCTGGGAAGGTTCTTTTTGTTCCATGGGTGGAAACTGACTTCAGGACTGGTGATGCTCCATGGTGGTCTTAAGACTCTTCAACAAGAAAAAGAGAAAGATTTGGTCTTTTTGTGTAAGACTTGTTTGAATGTTCTTATAATGTATAAGCTACATTTCATCGCAATTACTCTGTGAATTCTTGCCTCTTATATGAAATATTATGTTCATTCACTTCCCA
'''
