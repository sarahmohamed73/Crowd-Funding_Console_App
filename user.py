from project import Project
import re
from getpass import getpass
# Class User
class User:
  RESET = "\033[0m"
  RED = "\033[31m"
  GREEN = "\033[32m"
  YELLOW = "\033[33m"
  BLUE = "\033[34m"
  # Registration
  @classmethod
  def registration(cls):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    phone_regex = "^01[0125][0-9]{8}$"
    special_symbols = ['$', '@', '#', '_', '-', '!', '%', '&']
    Blocked_symbols = [':', ";"]
    # Check First Name
    while True:
      first_name = input(f"{cls.YELLOW}Enter Your First Name: {cls.RESET}").strip()
      if first_name.isalpha():
          break
      else:
          print(f"{cls.RED}Invalid Name!! \U0001F612{cls.RESET}")
    # Check Last Name
    while True:
      last_name = input(f"{cls.YELLOW}Enter Your Last Name: {cls.RESET}").strip()
      if last_name.isalpha():
          break
      else:
          print(f"{cls.RED}Invalid Name!! \U0001F612{cls.RESET}")
    # Check Email
    while True:
      email = input(f"{cls.YELLOW}Enter Your E-mail Address: {cls.RESET}").strip()
      flag = True
      if re.fullmatch(email_regex, email):
          try:
              with open("users.txt") as user_data:
                users = user_data.readlines()
                for user in users:
                    user = user.strip("\n")
                    user_info = user.split(":")
                    if user_info[2] == email:
                        print(f"{cls.RED}This E-mail Is Already Used \U0001F642{cls.RESET}")
                        flag = False
                        break
          except:
              flag = True
          if flag:
              break
      else:
          print(f"{cls.RED}Invalid Email!! \U0001F612{cls.RESET}")
    # Check Password
    while True: 
      password = getpass(f"{cls.YELLOW}Enter Your Password: {cls.RESET}").strip()
      if len(password) < 6 or len(password) > 20:
          print(f"{cls.RED}Your Password Must Not be Less Than 6 Characters Or More Than 20{cls.RESET}")
      elif not any(char.isdigit() for char in password):
          print(f"{cls.RED}Password Must Have Number{cls.RESET}")
      elif not any(char.isupper() for char in password):
          print(f"{cls.RED}Password Must Have Uppercase Letter{cls.RESET}")
      elif not any(char.islower() for char in password):
          print(f"{cls.RED}Password Must Have Lower Letter{cls.RESET}")
      elif not any(char in special_symbols for char in password):
          print(f"{cls.RED}Password Must Have Special Character[$@#_!%&]{cls.RESET}")
      elif any(char in Blocked_symbols for char in password):
          print(f"{cls.RED}Password Mustn't Have This Special Character[:;]{cls.RESET}")
      else:
          break
    # Check Confirm Password
    while True:
      confirm_password = getpass(f"{cls.YELLOW}Confirm Your Password: {cls.RESET}").strip()
      if password == confirm_password:
          break
      else:
          print(f"{cls.RED}Not Matched Password \U0001F607{cls.RESET}")
    # Check Phone Number
    while True:
      phone_number = input(f"{cls.YELLOW}Enter Your Phone Number [Egypt]: {cls.RESET}")
      if re.fullmatch(phone_regex, phone_number):
          break
      else:
          print(f"{cls.RED}Invalid Phone Number!! \U0001F612{cls.RESET}")
    # Insert User
    user_information = f"{first_name}:{last_name}:{email}:{password}:{confirm_password}:{phone_number}"
    with open("users.txt","a") as user_data:
      # data = user_information.strip("\n")
      data = f"{user_information}\n"
      user_data.write(data)
    print("*************************************************")
    print(f"{cls.GREEN}You Have Register Successfully, You Will Back To Main Menu To Login... \u2764{cls.RESET}")
    print("*************************************************")
  #******************************************************************************
  # Login 
  @classmethod
  def login(cls):
      while True:
        flag = False
        email = input(f"{cls.YELLOW}Enter Your Email: {cls.RESET}").strip()
        password = getpass(f"{cls.YELLOW}Enter Your Password: {cls.RESET}").strip()
        try:
          with open("users.txt") as user_data:
              users = user_data.readlines()
              for user in users:
                user = user.strip("\n")
                user_info = user.split(":")
                if user_info[2] == email and user_info[3] == password: 
                  flag = True 
                  break
        except:
          flag = False
        if flag:
          print(f"{cls.GREEN}*************************************************")
          print("Login Successfully... \u2764")
          print(f"*************************************************{cls.RESET}")
          Project.project_menu(email)
          break
        else:
          print(f"{cls.RED}Invalid Email or Password ,Please Try Again \U0001F612{cls.RESET}")