import tkinter as tk


class ByteGUI:
    def __init__(self):
        self.window = tk.Tk() #window creation
        self.window.geometry("300x500") #window size x,y
        self.window.title("ByteBurglar") #window title

        self.title = tk.Label(self.window, text='ByteBurglar', font=('Arial', 18)) #actual title
        self.title.pack(padx=20, pady=20) #title placement x,y

        
        self.button_keylogger = tk.Button(self.window, text='Press for Keylogger', font=('Roboto', 14), command=self.activate_keylogger)
        #button creation. takes text, font and size. creates a command linking the methods
        self.button_keylogger.pack(padx=20, pady=0)

        self.button_packet_sniffer = tk.Button(self.window, text='Press for Packet Sniffer', font=('Roboto', 14), command=self.activate_packet_sniffer)
        self.button_packet_sniffer.pack(padx=20, pady=0)

        self.button_both = tk.Button(self.window, text='Press to run both', font=('Roboto', 14), command=self.activate_both)
        self.button_both.pack(padx=20, pady=0)

        self.button_close = tk.Button(self.window, text='Close', font=('Arial', 14), command=self.window.destroy)
        self.button_close.pack(padx=20, pady=120)

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

