#The program greets user and describes what's the purpose of the program.
name = input("Hello, What's your name? ")
print(f"Hello {name} it's nice to meet you! This program converts units. More specifically, kilometers into miles. Just enter number of kilometers you wish to convert.")

def convert_km():
    #User enters the amount of kilometers.
    kilometers = float(input("Enter value in kilometers: "))
    #The program converts these kilometers into miles and prints them.
    conv_fac = 0.621371 #conversion factor
    miles = kilometers * conv_fac   # calculate miles
    print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
convert_km()

#The program asks user if they'd want to do another conversion.
while True:
    replay = input("Do you wish to run the program again? ")
    if replay.lower() == "yes":
        convert_km()
    else:
        print("Goodbye!")
        break