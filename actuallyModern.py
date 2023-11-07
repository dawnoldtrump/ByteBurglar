import customtkinter as ctk  # import customtkinter instead of tkinter. 
'''you have to install library. 
    1. go to terminal or open command prompt 
    2. enter: python -m pip install customtkinter
'''

class ByteGUI:
    def __init__(self):
        self.window = ctk.CTk()  # Use CTk instead of Tk
        self.window.geometry("300x500")  # Window size x,y
        self.window.title("ByteBurglar")  # Window title

        self.title = ctk.CTkLabel(self.window, text='ByteBurglar', font=('Arial', 18))  # Use CTkLabel instead of Label
        self.title.pack(padx=20, pady=20)  # Title placement x,y;
        #y starts at 0 at the top and as 0 increases y moves down. If you want a button further down you increase y
        
        self.button_keylogger = ctk.CTkButton(self.window, text='Press for Keylogger', command=self.activate_keylogger) #creating buttons
        self.button_keylogger.pack(padx=20, pady=20)

        self.button_packet_sniffer = ctk.CTkButton(self.window, text='Press for Packet Sniffer', command=self.activate_packet_sniffer)
        self.button_packet_sniffer.pack(padx=20, pady=30)

        self.button_both = ctk.CTkButton(self.window, text='Press to run both', command=self.activate_both)
        self.button_both.pack(padx=20, pady=40)

        self.button_close = ctk.CTkButton(self.window, text='Close', command=self.window.destroy)
        self.button_close.pack(padx=20, pady=60)

        self.window.mainloop()

    def activate_keylogger(self):
        self.button_pressed_keylogger = True
        print("Keylogger activated!")

    def activate_packet_sniffer(self):
        self.button_pressed_p_s = True
        print("Packet sniffer activated!")

    def activate_both(self):
        self.button_pressed_both = True
        print("Both keylogger and packet sniffer activated!")

# Create an instance of the class to run the GUI
ByteGUI()
