employeeData = [
    ["Bob", "Manager", [1, 3, 9, 10, 11, 2, 1]],
    ["Rob", "Barista", [6, 7, 5, 8, 9, 4, 6]],
    ["Dom", "Cleaner", [7, 8, 3, 2, 4, 7, 0]],
]

name = 0
position = 1
hoursWorked = 2


o = 1
for i in employeeData:
    h = 0

    for y in i[hoursWorked]:
        h += y

    print(
        f"Employee Number {o}, name is {i[name]} and their position is {i[position]}, this week they worked a total of {h} hours"
    )
    o += 1
