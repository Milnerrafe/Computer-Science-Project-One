employeeData = [
    {
        "name": "Rosa Lina",
        "position": "Manager",
        "hoursperday": [4.0, 4.0, 4.0, 4.0, 14.0, 0.0, 12.0],
        "holidays": [False, False, False, False, False, False, False],
        "payperday": [120.0, 120.0, 120.0, 120.0, 469.5, 0.0, 459.0],
        "totalpay": 1408.5,
    },
]

index = 0


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
    # Define pay variable
    pay = 0.0

    # Based on the employee's position define pay rate.
    if employeeData[index]["position"] == "Manager":
        payrate = 30.0
    else:
        payrate = 23.0

    # Define overtime rates.
    overtime1 = 25.0
    overtime2 = 45.0

    # Change overtime and pay rates for weekends.
    # If it is the weekend or a holiday, Change overtime to 50% and change pay rate.
    if (
        day == "Sunday"
        or employeeData[index]["holidays"][dayNumber]
        or day == "Saturday"
    ):
        # If it is a holiday or Sunday, set the pay rate to 4.
        # If it's not, which would be Saturday, set it to 3.
        payrate += (
            4 if day == "Sunday" or employeeData[index]["holidays"][dayNumber] else 3
        )
        # Set overtime to weekend holiday values.
        overtime1 = 50.0
        overtime2 = 50.0

    # If the employee has worked less than the overtime threshold on that day;
    if employeeData[index]["hoursperday"][dayNumber] <= 9.0:
        # Then their hours worked is simply multiplied by the pay rate,
        # which has already been adjusted to include the weekend and holiday benefits.
        pay = employeeData[index]["hoursperday"][dayNumber] * payrate

        # The data is then saved into the array value for that day.
        employeeData[index]["payperday"][dayNumber] = pay

        # And the total pay for the weekly period is then calculated by summing that array.
        totalpay = sum(employeeData[index]["payperday"])
        employeeData[index]["totalpay"] = totalpay
    else:
        # If the employee has worked more than 9 hours,
        # then we subtract 9 hours from the hours worked and calculate
        # those 9 hours at the normal pay rate for them.
        hoursworked = employeeData[index]["hoursperday"][dayNumber]
        print("0")
        print(dayNumber)
        print(pay)
        print(hoursworked)
        hoursworked = hoursworked - 9
        pay = 9 * payrate

        print("1")
        print(dayNumber)
        print(pay)
        print(hoursworked)

        # If the employee has worked more than three hours, putting them in the higher band of overtime, then;
        if hoursworked > 3:
            print("2")
            print(dayNumber)
            print(pay)
            print(hoursworked)
            # We first remove the three hours from the hours worked and then calculate those three hours at their pay rate,
            # then increase it by the overtime amount.
            hoursworked = hoursworked - 3
            pay += (3 * payrate) * float(f"1.{int(overtime1)}")
            print("3")
            print(dayNumber)
            print(pay)
            print(hoursworked)

            # Finally, the remaining hours are multiplied by the pay rate and then multiplied by
            # the higher overtime rate.
            pay += (hoursworked * payrate) * float(f"1.{int(overtime2)}")
            print(float(f"1.{int(overtime2)}"))
            print("4")
            print(dayNumber)
            print(pay)
            print(hoursworked)
        else:
            print("5")
            print(dayNumber)
            print(pay)
            print(hoursworked)
            # If the employee has not worked enough hours to go into the higher band of overtime,
            # then the amount of hours they worked is times by their pay rate and increased by the lower overtime rate.
            pay += (hoursworked * payrate) * float(f"1.{int(overtime1)}")
            print("6")
            print(dayNumber)
            print(pay)
            print(hoursworked)

        # The data is then saved into the array value for that day.
        employeeData[index]["payperday"][dayNumber] = pay

        # And the total pay for the weekly period is then calculated by summing that array.
        totalpay = sum(employeeData[index]["payperday"])
        employeeData[index]["totalpay"] = totalpay


print(employeeData)
