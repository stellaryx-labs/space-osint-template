from rich.console import Console
from modules.terminal_tools import *

console = Console()


def generate_option(options):
    for i, item in enumerate(options):
        option = f"[{str(i + 1)}] {item}"
        print_log(option, "blue")

    res = get_input("ENTER INPUT", "blue")

    if not res.isdigit() or int(res) < 1 or int(res) > len(options):
        print_log("INVALID OPTION", "red")
        return None

    print_log("\n")

    return int(res)
