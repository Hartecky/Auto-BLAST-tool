from open_browser import *
from submit_query import *
from download_seq import *
from redirect_page import *
from arguments import *
import warnings

def main():

    # Open browser functions
    driver = get_driver()
    action = make_action(driver)
    open_website(driver)

    # Submit query main functions
    paste_sequence(driver, args.query)
    paste_organism(driver, action, args.organism)

    # Check if -e flag is True
    exclude_organism(driver, args.exclude)

    # Submit additional options
    open_options(driver, action)
    select_options(driver, action, args.num_seq)
    click_button(driver)

    # Redirecting page and downloading seq
    proceed_submit(driver)
    download_button(driver)

    download_sequences(driver, args.align, args.output)
    driver.quit()

if __name__ == '__main__':

    warnings.filterwarnings("ignore")

    args = parse_arguments()
    main()

