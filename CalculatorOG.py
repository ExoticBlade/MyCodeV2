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


#Welcome the User
print("Welcome to my " + color.BOLD + "Calculator!")
print("_________________________")

#Give the User Instructions
print("\n(Type the " + color.BOLD + color.YELLOW + "#" + color.END + " of the " + color.BOLD +  color.YELLOW + "Operation " + color.END + "you want!)")

#List of Operations
print(color.BOLD + "(1)" + color.END + ". Addition")
print(color.BOLD + "(2)" + color.END + ". Subtract")
print(color.BOLD + "(3)" + color.END + ". Multiply")
print(color.BOLD + "(4)" + color.END + ". Divide")

#Asking input from the User
Operation = input("\nConsole: ")

#Making the Functions for the Operations
def Addition_Function():
    NumberAdd = input("\nType the" + color.BOLD + color.YELLOW + " first " + color.END + "number: ")
    NumberAdd2 = input("Type the" + color.BOLD + color.YELLOW + " second " + color.END + "number: ")
    SumAdd = float(NumberAdd) + float(NumberAdd2)
    print("\nYour number is: " + str(SumAdd))
    print("\nThanks for using my Calculator!")
    exit()

def Subtract_Function():
    NumberSubtract = input("\nType the" + color.BOLD + color.YELLOW + " first " + color.END + "number: ")
    NumberSubtract2 = input("Type the" + color.BOLD + color.YELLOW + " second " + color.END + "number: ")
    SumSubtract = float(NumberSubtract) - float(NumberSubtract2)
    print("\nYour number is: " + str(SumSubtract))
    print("\nThanks for using my Calculator!")
    exit()
    
def Multiply_Function():
    NumberMultiply = input("\nType the" + color.BOLD + color.YELLOW + " first " + color.END + "number: ")
    NumberMultiply2 = input("Type the" + color.BOLD + color.YELLOW + " second " + color.END + "number: ")
    SumMultiply = float(NumberMultiply) * float(NumberMultiply2)
    print("\nYour number is: " + str(SumMultiply))
    print("\nThanks for using my Calculator!")
    exit()

def Divide_Function():
    NumberDivide = input("\nType the" + color.BOLD + color.YELLOW + " first " + color.END + "number: ")
    NumberDivide2 = input("Type the" + color.BOLD + color.YELLOW + " second " + color.END + "number: ")
    SumDivide = float(NumberDivide) / float(NumberDivide2)
    print("\nYour number is: " + str(SumDivide))
    print("\nThanks for using my Calculator!")
    exit()
    

#If statements to Call Functions
if Operation == "1" or Operation == "addition":
    Addition_Function()
if Operation == "2" or Operation == "subtract":
    Subtract_Function()
if Operation == "3" or Operation == "multiply":
    Multiply_Function()
if Operation == "4" or Operation == "Divide":
    Divide_Function()
if Operation >str("4"):
    print("\n" + color.BOLD + color.RED + "Error" + color.END + ", That is not a valid option!\n----------------------------------\nQuitting Program...")