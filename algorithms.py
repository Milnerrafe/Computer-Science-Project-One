employeesData = [
    {
        "name": "Bob",
        "position": "Manager",
        "hoursperday": [1, 3, 9, 10, 11, 2, 1],
    },
    {
        "name": "Dom",
        "position": "Cleaner",
        "hoursperday": [7, 8, 3, 2, 4, 7, 0],
    },
    {
        "name": "Rob",
        "position": "Manager",
        "hoursperday": [1, 3, 9, 10, 11, 2, 1],
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
                getdata()
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

iterationNumber = 0
for employee in employeesData:
    employee["position"] = employee["position"] + " Hi"

    iterationNumber += 1
    hoursWorked = 0

    for hoursperday in employee["hoursperday"]:
        hoursWorked += hoursperday

    if employee["position"] == "Manager":
        pay = hoursWorked * 30
    else:
        pay = hoursWorked * 26

    print(
        f"Employee Number {iterationNumber}, name is {employee['name']} and their position is {employee['position']}, this week they worked a total of {hoursWorked} hours and should be payed ${pay} this week."
    )

syncdata()
