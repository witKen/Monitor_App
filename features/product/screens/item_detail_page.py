
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Label, Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Frame



OUTPUT_PATH2 = Path(__file__).parent
ASSETS_PATH2 = OUTPUT_PATH2.parent.parent.parent / "assets/frame2"

def relative_to_assets2(path: str) -> Path:
    return ASSETS_PATH2 / Path(path)


class ItemDetailPage(Frame):
    def __init__(self, parent, drink_id, drink_flavour, drink_price, drink_description, drink_image):
        super().__init__(parent, background="white")
        
        self.drink_id = drink_id
        self.drink_flavour = drink_flavour
        self.drink_price = drink_price
        self.drink_description = drink_description
        self.drink_image = drink_image
        self.quantity = 1

        # Set main window to maximum screen
        # screen_width = self.winfo_screenwidth()
        # screen_height = self.winfo_screenheight()
        # self.geometry(f"{screen_width}x{screen_height}+0+0")
        
        # self.geometry("1024x720")
        # self.configure(bg = "#FFFFFF")

        canvas = Canvas(
            parent,
            bg = "#FFFFFF",
            height = 720,
            width = 1024,
            relief = "ridge"
        )
        
        canvas.pack(fill="both", expand=True)
        print(canvas.winfo_width())
        print(canvas.winfo_height())
        canvas.create_rectangle(
            0.0,
            0.0,
            1024.0,
            600,
            fill="#FF4438",
        )
        title = "Green Tea"
        title_text = Label(canvas, foreground="#FFFFFF", background="#FF4438",font=('Arial', 18), text=title, justify="center")
        title_text.pack(pady=10, side="top", anchor="center")
        # title_text.configure(justify="center")
        # canvas.create_text(
        #     333.0,
        #     35.0,
        #     anchor="nw",
        #     text="Green Tea",
        #     fill="#FFFFFF",
        #     font=("CADTMonoDisplay Regular", 48 * -1)
        # )

        image_image_1 = PhotoImage(
            file=relative_to_assets2("image_1.png"))
        image_1 = canvas.create_image(
            511.0,
            280.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets2("image_2.png"))
        image_2 = canvas.create_image(
            511.0,
            298.0,
            image=image_image_2
        )
        # Create a debug window
        
        button_image_1 = PhotoImage(
            file=relative_to_assets2("button_1.png")
        )
        button_1 = Button(
            parent,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=354.0,
            y=600.0,
            width=316.0545654296875,
            height=66.37145233154297
        )
        
        debug_window = Toplevel()
        label = Label(debug_window, image=button_image_1)
        label.pack()
        print(relative_to_assets2("button_1.png"))
        canvas.create_text(
            46.0,
            236.0,
            anchor="nw",
            text="Medium Size Drink",
            fill="#FFFFFF",
            font=("Niradei Bold", 28 * -1)
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets2("image_3.png"))
        image_3 = canvas.create_image(
            390.0,
            260.4375,
            image=image_image_3
        )

        canvas.create_text(
            716.0,
            252.0,
            anchor="nw",
            text="Sugar 70%",
            fill="#FFFFFF",
            font=("Niradei Regular", 28 * -1)
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets2("image_4.png"))
        image_4 = canvas.create_image(
            628.0,
            274.5,
            image=image_image_4
        )

        canvas.create_text(
            90.0,
            378.0,
            anchor="nw",
            text="Stay Refreshing",
            fill="#FFFFFF",
            font=("Niradei Regular", 28 * -1)
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets2("image_5.png"))
        image_5 = canvas.create_image(
            412.5887451171875,
            366.32843017578125,
            image=image_image_5
        )

        canvas.create_text(
            723.0,
            394.0,
            anchor="nw",
            text="Fresh Milk",
            fill="#FFFFFF",
            font=("Niradei Bold", 28 * -1)
        )

        image_image_6 = PhotoImage(
            file=relative_to_assets2("image_6.png"))
        image_6 = canvas.create_image(
            631.0,
            380.1875,
            image=image_image_6
        )

        canvas.create_text(
            366.0,
            510.0,
            anchor="nw",
            text="Enjoy your drink",
            fill="#FFFFFF",
            font=("Niradei Regular", 36 * -1)
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets2("button_2.png"))
        button_2 = Button(
            parent,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=86.0,
            y=50.0,
            width=45.0,
            height=47.0
        )

        canvas.create_rectangle(
            843.0,
            0.0,
            938.0,
            123.0,
            fill="#FF4438",
            outline="")

        canvas.create_rectangle(
            843.0,
            0.0,
            937.8163681030273,
            122.78878021240234,
            fill="#11284C",
            outline="")

        canvas.create_text(
            865.0,
            38.0,
            anchor="nw",
            text="2$",
            fill="#FFFFFF",
            font=("Niradei Bold", 36 * -1)
        )



