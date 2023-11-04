number = 10
hasPaintedPoints = False

while number >= 0:
    if (number >= 8 or number <= 2):      
        print(number)
        userInput = input("Qué cable corto? ")
        if userInput == "verde":
            print("Enhorabuena! Has sobrevivido!")
            break
        elif userInput == "rojo":
            print("BOOM!!")
            break
    elif not hasPaintedPoints:
        print("...")
        hasPaintedPoints = True
        continue
    if (number == 0):
        print("BOOM!!")
    number -= 1