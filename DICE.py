#DICE ROLL
import os ; import time ; import random 

up_down = "==============="
side1 = """|             |
                      |             |
                      |      *      |
                      |             |
                      |             |"""

side2 = """|             |
                      |             |
                      |    *   *    |
                      |             |
                      |             |"""
side3 = """|             |
                      |      *      |
                      |    *   *    |
                      |             |
                      |             |"""
side4 ="""|             |
                      |      *      |
                      |    *   *    |
                      |      *      |
                      |             |"""
side5 = """|             |
                      |    *   *    |
                      |      *      |
                      |    *   *    |
                      |             |"""
side6 = """|             |
                      |    *   *    |
                      |    *   *    |
                      |    *   *    |
                      |             |"""

def dice_roll():
    os.system('cls')
    print("\n\n\n\n\n")
    print("                      "+up_down)
    print("                      "+side1)
    print("                      "+up_down)
    time.sleep(0.1)
    os.system('cls')
    print("\n\n\n\n\n")
    print("                      "+up_down)
    print("                      "+side2)
    print("                      "+up_down)
    time.sleep(0.1)
    os.system('cls')
    print("\n\n\n\n\n")
    print("                      "+up_down)
    print("                      "+side3)
    print("                      "+up_down)
    time.sleep(0.1)
    os.system('cls')
    print("\n\n\n\n\n")
    print("                      "+up_down)
    print("                      "+side4)
    print("                      "+up_down)
    time.sleep(0.1)
    os.system('cls')
    print("\n\n\n\n\n")
    print("                      "+up_down)
    print("                      "+side5)
    print("                      "+up_down)
    time.sleep(0.1)
    os.system('cls')
    print("\n\n\n\n\n")
    print("                      "+up_down)
    print("                      "+side6)
    print("                      "+up_down)
def result():
    time.sleep(0.5)
    os.system('cls')
    side = random.randint(1,7)
    if side == 1:
        print("\n\n\n\n\n")
        print("                      "+up_down)
        print("                      "+side1)
        print("                      "+up_down)
        time.sleep(1)
    elif side == 2:
        print("\n\n\n\n\n")
        print("                      "+up_down)
        print("                      "+side2)
        print("                      "+up_down)
        time.sleep(1)
    elif side == 3:
        print("\n\n\n\n\n")
        print("                      "+up_down)
        print("                      "+side3)
        print("                      "+up_down)
        time.sleep(1)
    elif side == 4:
        print("\n\n\n\n\n")
        print("                      "+up_down)
        print("                      "+side4)
        print("                      "+up_down)
        time.sleep(1)
    elif side == 5:
        print("\n\n\n\n\n")
        print("                      "+up_down)
        print("                      "+side5)
        print("                      "+up_down)
        time.sleep(1)
    else:
        print("\n\n\n\n\n")
        print("                      "+up_down)
        print("                      "+side6)
        print("                      "+up_down)
        time.sleep(1)

dice_roll()
dice_roll()
result()
while True:
    choice = input("\n                        GO AGAIN ? :")
    if choice.lower() == "n":
        break
    else:
        os.system('cls')
        dice_roll()
        dice_roll()
        result()