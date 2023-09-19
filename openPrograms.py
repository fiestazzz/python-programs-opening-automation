import os
import webbrowser
import subprocess


def openMySqlWorkbench():
    os.startfile(
        r"C:\Program Files\MySQL\MySQL Workbench 8.0 CE\MySQLWorkbench.exe")


def openSTS():
    os.startfile(
        r"C:\Users\papab\Desktop\sts-4.17.0.RELEASE\SpringToolSuite4.exe")


def openVisualStudioCode():
    subprocess.Popen(
        r"C:\Users\papab\AppData\Local\Programs\Microsoft VS Code\Code.exe")


def openSourceTree():
    os.startfile(
        r"C:\Users\papab\AppData\Local\SourceTree\SourceTree.exe")


def openDailyPrograms():
    openMySqlWorkbench()
    openVisualStudioCode()
    openSTS()
    openSourceTree()


openDailyPrograms()
