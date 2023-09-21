import os
import subprocess
import time
import pyautogui


def openMySqlWorkbench():
    os.startfile(
        r"C:\Program Files\MySQL\MySQL Workbench 8.0 CE\MySQLWorkbench.exe")


def openSTS():
    os.startfile(
        r"C:\Users\papab\Desktop\sts-4.17.0.RELEASE\SpringToolSuite4.exe")


def openSourceTree():
    os.startfile(
        r"C:\Users\papab\AppData\Local\SourceTree\SourceTree.exe")


def openVSCode():
    # open visual studio code at the path specified
    vscode_path = r"C:\Users\papab\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    subprocess.Popen([vscode_path])

    # Wait for Visual Studio Code to start (adjust the delay as needed)
    time.sleep(5)

    # ctrl + shift + e to open the side menu
    pyautogui.hotkey('ctrl', 'shift', 'e')

    # Simulate Ctrl + K, Ctrl + O (to open a folder)
    pyautogui.hotkey('ctrl', 'k')
    pyautogui.hotkey('ctrl', 'o')

    # Type the folder path and press Enter
    time.sleep(1)
    path_to_open = r"C:\Users\papab\Documents\portfolio-projects\chaseToAMillionBucks"
    pyautogui.write(path_to_open)
    pyautogui.press('enter')

    # press enter to open the selected folder
    time.sleep(1)
    pyautogui.press('enter')

    # open terminal, ctrl + shift + '   or crtl + shift + ò
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', '\'')

    # wait for terminal to be ready and then type command to start server and open browser
    time.sleep(3)
    run_angular_server = "ng serve -o"
    pyautogui.write(run_angular_server)
    pyautogui.press('enter')


def openDailyPrograms():
    openVSCode()
    # openMySqlWorkbench()
    # openSTS()
    # openSourceTree()


openDailyPrograms()
