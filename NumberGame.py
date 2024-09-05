class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

import random
import os

print("Welcome to the" + color.BOLD + color.YELLOW + " Number Guessing Game!" + color.END)

print(color.BOLD + color.YELLOW + color.UNDERLINE + "\nInstructions:" + color.END)

print("\n(1). You pick a" + color.BOLD + color.YELLOW + " Game Mode" + color.END)
print("(2). The" + color.BOLD + color.YELLOW + " Bot" + color.END + " will select a " + color.BOLD + color.YELLOW + "Random Number" + color.END)
print("(3). You will" + color.BOLD + color.YELLOW + " Guess" + color.END + " the " + color.BOLD + color.YELLOW + "Number" + color.END)
print("(4). The" + color.BOLD + color.YELLOW + " Bot" + color.END + " will say" + color.BOLD + color.YELLOW + " Correct" + color.END + " or" + color.BOLD + color.YELLOW + " Incorrect" + color.END)

Continue = input("\nPress" + color.BOLD + color.CYAN + " [Enter]" + color.END + " to continue")
os.system('clear')

print("\n\n " + color.BOLD + color.YELLOW + color.UNDERLINE + "Game Modes:" + color.END)
print("\n\n(1). 1-5")
print("(2). 1-10")
print("(3). 1-15")

Game_Mode = input("\nSelect Game Mode: ")

def One_To_Five():
    print("\n\n1-5 Game mode selected")
    print("\n The Bot is picking a #...")
    OT5 = [1, 2, 3, 4, 5]
    BotNumberOT5 = random.choice(OT5)
    UsernumberOT5 = input("\nChoose a number within the range!: ")
    if UsernumberOT5 >str(5):
        print("That number is not in the range")
        exit()
    if str(UsernumberOT5) == str(BotNumberOT5):
        print("\nCorrect! The bots number was " + str(BotNumberOT5))
    if str(UsernumberOT5) != str(BotNumberOT5):
        print("\nIncorrect! The bots number was " + str(BotNumberOT5))

def One_To_Ten():
    print("\n\n1-10 Game mode selected")
    print("\nThe Bot is picking a #...")
    OT10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    BotNumberOT10 = random.choice(OT10)
    UsernumberOT10 = input("\nChoose a number within the range!: ")
    if int(UsernumberOT10) >(10):
        print("That number is not in the range")
        exit()
    if str(UsernumberOT10) == str(BotNumberOT10):
        print("\nCorrect! The bots number was " + str(BotNumberOT10))
    if str(UsernumberOT10) != str(BotNumberOT10):
        print("\nIncorrect! The bots number was " + str(BotNumberOT10))
        
def One_To_Fifteen():
    print("\n\n1-15 Game mode selected")
    print("\nThe Bot is picking a #...")
    OT15 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    BotNumberOT15 = random.choice(OT15)
    UsernumberOT15 = input("\nChoose a number within the range!: ")
    if UsernumberOT15 >str(15):
        print("That number is not in the range")
        exit()
    if str(UsernumberOT15) == str(BotNumberOT15):
        print("\nCorrect! The bots number was " + str(BotNumberOT15))
    if str(UsernumberOT15) != str(BotNumberOT15):
        print("\nIncorrect! The bots number was " + str(BotNumberOT15))
        
if Game_Mode == "1":
    One_To_Five()
if Game_Mode == "2":
    One_To_Ten()
if Game_Mode == "3":
    One_To_Fifteen()