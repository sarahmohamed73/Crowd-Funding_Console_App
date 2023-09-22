import re
from datetime import datetime
import os
# Class Project
class Project:
  RESET = "\033[0m"
  RED = "\033[31m"
  GREEN = "\033[32m"
  YELLOW = "\033[33m"
  BLUE = "\033[34m"
  # Project Menu
  @classmethod
  def project_menu(cls, email):
    while True:
        print(f"{cls.YELLOW}*************************************************")
        print("Choose Number From The List Below \U0001F601")
        print("*************************************************")
        print("[1] Create A Project")
        print("[2] View All Projects")
        print("[3] Edit Your Own Projects")
        print("[4] Delete Your Own Project")
        print("[5] Search For A Project")
        print("[6] Back")
        print("[7] Exit")
        print(f"*************************************************{cls.RESET}")
        user_email = email
        choise = input(f"{cls.YELLOW}Enter Your Choise: {cls.RESET}").strip()
        if choise.isnumeric():
          choise = int(choise)
          if choise == 1:
            cls.create_project(user_email)
          elif choise == 2:
            cls.view_projects(user_email)
          elif choise == 3:
            cls.edit_project(user_email)
          elif choise == 4:
            cls.delete_project(user_email)
          elif choise == 5:
            cls.search_for_project(user_email)
          elif choise == 6:
            return
          elif choise == 7:
            print(f"{cls.BLUE}Good Bye, See You Again \u2764{cls.RESET}")
            exit()
          else:
            print(f"{cls.RED}Invalid Choise \U0001F612{cls.RESET}")
        else:
          print(f"{cls.RED}Invalid Input \U0001F612{cls.RESET}")
  #****************************************************************************** 
  # Create Project
  @classmethod
  def create_project(cls, email):
    # Check Title
    title_regex = '[a-zA-Z][_a-zA-Z0-9]*'
    while True:
      title = input(f"{cls.YELLOW}Enter Your Project Title: {cls.RESET}").strip()
      flag = True
      if re.fullmatch(title_regex, title):
        try:
            with open("projects.txt") as project_data:
              projects = project_data.readlines()
              for project in projects:
                project = project.strip("\n")
                project_info = project.split(":")
                if project_info[1] == title:
                  print(f"{cls.RED}This Project Title Is Already Used \U0001F642{cls.RESET}")
                  flag = False
                  break
        except:
          flag = True
        if flag:
          break
      else:
        print(f"{cls.RED}Invalid Project Title!! \U0001F607{cls.RESET}")
    
    # Get Project Details
    details = input(f"{cls.YELLOW}Enter The Project Details: {cls.RESET}")

    # Check Target
    while True:
      target = input(f"{cls.YELLOW}Enter The Project Target In EGP: {cls.RESET}")
      if target.isnumeric():
        break
      else:
        print(f"{cls.RED}Invalid Input!! \U0001F612{cls.RESET}")
    
    # Check Start Date
    while True:
      start_date = input(f"{cls.YELLOW}Enter The Start Date For The Project in This Format [YYYY-MM-DD]: {cls.RESET}")
      time_regex = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
      year = datetime.now().year
      month = datetime.now().month
      day = datetime.now().day
      today_date = f"{year}-{month}-{day}"
      if re.fullmatch(time_regex, start_date):
        today_date = datetime.strptime(today_date, '%Y-%m-%d')
        today_date = str(today_date.strftime("%Y-%m-%d"))
        # today_date = str(today_date)
        if today_date <= start_date:
          break
        else:
          print(f"{cls.RED}Start Date Can't Be Before Today!! \U0001F910{cls.RESET}")
      else:
        print(f"{cls.RED}Incorrect Data Format, Should Be [YYYY-MM-DD] \U0001F607{cls.RESET}")

    # Check End Date
    while True:
      time_regex = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
      end_date = input(f"{cls.YELLOW}Enter The End Date For The Project in This Format [YYYY-MM-DD]: {cls.RESET}")
      if re.fullmatch(time_regex, end_date):
        if start_date < end_date:
            break
        else:
            print(f"{cls.RED}End Date Can't Be Before Start Date!! \U0001F910{cls.RESET}")
      else:
        print(f"{cls.RED}Incorrect Data Format, Should Be [YYYY-MM-DD] \U0001F607{cls.RESET}")

    # Insert Project
    project_information = f"{email}:{title}:{details}:{target}:{start_date}:{end_date}"
    with open("projects.txt", "a") as project_data:
      # data = user_information.strip("\n")
      data = f"{project_information}\n"
      project_data.write(data)
    print(f"{cls.GREEN}You Add Project Successfully, You Will Back To Menu... \u2764{cls.RESET}")

  #******************************************************************************
  # View Project
  @classmethod
  def view_projects(cls, email):
    flag = False
    try:
      with open("projects.txt") as project_data:
        projects = project_data.readlines()
        counter = 1
        for project in projects:
          project = project.strip("\n")
          project_information = project.split(":")
          if email == project_information[0]:
            print(f"{cls.BLUE}========================== Project {counter}  \u2764 ===========================")
            print(f"User Email:         {project_information[0]}")
            print(f"Project Title:      {project_information[1]}")
            print(f"Details:            {project_information[2]}")
            print(f"Total Target:       {project_information[3]}")
            print(f"Start Date:         {project_information[4]}")
            print(f"End Date:           {project_information[5]}{cls.RESET}")
            counter += 1
            flag = True
    except:
      flag = False
    if not flag:
      print(f"{cls.BLUE}*************************************************")
      print("You have No Projects Yet, You Will Back To Menu... \U0001F607")
      print(f"*************************************************{cls.RESET}")

  #******************************************************************************
  # Edit Project
  @classmethod
  def edit_project(cls, email):
    while True:
      print(f"{cls.YELLOW}*************************************************")
      print("Choose Number From The List Below")
      print("*************************************************")
      print("[1] Edit Title")
      print("[2] Edit Details")
      print("[3] Edit Total Target")
      print("[4] Edit Start Date")
      print("[5] Edit End Date")
      print("[6] Back")
      print("*************************************************")
      user_email = email
      choise = input(f"Enter Your Choise: {cls.RESET}").strip()
      if choise.isnumeric():
        choise = int(choise)
        if choise == 1:
          cls.edit_title(user_email)
        elif choise == 2:
          cls.edit_details(user_email)
        elif choise == 3:
          cls.edit_target(user_email)
        elif choise == 4:
          cls.edit_start_date(user_email)
        elif choise == 5:
          cls.edit_end_date(user_email)
        elif choise == 6:
          return
        else:
         print(f"{cls.RED}Invalid Choise!! \U0001F612{cls.RESET}")
      else:
        print(f"{cls.RED}Invalid Input!! \U0001F612{cls.RESET}")

  @classmethod
  def edit_title(cls, email):
    title_regex = '[a-zA-Z][_a-zA-Z0-9]*'
    flag = False
    while True:
      title = input(f"{cls.YELLOW}Enter The Project Title: {cls.RESET}").strip()
      if re.fullmatch(title_regex, title):
          break
      else:
          print(f"{cls.RED}Invalid Project Title!! \U0001F612{cls.RESET}")
    try:
      with open("projects.txt") as project_data:
        projects = project_data.readlines()
        for project in projects:
          project = project.strip("\n")
          project_information = project.split(":")
          if email == project_information[0]:
            if title == project_information[1]:
              while True:
                new_title = input(f"{cls.YELLOW}Enter New Title: {cls.RESET}").strip()
                flag = True
                if re.fullmatch(title_regex, new_title):
                  try:
                      with open("projects.txt") as project_data:
                        projects = project_data.readlines()
                        for project in projects:
                          project = project.strip("\n")
                          project_info = project.split(":")
                          if project_info[1] == new_title:
                            print(f"{cls.RED}This Project Title Is Already Used \U0001F642{cls.RESET}")
                            flag = False
                            break
                  except:
                    flag = True
                  if flag:
                    break
                else:
                  print(f"{cls.RED}Invalid Project Title!! \U0001F612{cls.RESET}")
              project_information[1] = new_title
              new_information = ":".join(project_information)
              with open("temp.txt", "a") as new_file:
                data = new_information.strip("\n")
                data = f"{data}\n"
                new_file.writelines(data)
                print(f"{cls.GREEN}*************************************************")
                print("Title Changed Successfully...  \u2764")
                print(f"*************************************************{cls.RESET}")
                flag = True
            else:
              project_information = ":".join(project_information)
              with open("temp.txt", "a") as new_file:
                  data = project_information.strip("\n")
                  data = f"{data}\n"
                  new_file.writelines(data)
          else:
            project_information = ":".join(project_information)
            with open("temp.txt", "a") as new_file:
                data = project_information.strip("\n")
                data = f"{data}\n"
                new_file.writelines(data)
    except:
      flag = False
    if not flag:
      print(f"{cls.RED}*************************************************")
      print("There Is No Project With This Title \U0001F607")
      print(f"*************************************************{cls.RESET}")
    os.remove("projects.txt")
    os.rename("temp.txt", "projects.txt")
  
  # Change Details
  @classmethod
  def edit_details(cls, email):
    title_regex = '[a-zA-Z][_a-zA-Z0-9]*'
    flag = False
    while True:
      title = input(f"{cls.YELLOW}Enter The Project Title: {cls.RESET}").strip()
      if re.fullmatch(title_regex, title):
          break
      else:
          print(f"{cls.RED}Invalid Project Title!! \U0001F612{cls.RESET}")
    try:
      with open("projects.txt") as project_data:
        projects = project_data.readlines()
        for project in projects:
          project = project.strip("\n")
          project_information = project.split(":")
          if email == project_information[0]:
            if title == project_information[1]:
              new_details = input(f"{cls.YELLOW}Enter New Details: {cls.RESET}").strip()
              project_information[2] = new_details
              new_information = ":".join(project_information)
              with open("temp.txt", "a") as new_file:
                data = new_information.strip("\n")
                data = f"{data}\n"
                new_file.writelines(data)
                print(f"{cls.GREEN}*************************************************")
                print("Details Changed Successfully...  \u2764")
                print(f"*************************************************{cls.RESET}")
                flag = True
            else:
              project_information = ":".join(project_information)
              with open("temp.txt", "a") as new_file:
                  data = project_information.strip("\n")
                  data = f"{data}\n"
                  new_file.writelines(data)
          else:
            project_information = ":".join(project_information)
            with open("temp.txt", "a") as new_file:
                data = project_information.strip("\n")
                data = f"{data}\n"
                new_file.writelines(data)
    except:
      flag = False
    if not flag:
      print(f"{cls.RED}*************************************************")
      print("There Is No Project With This Title \U0001F607")
      print(f"*************************************************{cls.RESET}")
    os.remove("projects.txt")
    os.rename("temp.txt", "projects.txt")

  # Change Total Target
  @classmethod
  def edit_target(cls, email):
    title_regex = '[a-zA-Z][_a-zA-Z0-9]*'
    flag = False
    while True:
      title = input(f"{cls.YELLOW}Enter The Project Title: {cls.RESET}").strip()
      if re.fullmatch(title_regex, title):
          break
      else:
          print(f"{cls.RED}Invalid Project Title!! \U0001F612{cls.RESET}")
    try:
      with open("projects.txt") as project_data:
        projects = project_data.readlines()
        for project in projects:
          project = project.strip("\n")
          project_information = project.split(":")
          if email == project_information[0]:
            if title == project_information[1]:
              while True:
                new_target = input(f"{cls.YELLOW}Enter The New Target In EGP: {cls.RESET}")
                if new_target.isnumeric():
                  break
                else:
                  print(f"{cls.RED}Invalid Input!! \U0001F612{cls.RESET}")
              project_information[3] = new_target
              new_information = ":".join(project_information)
              with open("temp.txt", "a") as new_file:
                data = new_information.strip("\n")
                data = f"{data}\n"
                new_file.writelines(data)
                print(f"{cls.GREEN}*************************************************")
                print("Total Target Changed Successfully...  \u2764")
                print(f"*************************************************{cls.RESET}")
                flag = True
            else:
              project_information = ":".join(project_information)
              with open("temp.txt", "a") as new_file:
                  data = project_information.strip("\n")
                  data = f"{data}\n"
                  new_file.writelines(data)
          else:
            project_information = ":".join(project_information)
            with open("temp.txt", "a") as new_file:
                data = project_information.strip("\n")
                data = f"{data}\n"
                new_file.writelines(data)
    except:
      flag = False
    if not flag:
      print(f"{cls.RED}*************************************************")
      print("There Is No Project With This Title \U0001F607")
      print(f"*************************************************{cls.RESET}")
    os.remove("projects.txt")
    os.rename("temp.txt", "projects.txt")

  # Change Start Date
  @classmethod
  def edit_start_date(cls, email):
    title_regex = '[a-zA-Z][_a-zA-Z0-9]*'
    flag = False
    while True:
      title = input(f"{cls.YELLOW}Enter The Project Title: {cls.RESET}").strip()
      if re.fullmatch(title_regex, title):
          break
      else:
          print(f"{cls.RED}Invalid Project Title!! \U0001F612{cls.RESET}")
    try:
      with open("projects.txt") as project_data:
        projects = project_data.readlines()
        for project in projects:
          project = project.strip("\n")
          project_information = project.split(":")
          if email == project_information[0]:
            if title == project_information[1]:
              while True:
                new_start_date = input(f"{cls.YELLOW}Enter The New Start Date For The Project in This Format [YYYY-MM-DD]: {cls.RESET}")
                time_regex = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
                year = datetime.now().year
                month = datetime.now().month
                day = datetime.now().day
                today_date = f"{year}-{month}-{day}"
                if re.fullmatch(time_regex, new_start_date):
                  today_date = datetime.strptime(today_date, '%Y-%m-%d')
                  today_date = str(today_date.strftime("%Y-%m-%d"))
                  # today_date = str(today_date)
                  if today_date <= new_start_date and project_information[5] > new_start_date:
                    break
                  else:
                    print(f"{cls.RED}Start Date Can't Be Before Today or After End Date!! \U0001F910{cls.RESET}")
                else:
                  print(f"{cls.RED}Incorrect Data Format, Should Be [YYYY-MM-DD] \U0001F607{cls.RESET}")
              project_information[4] = new_start_date
              new_information = ":".join(project_information)
              with open("temp.txt", "a") as new_file:
                data = new_information.strip("\n")
                data = f"{data}\n"
                new_file.writelines(data)
                print(f"{cls.GREEN}*************************************************")
                print("Start Date Changed Successfully...  \u2764")
                print(f"*************************************************{cls.RESET}")
                flag = True
            else:
              project_information = ":".join(project_information)
              with open("temp.txt", "a") as new_file:
                  data = project_information.strip("\n")
                  data = f"{data}\n"
                  new_file.writelines(data)
          else:
            project_information = ":".join(project_information)
            with open("temp.txt", "a") as new_file:
                data = project_information.strip("\n")
                data = f"{data}\n"
                new_file.writelines(data)
    except:
      flag = False
    if not flag:
      print(f"{cls.RED}*************************************************")
      print("There Is No Project With This Title \U0001F607")
      print(f"*************************************************{cls.RESET}")
    os.remove("projects.txt")
    os.rename("temp.txt", "projects.txt")

  # Change End Date
  @classmethod
  def edit_end_date(cls, email):
    title_regex = '[a-zA-Z][_a-zA-Z0-9]*'
    flag = False
    while True:
      title = input(f"{cls.YELLOW}Enter The Project Title: {cls.RESET}").strip()
      if re.fullmatch(title_regex, title):
          break
      else:
          print(f"{cls.RED}Invalid Project Title!! \U0001F612{cls.RESET}")
    try:
      with open("projects.txt") as project_data:
        projects = project_data.readlines()
        for project in projects:
          project = project.strip("\n")
          project_information = project.split(":")
          if email == project_information[0]:
            if title == project_information[1]:
              while True:
                time_regex = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
                new_end_date = input(f"{cls.YELLOW}Enter The New End Date For The Project in This Format [YYYY-MM-DD]: {cls.RESET}")
                if re.fullmatch(time_regex, new_end_date):
                  if project_information[4] < new_end_date:
                      break
                  else:
                      print(f"{cls.RED}End Date Can't Be Before Start Date!! \U0001F910{cls.RESET}")
                else:
                  print(f"{cls.RED}Incorrect Data Format, Should Be [YYYY-MM-DD] \U0001F607{cls.RESET}")
              project_information[5] = new_end_date
              new_information = ":".join(project_information)
              with open("temp.txt", "a") as new_file:
                data = new_information.strip("\n")
                data = f"{data}\n"
                new_file.writelines(data)
                print(f"{cls.GREEN}*************************************************")
                print("End Date Changed Successfully...  \u2764")
                print(f"*************************************************{cls.RESET}")
                flag = True
            else:
              project_information = ":".join(project_information)
              with open("temp.txt", "a") as new_file:
                  data = project_information.strip("\n")
                  data = f"{data}\n"
                  new_file.writelines(data)
          else:
            project_information = ":".join(project_information)
            with open("temp.txt", "a") as new_file:
                data = project_information.strip("\n")
                data = f"{data}\n"
                new_file.writelines(data)
    except:
      flag = False
    if not flag:
      print(f"{cls.RED}*************************************************")
      print("There Is No Project With This Title \U0001F607")
      print(f"*************************************************{cls.RESET}")
    os.remove("projects.txt")
    os.rename("temp.txt", "projects.txt")

  #******************************************************************************
  # Delete Project
  @classmethod
  def delete_project(cls, email):
    title_regex = '[a-zA-Z][_a-zA-Z0-9]*'
    flag = False
    while True:
      title = input(f"{cls.YELLOW}Enter The Project Title: {cls.RESET}").strip()
      if re.fullmatch(title_regex, title):
          break
      else:
          print(f"{cls.RED}Invalid Project Title!! \U0001F612{cls.RESET}")
    try:
      with open("projects.txt") as project_data:
        projects = project_data.readlines()
        for project in projects:
          project = project.strip("\n")
          project_information = project.split(":")
          if email == project_information[0]:
            if title != project_information[1]:
              project_information = ":".join(project_information)
              with open("temp.txt", "a") as new_file:
                  data = project_information.strip("\n")
                  data = f"{data}\n"
                  new_file.writelines(data)
            else:
              flag = True
          else:
            project_information = ":".join(project_information)
            with open("temp.txt", "a") as new_file:
                data = project_information.strip("\n")
                data = f"{data}\n"
                new_file.writelines(data)
    except:
      flag = False
    if not flag:
      print(f"{cls.RED}*************************************************")
      print("There Is No Project With This Title \U0001F607")
      print(f"*************************************************{cls.RESET}")
    else:
      print(f"{cls.GREEN}*************************************************")
      print("Your Record Has Been Deleted Successfully...  \u2764")
      print(f"*************************************************{cls.RESET}")
    os.remove("projects.txt")
    os.rename("temp.txt", "projects.txt")
  #******************************************************************************
  # Search For A Project
  @classmethod
  def search_for_project(cls, email):
    time_regex = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
    flag = False
    while True:
      start_date = input(f"{cls.YELLOW}Enter The Start Date For The Project You Want in This Format [YYYY-MM-DD]: {cls.RESET}")
      if re.fullmatch(time_regex, start_date):
        break
      else:
        print(f"{cls.RED}Incorrect Data Format, Should Be [YYYY-MM-DD] \U0001F607{cls.RESET}")
    while True:
      end_date = input(f"{cls.YELLOW}Enter The End Date For The Project You Want in This Format [YYYY-MM-DD]: {cls.RESET}")
      if re.fullmatch(time_regex, end_date):
        break
      else:
        print(f"{cls.RED}Incorrect Data Format, Should Be [YYYY-MM-DD] \U0001F607{cls.RESET}")
    try:
      with open("projects.txt") as project_data:
        projects = project_data.readlines()
        for project in projects:
          project = project.strip("\n")
          project_information = project.split(":")
          if email == project_information[0]:
            if start_date == project_information[4] and end_date == project_information[5]:
              print(f"{cls.BLUE}========================== Project {project_information[1]} ===========================")
              print(f"User Email:         {project_information[0]}")
              print(f"Project Title:      {project_information[1]}")
              print(f"Details:            {project_information[2]}")
              print(f"Total Target:       {project_information[3]}")
              print(f"Start Date:         {project_information[4]}")
              print(f"End Date:           {project_information[5]}{cls.RESET}")
              flag = True
    except:
      flag = False
    if not flag: 
      print(f"{cls.RED}*************************************************")
      print("There Is No Project With This Date \U0001F607")
      print(f"*************************************************{cls.RESET}")