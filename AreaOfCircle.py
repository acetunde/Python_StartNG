#a basic code to find the area of a circle, given the radius
marker = True

while marker == True:
    Area = 0
    try:
        r = int(input ("Please enter the circle's radius: "))
        if r<0:
            r = str(r) #negative input converted to string so as to generate an error
        Area = 22 * r * 2 / 7
        print("The area of the circle is", round(Area,2), "sq units \n")
        while True:
            try:
                question = input("Do you want to calculate another area? (y/n): ")
                if question == "y":
                    marker = True
                    break
                elif question == "n":
                    marker = False
                    break
            except:
                continue
        
    except ValueError:
        print("\nPlease enter a number \n")
        continue
    except TypeError:
        print("\nRadius can't be negative \n")

