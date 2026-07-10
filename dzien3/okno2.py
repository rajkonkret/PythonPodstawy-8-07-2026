import tkinter


class MyGui:
    """
    Okienko z przyciskiem zmieniajacym tekst.
    """

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Okno 2")
        self.main_window.geometry("640x480")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.message = tkinter.StringVar()
        self.message.set("Witaj Swiecie")

        self.label = tkinter.Label(self.top_frame, textvariable=self.message)
        self.show_button = tkinter.Button(
            self.bottom_frame,
            text="Zmien tekst",
            command=self.change_text
        )
        self.quit_button = tkinter.Button(
            self.bottom_frame,
            text="Wyjscie",
            command=self.main_window.destroy
        )

        self.label.pack()
        self.show_button.pack(side="left")
        self.quit_button.pack(side="left")

        self.top_frame.pack(pady=20)
        self.bottom_frame.pack()

        tkinter.mainloop()

    def change_text(self):
        self.message.set("Przycisk zostal klikniety")


my_gui = MyGui()
