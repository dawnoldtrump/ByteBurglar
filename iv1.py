def inputValidation(): 

    while True: 
        try:
            user_input = int(input("Press 1 for Keylogger: \nPress 2 for Packet Sniffer: \nPress 3 for both: \nPress 0 to exit: \n"))
            if user_input == 0:
                print(user_input,' has been entered, Now exiting program.\n')
                raise SystemExit 
            elif user_input == 1:
                print(user_input, "has been selected. Now booting up Keylogger.\n")
                break
            elif user_input == 2:
                print(user_input, ' has been selected. Now booting up: Packet sniffer.\n')
                break 
            elif user_input == 3:
                print(user_input, ' has been selected. Now booting up Keylogger and Packet sniffer\n')
                break
        except Exception : ValueError
        print("Please enter 1, 2 or 3.\n")
    return user_input
print(inputValidation())

#From here you would assign user input to the function to run the keylogger or packet sniffer or both