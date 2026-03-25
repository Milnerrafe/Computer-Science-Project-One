import os

from colorist import BgColorRGB, Color, ColorRGB, Effect


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


marioRed = BgColorRGB(238, 28, 37)

clear()

print(
    f"Welcome to {Color.WHITE}{marioRed}Mushroom Cafe{marioRed.OFF}{Color.OFF} Payroll Management \n \n"
)


print("Select task:")
print(f"{Effect.BOLD}1{Effect.OFF}. Enter hours worked")
print(f"{Effect.BOLD}2{Effect.OFF}. Manage employees")
print(f"{Effect.BOLD}3{Effect.OFF}. Export payroll slips")
print(f"{Effect.BOLD}4{Effect.OFF}. View statistics in detail \n")
taskNumber = int(input("Enter the number of the task you would like to do: "))

clear()

taskNumber = int(input("Enter the number of the task you would like to do: "))
