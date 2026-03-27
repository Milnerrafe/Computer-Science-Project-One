class color:
    ostype = 0

    error = "*/error/*"
    errorOFF = "*/error:OFF/*"

    warning = "*/warning/*"
    warningOFF = "*/warning:OFF/*"

    success = "*/success/*"
    successOFF = "*/success:OFF/*"

    information = "*/information/*"
    informationOFF = "*/information:OFF/*"

    important = "*/important/*"
    importantOFF = "*/important:OFF/*"

    context = "*/context/*"
    contextOFF = "*/context:OFF/*"

    bold = "*/bold/*"
    bold = "*/bold:OFF/*"

    hextextOFF = "*/hex-text:OFF/*"
    hexbgOFF = "*/hex-bg:OFF/*"

    @classmethod
    def output(cls, string):
        import os
        import sys

        if "idlelib" in sys.modules:
            try:
                shell_connect = sys.stdout.shell
                cls.ostype = 1
            except AttributeError:
                cls.ostype = -1
        else:
            cls.ostype = 2

        if cls.ostype == 1:
            print()

        elif cls.ostype == 2:
            print()

        elif cls.ostype == -1:
            raise Exception("Rainbow-Snake does not support your os or interpreter")
        else:
            raise Exception("Rainbow-Snake does not support your os or interpreter")

    @classmethod
    def hextext(cls, hex):
        hexdehashtag = hex.replace("#", "")

        if len(hexdehashtag) == 6:
            try:
                red = int(hexdehashtag[0] + hexdehashtag[1], 16)
            except ValueError:
                raise Exception(
                    f"{hex} Is not a correct hex code. Format your hex code to look like, #FFFFFF or FFFFFF"
                )

            try:
                green = int(hexdehashtag[2] + hexdehashtag[3], 16)
            except ValueError:
                raise Exception(
                    f"{hex} Is not a correct hex code. Format your hex code to look like, #FFFFFF or FFFFFF"
                )

            try:
                blue = int(hexdehashtag[4] + hexdehashtag[5], 16)
            except ValueError:
                raise Exception(
                    f"{hex} Is not a correct hex code. Format your hex code to look like, #FFFFFF or FFFFFF"
                )

        else:
            raise Exception(
                f"{hex} Is not a correct hex code. Format your hex code to look like, #FFFFFF or FFFFFF"
            )

        return f"*/hex-text:{str(red).zfill(3)},{str(green).zfill(3)},{str(blue).zfill(3)}/*"

    @classmethod
    def hexbg(cls, hex):
        hexdehashtag = hex.replace("#", "")

        if len(hexdehashtag) == 6:
            try:
                red = int(hexdehashtag[0] + hexdehashtag[1], 16)
            except ValueError:
                raise Exception(
                    f"{hex} Is not a correct hex code. Format your hex code to look like, #FFFFFF or FFFFFF"
                )

            try:
                green = int(hexdehashtag[2] + hexdehashtag[3], 16)
            except ValueError:
                raise Exception(
                    f"{hex} Is not a correct hex code. Format your hex code to look like, #FFFFFF or FFFFFF"
                )

            try:
                blue = int(hexdehashtag[4] + hexdehashtag[5], 16)
            except ValueError:
                raise Exception(
                    f"{hex} Is not a correct hex code. Format your hex code to look like, #FFFFFF or FFFFFF"
                )

        else:
            raise Exception(
                f"{hex} Is not a correct hex code. Format your hex code to look like, #FFFFFF or FFFFFF"
            )

        return f"*/hex-bg:{red},{str(green).zfill(3)},{str(blue).zfill(3)}/*"

    @classmethod
    def clear(cls):
        import os
        import sys

        if "idlelib" in sys.modules:
            try:
                shell_connect = sys.stdout.shell
                cls.ostype = 1
            except AttributeError:
                cls.ostype = -1
        else:
            cls.ostype = 2

        if cls.ostype == 1:
            print("\n" * 5)
            print("\n" * 5)
            print("\n" * 5)
            print("\n" * 5)
            print("\n" * 5)
            print("\n" * 5)
        elif cls.ostype == 2:
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
        elif cls.ostype == -1:
            raise Exception("Rainbow-Snake does not support your os or interpreter")
        else:
            raise Exception("Rainbow-Snake does not support your os or interpreter")


color.clear()
color.clear()

print(f"{color.hexbg('#ff780F')}Hi{color.hexbgOFF}")
