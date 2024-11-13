import os
import time
import random
import platform
import subprocess

os.system('')  # Enables ANSI escape codes on Windows

attempts = 0
max_attempts = 3

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def initialize():
    global attempts
    clear_screen()
    print('\033[96m')
    print("""
    ███╗   ███╗██╗   ██╗██╗     ████████╗██╗        ████████╗ █████╗  █████╗ ██╗
    ████╗ ████║██║   ██║██║     ╚══██╔══╝██║        ╚══██╔══╝██╔══██╗██╔══██╗██║
    ██╔████╔██║██║   ██║██║        ██║   ██║  █████╗   ██║   ██║  ██║██║  ██║██║
    ██║╚██╔╝██║██║   ██║██║        ██║   ██║  ╚════╝   ██║   ██║  ██║██║  ██║██║
    ██║ ╚═╝ ██║╚██████╔╝███████╗   ██║   ██║           ██║   ╚█████╔╝╚█████╔╝███████╗
    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝           ╚═╝    ╚════╝  ╚════╝ ╚══════╝
    """)
    print("Welcome to the vifez multi tool")
    print("Please log in to proceed.\n")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == "root" and password == "root":
        welcome(username)
    else:
        attempts += 1
        if attempts >= max_attempts:
            print("[!] Too many failed attempts! Exiting now...")
            time.sleep(2)
            exit()
        print(f"[!] Incorrect login, please try again. You have {attempts}/{max_attempts} attempts remaining.")
        input("Press Enter to continue...")
        initialize()

def welcome(username):
    clear_screen()
    print(f"\n\nYou have successfully logged in, {username}!")
    print("Here’s a motivational quote for you:\n")
    random_quote()
    time.sleep(3)
    main_menu(username)

def main_menu(username):
    while True:
        clear_screen()
        print(f"""
        ╔═══════════════════════════════════════════════╗
        ║            Multi-Tool Dashboard               ║
        ║                                               ║
        ║    1. Calculator                              ║
        ║    2. Save a Note                             ║
        ║    3. View System Information                 ║
        ║    4. View Credits                            ║
        ║    5. Exit                                    ║
        ║                                               ║
        ╚═══════════════════════════════════════════════╝
        """)
        choice = input(f"Select an option [{username}]: ")
        
        if choice == "1":
            calculator()
        elif choice == "2":
            save_note()
        elif choice == "3":
            system_info()
        elif choice == "4":
            credits()
        elif choice == "5":
            exit_tool()
        else:
            print("[!] Invalid choice. Please select a valid option.")
            time.sleep(1)

def calculator():
    clear_screen()
    print("""
    ╔═══════════════════════════════════════════════╗
    ║               Simple Calculator               ║
    ╚═══════════════════════════════════════════════╝
    """)
    calc_expr = input("Enter expression (e.g., 1231*321): ")
    try:
        result = round(eval(calc_expr), 3)
        print(f"Result: {result}")
    except:
        print("Invalid expression")
    input("Press Enter to continue...")

def save_note():
    clear_screen()
    print("""
    ╔═══════════════════════════════════════════════╗
    ║                 Save a Note                   ║
    ╚═══════════════════════════════════════════════╝
    """)
    note = input("Write your note: ")
    try:
        with open("notes.txt", "a", encoding="utf-8") as file:
            file.write(note + "\n")
        print('Note saved to "notes.txt".')
    except Exception as e:
        print(f"An error occurred while saving the note: {e}")
    input("Press Enter to continue...")

def system_info():
    clear_screen()
    print("""
    ╔═══════════════════════════════════════════════╗
    ║             System Information                ║
    ╚═══════════════════════════════════════════════╝
    """)
    print("OS Name:", platform.system())
    print("OS Version:", platform.version())
    print("System Type:", platform.machine())
    try:
        mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
        print("Total Physical Memory:", f"{mem_bytes / (1024**3):.2f} GB")
    except:
        print("Memory Information: Unavailable")
    input("Press Enter to continue...")

def credits():
    clear_screen()
    print("""
    ╔═══════════════════════════════════════════════╗
    ║                  CREDITS                      ║
    ║                                               ║
    ║      This tool was developed by: vifez        ║
    ║                                               ║
    ╚═══════════════════════════════════════════════╝
    """)
    time.sleep(3)

def exit_tool():
    clear_screen()
    print("Logging out...")
    print("(Please wait)")
    time.sleep(2)
    exit()

def random_quote():
    quotes = [
        "developed by vifez fr.",
        "Put a quote here",
        "Put a quote here",
        "Put a quote here",
        "Put a quote here"
    ]
    print(random.choice(quotes))

initialize()