import SimpleProblemSolvingAgent as SPSA

def main():
    #Ask user for cities they would like to find a path between
    print("Hello, where will you be traveling in Romania?")
    cityOne = input("Enter the first city: ")
    cityTwo = input("Enter the second city: ")

    #Check to see if cities are valid
    #If not, prompt user to re-enter cities or allow them to exit
    while SPSA.checkCities(cityOne,cityTwo):
        print()
        print("Please enter valid (and different) cities...")
        cityOne = input("Enter the first city: (or exit to quit) ")
        cityTwo = input("Enter the second city: (or exit to quit) ")
        if cityOne.lower() == 'exit' or cityTwo.lower() == 'exit':
            return

##############################################################################################


#Where the code to execute the algorithms should go....



##############################################################################################

    #Once search is completed
    #Allow user the option to search for a path between a new pair or cities or exit
    again = input('\n' + 'Would you like to check another pair of cities? ')
    again = SPSA.inputTest(again)
    if again is None:
        return
    if again.lower() == 'yes':
        print()
        main()
    else:
        print("Thank You for Using Our App")


if __name__ == "__main__":
    main()