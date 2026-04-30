import json
import os
import sys

from rainbowsnake import Color

employeesData = [
    {
        "name": "Rafe Milner",
        "position": "Manager",
        "hoursperday": [1, 3, 9, 10, 11, 2, 1],
    },
    {
        "name": "I can't do that, Hater",
        "position": "Barista",
        "hoursperday": [6, 7, 5, 8, 9, 4, 6],
    },
    {"name": "Somepeople", "position": "Barista", "hoursperday": [7, 8, 3, 2, 4, 7, 0]},
    {
        "name": "Best Friend",
        "position": "Cleaner",
        "hoursperday": [7, 8, 3, 2, 4, 7, 0],
    },
]


hasopenedata = False


def syncdata():
    global hasopenedata
    global employeesData

    import json

    if not hasopenedata:
        try:
            with open(
                "wage-program-data-and-settings.json", "r", encoding="utf-8"
            ) as file:
                data = json.load(file)
                employeesData = data
                hasopenedata = True
                syncdata()
        except FileNotFoundError:
            data = employeesData

            with open("wage-program-data-and-settings.json", "w") as file:
                json.dump(data, file)
    else:
        data = employeesData

        with open("wage-program-data-and-settings.json", "w") as file:
            json.dump(data, file)

        with open("wage-program-data-and-settings.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            employeesData = data


syncdata()


def function1(number):
    print(number)
    return "exit"


def function2(number):
    print(number)
    return "back"


def function5(number):
    def center(string, type):
        match type:
            case "number":
                text = str(string)
                return text.center(14)
            case "name":
                bigest = 0
                for employee in employeesData:
                    if len(str(employee["name"])) > bigest:
                        bigest = len(str(employee["name"]))

                text = str(string)
                return text.center(bigest + 6)

            case "position":
                bigest = 0
                for employee in employeesData:
                    if len(str(employee["position"])) > bigest:
                        bigest = len(str(employee["position"]))

                text = str(string)
                return text.center(bigest + 8)

    shouldExit = False
    action = "continue"
    errormessage = ""

    while not shouldExit:
        Color.clear()
        Color.clear()
        match action.lower():
            case "continue":
                shouldExit = False
                Color.output(
                    f"{Color.bold + Color.hexbg('#000000') + Color.hextext('#ffffff')}Manage employees:{Color.hexOFF + Color.boldOFF} \n  "
                )

                starttext = f"|{Color.bold}{center('Number', 'number')}{Color.boldOFF}|{Color.bold}{center('Name', 'name')}{Color.boldOFF}|{Color.bold}{center('Position', 'position')}{Color.boldOFF}|"
                starttextforlen = f"|{center('Number', 'number')}|{center('Name', 'name')}|Position       |"

                Color.output(starttext)
                Color.output("-" * len(starttextforlen))

                syncdata()
                for index, employee in enumerate(employeesData):
                    Color.output(
                        f"|{center(index, 'number')}|{center(employee['name'], 'name')}|{center(employee['position'], 'position')}|"
                    )
                    Color.output("-" * len(starttextforlen))
                syncdata()

                Color.output(errormessage if errormessage else "\n")
                errormessage = ""
                try:
                    action = Color.input(
                        f"Take action, {Color.error}[d]elete employee{Color.errorOFF}, {Color.success}[a]dd employee{Color.successOFF}, {Color.warning}[e]dit employee{Color.warningOFF}, {Color.information}go [h]ome{Color.informationOFF}:   "
                    )
                except KeyboardInterrupt:
                    errormessage = f"{Color.warning}Please enter 'exit' to exit to allow the program to properly shut down.{Color.warningOFF} \n"
                    continue

            case "h":
                return "back"

            case "e":
                errormessage = ""

                while True:
                    Color.clear()
                    Color.clear()

                    Color.output(f"{Color.warning}Edit employee:{Color.warningOFF} \n ")

                    starttext = f"|{Color.bold}{center('Number', 'number')}{Color.boldOFF}|{Color.bold}{center('Name', 'name')}{Color.boldOFF}|{Color.bold}{center('Position', 'position')}{Color.boldOFF}|"
                    starttextforlen = f"|{center('Number', 'number')}|{center('Name', 'name')}|Position       |"

                    Color.output(starttext)
                    Color.output("-" * len(starttextforlen))

                    syncdata()
                    for index, employee in enumerate(employeesData):
                        Color.output(
                            f"|{center(index, 'number')}|{center(employee['name'], 'name')}|{center(employee['position'], 'position')}|"
                        )
                        Color.output("-" * len(starttextforlen))
                    syncdata()

                    Color.output("\n")

                    Color.output(errormessage + "\n" if errormessage else "\n")
                    errormessage = ""

                    delninput = Color.input(
                        "Enter the number of the employee you wish to edit or press [b] to go back:  "
                    )

                    if delninput == "b":
                        action = "continue"
                        break
                    else:
                        try:
                            delnumber = int(delninput)
                        except ValueError:
                            errormessage = f"{Color.warning}Please enter a number or press [b] to go back{Color.warningOFF}"
                            continue

                    if employeesData[delnumber]:
                        externalContinue = False
                        externalBreak = False
                        name = ""

                        while True:
                            Color.clear()
                            Color.clear()

                            Color.output(
                                f"{Color.warning}Edit employee:{Color.warningOFF} \n "
                            )

                            starttext = f"|{Color.bold}{center('Number', 'number')}{Color.boldOFF}|{Color.bold}{center('Name', 'name')}{Color.boldOFF}|{Color.bold}{center('Position', 'position')}{Color.boldOFF}|"
                            starttextforlen = f"|{center('Number', 'number')}|{center('Name', 'name')}|Position       |"

                            Color.output(starttext)
                            Color.output("-" * len(starttextforlen))

                            syncdata()
                            for index, employee in enumerate(employeesData):
                                if index == delnumber:
                                    Color.output(
                                        f"{Color.warning}|{center(index, 'number')}|{center(employee['name'], 'name')}|{center(employee['position'], 'position')}|{Color.warningOFF}"
                                    )
                                else:
                                    Color.output(
                                        f"|{center(index, 'number')}|{center(employee['name'], 'name')}|{center(employee['position'], 'position')}|"
                                    )
                                Color.output("-" * len(starttextforlen))
                            syncdata()

                            Color.output(errormessage + "\n" if errormessage else "\n")
                            errormessage = ""

                            if not name:
                                confirm = Color.input(
                                    f"Edit Name for, {Color.warning}{employeesData[delnumber]['name']}{Color.warningOFF}; [Y]es, [N]o:  "
                                )

                                if confirm.lower() == "y":
                                    name = Color.input("Enter New Name:   ")
                                    employeesData[delnumber]["name"] = name
                                    syncdata()
                                elif confirm.lower() == "n":
                                    name = "n"
                                else:
                                    errormessage = f"{Color.warning}Please select yes or no{Color.warningOFF}"
                                    continue
                            else:
                                if name != "n":
                                    Color.output(f"New Name:   {name}\n")

                                confirm = Color.input(
                                    f"Edit Position for, {Color.warning}{employeesData[delnumber]['name']}{Color.warningOFF}; [Y]es, [N]o:  "
                                )

                                if confirm.lower() == "y":
                                    position = Color.input(
                                        "Which position does this employee have? [1]-Manager, [2]-Barista, [3]-Cleaner:  "
                                    )

                                    match position:
                                        case "1":
                                            position = "Manager"
                                        case "2":
                                            position = "Barista"
                                        case "3":
                                            position = "Cleaner"
                                        case _:
                                            position = ""
                                            errormessage = f"{Color.warning}Please select one of the options; [1]-Manager, [2]-Barista, [3]-Cleaner{Color.warningOFF}"
                                            continue

                                    employeesData[delnumber]["position"] = position
                                    syncdata()

                                    externalBreak = True
                                    break
                                elif confirm.lower() == "n":
                                    name = "n"
                                    externalBreak = True
                                    break
                                else:
                                    errormessage = f"{Color.warning}Please select yes or no{Color.warningOFF}"
                                    continue

                        if externalContinue:
                            continue
                        if externalBreak:
                            action = "continue"
                            break

                    else:
                        errormessage = f"{Color.warning}Please enter an employee number from the list{Color.warningOFF}"

                action = "continue"
                continue

            case "d":
                errormessage = ""

                while True:
                    Color.clear()
                    Color.clear()

                    Color.output(f"{Color.error}Delete employee:{Color.errorOFF} \n ")

                    starttext = f"|{Color.bold}{center('Number', 'number')}{Color.boldOFF}|{Color.bold}{center('Name', 'name')}{Color.boldOFF}|{Color.bold}{center('Position', 'position')}{Color.boldOFF}|"
                    starttextforlen = f"|{center('Number', 'number')}|{center('Name', 'name')}|Position       |"

                    Color.output(starttext)
                    Color.output("-" * len(starttextforlen))

                    syncdata()
                    for index, employee in enumerate(employeesData):
                        Color.output(
                            f"|{center(index, 'number')}|{center(employee['name'], 'name')}|{center(employee['position'], 'position')}|"
                        )
                        Color.output("-" * len(starttextforlen))
                    syncdata()

                    Color.output("\n")

                    Color.output(errormessage + "\n" if errormessage else "\n")
                    errormessage = ""

                    delninput = Color.input(
                        "Enter the number of the employee you wish to delete or press [b] to go back:  "
                    )

                    if delninput == "b":
                        action = "continue"
                        break
                    else:
                        try:
                            delnumber = int(delninput)
                        except ValueError:
                            errormessage = f"{Color.warning}Please enter a number or press [b] to go back{Color.warningOFF}"
                            continue

                    if employeesData[delnumber]:
                        externalContinue = False
                        externalBreak = False

                        while True:
                            Color.clear()
                            Color.clear()

                            Color.output(
                                f"{Color.error}Delete employee:{Color.errorOFF} \n "
                            )

                            starttext = f"|{Color.bold}{center('Number', 'number')}{Color.boldOFF}|{Color.bold}{center('Name', 'name')}{Color.boldOFF}|{Color.bold}{center('Position', 'position')}{Color.boldOFF}|"
                            starttextforlen = f"|{center('Number', 'number')}|{center('Name', 'name')}|Position       |"

                            Color.output(starttext)
                            Color.output("-" * len(starttextforlen))

                            syncdata()
                            for index, employee in enumerate(employeesData):
                                if index == delnumber:
                                    Color.output(
                                        f"{Color.error}|{center(index, 'number')}|{center(employee['name'], 'name')}|{center(employee['position'], 'position')}|{Color.errorOFF}"
                                    )
                                else:
                                    Color.output(
                                        f"|{center(index, 'number')}|{center(employee['name'], 'name')}|{center(employee['position'], 'position')}|"
                                    )
                                Color.output("-" * len(starttextforlen))
                            syncdata()

                            Color.output(errormessage + "\n" if errormessage else "\n")
                            errormessage = ""

                            confirm = Color.input(
                                f"Are you sure you want to delete, {Color.error}{employeesData[delnumber]['name']}{Color.errorOFF}; [Y]es, [N]o:  "
                            )

                            if confirm.lower() == "y":
                                del employeesData[delnumber]
                                syncdata()
                                externalBreak = True
                                break
                            elif confirm.lower() == "n":
                                externalContinue = True
                                break
                            else:
                                errormessage = f"{Color.warning}Please select yes or no{Color.warningOFF}"
                                continue

                        if externalContinue:
                            continue
                        if externalBreak:
                            action = "continue"
                            break

                    else:
                        errormessage = f"{Color.warning}Please enter an employee number from the list{Color.warningOFF}"

                action = "continue"
                continue

            case "a":
                name = ""
                position = ""

                while True:
                    Color.clear()
                    Color.clear()

                    Color.output(
                        f"{Color.bold + Color.hexbg('#000000') + Color.hextext('#ffffff')}Add employee:{Color.hexOFF + Color.boldOFF} \n "
                    )

                    starttextforlen = f"|{center('Number', 'number')}|{center('Name', 'name')}|Position       |"
                    starttext = f"|{Color.bold}{center('Number', 'number')}{Color.boldOFF}|{Color.bold}{center('Name', 'name')}{Color.boldOFF}|{Color.bold}{center('Position', 'position')}{Color.boldOFF}|"

                    Color.output(
                        f"{Color.bold}{'New employee'.center(len(starttextforlen))}{Color.boldOFF}"
                    )
                    Color.output("-" * len(starttextforlen))
                    Color.output(starttext)
                    Color.output("-" * len(starttextforlen))
                    Color.output(
                        f"|{center((len(employeesData) + 1), 'number')}|{center(name if name else '????? ??????', 'name')}|{center(position if position else '??????', 'position')}|"
                    )
                    Color.output("\n")

                    Color.output(errormessage + "\n" if errormessage else "\n")
                    errormessage = ""

                    if name:
                        Color.output(f"Enter employee name:   {name}")

                    if not name:
                        name = Color.input("Enter employee name:   ")
                    elif not position:
                        position = Color.input(
                            "Which position does this employee have? [1]-Manager, [2]-Barista, [3]-Cleaner:  "
                        )

                        match position:
                            case "1":
                                position = "Manager"
                            case "2":
                                position = "Barista"
                            case "3":
                                position = "Cleaner"
                            case _:
                                position = ""
                                errormessage = f"{Color.warning}Please select one of the options; [1]-Manager, [2]-Barista, [3]-Cleaner{Color.warningOFF}"

                    if name and position:
                        newemployee = dict(
                            name=name,
                            position=position,
                            hoursperday=[0, 0, 0, 0, 0, 0, 0],
                        )
                        employeesData.append(newemployee)

                        syncdata()

                        break

                action = "continue"
                continue

            case "exit":
                return "exit"

            case _:
                errormessage = f'{Color.warning}Please enter one of the commands below or type "exit" at anytime to quit the program.{Color.warningOFF} \n'
                action = "continue"
                continue

    return "exit"


def mainloop():
    shouldExit = False

    while not shouldExit:
        stepone = True
        functionNumber = None
        steponePrintlog = ""

        while stepone:
            Color.clear()
            Color.clear()

            Color.output(
                f"\nWelcome to {Color.bold + Color.hexbg('#EE1C25') + Color.hextext('#ffffff')}Mushroom Cafe{Color.hexOFF + Color.boldOFF} Payroll Management \n \n"
            )

            Color.output("Select task:")
            Color.output(f"{Color.bold}1{Color.boldOFF}. Use Wizard")
            Color.output(f"{Color.bold}2{Color.boldOFF}. Enter hours worked")
            Color.output(f"{Color.bold}3{Color.boldOFF}. View Employee Pay")
            Color.output(f"{Color.bold}4{Color.boldOFF}. View Employee statistics")
            Color.output(f"{Color.bold}5{Color.boldOFF}. Manage Employees \n")

            if steponePrintlog:
                Color.output(steponePrintlog)
                steponePrintlog = ""
            else:
                Color.output("\n")

            try:
                taskInput = Color.input(
                    "Enter the number of the task you would like to do: "
                )
            except KeyboardInterrupt:
                steponePrintlog = f"{Color.warning}Please enter 'exit' to exit to allow the program to properly shut down.{Color.warningOFF} \n"
                continue

            if taskInput == "exit":
                exit()
            else:
                try:
                    taskNumber = int(taskInput)
                except ValueError:
                    steponePrintlog = f"{Color.warning}Please enter a number between 1 and 5{Color.warningOFF} \n"
                    continue

                if taskNumber < 1 or taskNumber > 5:
                    steponePrintlog = f"{Color.warning}Please enter a number between 1 and 5{Color.warningOFF} \n"
                    continue
                else:
                    stepone = False
                    functionNumber = taskNumber

            Color.clear()
            Color.clear()

        if functionNumber:
            match functionNumber:
                case 1:
                    goWhere = function1("1")

                    syncdata()

                    functionNumber = None if goWhere == "back" else None
                    shouldExit = True if goWhere == "exit" else None

                case 2:
                    goWhere = function2("1")

                    syncdata()

                    functionNumber = None if goWhere == "back" else None
                    shouldExit = True if goWhere == "exit" else None

                case 3:
                    goWhere = function3("1")

                    syncdata()

                    functionNumber = None if goWhere == "back" else None
                    shouldExit = True if goWhere == "exit" else None

                case 4:
                    goWhere = function4("1")

                    syncdata()

                    functionNumber = None if goWhere == "back" else None
                    shouldExit = True if goWhere == "exit" else None

                case 5:
                    goWhere = function5("1")

                    syncdata()

                    functionNumber = None if goWhere == "back" else None
                    shouldExit = True if goWhere == "exit" else None


mainloop()
