import tkinter
from tkinter import filedialog


class MyGui:
    """
    Okienko z przyciskiem otwierajacym okno wyboru pliku.
    """

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Okno 2")
        self.main_window.geometry("640x480")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.message = tkinter.StringVar()
        self.message.set("Nie wybrano pliku")

        self.label = tkinter.Label(self.top_frame, textvariable=self.message)
        self.show_button = tkinter.Button(
            self.bottom_frame,
            text="Wybierz plik",
            command=self.select_file
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

    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Wybierz plik"
        )

        if file_path:
            self.message.set(file_path)
        else:
            self.message.set("Nie wybrano pliku")


my_gui = MyGui()
