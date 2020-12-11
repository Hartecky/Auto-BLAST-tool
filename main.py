from open_browser import *
from submit_query import *
from download_seq import *
from redirect_page import *
from arguments import *




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
    select_options(driver, action)
    click_button(driver)

    # Redirecting page and downloading seq
    proceed_submit(driver)
    download_sequences(driver)
    driver.quit()

if __name__ == '__main__':

    # Generate arguments
    args = parse_arguments()
    main()

