import time
import os

def check_file():
    """Checks if a file 'seqdump.txt' is in a directory, otherwise it waits untill it will appear
    """
    while not os.path.exists('C:\\Users\\amplicon\\Downloads\\seqdump.txt'):
        time.sleep(1)

    if os.path.isfile('C:\\Users\\amplicon\\Downloads\\seqdump.txt'):
        return(True)
    else:
        raise ValueError("%s is not a file" % 'C:\\Users\\amplicon\\Downloads\\seqdump.txt')
