#  #  #  #  #  #  #  #  #  #  #
#         Master Tool         #
#     By: Jordan Goddard      #
#  #  #  #  #  #  #  #  #  #  #



import os
import sys
import subprocess
import re

response = None
file_path = None

def create_file():
    file = open("T:\\Development\\tools\\breakout_layout_tool\\data\\pass_in\\breakout_log.txt", "w")
    file.write("file=C:\\Temp\n000.0000")
    file.close()

def check_file():
    try:
        file = open("T:\\Development\\tools\\breakout_layout_tool\\data\\pass_in\\breakout_log.txt", "r")
    except:
        create_file()
        print("\nThe file is empty, please enter data into the file\n")

def read_file():
    file = open("T:\\Development\\tools\\breakout_layout_tool\\data\\pass_in\\breakout_log.txt", "r")
    print("\n-------------------------------------------------------------------------\n")
    for line in file:
        print(line)
    print("\n-------------------------------------------------------------------------\n")

def question_one():
    print("\nThe following shots have been set for breakout: ")
    read_file()
    print("\nIs this correct? (y/n)")
    response = input()
    question_one_answer(response)
    

def question_one_answer(response):
    if response == 'y':
        print("\nBreakout check is beginning\n")
        run_scripts()
    elif response == 'n':
        print("Please update the file with correct data")
        question_two()
    else:
        print("\nInvalid Entry!\nPlease try again!")
        question_one()

def execute():
    print("\n-------------------------------------------------------------------------\n")
    check_file()
    question_one()

def run_scripts():
    try:
        file = open("T:\\Development\\tools\\breakout_layout_tool\\data\\pass_in\\breakout_log.txt", "r")
    except:
        print("File Error!")
        file = open("T:\\Development\\tools\\breakout_layout_tool\\data\\pass_in\\breakout_log.txt", "w")
        file.close()
    else:
        for line in file.readlines():
            if line.startswith('file='):
                match=re.match("file=(\S+)", line)
                file_path = match.group(1)
            else:
                file_new = open("C:\\Temp\\pass_temp.txt", "w")
                match = re.match(r'(\d+\.\d+)',line)
                scene_name = match.group(1)
                file_new.write("%s\n%s" %(scene_name,file_path))
                file_new.close()
                subprocess.call("T:\\Development\\tools\\breakout_layout_tool\\scripts\\check_batch_code.bat")
    finally:
        question_two()
    
    
def question_two():
    print("\n\n\n\nDo you want to run the breakout on the files that were checked?(y/n)")
    response = input()
    question_two_answer(response)

def question_two_answer(response):
    if response == 'y':
        print("\nBreakout is beginning\n")
        run_scripts_again()
    elif response == 'n':
        print("\n\nFile Closing!")
    else:
        print("\nInvalid Entry!\nPlease try again!")
        questiion_two()

def run_scripts_again():
    try:
        file = open("c:\\Temp\\breakout_log.txt", "r")
    except:
        print("File Error!")
        file = open("c:\\Temp\\breakout_log.txt", "w")
        file.close()
    else:
        for line in file.readlines():
            if line.startswith('file='):
                match=re.match("file=(\S+)", line)
                file_path = match.group(1)
            else:
                file_new = open("C:\\Temp\\pass_temp.txt", "w")
                match = re.match(r'(\d+\.\d+)',line)
                scene_name = match.group(1)
                file_new.write("%s\n%s" %(scene_name,file_path))
                file_new.close()
                subprocess.call("T:\\Development\\tools\\breakout_layout_tool\\scripts\\breakout_batch_code.bat")
    finally:
        print("\n\nComplete\n\n")

execute()