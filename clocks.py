from colorama import Fore
import datetime
import time
import os
import num
import dots
palette = [Fore.CYAN, Fore.LIGHTBLUE_EX, Fore.BLUE]
d = 0
while True:
    for color in range(3):
        for d in range(5):
            time_now = datetime.datetime.now().time()
            clocks= time_now.strftime("%H:%M:%S")
            for line in range (11):
                for i in clocks:
                    if i == ":":   
                        dot = dots.dots[d].split("\n")
                        print(palette[color] + dot[line] + palette[color], end="")
                    else:
                        number = num.num[i].split("\n")
                        print(palette[color] + number[line] + palette[color], end="")         
                print("")  
            time.sleep(0.4)
            os.system('cls' if os.name == 'nt' else 'clear')