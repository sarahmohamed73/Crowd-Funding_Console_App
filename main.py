def main():
    while True:
        print("Choose Number From The List Below")
        print("(1) Registration")
        print("(2) Login")
        print("(3) Exit")
        choise = input("Enter Your Choise: ").strip()
        if choise.isnumeric():
            choise = int(choise)
            if choise == 1:
                print("Welcome To Registration")
                registration()
            elif choise == 2:
                print("Welcome To Login")
                login()
            elif choise == 3:
                print("Good Bye, See You Again")
                exit()
            else:
                print("Invalid Choise")
        else:
            print("Invalid Input")


def registration():
    pass

def login():
    pass

main()