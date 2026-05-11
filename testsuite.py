import time

start_time = time.perf_counter()

# Main Logic Test
testValues_for_main = [0, 1, 2, 3, 4, 5, "Hello World", "Smart Cookie", "67"]
shouldpass = [False, True, True, True, False, False, False, False, False]
passtestone = True

for index, testValue in enumerate(testValues_for_main):
    try:
        functionnumber = int(testValue)

    except ValueError:
        if shouldpass[index]:
            print(
                f"1: Test failed. Case {testValue} was identified as a invalid value; Main Logic Test"
            )
            passtestone = False
            continue

    if functionnumber == 1:
        if not shouldpass[index]:
            print(
                f"2: Test failed. Case {testValue} was identified as a passing value; Main Logic Test"
            )
            passtestone = False

    elif functionnumber == 2:
        if not shouldpass[index]:
            print(
                f"3: Test failed. Case {testValue} was identified as a passing value; Main Logic Test"
            )
            passtestone = False

    elif functionnumber == 3:
        if not shouldpass[index]:
            print(
                f"4: Test failed. Case {testValue} was identified as a passing value; Main Logic Test"
            )
            passtestone = False
    else:
        if shouldpass[index]:
            print(
                f"5: Test failed. Case {testValue} was identified as a invalid value; Main Logic Test"
            )
            passtestone = False
        continue


# Input Logic Test

testValues_for_input = [0, 10, 24, 31, 4, 9, "Hello World", "Smart Cookie", "67"]
shouldpasstwo = [True, True, True, False, True, True, False, False, False]
passtesttwo = True


for index, testValue in enumerate(testValues_for_input):
    try:
        hoursworked = float(testValue)
    except ValueError:
        if shouldpasstwo[index]:
            print(
                f"1: Test failed. Case {testValue} was identified as a failing value; Input Logic Test"
            )
            passtestone = False
        continue

    # Check whether the input is in range.
    if hoursworked < 0.0 or hoursworked > 24.0:
        if shouldpasstwo[index]:
            print(
                f"3: Test failed. Case {testValue} was identified as a failing value; Input Logic Test"
            )
            passtestone = False
        continue
    else:
        if not shouldpasstwo[index]:
            print(
                f"2: Test failed. Case {testValue} was identified as a passing value; Input Logic Test"
            )
            passtestone = False


# Inform user of test results

end_time = time.perf_counter()

if not passtesttwo or not passtestone:
    print(f"Test has failed in {end_time - start_time:.6f}")
else:
    print(f"Test past in {end_time - start_time:.6f}")
