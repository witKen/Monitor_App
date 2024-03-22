
from pathlib import Path
import tkinter as tk
from tkinter import Button, Label, PhotoImage
from PIL import Image, ImageTk
import requests
from io import BytesIO
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH.parent.parent.parent / "assets/frame0"
# ASSETS_PATH = OUTPUT_PATH / Path(r"Monitor_App/assets/frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class DrinkTile(tk.Frame):
    def __init__(self, parent, drink_id,drink_flavour, drink_price, drink_description, drink_image):
        super().__init__(parent, bg="white", borderwidth=2, highlightbackground="red", highlightthickness=1)
        self.drink_id = drink_id
        self.drink_flavour = drink_flavour
        self.drink_price = drink_price
        self.drink_description = drink_description
        self.drink_image = drink_image
        self.create_widgets()
        self.pack()
        
        # Bind left mouse button click event to the show_product_detail method
        # self.bind("<Button-1>", self.show_product_detail)
    def load_image_from_url(self, url):
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img = img.resize((100, 100), Image.ADAPTIVE)
        
        return ImageTk.PhotoImage(img)
    
    def create_widgets(self):
        # button_image_1 = PhotoImage(
        #     file=relative_to_assets("button_1.png"))
        # button_1 = Button(
        #     image=button_image_1,
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: print("button_1 clicked"),
        #     relief="flat"
        # )
        # button_1.place(
        #     x=44.0,
        #     y=211.0,
        #     width=185.10841369628906,
        #     height=235.8418426513672
        # )
        # Load drink image from Cloudinary URL
        image = self.load_image_from_url(self.drink_image)
        image_label = Label(self, image=image, width=100, height=100)
        image_label.image = image
        image_label.grid(row=0, column=0, rowspan=2, padx=12, pady=12)
        # image_label.bind("<Button-1>", self.show_product_detail)
        flavour_label = Label(self, text=self.drink_flavour, font=('Helvetica', 15),bg="white", padx=12)
        flavour_label.grid(row=0, column=1, sticky=tk.W)
        # flavour_label.bind("<Button-1>", self.show_product_detail)
        price_label = Label(self, text=f"${self.drink_price:.2f}", font=('Helvetica', 20), bg="white", padx=12)
        price_label.grid(row=1, column=1, sticky=tk.W)
        
        # price_label.bind("<Button-1>", self.show_product_detail)
    
    # def show_product_detail(self, event):
    #     print("product")
    # ProductDetailScreen(self.master,self.drink_id ,self.drink_flavour, self.drink_price, self.drink_description, self.drink_image)
