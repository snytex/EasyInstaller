import requests
from termcolor import colored
import time
from colorama import init
from rich.console import Console
import programs
import os
from os import system as cmd
import fade
from tqdm import tqdm

console = Console
cmd("mode con:cols=132 lines=30")

def centered(text, width=130):
    spaces = (width - len(text)) // 2  # Calculate the number of spaces needed for centering
    return " " * spaces + text + " " * spaces

import time
from termcolor import colored
from colorama import init

def animate_text_centered(text, width, delay, color):
    init()  # Initialize colorama
    spaces = (width - len(text)) // 2  # Calculate the number of spaces needed for centering
    for _ in range(spaces):
        print(" ", end='', flush=True)  # Print leading spaces

    for char in text:
        print(colored(char, color, attrs=['underline']), end='', flush=True)  # Print each character with color and underline
        time.sleep(delay)  # Delay between characters

    for _ in range(spaces):
        print(" ", end='', flush=True)  # Print trailing spaces

    print()  # Print a newline after the animation completes

# Example usage
window_width = 130
text = "EasyInstaller"
delay = 0.075
color = 'blue'  # Specify the color ('blue' in this example)

animate_text_centered(text, window_width, delay, color)

def print_text_centered(text, width, color):
    init()  # Initialize colorama
    spaces = (width - len(text)) // 2  # Calculate the number of spaces needed for centering
    centered_text = " " * spaces + text + " " * spaces
    print(colored(centered_text, color))

# Example usage
window_width = 130
text = "EasyInstaller"
color = 'blue'  # Specify the color ('blue' in this example)

time.sleep(2)

print()

def mainscreen():
    print(fade.water('''    --[Browsers]--            --[Gaming]--             --[Social Stuff]--             --[Drivers]--             --[Misc]--

    [1] > Opera GX          [7] > Minecraft             [13] > Discord             [19] > Nvidia GPUs         [25] > 7-Zip
    [2] > Chrome            [8] > Roblox                [14] > Skype               [20] > AMD GPUs            [26] > WinRAR
    [3] > Firefox           [9] > Steam                 [15] > Zoom                [21] > Intel GPUs          [27] > CCleaner
    [4] > Opera            [10] > Epic Games            [16] > Microsoft Teams     [22] > Audio Driver        [28] > Malwarebytes
    [5] > Brave            [11] > Origin                [17] > TeamSpeak 3         [23] > DS4Windows          [39] > ProtonVPN
    [6] > Tor              [12] > Uplay                 [18] > WhatsApp            [24] > Network Driver      [30] > Revo 
    '''))
mainscreen()

while True:
    user_input = input(colored("> ", "light_blue"))

    if user_input == "quit":
        break

    try:
        program_number = int(user_input)
        program_data = programs.get(program_number)

        if program_data:
            program_name = program_data['name']
            download_link = program_data['download_link']

            print(colored(f"Installing program: {program_name}", "light_blue"))

            # Download the program with progress bar
            response = requests.get(download_link, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            block_size = 1024  # 1 KB
            progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)

            # Save the program to the Downloads folder
            filename = os.path.join(os.path.expanduser('~'), 'Downloads', f"{program_name}.exe")
            with open(filename, 'wb') as file:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    file.write(data)

            progress_bar.close()

            print(colored(f"Program {program_name} installed in the Downloads folder.", "light_green"))
            time.sleep(3)
            cmd("cls")
            print_text_centered(text, window_width, color)
            print()
            mainscreen()
        else:
            print(colored("Invalid program number. Please try again.", "light_blue"))
    except ValueError:
        print(colored("Invalid input. Please enter a number or 'quit' to quit.", "light_blue"))