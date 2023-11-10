import customtkinter as ctk  # import customtkinter instead of tkinter.
from Keylogger import Keylogger 
'''you have to install library. 
    1. go to terminal or open command prompt 
    2. enter: python -m pip install customtkinter
'''

class ByteGUI:
    def __init__(main):
        main.window = ctk.CTk()  # Use CTk instead of Tk
        ctk.set_appearance_mode('dark')

        main.window.geometry("300x500")  # Window size x,y
        main.window.title("ByteBurglar")  # Window title

        main.title = ctk.CTkLabel(main.window, text='ByteBurglar', font=('Arial', 18))  # Use CTkLabel instead of Label
        main.title.pack(padx=20, pady=20)  # Title placement x,y;
        #y starts at 0 at the top and as 0 increases y moves down. If you want a button further down you increase y
        
        main.button_keylogger = ctk.CTkButton(main.window, text='Start keylogger', command=main.activate_keylogger) #creating buttons
        main.button_keylogger.pack(padx=20, pady=10)

        main.button_keylogger_stop = ctk.CTkButton(main.window, text = 'Stop keylogger', command = main.deactivate_keylogger)
        main.button_keylogger_stop.pack(padx = 20, pady =0)


        main.button_packet_sniffer = ctk.CTkButton(main.window, text='Start packet sniffer', command=main.activate_packet_sniffer)
        main.button_packet_sniffer.pack(padx=20, pady=20)

        main.button_packet_sniffer_stop = ctk.CTkButton(main.window, text='Stop packet sniffer', command=main.deactivate_packet_sniffer)
        main.button_packet_sniffer_stop.pack(padx=20, pady=0)

        main.button_both = ctk.CTkButton(main.window, text='Run both', command=main.activate_both)
        main.button_both.pack(padx=20, pady=40)

        main.button_close = ctk.CTkButton(main.window, text='Close', command=main.window.destroy)
        main.button_close.pack(padx=20, pady=60)

        main.window.mainloop()

    def activate_keylogger(main):
        main.button_pressed_keylogger = True
        print("Keylogger activated!")
        start_keylogger = Keylogger()
        start_keylogger.start()

    def deactivate_keylogger(main):
        print('Deacting keylogger')
        stop_keylogger = Keylogger()
        stop_keylogger.stop()



    def activate_packet_sniffer(main):
        main.button_pressed_p_s = True
        print("Packet sniffer activated!")
    def deactivate_packet_sniffer(main):
        print('Deactivating packet sniffer.')

    def activate_both(main):
        main.button_pressed_both = True
        print("Both keylogger and packet sniffer activated!")

    def close(main):
        print('Closing window. Stopping keylogger and packet sniffer')
        close = Keylogger
        close.stop()
        main.window(destroy)

# Create an instance of the class to run the GUI
ByteGUI()
