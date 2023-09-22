from user import User
def main():
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    while True:
        print(f"{BLUE}************************************************{RESET}")
        print(f"{BLUE}Crowd-Funding Console Application \U0001F600{RESET}")
        print(f"{BLUE}************************************************{RESET}")
        print(f"{YELLOW}Choose Number From The List Below \U0001F601")
        print("[1] Registration")
        print("[2] Login")
        print("[3] Exit")
        print(f"*************************************************{RESET}")
        choise = input(f"{YELLOW}Enter Your Choise: {RESET}").strip()
        if choise.isnumeric():
            choise = int(choise)
            if choise == 1:
                print(f"{BLUE}Welcome To Registration \U0001F600{RESET}")
                User.registration()
            elif choise == 2:
                print(f"{BLUE}Welcome To Login \U0001F600{RESET}")
                User.login()
            elif choise == 3:
                print(f"{BLUE}Good Bye, See You Again \u2764{RESET}")
                exit()
            else:
                print(f"{RED}Invalid Choise \U0001F612{RESET}")
        else:
            print(f"{RED}Invalid Input \U0001F612{RESET}")

if __name__ == "__main__":
    main()