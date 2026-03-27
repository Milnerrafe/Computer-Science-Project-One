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

    bold = "*/bold/*"
    boldOFF = "*/bold:OFF/*"

    hexOFF = ""

    @classmethod
    def output(cls, string):
        import os
        import re
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
            styleTable = {
                "error": ("shell_connect.write('", "', 'COMMENT')"),
                "warning": ("shell_connect.write('", "', 'KEYWORD')"),
                "success": ("shell_connect.write('", "', 'STRING')"),
                "information": ("shell_connect.write('", "', 'stdout')"),
                "important": ("shell_connect.write('", "', 'BUILTIN')"),
                "bold": ("shell_connect.write('", "', 'SYNC')"),
            }

            pattern = r"\*/(error|warning|success|information|important|context|bold)(?::(OFF))?/\*"

            import re

            def replOStypeone(m):
                esccode = m.group(1)
                is_off = m.group(2) == "OFF"

                if esccode not in styleTable:
                    return ""

                open_code, close_code = styleTable[esccode]
                return close_code if is_off else open_code

            result = re.sub(pattern, replOStypeone, string)

            patterntwo = r"(shell_connect\.write\([^)]*\))"

            parts = re.split(patterntwo, result)

            output = []

            for part in parts:
                if re.match(patterntwo, part):
                    output.append(part)
                else:
                    output.append(f"shell_connect.write('{part}', 'stdout')")

            result = "\n".join(output)

            exec(result)

            shell_connect.write("\n", "stdout")

        elif cls.ostype == 2:
            styleTable = {
                "error": "\x1b[1m\x1b[38;2;255;255;255m\x1b[48;2;255;60;60m",
                "warning": "\x1b[1m\x1b[38;2;255;255;255m\x1b[48;2;255;219;60m",
                "success": "\x1b[1m\x1b[38;2;255;255;255m\x1b[48;2;57;226;0m",
                "information": "\x1b[1m\x1b[38;2;255;255;255m\x1b[48;2;60;135;255m",
                "important": "\x1b[1m\x1b[38;2;255;255;255m\x1b[48;2;255;60;209m",
                "bold": "\x1b[1m",
            }

            pattern = r"\*/(error|warning|success|information|important|context|bold)(?::(OFF))?/\*"

            import re

            def replOStypetwo(m):
                esccode = m.group(1)
                is_off = m.group(2) == "OFF"

                if esccode not in styleTable:
                    return ""

                open_esccode = styleTable[esccode]
                return "\x1b[0m" if is_off else open_esccode

            result = re.sub(pattern, replOStypetwo, string)

            print(result)

        elif cls.ostype == -1:
            raise Exception("Rainbow-Snake does not support your os or interpreter")
        else:
            raise Exception("Rainbow-Snake does not support your os or interpreter")

    @classmethod
    def hextext(cls, hex):
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
            return ""
        elif cls.ostype == 2:
            cls.hexOFF = "\x1b[0m"

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

            return f"\x1b[38;2;{red};{green};{blue}m"
        elif cls.ostype == -1:
            raise Exception("Rainbow-Snake does not support your os or interpreter")
        else:
            raise Exception("Rainbow-Snake does not support your os or interpreter")

    @classmethod
    def hexbg(cls, hex):
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
            return ""
        elif cls.ostype == 2:
            cls.hexOFF = "\x1b[0m"

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

            return f"\x1b[48;2;{red};{green};{blue}m"
        elif cls.ostype == -1:
            raise Exception("Rainbow-Snake does not support your os or interpreter")
        else:
            raise Exception("Rainbow-Snake does not support your os or interpreter")

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
