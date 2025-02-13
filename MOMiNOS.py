import os ; import time; import colorama as c
from colorama import Fore, Back, Style
items = {}
error = ""
checkout = ""

#Terminal UI design
def menu():
    global error
    global menupage
    os.system('cls')
    print(f"{Style.BRIGHT}               {Fore.BLUE}MOMi{Fore.RED}NO'S{Style.RESET_ALL} ")
    print(f"{Fore.YELLOW}{Style.BRIGHT}≡ MENU{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}\n1. 🍕 PIZZAS \n2. 🍝 DIPS \n3. 🍟 SNACKS \n4. 🍹 DRINKS      {checkout}")
    print(f"\n-------------------------------{Style.RESET_ALL}",end = "\n")
    print(error,end='\n')
    while True:
        menupage = (input("ENTER CHOICE NUMBER : "))
        if menupage == '1':
            break
        elif menupage == '2':
            break
        elif menupage == '3':
            break
        elif menupage == '4':
            break
        elif menupage.lower() == 'c':
            break
        else:
            error = Fore.RED+Style.BRIGHT+"#RETRY"+Style.RESET_ALL
            os.system('cls')
            menu()
            print(Style.RESET_ALL)
            error = ""
            break

def pizzas():
    global pizza
    global quantity1
    global error
    os.system('cls')
    print(f"{Style.BRIGHT}               {Fore.BLUE}MOMi{Fore.RED}NO'S{Style.RESET_ALL} ")
    print(f"{Fore.YELLOW}{Style.BRIGHT}≡ PIZZAS 🍕{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}\n1. 🧀 CHEESE MARGHERITA   240rs.\n2. 🌶️ PEPPY PANEER        250rs.\n3. 🌽 VEGGIE PIZZA        220rs.\n\n    🔷 {Fore.BLUE}{Style.BRIGHT} BACK (B){Style.RESET_ALL}")

    print(f"\n{Style.BRIGHT}-------------------------------{Style.RESET_ALL}",end = "\n")
    print(error,end = "\n")
    while True:
        pizza = input("ENTER CHOICE NUMBER : ")
        if pizza == '1':
            quantity1 = int(input(f"{Fore.CYAN}{Style.BRIGHT}QUANTITY : "))
            items["CHEESE MARG "] = (quantity1,240)
            print(Style.RESET_ALL)
            break
        elif pizza == '2':
            quantity1 = int(input(f"{Fore.CYAN}{Style.BRIGHT}QUANTITY : "))
            items['PEPPY PANEER'] = (quantity1,250)
            print(Style.RESET_ALL)
            break
        elif pizza == '3':
            quantity1 = int(input(f"{Fore.CYAN}{Style.BRIGHT}QUANTITY : "))
            items['VEG PIZZA   '] = (quantity1,220)
            print(Style.RESET_ALL)
            break
        elif pizza.lower() == 'b':
            apploop()
            print(Style.RESET_ALL)
            break
        else:
            error = Fore.RED+Style.BRIGHT+"#RETRY"+Style.RESET_ALL
            os.system('cls')
            pizzas()
            print(Style.RESET_ALL)
            error = ""
            break

def dips():
    global error
    global dip
    os.system('cls')
    print(f"{Style.BRIGHT}               {Fore.BLUE}MOMi{Fore.RED}NO'S{Style.RESET_ALL} ")
    print(f"{Fore.YELLOW}{Style.BRIGHT}≡ SAUCES & DIPS 🍝{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}\n1. 🧀 CHEESE DIP        30rs.\n2. 🫙  MAYONAISE         20rs.\n3. 🍅 KETCH-UP          10rs.\n\n    🔷 {Fore.BLUE}{Style.BRIGHT} BACK (B){Style.RESET_ALL}")

    print(f"\n{Style.BRIGHT}-------------------------------{Style.RESET_ALL}",end = "\n")
    print(error,end = "\n")
    while True:
        dip = input("ENTER CHOICE NUMBER : ")
        if dip == '1':
            quantity1 = int(input(f"{Fore.CYAN}{Style.BRIGHT}QUANTITY : "))
            items["CHEESE DIP  "] = (quantity1,30)
            print(Style.RESET_ALL)
            break
        elif dip == '2':
            quantity1 = int(input(f"{Fore.CYAN}{Style.BRIGHT}QUANTITY : "))
            items['MAYO        '] = (quantity1,20)
            print(Style.RESET_ALL)
            break
        elif dip == '3':
            quantity1 = int(input(f"{Fore.CYAN}{Style.BRIGHT}QUANTITY : "))
            items['KETCH-UP    '] = (quantity1,10)
            print(Style.RESET_ALL)
            break
        elif dip.lower() == 'b':
            apploop()
            print(Style.RESET_ALL)
            break
        else:
            error = Fore.RED+Style.BRIGHT+"#RETRY"+Style.RESET_ALL
            os.system('cls')
            dips()
            print(Style.RESET_ALL)
            error = ""
            break

def snacks():
    global error
    global snack
    os.system('cls')
    print(f"{Style.BRIGHT}               {Fore.BLUE}MOMi{Fore.RED}NO'S{Style.RESET_ALL} ")
    print(f"{Fore.YELLOW}{Style.BRIGHT}≡ SNACKS 🍿{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}\n1. 🍟 FRIES     120rs.\n2. 🍜 NOODLES   50rs.\n3. 🍿 POPCORN   100rs.\n\n    🔷 {Fore.BLUE}{Style.BRIGHT} BACK (B){Style.RESET_ALL}")

    print(f"\n{Style.BRIGHT}-------------------------------{Style.RESET_ALL}",end = "\n")
    print(error,end = "\n")
    while True:
        snack = input("ENTER CHOICE NUMBER : ")
        if snack == '1':
            quantity1 = int(input(f"{Fore.CYAN}{Style.BRIGHT}QUANTITY : "))
            items["FRIES       "] = (quantity1,120)
            print(Style.RESET_ALL)
            break
        elif snack == '2':
            quantity1 = int(input(f"{Fore.CYAN}{Style.BRIGHT}QUANTITY : "))
            items['NOODLES     '] = (quantity1,50)
            print(Style.RESET_ALL)
            break
        elif snack == '3':
            quantity1 = int(input(f"{Fore.CYAN}{Style.BRIGHT}QUANTITY : "))
            items['POPCORN     '] = (quantity1,100)
            print(Style.RESET_ALL)
            break
        elif snack.lower() == 'b':
            apploop()
            print(Style.RESET_ALL)
            break
        else:
            error = Fore.RED+Style.BRIGHT+"#RETRY"+Style.RESET_ALL
            os.system('cls')
            snacks()
            print(Style.RESET_ALL)
            error = ""
            break

def drinks():
    global error
    global drink
    os.system('cls')
    print(f"{Style.BRIGHT}               {Fore.BLUE}MOMi{Fore.RED}NO'S{Style.RESET_ALL} ")
    print(f"{Fore.YELLOW}{Style.BRIGHT}≡ DRINKS 🥤{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}\n1. ☕ COFFEE           50rs.\n2. 🍵 TEA              40rs.\n3. 🍹 ORANGE JUICE     20rs.\n4. 🥤 COKE             40rs.\n5. 🧋 CHOCOLATE SHAKE   50rs.\n\n    🔷 {Fore.BLUE}{Style.BRIGHT} BACK (B){Style.RESET_ALL}")
    
    print(f"\n{Style.BRIGHT}-------------------------------{Style.RESET_ALL}",end = "\n")
    print(error,end = "\n")
    while True:
        drink = input("ENTER CHOICE NUMBER : ")
        if drink == '1':
            quantity1 = int(input(f"{Fore.CYAN}{Style.BRIGHT}QUANTITY : "))
            items["COFFEE      "] = (quantity1,50)
            print(Style.RESET_ALL)
            break
        elif drink == '2':
            quantity1 = int(input(f"{Fore.CYAN}{Style.BRIGHT}QUANTITY : "))
            items['TEA         '] = (quantity1,40)
            print(Style.RESET_ALL)
            break
        elif drink == '3':
            quantity1 = int(input(f"{Fore.CYAN}{Style.BRIGHT}QUANTITY : "))
            items['JUICE       '] = (quantity1,20)
            print(Style.RESET_ALL)
            break
        elif drink == '4':
            quantity1 = int(input(f"{Fore.CYAN}{Style.BRIGHT}QUANTITY : "))
            items['COKE        '] = (quantity1,40)
            print(Style.RESET_ALL)
            break
        elif drink == '5':
            quantity1 = int(input(f"{Fore.CYAN}{Style.BRIGHT}QUANTITY : "))
            items['SHAKE       '] = (quantity1,50)
            print(Style.RESET_ALL)
            break
        elif drink.lower() == 'b':
            apploop()
            print(Style.RESET_ALL)
            break
        else:
            error = Fore.RED+Style.BRIGHT+"#RETRY"+Style.RESET_ALL
            os.system('cls')
            drinks()
            print(Style.RESET_ALL)
            error = ""
            break

grand = 0
def bill():
    global name, mob,grand
    os.system('cls')
    print(f"{Style.BRIGHT}               {Fore.BLUE}MOMi{Fore.RED}NO'S{Style.RESET_ALL} ")
    print(f"\n{Style.BRIGHT}-------------------------------{Style.RESET_ALL}",end = "\n")
    name = input("NAME : ")
    mob = (input("MOBILE NO. : "))
    os.system('cls')
    time.sleep(0.5)
    l = items.keys()

    #bill interface
    print(f"{Style.BRIGHT}               {Fore.BLUE}MOMi{Fore.RED}NO'S{Style.RESET_ALL} ")
    print(f"\n{Style.BRIGHT}-----------------------------------------{Style.RESET_ALL}",end = "\n")
    print(f"{Fore.CYAN+Style.BRIGHT}NAME : {name.upper()}") ; print(f"MOB. NO. : {mob}{Style.RESET_ALL}")
    print(f"\n{Style.BRIGHT}-----------------------------------------{Style.RESET_ALL}",end = "\n")
    j = 0
    for i in l:
        j+=1
        print(f"{j}. {i}",end="");print(f"        Q. : {items[i][0]}",end="");print(f"    Rs. {items[i][0]*items[i][1]}\n",end="")
        grand += items[i][0]*items[i][1]
    print(f"\n{Style.BRIGHT}-----------------------------------------{Style.RESET_ALL}",end = "\n")
    print(f"{Fore.YELLOW+Style.BRIGHT}GRAND TOTAL :                        {grand}{Style.RESET_ALL}")
    if items == {}:
        print(f"{Fore.WHITE+Style.BRIGHT}PLEASE COME AGAIN...{Style.RESET_ALL}")
    else:
        print("\n\nYOUR ORDER IS BEING PREPARED...")
        print(f"{Fore.WHITE+Style.BRIGHT}THANKS FOR ORDERING !!!{Style.RESET_ALL}")
    print()


#main loop of the app
def apploop():
    global choice,error,menupage,checkout
    menu()
    if menupage == '1':
        pizzas()
    elif menupage == '2':
        dips()
    elif menupage == '3':
        snacks()
    elif menupage == '4':
        drinks()
    elif menupage.lower() == 'c':
        bill()
        input()
        quit()
    else:
        error = Fore.RED+Style.BRIGHT+"#RETRY"+Style.RESET_ALL
        os.system('cls')
        apploop()
        print(Style.RESET_ALL)
        error = ""
    while True:
        choice = (input(F"1. 💸 {Fore.WHITE+Style.BRIGHT}CHECKOUT      2. 🛒 {Fore.BLUE}ADD MORE   : {Style.RESET_ALL}"))
        if choice == '1':
            bill()
            input()
            quit()
        elif choice == '2':
            checkout = Fore.WHITE+Style.BRIGHT+'\n\n        💸 CHECKOUT (C)'+Style.RESET_ALL
            apploop()
            checkout = ""
            continue
        else:
            error = Fore.RED+Style.BRIGHT+"#RETRY"+Style.RESET_ALL
            print(error)
            error = ""
            continue
apploop()