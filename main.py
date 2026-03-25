import os
import sys


if 'idlelib' in sys.modules:
    print("Sorry, this program is not compatible with python IDLE, as it does not implement standard terminal features and does not allow for text coloring. Please run this application in a terminal with the command 'python3 PATH-TO-MAIN.PY' ")
    exit()


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


try:
    from colorist import BgColorRGB, Color, ColorRGB, Effect, effect_blink
except ImportError:
    clear()
    print("\n Dependencies are not installed, please run 'pip install colorist'")
    exit()


marioRed = BgColorRGB(238, 28, 37)
erroryellow = BgColorRGB(255, 219, 60)

stepone = True
steponePrintlog = ""

while stepone:
    clear()

    if steponePrintlog:
        print(steponePrintlog)

    print(
        f"\nWelcome to {Color.WHITE}{marioRed}Mushroom Cafe{marioRed.OFF}{Color.OFF} Payroll Management \n \n"
    )

    print("Select task:")
    print(f"{Effect.BOLD}1{Effect.OFF}. Enter hours worked")
    print(f"{Effect.BOLD}2{Effect.OFF}. Manage employees")
    print(f"{Effect.BOLD}3{Effect.OFF}. Export payroll slips")
    print(f"{Effect.BOLD}4{Effect.OFF}. View statistics \n")

    try:
        taskNumber = int(input("Enter the number of the task you would like to do: "))
    except ValueError:
        steponePrintlog = f"{Effect.BOLD}{Color.WHITE}{erroryellow}Please enter a number between 1 and 4{erroryellow.OFF}{Color.OFF}{Effect.OFF} \n"
        continue

    clear()
