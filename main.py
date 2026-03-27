import os
import sys

from rainbow_snake import color

stepone = True
steponePrintlog = ""

while stepone:
    color.clear()
    color.clear()

    color.output(
        f"\nWelcome to {color.bold + color.hexbg('#EE1C25') + color.hextext('#ffffff')}Mushroom Cafe{color.hexOFF + color.boldOFF} Payroll Management \n \n"
    )

    color.output("Select task:")
    color.output(f"{color.bold}1{color.boldOFF}. Enter hours worked")
    color.output(f"{color.bold}2{color.boldOFF}. Manage employees")
    color.output(f"{color.bold}3{color.boldOFF}. Export payroll slips")
    color.output(f"{color.bold}4{color.boldOFF}. View statistics \n")

    if steponePrintlog:
        color.output(steponePrintlog)
    else:
        color.output("\n")

    try:
        taskInput = input("Enter the number of the task you would like to do: ")
    except KeyboardInterrupt:
        steponePrintlog = f"{color.warning}Please enter 'exit' to exit to allow the program to properly shut down.{color.warningOFF} \n"
        continue

    if taskInput == "exit":
        exit()
    else:
        try:
            taskNumber = int(taskInput)
        except ValueError:
            steponePrintlog = f"{color.warning}Please enter a number between 1 and 4{color.warningOFF} \n"
            continue

        if taskNumber < 1 or taskNumber > 4:
            steponePrintlog = f"{color.warning}Please enter a number between 1 and 4{color.warningOFF} \n"
            continue
        else:
            stepone = False

    color.clear()
    color.clear()
