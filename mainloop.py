from rainbowsnake import Color


def function1(number):
    print(number)
    return "exit"


def function2(number):
    print(number)
    return "back"


def function3(number):
    print(number)
    return "back"


def function4(number):
    print(number)
    return "back"


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
            Color.output(f"{Color.bold}4{Color.boldOFF}. View Employee statistics \n")

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
                    steponePrintlog = f"{Color.warning}Please enter a number between 1 and 4{Color.warningOFF} \n"
                    continue

                if taskNumber < 1 or taskNumber > 4:
                    steponePrintlog = f"{Color.warning}Please enter a number between 1 and 4{Color.warningOFF} \n"
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

                    functionNumber = None if goWhere == "back" else None
                    shouldExit = True if goWhere == "exit" else None

                case 2:
                    goWhere = function2("1")

                    functionNumber = None if goWhere == "back" else None
                    shouldExit = True if goWhere == "exit" else None

                case 3:
                    goWhere = function3("1")

                    functionNumber = None if goWhere == "back" else None
                    shouldExit = True if goWhere == "exit" else None

                case 4:
                    goWhere = function4("1")

                    functionNumber = None if goWhere == "back" else None
                    shouldExit = True if goWhere == "exit" else None
