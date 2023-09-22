import re
from getpass import getpass
from datetime import datetime
import os
# Class Project
class Project:
  # Project Menu
  @classmethod
  def project_menu(cls, email):
    while True:
        print("*************************************************")
        print("Choose Number From The List Below")
        print("*************************************************")
        print("[1] Create A Project")
        print("[2] View All Projects")
        print("[3] Edit Your Own Projects")
        print("[4] Delete Your Own Project")
        print("[5] Search For A Project")
        print("[6] Back")
        print("[7] Exit")
        print("*************************************************")
        user_email = email
        choise = input("Enter Your Choise: ").strip()
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
            print("Good Bye, See You Again")
            exit()
          else:
            print("Invalid Choise")
        else:
          print("Invalid Input")
  #****************************************************************************** 
  # Create Project
  @classmethod
  def create_project(cls, email):
    # Check Title
    title_regex = '[a-zA-Z][_a-zA-Z0-9]*'
    while True:
      title = input("Enter Your Project Title: ").strip()
      flag = True
      if re.fullmatch(title_regex, title):
        try:
            with open("projects.txt") as project_data:
              projects = project_data.readlines()
              for project in projects:
                project = project.strip("\n")
                project_info = project.split(":")
                if project_info[1] == title:
                  print("This Project Title Is Already Used")
                  flag = False
                  break
        except:
          flag = True
        if flag:
          break
      else:
        print("Invalid Project Title!!")
    
    # Get Project Details
    details = input("Enter The Project Details: ")

    # Check Target
    while True:
      target = input("Enter The Project Target In EGP: ")
      if target.isnumeric():
        break
      else:
        print("Invalid Input!!")
    
    # Check Start Date
    while True:
      start_date = input("Enter The Start Date For The Project in This Format [YYYY-MM-DD]: ")
      time_regex = r'^\d{4}-\d{2}-\d{2}$'
      year = datetime.now().year
      month = datetime.now().month
      day = datetime.now().day
      today_date = f"{year}-{month}-{day}"
      if re.fullmatch(time_regex, start_date):
        today_date = datetime.strptime(today_date, '%Y-%m-%d')
        today_date = str(today_date.strftime("%Y-%m-%d"))
        # today_date = str(today_date)
        if today_date < start_date:
          break
        else:
          print("Start Date Can't Be Before Today!!")
      else:
        print("Incorrect Data Format, Should Be [YYYY-MM-DD]")

    # Check End Date
    while True:
      time_regex = r'^\d{4}-\d{2}-\d{2}$'
      end_date = input("Enter The End Date For The Project in This Format [YYYY-MM-DD]: ")
      if re.fullmatch(time_regex, end_date):
        if start_date < end_date:
            break
        else:
            print("End Date Can't Be Before Start Date!!")
      else:
        print("Incorrect Data Format, Should Be [YYYY-MM-DD]")

    # Insert Project
    project_information = f"{email}:{title}:{details}:{target}:{start_date}:{end_date}"
    with open("projects.txt", "a") as project_data:
      # data = user_information.strip("\n")
      data = f"{project_information}\n"
      project_data.write(data)
    print("You Have add project Successfully, You will back to Menu......")

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
            print(f"========================== Project {counter} ===========================")
            print(f"User Email:         {project_information[0]}")
            print(f"Project Title:      {project_information[1]}")
            print(f"Details:            {project_information[2]}")
            print(f"Total Target:       {project_information[3]}")
            print(f"Start Date:         {project_information[4]}")
            print(f"End Date:           {project_information[5]}")
            counter += 1
            flag = True
    except:
      flag = False
    if not flag:
      print("*************************************************")
      print("You have No Projects Yet, You Will Back To Menu.......!")
      print("*************************************************")

  #******************************************************************************
  # Edit Project
  @classmethod
  def edit_project(cls, email):
    while True:
      print("*************************************************")
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
      choise = input("Enter Your Choise: ").strip()
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
          print("Invalid Choise!!")
      else:
        print("Invalid Input!!")

  @classmethod
  def edit_title(cls, email):
    title_regex = '[a-zA-Z][_a-zA-Z0-9]*'
    flag = False
    while True:
      title = input("Enter The Project Title: ").strip()
      if re.fullmatch(title_regex, title):
          break
      else:
          print("Invalid Title")
    try:
      with open("projects.txt") as project_data:
        projects = project_data.readlines()
        for project in projects:
          project = project.strip("\n")
          project_information = project.split(":")
          if email == project_information[0]:
            if title == project_information[1]:
              while True:
                new_title = input("Enter New Title: ").strip()
                flag = True
                if re.fullmatch(title_regex, new_title):
                  try:
                      with open("projects.txt") as project_data:
                        projects = project_data.readlines()
                        for project in projects:
                          project = project.strip("\n")
                          project_info = project.split(":")
                          if project_info[1] == new_title:
                            print("This Project Title Is Already Used")
                            flag = False
                            break
                  except:
                    flag = True
                  if flag:
                    break
                else:
                  print("Invalid Project Title!!")
              project_information[1] = new_title
              new_information = ":".join(project_information)
              with open("temp.txt", "a") as new_file:
                data = new_information.strip("\n")
                data = f"{data}\n"
                new_file.writelines(data)
                print("*************************************************")
                print("Title Changed Successfully...!")
                print("*************************************************")
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
      print("*************************************************")
      print("There Is No Project With This Title")
      print("*************************************************")
    os.remove("projects.txt")
    os.rename("temp.txt", "projects.txt")
  
  # Change Details
  @classmethod
  def edit_details(cls, email):
    title_regex = '[a-zA-Z][_a-zA-Z0-9]*'
    flag = False
    while True:
      title = input("Enter The Project Title: ").strip()
      if re.fullmatch(title_regex, title):
          break
      else:
          print("Invalid Title")
    try:
      with open("projects.txt") as project_data:
        projects = project_data.readlines()
        for project in projects:
          project = project.strip("\n")
          project_information = project.split(":")
          if email == project_information[0]:
            if title == project_information[1]:
              new_details = input("Enter New Details: ").strip()
              project_information[2] = new_details
              new_information = ":".join(project_information)
              with open("temp.txt", "a") as new_file:
                data = new_information.strip("\n")
                data = f"{data}\n"
                new_file.writelines(data)
                print("*************************************************")
                print("Details Changed Successfully...!")
                print("*************************************************")
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
      print("*************************************************")
      print("There Is No Project With This Title")
      print("*************************************************")
    os.remove("projects.txt")
    os.rename("temp.txt", "projects.txt")

  # Change Total Target
  @classmethod
  def edit_target(cls, email):
    title_regex = '[a-zA-Z][_a-zA-Z0-9]*'
    flag = False
    while True:
      title = input("Enter The Project Title: ").strip()
      if re.fullmatch(title_regex, title):
          break
      else:
          print("Invalid Title")
    try:
      with open("projects.txt") as project_data:
        projects = project_data.readlines()
        for project in projects:
          project = project.strip("\n")
          project_information = project.split(":")
          if email == project_information[0]:
            if title == project_information[1]:
              while True:
                new_target = input("Enter The New Target In EGP: ")
                if new_target.isnumeric():
                  break
                else:
                  print("Invalid Input!!")
              project_information[3] = new_target
              new_information = ":".join(project_information)
              with open("temp.txt", "a") as new_file:
                data = new_information.strip("\n")
                data = f"{data}\n"
                new_file.writelines(data)
                print("*************************************************")
                print("Total Target Changed Successfully...!")
                print("*************************************************")
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
      print("*************************************************")
      print("There Is No Project With This Title")
      print("*************************************************")
    os.remove("projects.txt")
    os.rename("temp.txt", "projects.txt")

  # Change Start Date
  @classmethod
  def edit_start_date(cls, email):
    title_regex = '[a-zA-Z][_a-zA-Z0-9]*'
    flag = False
    while True:
      title = input("Enter The Project Title: ").strip()
      if re.fullmatch(title_regex, title):
          break
      else:
          print("Invalid Title")
    try:
      with open("projects.txt") as project_data:
        projects = project_data.readlines()
        for project in projects:
          project = project.strip("\n")
          project_information = project.split(":")
          if email == project_information[0]:
            if title == project_information[1]:
              while True:
                new_start_date = input("Enter The New Start Date For The Project in This Format [YYYY-MM-DD]: ")
                time_regex = r'^\d{4}-\d{2}-\d{2}$'
                year = datetime.now().year
                month = datetime.now().month
                day = datetime.now().day
                today_date = f"{year}-{month}-{day}"
                if re.fullmatch(time_regex, new_start_date):
                  today_date = datetime.strptime(today_date, '%Y-%m-%d')
                  today_date = str(today_date.strftime("%Y-%m-%d"))
                  # today_date = str(today_date)
                  if today_date < new_start_date and project_information[5] > new_start_date:
                    break
                  else:
                    print("Start Date Can't Be Before Today or After End Date!!")
                else:
                  print("Incorrect Data Format, Should Be [YYYY-MM-DD]")
              project_information[4] = new_start_date
              new_information = ":".join(project_information)
              with open("temp.txt", "a") as new_file:
                data = new_information.strip("\n")
                data = f"{data}\n"
                new_file.writelines(data)
                print("*************************************************")
                print("Start Date Changed Successfully...!")
                print("*************************************************")
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
      print("*************************************************")
      print("There Is No Project With This Title")
      print("*************************************************")
    os.remove("projects.txt")
    os.rename("temp.txt", "projects.txt")

  # Change End Date
  @classmethod
  def edit_end_date(cls, email):
    title_regex = '[a-zA-Z][_a-zA-Z0-9]*'
    flag = False
    while True:
      title = input("Enter The Project Title: ").strip()
      if re.fullmatch(title_regex, title):
          break
      else:
          print("Invalid Title")
    try:
      with open("projects.txt") as project_data:
        projects = project_data.readlines()
        for project in projects:
          project = project.strip("\n")
          project_information = project.split(":")
          if email == project_information[0]:
            if title == project_information[1]:
              while True:
                time_regex = r'^\d{4}-\d{2}-\d{2}$'
                new_end_date = input("Enter The New End Date For The Project in This Format [YYYY-MM-DD]: ")
                if re.fullmatch(time_regex, new_end_date):
                  if project_information[4] < new_end_date:
                      break
                  else:
                      print("End Date Can't Be Before Start Date!!")
                else:
                  print("Incorrect Data Format, Should Be [YYYY-MM-DD]")
              project_information[5] = new_end_date
              new_information = ":".join(project_information)
              with open("temp.txt", "a") as new_file:
                data = new_information.strip("\n")
                data = f"{data}\n"
                new_file.writelines(data)
                print("*************************************************")
                print("End Date Changed Successfully...!")
                print("*************************************************")
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
      print("*************************************************")
      print("There Is No Project With This Title")
      print("*************************************************")
    os.remove("projects.txt")
    os.rename("temp.txt", "projects.txt")

  #******************************************************************************
  # Delete Project
  @classmethod
  def delete_project(cls, email):
    title_regex = '[a-zA-Z][_a-zA-Z0-9]*'
    flag = False
    while True:
      title = input("Enter The Project Title: ").strip()
      if re.fullmatch(title_regex, title):
          break
      else:
          print("Invalid Title")
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
      print("*************************************************")
      print("There Is No File With This Title")
      print("*************************************************")
    else:
      print("*************************************************")
      print("Your Record Has Been Deleted Successfully...!")
      print("*************************************************")
    os.remove("projects.txt")
    os.rename("temp.txt", "projects.txt")
  #******************************************************************************
  # Search For A Project
  @classmethod
  def search_for_project(cls, email):
    time_regex = r'^\d{4}-\d{2}-\d{2}$'
    flag = False
    while True:
      start_date = input("Enter The Start Date For The Project You Want in This Format [YYYY-MM-DD]: ")
      if re.fullmatch(time_regex, start_date):
        break
      else:
        print("Incorrect Data Format, Should Be [YYYY-MM-DD]")
    while True:
      end_date = input("Enter The End Date For The Project You Want in This Format [YYYY-MM-DD]: ")
      if re.fullmatch(time_regex, end_date):
        break
      else:
        print("Incorrect Data Format, Should Be [YYYY-MM-DD]")
    try:
      with open("projects.txt") as project_data:
        projects = project_data.readlines()
        for project in projects:
          project = project.strip("\n")
          project_information = project.split(":")
          if email == project_information[0]:
            if start_date == project_information[4] and end_date == project_information[5]:
              print(f"========================== Project {project_information[1]} ===========================")
              print(f"User Email:         {project_information[0]}")
              print(f"Project Title:      {project_information[1]}")
              print(f"Details:            {project_information[2]}")
              print(f"Total Target:       {project_information[3]}")
              print(f"Start Date:         {project_information[4]}")
              print(f"End Date:           {project_information[5]}")
              flag = True
    except:
      flag = False
    if not flag: 
      print("*************************************************")
      print("There Is No Project With This Date")
      print("*************************************************")