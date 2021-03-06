#!/usr/bin/env python3
# Author David Boh // herrboh@live.com
import os


def create_html():
    file_ext = ".html"
    filename = input("Please enter a name for your file: ")
    with open("{}{}".format(filename, file_ext), "w") as file:
        file.write("<!DOCTYPE html>\n")
        file.write("<html lang=\"en\">\n")
        file.write("<head>\n")
        file.write("\t<meta charset=\"UTF-8\">\n")
        file.write("\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n")
        file.write("\t<title>My Page</title>\n")
        file.write("</head>\n")
        file.write("<body>\n")
        file.write("\t\n")
        file.write("</body>\n")
        file.write("</html>\n")
    final_name = "{}{}".format(filename, file_ext)
    print("\nFile {} has been created\n".format(final_name))

def create_php():
    file_ext = ".php"
    filename = input("Please enter a name for your file: ")
    with open("{}{}".format(filename, file_ext), "w") as file:
        file.write("<?php\n")
        file.write("session_start();\n")
        file.write("require_once \"pdo.php\"\n")
        file.write("\t \n")
        file.write("?>\n")
        file.write("<html lang=\"en\">\n")
        file.write("<head>\n")
        file.write("\t<meta charset=\"UTF-8\">\n")
        file.write("\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n")
        file.write("\t<title>My Page</title>\n")
        file.write("</head>\n")
        file.write("<body>\n")
        file.write("\t\n")
        file.write("</body>\n")
        file.write("</html>\n")
    final_name = "{}{}".format(filename, file_ext)
    print("\nFile {} has been created\n".format(final_name))

def creation():
    file_ext = ""
    active = True
    while active:
        userinput = input("\nPlease choose file type\npress h for html\npress p for php\npress q to quit\n\n")
        if userinput == 'q':
            active = False
            break
        if userinput == 'p':
            create_php()
            break
        if userinput == 'h':
            create_html()
            break
        if userinput != 'h' or userinput != 'p' or userinput != 'q':
            print("\nInvalid Input\n")
            creation()
            break

creation()
