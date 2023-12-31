import subprocess
import time
import pyautogui
import asyncio

# First attemp to automate programs with python


async def openMySqlWorkbench():
    mysql_workbench_path = r"C:\Program Files\MySQL\MySQL Workbench 8.0 CE\MySQLWorkbench.exe"
    subprocess.Popen([mysql_workbench_path])


async def openSTS():
    sts_path = r"C:\Users\papab\Desktop\sts-4.17.0.RELEASE\SpringToolSuite4.exe"
    subprocess.Popen([sts_path])

    # wait for sts to be ready
    time.sleep(15)
    pyautogui.press('enter')


async def openSourceTree():
    sourceTree_path = r"C:\Users\papab\AppData\Local\SourceTree\SourceTree.exe"
    subprocess.Popen([sourceTree_path])


async def openVSCode():
    # open visual studio code at the path specified
    vscode_path = r"C:\Users\papab\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    subprocess.Popen([vscode_path])

    # Wait for Visual Studio Code to start (adjust the delay as needed)
    await asyncio.sleep(5)

    # ctrl + shift + e to open the side menu
    pyautogui.hotkey('ctrl', 'shift', 'e')

    # Simulate Ctrl + K, Ctrl + O (to open a folder)
    pyautogui.hotkey('ctrl', 'k')
    pyautogui.hotkey('ctrl', 'o')

    # Type the folder path and press Enter
    await asyncio.sleep(1)
    path_to_open = r"C:\Users\papab\Documents\portfolio-projects\chaseToAMillionBucks"
    pyautogui.write(path_to_open)
    pyautogui.press('enter')

    # press enter to open the selected folder
    await asyncio.sleep(1)
    pyautogui.press('enter')

    # open terminal, ctrl + shift + '   or crtl + shift + ò
    await asyncio.sleep(5)
    pyautogui.hotkey('ctrl', 'shift', '\'')

    # wait for terminal to be ready and then type command to start server and open browser
    await asyncio.sleep(20)
    run_angular_server = "ng serve -o"
    pyautogui.write(run_angular_server)
    pyautogui.press('enter')


async def openDailyPrograms():
    await openVSCode()
    await openSTS()
    await openMySqlWorkbench()
    await openSourceTree()


asyncio.run(openDailyPrograms())
