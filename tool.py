from rich.console import Console
from modules.option import *
from modules.menu import *
from modules.table import *
from modules.api import *
from modules.terminal_tools import *

console = Console()

# TODO: Enter the API for your tool below:
API_URL = "https://api.spacexdata.com/v4/starlink/"


def main():
    print_menu()
    # TODO: change the input description to the data your tool needs
    input = get_input("Enter Starlink Satellite Name", "blue")
    print("\n")  # prints an empty line for spacing

    data = get_api_data(API_URL)
    found = False

    table_title = f"Information for {input} 🛰️"

    # TODO: change the API data handling logic below for your tool
    if data:
        for entry in data:
            if entry["spaceTrack"]["OBJECT_NAME"] == input:
                print_data(table_title, entry["spaceTrack"])
                found = True

    if found == False:
        print_error("Information Not Found!")

    generate_options()


# TODO: make your own options
def generate_options():
    options = [
        "Run Again",
        "Exit Tool"
    ]

    option = generate_option(options)

    if option == 1:
        main()  # run the tool again
    else:
        return  # exit the tool


if __name__ == "__main__":
    main()
