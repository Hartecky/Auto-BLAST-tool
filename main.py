from open_browser import *
from submit_query import *
from download_seq import *
from redirect_page import *
from arguments import *

def main():
    # Generate arguments
    args = parse_arguments()

    # Open browser functions
    driver = get_driver()
    open_website(driver)

    # Submit query functions
    action = make_action(driver)
    paste_sequence(driver, args.query)
    paste_organism(driver, action, args.organism)
    open_options(driver, action)
    select_options(driver, action)
    click_button(driver)

    # Redirecting page and downloading seq
    redirect_page(driver)

main()


