import time
import os
import math

# #Q.1
# def great():
#     a = int(input("Number 1 : "))
#     b = int(input("Number 2 : "))
#     if a > b:
#         print("number 1:",a," is greater.")
#     elif a == b:
#         print(a,"and",b,"are equal.")
#     else:
#         print("number 2:",b," is greater." )
# great()

# #Q.2
# def area_o_circle():
#     r = int(input("Radius : "))
#     ar = r*((22/7)*r)
#     print("")
#     print("Area of circle = ",round(ar,2))
# area_o_circle()

# #Q.3
# def sell_price():
#     c = eval(input("Cost : Rs."))
#     p = eval(input("Profit % : "))
#     print("SELLING PRICE : ",c+((p/100)*c))
# sell_price()

# #Q.4
# def time():
#     t = int(input("TIME IN MINS : "))
#     h = t//60
#     m = t%60
#     print(h,"Hours and",m,"Minutes")
# time()

# # #Q.5
# def celcius():
#     c = float(input("CELCIUS: "))
#     f = ((9/5)*c)+32
#     print(round(f,2))
# celcius()

# #Q.6
# def swap():
#     # Using 3rd variable
#     a = 5
#     b = 10
#     temp = a
#     a = b
#     b = temp
#     print(a,b,sep = ", ")
#     # Without 3rd variable
#     c,d = 5,10
#     c,d = d,c
#     print(c,d,sep=", ")
# swap()

# #Q.7
# def isEven():
#     n = int(input("Number : "))
#     if n%2==0:
#         print("Number is even")
#     else:
#         print("Number is odd")
# isEven()

# #Q.8
# def perc():
#     while True:
#         perc = float(input("Your percentage: "))
#         if perc > 100:
#             print("RETRY")
#         elif perc >= 90 and perc <= 100:
#             print("Your Grade is A+")
#             break
#         elif perc >= 80 and perc < 90:
#             print("Your Grade is B")
#             break
#         elif perc >= 60 and perc < 80:
#             print("Your Grade is C")
#             break
#         elif perc >= 40 and perc < 60:
#             print("Your Grade is D")
#             break
#         elif perc >= 33 and perc < 40:
#             print("Your Grade is E")
#             break
#         elif perc < 33 and perc >= 0:
#             print("Your Grade is F")
#             break
# perc()

# #Q.9
# def peri():
#     l = int(input("Length = "))
#     b = int(input("Breadth = "))
#     while True:
#         choice = int(input("1. AREA     2. PERIMETER :   "))
#         if choice > 2:
#             print("choose out of given two options\n")
#         elif choice == 1:
#             print("AREA = ",l*b,"sq. cm")
#             break
#         elif choice == 2:
#             print("PERIMETER = ",2*(l+b),"cm")
#             break
# peri()

# #Q.10
# def account():
#     while True:
#         name = str(input("USER NAME :- "))
#         pwd = str(input("PASSWORD :- "))
#         print(" ")
#         if name.lower() == "admin" and pwd.lower() == "root":
#             print("WELCOME, ADMIN")
#             break
#         elif name.lower() == "user" and pwd.lower() == "root":
#             print("WELCOME, USER")
#             break
#         else:
#             print("USER NOT AUTHORIZED\n")
# account()

# #Q.11
# def prime():
#    n = int(input("Enter a number = "))
#    chk = 0
#    if n == 2 or n == 3:
#        print("PRIME")
#    elif n == 1 or n == 4:
#        print("COMPOSITE")
#    else:
#        for i in range(2,n,1):
#            if n%i == 0:
#                chk += 1
#            else:
#                break
#        if chk > 0:
#            print("Composite. It has",chk+2,"factors")
#        else:
#            print("PRIME")
# prime()

# #Q.12 i.)
# def sum_o_series():
#     #series = 1+x+(x^2)+(x^3)+.....+(x^n)
#     x = int(input("Enter a number: "))
#     n = int(input("Highest power: "))
#     sum = 0
#     for i in range(n+1):
#         s = x**i
#         sum += s
#     print("SUM =",sum)
# sum_o_series()

# # #Q.12 ii.)
# def sum_diff():
#     x = int(input("Number = "))
#     n = int(input("Highest power = "))
#     sum = 0
#     for i in range(n+1):
#         s = x**i
#         if i%2==0:
#             sum += s
#         else:
#             sum -= s
#         i+=1
#     print(sum)
# sum_diff()
    
# #Q.12 iii.)
# # 1+x+(x**2)/2+(x**3)/3...(x**n)/n
# def sum_series():
#     x = int(input("Number = "))
#     n = int(input("Highest power = "))
#     sum = 0
#     for i in range(1,n+1):
#         s = (x**i)/i
#         sum+=s
#         i += 1
#     print(sum)
# sum_series()

# #Q.13
# def factorial():
#     fact = 1
#     a = int(input("Enter a number to\nshow factorial : "))
#     for i in range(1,a+1):
#         fact *= i
#     print("FACTORIAL = ",fact)
# factorial()

# #Q.14 
# # PALINDROME
# def palindrome():
#     a = input("ENTER A NUMBER OR TEXT : ")
#     b = a[::-1] #slicing to see whether the str is the same backwards
#     if a == b:
#         print("Palindrome") #only when the str is the exact copy of its reverse
#     else:
#         print("Not Palindrome")
# palindrome()

# # Q.15 FIBONACCI SERIES...
# def fibo():
#    n = int(input("LIMIT OF FIBO SERIES : "))
#    a = 0
#    b = 1
#    print(a)
#    print(b)
#    for i in range(n-2):
#        print(a+b)
#        c = a + b
#        a = b
#        b = c
# fibo()

# #Q.16 PATTERNS
# def pattern1(): #STARS
#    n = int(input("Height = "))
#    for i in range(n):
#        for j in range(i+1):
#            print("*",end=" ")
#            j+=1
#        print()
# pattern1()

# def pattern2(): #ABCD
#     while True:
#         a = int(input("HEIGHT = "))
#         if a > 26:
#             print("")
#             print("Can't be more than 26")
#             print("")
#         else:
#             break
#     ch = 65
#     for i in range(1,a+1):
#         pat = str(chr(ch)*i)
#         print(((chr(ch)+" ")*i),end = " \n")
#         ch+=1
#         i+=1
#     print()
# pattern2()

# def pattern3():
#     a = int(input("HEIGHT : "))
#     for i in range(a,0,-1): #step -1 for backward printing of pyramid
#         for j in range(1,i+1):
#             print(j,end=" ")
#         print()
# pattern3()

# STRINGS

#Q.17
# string = input("ENTER STRING: ")
# string2 = ''
# for a in range(0,len(string),2):
#     string2+=string[a]
#     if a<len(string)-1:
#         string2+=string.upper()[a+1]
# print(string2)

# #Q.18
# string = input("String : ")
# alpha=upper=lower=digit=0
# for i in range(0,len(string),1):
#     if string[i].isalpha():
#         alpha+=1
#         if string[i].isupper():
#             upper+=1
#         elif string[i].islower():
#             lower+=1
#     elif string[i].isdigit():
#         digit+=1
#     else:
#         continue
# print("ALPHABETS = ",alpha)
# print("DIGITS = ",digit)
# print("UPPER, LOWER = ",upper,",", lower)

# #Q.19
# str1 = input("STRING = ")
# word = str1.split()
# count=0
# for i in word:
#     count+=1
# print("Number of words = ",count)

# #Q.20
# str1 = input("STRING : ")
# x = str1.split()
# vowel = 'aieou'
# count=0
# for i in x:
#     if i[0] in vowel.lower() or i[0] in vowel.upper():
#         count+=1
#         print(i)
# print("VOWEL WORDS = ",count)

# #Q.21
# str1 = input("STRING = ")
# maxlen = 0
# word = str1.split()
# biggest = ""
# for i in word:
#     x = len(i)
#     if x > maxlen and i.isalpha:
#         maxlen = x
#         biggest = i
# print("BIGGEST WORD IN THE STRING IS","'"+biggest+"'")

#STARTS FROM LIST QUESTIONS TO DICTIONARIES...

#LISTS

# #Q.22 INPUT NO. AND COUNT OCCURENCES
# list_ = [10, 20 ,10, 30, 40, 50, 10]
# num = eval(input('ENTER THE NUMBER = '))
# count = 0
# for i in list_:
#     if num == i:
#         count+=1
# print('The number',num,'is present',count,'times.')


# #Q.23 MAKE SEPARATE LISTS FROM A GIVEN LIST
# #OF DAYS AND TEMPERATURE...
# Wtemp = ['Mon',45,'tue',43,'wed',42,'thu',40,'fri',38,'sat',40,'sun',38]
# days = []
# temp = []
# for i in range(0,len(Wtemp)):
#     if not i%2==0:
#         temp.append(Wtemp[i])
#     else:
#         days.append(Wtemp[i])
# print(temp,days)
# input()


# #Q.24 menu driven program to perform various operations
# L1 = []
# while True:
#     print("""    0. DISPLAY LIST
#     1. APPEND ELEMENTS
#     2. INSERT AN ELEMENT AT INDEX
#     3. ADD A LIST AS ELEMENT
#     4. MODIFY AN ELEMENT
#     5. DELETE AN ELEMENT
#     6. DELETE AN INDEX
#     7. EXIT
#         \n""")
#     try:
#         choice = int(input("Select from the options :  "))
#         print("\n")
#         if choice == 1:
#             n = int(input("No. of elements : "))
#             print("ENTER ELEMENTS :\n")
#             for i in range(n):
#                 elem = input("\t")
#                 L1.append(elem)
#                 print()
#             print("\nELEMENTS HAVE BEEN ADDED\n")
#         elif choice == 2:
#             print("ENTER ELEMENT : ")
#             elem = input("\t")
#             index = int(input("ENTER INDEX : "))
#             L1.insert(index,elem)
#             print("\nELEMENT ADDED\n")
#         elif choice == 3:
#             L2 = []
#             n = int(input("No. of elements: "))
#             print("ENTER ELEMENTS")
#             for i in range(n):
#                 elem = input("\t")
#                 L2.append(elem)
#                 print()
#             L1.extend(L2)
#             print("\nLIST HAS BEEN EXTENDED\n")
#         elif choice == 4:
#             index = int(input("Index of element : "))
#             elem = input("Element : ")
#             L1[index] = elem
#             print("\nELEMENT MODIFIED\n")
#         elif choice == 5:
#             elem = input("Element for deletion : ")
#             del L1[L1.index(elem)]
#             print("\nELEMENT DELETED\n")
#         elif choice == 6:
#             index = int(input("Index of element to delete : "))
#             del L1[index]
#             print("\nELEMENT FROM INDEX -",index,"DELETED\n")
#         elif choice == 7:
#             print("\n\nExiting...\n\n")
#             break
#         elif choice == 0:
#             print("List :",L1,end = "\n")
#         else:
#             print("\nRETRY\n")
#     except ValueError :
#         print("\nRETRY\n")


#Q.25 separate +ve and -ve integers from a list
# n = int(input("No. of elements = "))
# nums = []
# neg = []
# pos = []
# for i in range(0,n):
#     num = int(input("Integer = "))
#     nums.append(num)
# print("LIST = ",nums)
# for i in range(len(nums)):
#     if nums[i]<0:
#         neg.append(nums[i])
#     else:
#         pos.append(nums[i])
# print(neg)
# print(pos)
# input()


# #Q.26 find largest and sec largest element
# list1 = [10,20,30,40,50,70,90,99]
# for i in range(2):
#     print(max(list1))
#     list1.pop(list1.index(max(list1)))
# print(list1)
# input()


#TUPLES

# #Q.27 swapping two tuples
# tup1 = (1,2,3,4,5)
# tup2 = (6,7,8,9,10)
# print(tup1,tup2)
# tup2,tup1=tup1,tup2
# print(tup1, tup2)
# input()

# #Q.28 sum, mean, length of tuple and its element
# n = int(input("No. of elements = "))
# tup1 = ()
# for i in range(n):
#     elem = int(input("Integer = "))
#     tup1+=(elem,)
# print(tup1)
# sum = 0
# for i in range(len(tup1)):
#     sum += tup1[i]
# mean = sum/(len(tup1))
# print(f"MAX = {max(tup1)} MIN = {min(tup1)} SUM = {sum} MEAN = {mean}")


# DICTIONARIES

# #Q.29   ENTER STUDENT DATABASE INTO DICTIONARY

# database = {}
# i = 1
# n = int(input("No. Of Entries : "))
# for i in range(n):
#     name = str(input('Name of student : '))
#     clss = (input('class and section : '))
#     adm = (input("Adm. No. : "))
#     perc = float(input('Enter percentage :'))
#     print()
#     tup = (name,clss,perc)
#     database[adm]=tup #this is to add all the info to a specific adm no.
# l = database.keys()

# for j in l:
#     print('\nADM. NO. :',j,'\n')
#     z = list(database[j])
#     print("NAME\t\t","CLASS\t\t","PERCENT\t\t")
#     print(z[0],"\t",z[1],"\t\t",z[2])
#     print("________________________________________")


# #Q.30  n employees and their details

# d1 = {}
# j  = 0
# n = int(input("Number of employees : "))
# #inputting every employee, at the end summing the salary
# for i in range(n):
#     nm = input("\nNAME : ")
#     pay = int(input("Basic salary : "))
#     hra = int(input("House rent allowance : "))
#     ca = int(input("Conveyance allowance : "))
#     print("___________________________________________")
#     d1[nm] = (pay,hra,ca)
# #let
# l = d1.keys()
# #display of database
# print()
# print(" ",'NAME\t\t','NET SALARY')
# for i in l:
#     j+=1
#     z = list(d1[i])
#     salary = z[0]+z[1]+z[2]
#     print(j,i,'\t\t',salary,end = "\n")
# print()

# #Q.31   countries, capitals and currencies...
# country = {}
# n = int(input("Number of entries : "))
# for i in range(n):
#     cname = input("\nName of country : ")
#     capital = input("Capital : ")
#     curr = input('Name of currency : ')
#     country[cname] = (capital,curr)
# l = country.keys()
# print()
# print("COUNTRY\t\t","CAPITAL\t\t","CURRENCY")
# for i in l:
#     z = list(country[i])
#     print(i,'\t\t',z[0],'\t\t\t',z[1])
# print()
# # DEBUGGED...


# #Q.32    Phone a friend...

# n = int(input("No. of friends : "))
# ph_no = {}
# for i in range(n):
#     nm = input("\nName of friend : ")
#     no = int (input("Contact No. : "))
#     ph_no[nm.lower()]=no
# print("\nMenu\n")
# while True:
#     print("""    1. DISPLAY ALL FRIENDS
#     2. ADD A NEW FRIEND
#     3. DELETE A FRIEND'S CONTACT
#     4. MODIFY A CONTACT NUMBER
#     5. SEARCH FOR A FRIEND'S CONTACT
#     6. DISPLAY CONTACTS IN SORTED ORDER
#     7. EXIT\n""")
#     try:
#         choice = int(input("Option :  "))
#         print("\n")
#         if choice == 1: 
#             for i in ph_no:
#                 print(i.upper()," : ",ph_no[i],end = "\n\n")
#             input("Enter to continue...")
#             print("\nMenu\n")

#         elif choice == 2:
#             nm = input("\nName of friend : ")
#             no = int(input("Contact No. : "))
#             ph_no[nm.lower()]=no
#             print("*CONTACT ADDED*")

#         elif choice == 3:
#             nm = input("Name of contact to delete : ")
#             if nm.lower() in ph_no:
#                 del ph_no[nm.lower()]
#                 print("*CONTACT DELETED*\n\n")
#             else:
#                 print("\nRETRY")

#         elif choice == 4:
#             nm = input("Contact to modify : ")
#             if nm.lower() in ph_no:
#                 no = int(input("Changed number : "))
#                 ph_no[nm.lower()] = no
#                 print("*CONTACT MODIFIED*\n\n")
#             else:
#                 print("\nRETRY\n")

#         elif choice == 5:
#             nm = input("SEARCH CONTACT : ")
#             if nm.lower() in ph_no:
#                 print(nm.upper()," : ",ph_no[nm.lower()],end = "\n\n")
#             else:
#                 print("*CONTACT NOT FOUND*")

#         elif choice == 6:
#             sort_name = str(sorted(ph_no.items()))
#             print("""A -> Z:\n""")
#             print(sort_name.upper())

#         elif choice == 7:
#             print("\n\nExiting...\n\n")
#             break

#     except ValueError :
#         print("\nRETRY\n")
#         print("\nMenu\n")


# #SHAPES

# def iterate():
#     height = int(input("HEIGHT = "))
#     if height%2==0:
#         print()
#         for i in range((height//2)+1):
#             for j in range(i+1):
#                 print("*",end=' ')
#             print()
#         for k in range((height//2),0,-1):
#             for l in range(k,0,-1):
#                 print("*",end=' ')
#             print()
#     else:
#         for i in range(height//2):
#             for j in range(i+1):
#                 print("*",end=' ')
#             print()
#         print("* "*((height//2)+1))
#         for k in range((height//2),0,-1):
#             for l in range(k,0,-1):
#                 print("*",end=' ')
#             print()
# def pyra(): #the pyramid maker
#     while True: #to avoid terminal errors
#         n = int(input("ENTER THE HEIGHT: "))
#         if n > 30:
#             print("")
#             print("This will break the program")
#             print("")
#         else: # takes height and makes a pyramid
#             for i in range(n):
#                 for j in range(i+1):
#                     print("*",end=" ")
#                     j+=1
#                 print()
#             break
#     print("")
def diamond():
    def evendiamond():
        sp = (height)
        for i in range(1,(height)+1,2):
            print(" "*sp,"* "*i,end = " \n")
            sp-=2
        for j in range((height)+1,0,-2):
            print(" "*sp,"* "*j,end = " \n")
            sp+=2
    def odddiamond():
        sp = (height)
        for i in range(1,(height),2):
            print(" "*sp,"* "*i,end = " \n")
            sp-=2
        for j in range((height),0,-2):
            print(" "*sp,"* "*j,end = " \n")
            sp+=2
    while True:
        try:
            height = int(input("Height = "))
            if height%2==0:
                evendiamond()
                break
            else:
                odddiamond()
                break
        except ValueError:
            print("\nRetry\n")
diamond()

# def A():
#     def a():
#         sp = height
#         sp1 = 0
#         print(" "*sp,"*",end=" \n")
#         sp-=1
#         print(" "*sp,"* *",end=" \n")
#         for i in range(height-2,0,-1):
#             if height/2==i:
#                 print(" "*i,"* "*((height-i)+1),end=" \n")
#                 sp1+=1
#             else:
#                 print(" "*i,"*"," "*(sp1),(sp1)*" ","*",end="\n")
#                 sp1+=1
#     while True:
#         try:
#             height = int(input("HEIGHT (EVEN) = "))
#             if height > 40:
#                 print("TRY SMALLER VALUE")
#             elif height%2==0:
#                a()
#                break
#             else:
#                 print("\nEnter an even value \n")
#         except ValueError:
#             print("*INVALID INPUT*")

# def start():
#     while True:
#         try:
#             choice = int(input("1. TRIANGLE            2. PYRAMID            3. DIAMOND            4. PRINT 'A' : "))
#             if choice == 1:
#                 iterate()
#                 break
#             elif choice == 2:
#                 pyra()
#                 break
#             elif choice == 3:
#                 diamond()
#                 break
#             elif choice == 4:
#                 A()
#                 break
#             else:
#                 print("RETRY")
#         except ValueError:
#             print("RETRY")
# start()

# while True:
#     try:
#         r = int(input("1. restart     2. exit :     "))
#         print()
#         if r > 2 or r == 0:
#             print("select 1 or 2")
#             print()
#         elif r == 2:
#             print("EXITING...")
#             time.sleep(0.15)
#             quit()
#         else:
#             os.system('cls')
#             start()
#     except ValueError:
#         print("Select 1 or 2")


# MODULES

# # Q. 33 CALCULATOR

# print("CALCULATOR :")
# print("1. ADD 2 NUMBERS \n2. SUBTRACT 2 NUMBERS")
# print("3. MULTIPLY 2 NUMBERS \n4. DIVIDE 2 NUMBERS")
# print("5. log(X)\n6. sin(X) \n7. cos(X)\n\n")

# choice = int(input("CHOICE : "))

# if choice == 1:
#     a = int(input("Num 1 = ")) ; b = int(input("Num 2 = "))
#     print(f"SUM = {a+b}")
# elif choice == 2:
#     a = int(input("Num 1 = ")) ; b = int(input("Num 2 = "))
#     print(f"DIFFERENCE = {a-b}")
# elif choice == 3:
#     a = int(input("Num 1 = ")) ; b = int(input("Num 2 = "))
#     print(f"PRODUCT = {a*b}")
# elif choice == 4:
#     a = int(input("Num 1 = ")) ; b = int(input("Num 2 = "))
#     print(f"QUOTIENT = {a/b}")
# elif choice == 5:
#     x = int(input("X = "));
#     print(f"log({x}) = {math.log(x,10)}")
# elif choice == 6:
#     x = int(input("X = "))
#     print(f"sin({x}) = {math.sin(x)}")
# elif choice == 7:
#     x = int(input("X = "))
#     print(f"cos({x}) = {math.cos(x)}")
# else:
#     print("\nPLEASE RETRY")


# # Q.34 AREA, PERIMETER AND SURFACE AREA

# def square(side):
#     area = math.pow(side,2)
#     print(F"AREA OF SQUARE = {area}")
#     print(f"PERIMETER = {4*side}")

# def circle(radius):
#     area = 3.14*(radius**2)
#     print(f"AREA OF CIRCLE = {area}")
#     print(f"CIRCUMFERENCE = {2*3.14*radius}")

# def eq_triangle(side):
#     area = (1.73/4)*(side**2)
#     print(f"AREA OF TRIANGLE = {area}")
#     print(f"PERIMETER = {3*side}")

# def rectangle(l,b):
#     print(f"AREA OF RECTANGLE = {l*b}")
#     print(f"PERIMETER = {2*(l+b)}")

# def cylinder(radius,height):
#     area = 2*3.14*radius*(radius+height)
#     print(f"SURFACE AREA OF CYLINDER = {area}")
#     volume = 3.14*(radius**2)*height
#     print(f"VOLUME = {volume}")

# circle(10)


# # # Q.35 STATISTICS
# import statistics as stat

# temp = [41,32,43,40,28,45]
# print(f"MEAN TEMPERATURE = {stat.mean(temp)} \nMEDIAN TEMPERATURE = {stat.median(temp)}\n")

# temp_ = [21,12,23,20,8,25] #temp after 20 deg variation
# print(f"MEAN TEMP. IN DECEMBER = {stat.mean(temp_)} \nMEDIAN TEMP. IS DECEMBER = {stat.median(temp_)}")

# # #Q.36 Traffic light
# import random

# print("YELLOW --> SLOW DOWN")
# time.sleep(random.randint(1,5))
# print("RED --> STOP")
# time.sleep(random.randint(1,5))
# print("GREEN --> GO!")
