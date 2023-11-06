import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox

CURRENT_PATH = Path(__file__).parent
ASSETS_PATH = CURRENT_PATH / "assets" / "frame0"


def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)


class Register_sale:

    def __init__(self):
        self.window = None
        self.canvas = None

        self.button_image_1 = None
        self.button_image_2 = None

        self.button_1 = None
        self.button_2 = None

        self.entry_image_1 = None
        self.entry_image_2 = None

        self.image_image_1 = None
        self.image_image_2 = None
        self.image_image_3 = None

        self.quantity_data = None
        self.code_data = None

        self.code_current = None
        self.quantity_current = None

    def create_window(self):
        self.window = Tk()
        self.window.geometry("500x800")
        self.window.configure(bg="#58A76E")

    def create_canvas(self):
        self.canvas = Canvas(
            self.window,
            bg="#58A76E",
            height=800,
            width=500,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            500.0,
            800.0,
            fill="#FFFFFF",
            outline="")

    def button_back_register_sale(self):
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("back"),
            relief="flat"
        )
        self.button_1.place(
            x=173.0,
            y=339.0,
            width=138.0,
            height=50.0
        )

    def button_register_sale(self):
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.get_information,
            relief="flat"
        )
        self.button_2.place(
            x=84.0,
            y=254.0,
            width=312.0,
            height=78.0
        )

    def quantity_register_sale(self):
        self.canvas.create_text(
            206.0,
            216.63265991210938,
            anchor="nw",
            text="QUANTITY",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.canvas.create_rectangle(
            106.0,
            208.28570556640625,
            373.0,
            209.28570556640625,
            fill="#000000",
            outline="")

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            286.0,
            189.69387817382812,
            image=self.entry_image_1
        )
        self.quantity_data = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.quantity_data.place(
            x=166.0,
            y=175.0,
            width=240.0,
            height=27.38775634765625
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            141.27777862548828,
            192.79591369628906,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            140.61111450195312,
            179.0,
            image=self.image_image_2
        )

    def code_register_sale(self):
        self.canvas.create_text(
            222.0,
            140.2127685546875,
            anchor="nw",
            text="CODE",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.canvas.create_rectangle(
            106.0,
            133.93617248535156,
            373.0,
            134.93617248535156,
            fill="#000000",
            outline="")

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            287.0,
            110.82978820800781,
            image=self.entry_image_2
        )
        self.code_data = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.code_data.place(
            x=167.0,
            y=95.0,
            width=240.0,
            height=29.659576416015625
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            139.66666412353516,
            113.63829803466797,
            image=self.image_image_3
        )

    def logo(self):
        self.canvas.create_text(
            138.0,
            38.0,
            anchor="nw",
            text="REGISTER SALE",
            fill="#000000",
            font=("Inter", 25 * -1)
        )

    def start_window(self):
        self.window.resizable(False, False)
        self.window.mainloop()

    def get_information_code(self):
        if self.code_data.get():
            self.code_current = self.code_data.get()
        else:
            messagebox.showerror("Error", "El campo del code está vacío")

    def get_information_quantity(self):
        if self.quantity_data.get():
            self.quantity_current = self.quantity_data.get()
        else:
            messagebox.showerror("Error", "El campo del quantity está vacío")

    def get_information(self):
        self.get_information_code()
        self.get_information_quantity()

        print(self.code_current, self.quantity_current)

    def start_register_sale(self):
        register_sale = Register_sale()
        register_sale.create_window()
        register_sale.create_canvas()
        register_sale.button_back_register_sale()
        register_sale.button_register_sale()
        register_sale.quantity_register_sale()
        register_sale.code_register_sale()
        register_sale.logo()
        register_sale.start_window()


ventana = Register_sale()
ventana.start_register_sale()