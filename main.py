import os
import sys

from rainbowsnake import Color

stepone = True
steponePrintlog = ""

while stepone:
    Color.clear()
    Color.clear()

    Color.output(
        f"\nWelcome to {Color.bold + Color.hexbg('#EE1C25') + Color.hextext('#ffffff')}Mushroom Cafe{Color.hexOFF + Color.boldOFF} Payroll Management \n \n"
    )

    Color.output("Select task:")
    Color.output(f"{Color.bold}1{Color.boldOFF}. Enter hours worked")
    Color.output(f"{Color.bold}2{Color.boldOFF}. Manage employees")
    Color.output(f"{Color.bold}3{Color.boldOFF}. Export payroll slips")
    Color.output(f"{Color.bold}4{Color.boldOFF}. View statistics \n")

    if steponePrintlog:
        Color.output(steponePrintlog)
        steponePrintlog = ""
    else:
        Color.output("\n")

    try:
        taskInput = Color.input("Enter the number of the task you would like to do: ")
    except KeyboardInterrupt:
        steponePrintlog = f"{Color.warning}Please enter 'exit' to exit to allow the program to properly shut down.{Color.warningOFF} \n"
        continue

    if taskInput == "exit":
        exit()
    else:
        try:
            taskNumber = int(taskInput)
        except ValueError:
            steponePrintlog = f"{Color.warning}Please enter a number between 1 and 4{Color.warningOFF} \n"
            continue

        if taskNumber < 1 or taskNumber > 4:
            steponePrintlog = f"{Color.warning}Please enter a number between 1 and 4{Color.warningOFF} \n"
            continue
        else:
            stepone = False

    Color.clear()
    Color.clear()
