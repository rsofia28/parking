parking = ["", "", "", "", "", "", "", "", "", ""]

while True:

    print("1. Spaces")
    print("2. Enter a car")
    print("3. Take out car")
    print("4. Go out")

    opcion = input("Please select an option: ")

    if opcion == "1":
        for i in range(10):
            if parking[i] == "":
                print("Spaces", i+1, ": free")
            else:
                print("Spaces", i+1, ": occupied by", parking[i])

    elif opcion == "2":

        plate = input("Enter the plate: ")

        if plate in parking:
            print("This car is already inside")

        else:
            for i in range(10):
                if parking[i] == "":
                    parking[i] = plate
                    print("Car parked in space", i+1)
                    break
            else:
                print("Parking is full")

    elif opcion == "3":

        plate = input("Enter the plate to remove: ")

        if plate in parking:
            for i in range(10):
                if parking[i] == plate:
                    parking[i] = ""
                    print("Car removed from space", i+1)
                    break
        else:
            print("This car is not in the parking")

    elif opcion == "4":
        print("Chaulin pinguin")
        break
