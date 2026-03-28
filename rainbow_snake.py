class color:
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
    def whichos(cls):
        import sys

        if "idlelib" in sys.modules:
            try:
                shell_connect = sys.stdout.shell
                return "idle"
            except AttributeError:
                return "unknown"
        else:
            return "terminal"

    @classmethod
    def output(cls, string):
        match cls.whichos():
            case "idle":
                import sys

                shell_connect = sys.stdout.shell

                string = string.replace("\n", "{color.newline()}")

                styleTable = {
                    "error": ("shell_connect.write(f'''", "''', 'COMMENT')"),
                    "warning": ("shell_connect.write(f'''", "''', 'KEYWORD')"),
                    "success": ("shell_connect.write(f'''", "''', 'STRING')"),
                    "information": ("shell_connect.write(f'''", "''', 'stdout')"),
                    "important": ("shell_connect.write(f'''", "''', 'BUILTIN')"),
                    "bold": ("shell_connect.write(f'''", "''', 'SYNC')"),
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

                patterntwo = r"(shell_connect\.write\((?:[^()]*|\([^()]*\))*\))"

                parts = re.split(patterntwo, result)

                output = []

                for part in parts:
                    if re.match(patterntwo, part):
                        output.append(part)
                    else:
                        output.append(f"shell_connect.write(f'''{part}''', 'stdout')")

                codetorun = "\n".join(output)

                exec(codetorun)

                shell_connect.write("\n", "stdout")

            case "terminal":
                styleTable = {
                    "error": "\x1b[1m\x1b[38;2;255;255;255m\x1b[48;2;255;60;60m",
                    "warning": "\x1b[1m\x1b[38;2;0;0;0m\x1b[48;2;255;219;60m",
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

            case "unknown":
                import re

                removedcodes = re.sub(
                    r"\*/(error|warning|success|information|important|context|bold)(?::(OFF))?/\*",
                    "",
                    string,
                )
                print(removedcodes)

            case _:
                import re

                removedcodes = re.sub(
                    r"\*/(error|warning|success|information|important|context|bold)(?::(OFF))?/\*",
                    "",
                    string,
                )
                print(removedcodes)

    @classmethod
    def input(cls, string):
        match cls.whichos():
            case "idle":
                import sys

                shell_connect = sys.stdout.shell

                string = string.replace("\n", "{color.newline()}")

                styleTable = {
                    "error": ("shell_connect.write(f'''", "''', 'COMMENT')"),
                    "warning": ("shell_connect.write(f'''", "''', 'KEYWORD')"),
                    "success": ("shell_connect.write(f'''", "''', 'STRING')"),
                    "information": ("shell_connect.write(f'''", "''', 'stdout')"),
                    "important": ("shell_connect.write(f'''", "''', 'BUILTIN')"),
                    "bold": ("shell_connect.write(f'''", "''', 'SYNC')"),
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

                patterntwo = r"(shell_connect\.write\((?:[^()]*|\([^()]*\))*\))"

                parts = re.split(patterntwo, result)

                output = []

                for part in parts:
                    if re.match(patterntwo, part):
                        output.append(part)
                    else:
                        output.append(f"shell_connect.write(f'''{part}''', 'stdout')")

                codetorun = "\n".join(output)

                exec(codetorun)

                returnvar = input("")

                return returnvar

            case "terminal":
                styleTable = {
                    "error": "\x1b[1m\x1b[38;2;255;255;255m\x1b[48;2;255;60;60m",
                    "warning": "\x1b[1m\x1b[38;2;0;0;0m\x1b[48;2;255;219;60m",
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

                returnvar = input(result)

                return returnvar

            case "unknown":
                import re

                removedcodes = re.sub(
                    r"\*/(error|warning|success|information|important|context|bold)(?::(OFF))?/\*",
                    "",
                    string,
                )

                returnvar = input(removedcodes)

                return returnvar

            case _:
                import re

                removedcodes = re.sub(
                    r"\*/(error|warning|success|information|important|context|bold)(?::(OFF))?/\*",
                    "",
                    string,
                )
                print(removedcodes)

    @classmethod
    def hextext(cls, hex):
        match cls.whichos():
            case "terminal":
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

                    return f"\x1b[38;2;{red};{green};{blue}m"

            case _:
                return ""

    @classmethod
    def hexbg(cls, hex):
        match cls.whichos():
            case "terminal":
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

                    return f"\x1b[48;2;{red};{green};{blue}m"

            case _:
                return ""

    @classmethod
    def clear(cls):
        import os

        match cls.whichos():
            case "terminal":
                if os.name == "nt":
                    os.system("cls")
                else:
                    os.system("clear")

            case _:
                print("\n" * 5)
                print("\n" * 5)
                print("\n" * 5)
                print("\n" * 5)
                print("\n" * 5)
                print("\n" * 5)

    @classmethod
    def newline(cls):
        return "\n"
