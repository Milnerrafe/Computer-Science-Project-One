# Import date, time for date and time related functions.
from datetime import date

# Declaration of the Array of Employees
employeeData = [
    {
        "name": "Meg Docherty",
        "position": "Manager",
        "hoursperday": [1, 3, 9, 10, 11, 2, 1],
    }
]


# Clear function
def clear():
    # IntelliSense information
    """
    Clear the terminal
    """

    # Import the operating system module which allows for the clear command to be run in the macOS and windows terminal.
    import os

    # Import the system module, which allows for the identification for idle running, which requires different clear behaviour.
    import sys

    # Determine whether the code is running in idle or not.
    if "idlelib" in sys.modules:
        # If the code is running in idle, print newlines many times.
        # (This behaviour is required as idle does not support clear and using
        # a simple print with newline times 1000 will condense the lines not
        # achieving the attended effect)
        for i in range(10):
            print("\n" * 5)
    else:
        # If the code is running in terminal, run the clear command.
        if os.name == "nt":
            os.system("cls")
            os.system("cls")
        else:
            os.system("clear")
            os.system("clear")


def viewEmployeedata():
    print("hi")


# Function to check whether an employee exists in the data structure.
def checkEmployee(name):
    # IntelliSense information
    """
    Check whether an employee exists in the data structure

    Returns:
            boolean: True = Employee does not exist / False = employee does exist
            int: The index of the employee
    """

    # Using iteration control structure, check whether the name provided is in the list of employees.
    for index, employee in enumerate(employeeData):
        # If the name is in the list of employees, return false and provide the index to that data.
        # Strings modified to remove spaces and lowercase all uppercase characters.
        if "".join(name.split()).lower() == "".join(employee["name"].split()).lower():
            return True, index
        else:
            continue

    # If the name is not in the data structure, return true and do not provide an index.
    return False, None


# Enter employee information and hours function.
def enterEmployeehours():
    # IntelliSense information
    """
    Employee information and hours function
    """

    # Define error message variable used to present error in the next iteration.
    errormessage = ""

    # Define the step that the loop is in
    step = 0
    name = ""
    position = ""
    index = None

    # Define function loop
    while True:
        # Clear the terminal to remove the previous screen.
        clear()

        print("Enter Employee hours: \n")
        print("Press [B] to go back to home. \n")

        # If the user has entered an acceptable name, move the step from 0 to 1.
        if name:
            step = 1

        # If the user has entered an position, move the step from 1 to 2.
        if index:
            step = 2

        if step == 0:
            # If there is an error message, print it.
            if errormessage:
                print(errormessage + "\n")
                errormessage = ""

            # Try accept expression for name input to allow for clean exiting, back to the main screen.
            try:
                nameInput = input(
                    "What is the name of the employee you would like to add:   "
                )
            except KeyboardInterrupt:
                clear()
                break

            # Check if the user would like to return to the homepage.

            if nameInput.lower() == "b":
                clear()
                break

            # Check if the employee already exists.
            employeeExists, indexOfemployee = checkEmployee(nameInput)

            if employeeExists:
                errormessage = "That name is already used, Enter a different name."
            else:
                name = nameInput
                continue
        else:
            # Show user visual confirmation that they have entered a name.
            print(f"What is the name of the employee you would like to add: {name}")

        if step == 1:
            # If there is an error message, print it.
            if errormessage:
                print(errormessage + "\n")
                errormessage = ""

            # Ask the user which position the employee will fill.
            position = input(
                "Which position does this employee have? [1]-Manager, [2]-Barista, [3]-Cleaner:  "
            )

            # Match the user's input position. If there isn't a position, return an error.
            match position:
                case "1":
                    position = "Manager"
                case "2":
                    position = "Barista"
                case "3":
                    position = "Cleaner"
                case _:
                    position = ""
                    errormessage = "Please select one of the options; [1]-Manager, [2]-Barista, [3]-Cleaner"
                    continue

            # Create dictionary based on the given information then calculate its index in the employee data array.
            employeeObject = dict(
                name=name,
                position=position,
                hoursperday=[0, 0, 0, 0, 0, 0, 0],
                holidays=[False, False, False, False, False, False, False],
                payperday=[0, 0, 0, 0, 0, 0, 0],
                totalpay=0,
            )
            employeeData.append(employeeObject)
            index = len(employeeData) - 1

        else:
            # Show user visual confirmation that they have entered a Position.
            print(f"Which position does this employee have?: {position}")

        if step == 2:
            # Print message to user to inform them to enter the hours for the employee.
            # Getting the employees name from the index and dictionary created earlier,
            # ensuring that if there is an error then it is thrown immediately.
            print(f"\n \nEnter Hours for {employeeData[index]['name']}")

            days = [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday",
            ]

            for dayNumber, day in enumerate(days):
                internalErrormessage = ""
                while True:
                    # Have the first day Feature a message referencing the Employees's name.
                    if day == "Monday":
                        inputString = f"Enter the hours worked by {employeeData[index]['name']} for {day}:  "
                    else:
                        inputString = f"Enter the hours worked for {day}:  "

                    # Print internal error message.
                    if internalErrormessage:
                        print(internalErrormessage)

                    # Error handling for float numbers.
                    try:
                        hoursworked = float(input(inputString))
                    except ValueError:
                        internalErrormessage = (
                            "Please enter a number between 0.1 and 24"
                        )
                        continue

                    # Check whether the input is in range.
                    if hoursworked < 0.1 or hoursworked > 24:
                        internalErrormessage = (
                            "Please enter a number between 0.1 and 24"
                        )
                        continue
                    else:
                        employeeData[index]["hoursperday"][dayNumber] = hoursworked

                    internalinternalErrormessage = ""
                    while True:
                        # If there is an error with the user entering yes or no, then it is displayed.
                        if internalinternalErrormessage:
                            print(internalinternalErrormessage)

                        # Input for holidays
                        holdayInput = input(f"Is {day}, a holday? [Y]es/[N]o:  ")

                        if holdayInput.lower() == "yes" or holdayInput.lower() == "y":
                            employeeData[index]["holidays"][dayNumber] = True
                            break
                        elif holdayInput.lower() == "no" or holdayInput.lower() == "n":
                            break
                        else:
                            internalinternalErrormessage = "Please enter yes or no"
                            continue

                    # Move to step 3 using the selection control structure of the iteration loop.
                    step = 3
                    break

            if step == 3:
                input(employeeData)

            break

    viewEmployeedata()


# Main function (The main function controls the selection of which function
# the user would like to run and has looping functions to allow the user
# to perform multiple tasks.)
def main():
    # IntelliSense information
    """
    Main loop and program entry point
    """

    # Define main loop
    # (While loops continue when the variable they are observing is truthy,
    # by setting the value of true the loop will never stop but it can be
    # broken by using the break keyword. This means that a set variable
    # is not required.)

    # Define error message variable used to present error in the next iteration.
    errormessage = ""

    while True:
        clear()

        # Try statement to catch users entering values that are not integers and informing them of their mistake.
        try:
            # Function number is a variable defined as an input converted into an integer
            # with a multi-line string that presents the user interface and fstring
            # placeholders for today's date and a possible error message.
            functionnumber = int(
                input(f"""Welcome to Mushroom Cafe Payroll Management:

Today is {date.today().strftime("%A") + " the " + date.today().strftime("%d") + " of " + date.today().strftime("%B, %Y")}

What function would you like to perform?
(1) - Enter employee hours
(2) - View employee hours and pay
(3) - Exit

{errormessage}

Enter the function number and press enter to continue: """)
            )

        # Handle, integer error, set error message and restart the loop.
        except ValueError:
            errormessage = "Please enter the number of the function you would like to perform 1, 2 or 3"
            continue

        # Handle Control + C and cleanly close the program with no errors.
        except KeyboardInterrupt:
            clear()
            break

        # Selection control structure to run the correct function for 1, 2, 3
        #  and to inform the user of an error if they choose a different number.
        if functionnumber == 1:
            # Run enter employee hours, Then restart the loop when the function returns to
            # allow the user to use other functions.
            enterEmployeehours()
            continue
        elif functionnumber == 2:
            # Run View employee data, Then restart the loop when the function returns to
            # allow the user to use other functions.
            viewEmployeedata()
            continue
        elif functionnumber == 3:
            clear()
            break
        else:
            errormessage = "Please enter the number of the function you would like to perform 1, 2 or 3"
            continue


# Run the main function to start the program.
main()
