# Import date, time for date and time related functions.
from datetime import date

# Declaration of the Array of Employees
employeeData = []


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
        if name == employee.name:
            return False, index
        else:
            continue

    # If the name is not in the data structure, return true and do not provide an index.
    return True, None


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

    # Define function loop
    while True:
        # Clear the terminal to remove the previous screen.
        clear()

        print("Enter Employee hours: \n")

        # If there is an error message, print it, Otherwise, print a blank new line.
        print(errormessage) if errormessage else print("\n")

        if step == 0:
            # Try accept expression for name input to allow for clean exiting, back to the main screen.
            try:
                name = input(
                    "What is the name of the employee you would like to add:   "
                )
            except KeyboardInterrupt:
                clear()
                break

            if checkEmployee(name):
                print("yes")
            else:
                print("no")


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
