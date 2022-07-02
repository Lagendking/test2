from util.idk import *
colorama.init(autoreset=True)
os.system("cls")


def delete_last_line():
    sys.stdout.write("\x1b[1A")
    sys.stdout.write("\x1b[2K")

def load(db, clr, clr2, clr3):
    if not db: #First run
        clr = Fore.GREEN
        clr2 = Fore.LIGHTGREEN_EX
        clr3 = Fore.LIGHTRED_EX

    print(f"""{clr}                                                                                                                                      

                                        ██╗  ██╗ █████╗  █████╗ ██╗  ██╗██╗   ██╗
    (Hacky V1.0.0)                      ██║  ██║██╔══██╗██╔══██╗██║ ██╔╝╚██╗ ██╔╝
    (Created by Lagend)                 ███████║███████║██║  ╚═╝█████═╝  ╚████╔╝
                                        ██╔══██║██╔══██║██║  ██╗██╔═██╗   ╚██╔╝
                                        ██║  ██║██║  ██║╚█████╔╝██║ ╚██╗   ██║
                                        ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝   ╚═╝""".replace("█", f"{Fore.WHITE}█{clr}") + f"""                                                                                                                                                                       
    {clr2}┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃   [{clr3}1{clr2}] = idk   ┃   [{clr3}3{clr2}] = idk   ┃   [{clr3}5{clr2}] = idk       ┃                                                           ┃
    ┃   [{clr3}2{clr2}] = idk   ┃   [{clr3}4{clr2}] = idk   ┃   [{clr3}6{clr2}] = Settings  ┃                                                           ┃
    ┗━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ \n""")

def pick(db):

    global clr
    global clr2
    global clr3

    if not db: #First run
        clr = Fore.GREEN
        clr2 = Fore.LIGHTGREEN_EX
        clr3 = Fore.LIGHTRED_EX

    choice = input(f"{Fore.WHITE}[{Fore.LIGHTCYAN_EX}>>>{Fore.WHITE}]: ")
    choices = ["1", "2", "3", "4", "5", "6"] #Main choices
    choices2 = ["1", "2"] #Settings choices
    choices3 = ["1", "2", "3", "4", "5"] #Color choices
    hacky = "Hacky V1.0.0"
    delete_last_line()

    if not choice in choices: #incorrect choice
        print("Option not found")
        time.sleep(1)
        delete_last_line()
        pick(True)
        
    else:
        if choice == "6": #settings
            for x in range(0, 5):
                delete_last_line()

            print(f"{clr3}Settings")
            print(f"{clr2}[{clr3}1{clr2}] = Colors")
            print(f"{clr2}[{clr3}2{clr2}] = Delete")
            schoice = input(f"{Fore.WHITE}[{Fore.LIGHTCYAN_EX}>>>{Fore.WHITE}]: ")

            if schoice in choices2:
                if schoice == "1": #color settings
                    for x in range(0, 2 + len(choices2)):
                        delete_last_line()

                    print(f"{clr3}Colors")
                    print(f"{clr2}[{clr3}1{clr2}] = {Fore.GREEN}Green")
                    print(f"{clr2}[{clr3}2{clr2}] = {Fore.RED}Red")
                    print(f"{clr2}[{clr3}3{clr2}] = {Fore.MAGENTA}Purple")
                    print(f"{clr2}[{clr3}4{clr2}] = {Fore.BLUE}Blue")
                    print(f"{clr2}[{clr3}5{clr2}] = {Fore.YELLOW}Yellow")
                    cchoice = input(f"{Fore.WHITE}[{Fore.LIGHTCYAN_EX}>>>{Fore.WHITE}]: ")

                    if cchoice in choices3:
                        if cchoice == "1": #Green
                            os.system("cls")
                            clr = Fore.GREEN
                            clr2 = Fore.LIGHTGREEN_EX
                            clr3 = Fore.LIGHTRED_EX
                            load(True, clr, clr2, clr3)
                            pick(True)

                        elif cchoice == "2": #Red
                            os.system("cls")
                            clr = Fore.RED
                            clr2 = Fore.LIGHTRED_EX
                            clr3 = Fore.WHITE
                            load(True, clr, clr2, clr3)
                            pick(True)

                        elif cchoice == "3": #Purple
                            os.system("cls")
                            clr = Fore.MAGENTA
                            clr2 = Fore.LIGHTMAGENTA_EX
                            clr3 = Fore.LIGHTCYAN_EX
                            load(True, clr, clr2, clr3)
                            pick(True)

                        elif cchoice == "4": #Blue
                            os.system("cls")
                            clr = Fore.BLUE
                            clr2 = Fore.LIGHTBLUE_EX
                            clr3 = Fore.LIGHTCYAN_EX
                            load(True, clr, clr2, clr3)
                            pick(True)

                        elif cchoice == "5": #Yellow
                            os.system("cls")
                            clr = Fore.YELLOW
                            clr2 = Fore.LIGHTYELLOW_EX
                            clr3 = Fore.LIGHTWHITE_EX
                            load(True, clr, clr2, clr3)
                            pick(True)

                    else: #incorrect color choice
                        os.system("cls")
                        load(True, clr, clr2, clr3)
                        pick(True)

                elif schoice == "2": #Delete
                    for x in range(0, 2 + len(choices2)):
                        delete_last_line()
                    rc = input(f"{Fore.RED}Are you sure you want to remove hacky? (Y = yes | N = no) \n{Fore.WHITE}")

                    if rc == "y":
                        delete_last_line()
                        delete_last_line()
                        print(f"{Fore.RED}Removing {hacky}...")

                        for path in Path(os.getcwd()).glob("**/*"): #Delete files and folders
                            if path.is_file():
                                path.unlink()
                            elif path.is_dir():
                                shutil.rmtree(path)

                    else:
                        os.system("cls")
                        load(True, clr, clr2, clr3)
                        pick(True)

            else: #incorrect setting choice
                os.system("cls")
                load(True, clr, clr2, clr3)
                pick(True)

        elif choice == "1": #idk
            pass
            

load(False, Fore.GREEN, Fore.LIGHTGREEN_EX, Fore.LIGHTRED_EX)
pick(False)
