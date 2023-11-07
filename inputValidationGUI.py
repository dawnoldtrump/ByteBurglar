class inputValidation:
    def inputValidationGUI(): 
        str_prompt = 'Press 1 for Keylogger. \nPress 2 for Packet Sniffer. \nPress 3 to start both. \nPress 0 to exit.\n'
        str_exit = ' has been entered, exiting program.\n'
        str_keylogger = ' has been entered, starting Keylogger.\n'
        str_packet_sniffer = ' has been entered, staring Packet sniffer.\n'
        str_both = ' has been entered, starting Keylogger and Packet sniffer.\n'
        str_value_error = 'Invalid input. Please enter integers, 1, 2, or 3.\n'
        while True: #basic while loop from java
            try:
                user_input = int(input(str_prompt))
                if user_input == 0: #exit if enter 0
                    print(user_input, str_exit)
                    raise SystemExit 
                elif user_input == 1:
                    print(user_input, str_keylogger)
                    break
                elif user_input == 2:
                    print(user_input, str_packet_sniffer)
                    break
                elif user_input == 3:
                    print(user_input, str_both)
                    break
            except Exception:ValueError #repeat if they press a non integer
            print(str_value_error)
        return user_input
    print(inputValidationGUI())
#From here you would assign user input to the function to run the keylogger or packet sniffer or both.
