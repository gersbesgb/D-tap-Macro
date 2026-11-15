import os
import time
import random
import keyboard
import mouse

os.system("cls")

CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

banner = (
    CYAN
    + r"""
===========================================================================================================================================================
 $$$$$$\                                $$$$$$$\                      
$$  __$$\                               $$  __$$\                     
$$ /  \__| $$$$$$\   $$$$$$\   $$$$$$$\ $$ |  $$ | $$$$$$\   $$$$$$$\ 
$$ |$$$$\ $$  __$$\ $$  __$$\ $$  _____|$$$$$$$\ |$$  __$$\ $$  _____|
$$ |\_$$ |$$$$$$$$ |$$ |  \__|\$$$$$$\  $$  __$$\ $$$$$$$$ |\$$$$$$\  
$$ |  $$ |$$   ____|$$ |       \____$$\ $$ |  $$ |$$   ____| \____$$\ 
\$$$$$$  |\$$$$$$$\ $$ |      $$$$$$$  |$$$$$$$  |\$$$$$$$\ $$$$$$$  |
 \______/  \_______|\__|      \_______/ \_______/  \_______|\_______/ """
    + MAGENTA
    + r"""


 /$$      /$$ /$$                                                   /$$$$$$   /$$           /$$      /$$                                                  
| $$$    /$$$|__/                                                  /$$__  $$ | $$          | $$$    /$$$                                                  
| $$$$  /$$$$ /$$ /$$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$  /$$$$$$ | $$  \__//$$$$$$        | $$$$  /$$$$  /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$$
| $$ $$/$$ $$| $$| $$__  $$ /$$__  $$ /$$_____/ /$$__  $$|____  $$| $$$$   |_  $$_/        | $$ $$/$$ $$ |____  $$ /$$_____/ /$$__  $$ /$$__  $$ /$$_____/
| $$  $$$| $$| $$| $$  \ $$| $$$$$$$$| $$      | $$  \__/ /$$$$$$$| $$_/     | $$          | $$  $$$| $$  /$$$$$$$| $$      | $$  \__/| $$  \ $$|  $$$$$$ 
| $$\  $ | $$| $$| $$  | $$| $$_____/| $$      | $$      /$$__  $$| $$       | $$ /$$      | $$\  $ | $$ /$$__  $$| $$      | $$      | $$  | $$ \____  $$
| $$ \/  | $$| $$| $$  | $$|  $$$$$$$|  $$$$$$$| $$     |  $$$$$$$| $$       |  $$$$/      | $$ \/  | $$|  $$$$$$$|  $$$$$$$| $$      |  $$$$$$/ /$$$$$$$/
|__/     |__/|__/|__/  |__/ \_______/ \_______/|__/      \_______/|__/        \___/        |__/     |__/ \_______/ \_______/|__/       \______/ |_______/ 
                                                                                                                                                          
                                                                                                                                                                                                                                                                                                
===========================================================================================================================================================
"""
    + RESET
)



counter = 0



keyboard.press_and_release("f11")
print(banner)

mouse.wheel(1)
mouse.wheel(1)
mouse.wheel(1)
mouse.wheel(1)

OBind = input("What is your Obsidian Bind? \n }  ")
CBind = input("What is your Crystal Bind? \n }  ")
ACBind = input("What bind to activate D-tap Macro? \n }  ")


while True:
    if keyboard.is_pressed(ACBind):
        

        delay_ms = random.randint(40, 50)   # Random delay (Light AC bypass)
        delay_ms2 = random.randint(40, 50)
        spam_delay = random.randint(60, 80)


        print(f"Macro Activated {counter}")
        counter += 1


        time.sleep(0.015)
        keyboard.press_and_release(OBind)
        time.sleep(delay_ms / 1000.0)
        mouse.right_click()
        time.sleep(delay_ms2 / 1000.0)
        keyboard.press_and_release(CBind)
        time.sleep(0.020)
        mouse.right_click()
        time.sleep(spam_delay / 1000.0)
        mouse.click()
        time.sleep(spam_delay / 1000.0)
        mouse.right_click()
        time.sleep(spam_delay / 1000.0)
        mouse.click()
        time.sleep(spam_delay / 1000.0)
        mouse.right_click()
        time.sleep(spam_delay / 1000.0)
        mouse.click()
        time.sleep(spam_delay / 1000.0)
        mouse.right_click()
        time.sleep(spam_delay / 1000.0)
        mouse.click()


        
        while keyboard.is_pressed(ACBind): #ANTI SPAM DO NOT REMOVE!!
            time.sleep(0.001)