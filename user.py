from project import Project
import re
from getpass import getpass
# Class User
class User:
  # Registration
  @classmethod
  def registration(cls):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    phone_regex = "^01[0125][0-9]{8}$"
    special_symbols = ['$', '@', '#', '_', '-', '!', '%', '&']
    Blocked_symbols = [':', ";"]
    # Check First Name
    while True:
      first_name = input("Enter Your First Name: ").strip()
      if first_name.isalpha():
          break
      else:
          print("Invalid Name!!")
    # Check Last Name
    while True:
      last_name = input("Enter Your Last Name: ").strip()
      if last_name.isalpha():
          break
      else:
          print("Invalid Name!!")
    # Check Email
    while True:
      email = input("Enter Your E-mail Address: ").strip()
      flag = True
      if re.fullmatch(email_regex, email):
          try:
              with open("users.txt") as user_data:
                users = user_data.readlines()
                for user in users:
                    user = user.strip("\n")
                    user_info = user.split(":")
                    if user_info[2] == email:
                        print("This E-mail Is Already Used")
                        flag = False
                        break
          except:
              flag = True
          if flag:
              break
      else:
          print("Invalid Email!!")
    # Check Password
    while True: 
      password = getpass("Enter Your Password: ").strip()
      if len(password) < 6 or len(password) > 20:
          print("Your Password Must Not be Less Than 6 Characters Or More Than 20")
      elif not any(char.isdigit() for char in password):
          print("Password Must Have Number")
      elif not any(char.isupper() for char in password):
          print("Password Must Have Uppercase Letter")
      elif not any(char.islower() for char in password):
          print("Password Must Have Lower Letter")
      elif not any(char in special_symbols for char in password):
          print("Password Must Have Special Character[$@#_!%&]")
      elif any(char in Blocked_symbols for char in password):
          print("Password Mustn't Have This Special Character[:;]")
      else :
          break
    # Check Confirm Password
    while True:
      confirm_password = getpass("Confirm Your Password: ").strip()
      if password == confirm_password:
          break
      else:
          print("Not Matched Password")
    # Check Phone Number
    while True:
      phone_number = input("Enter Your Phone Number [Egypt]: ")
      if re.fullmatch(phone_regex, phone_number):
          break
      else:
          print("Invalid Phone Number!!")
    # Insert User
    user_information = f"{first_name}:{last_name}:{email}:{password}:{confirm_password}:{phone_number}"
    with open("users.txt","a") as user_data:
      # data = user_information.strip("\n")
      data = f"{user_information}\n"
      user_data.write(data)
    print("*************************************************")
    print("You Have Register Successfully, You Will Back To Main Menu To Login......")
    print("*************************************************")
  #******************************************************************************
  # Login 
  @classmethod
  def login(cls):
      while True:
        flag = False
        email = input("Enter Your Email: ").strip()
        password = getpass("Enter Your Password: ").strip()
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
          print("*************************************************")
          print("Login Successfully..!")
          print("*************************************************")
          Project.project_menu(email)
          break
        else:
          print("Invalid Email or Password ,Please Try Again")