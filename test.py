try:
    number = int(input("Enter a number: "))
except ValueError:
    number = 0

print(f"Your number is {number}")
