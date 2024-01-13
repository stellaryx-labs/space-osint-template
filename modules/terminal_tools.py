from rich.console import Console

console = Console()


def print_error(log):
    console.print(f"[bold red] ERROR: {log} [/bold red]")


def print_log(log, color):
    console.print(f"[bold {color}] {log} [/bold {color}]")


def get_input(prompt, color):
    res = console.input(f"[bold {color}] {prompt} > [/bold {color}]")
    return res
