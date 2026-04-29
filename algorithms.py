employeesData = [
    ["Bob", "Manager", [1, 3, 9, 10, 11, 2, 1]],
    ["Rob", "Barista", [6, 7, 5, 8, 9, 4, 6]],
    ["Dom", "Cleaner", [7, 8, 3, 2, 4, 7, 0]],
]

name = 0
position = 1
days = 2

iterationNumber = 0
for employee in employeesData:
    iterationNumber += 1
    hoursWorked = 0

    for hours in employee[days]:
        hoursWorked += hours

    if employee[position] == "Manager":
        pay = hoursWorked * 30
    else:
        pay = hoursWorked * 26

    print(
        f"Employee Number {iterationNumber}, name is {employee[name]} and their position is {employee[position]}, this week they worked a total of {hoursWorked} hours and should be payed ${pay} this week."
    )
