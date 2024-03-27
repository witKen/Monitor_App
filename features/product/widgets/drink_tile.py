
from pathlib import Path
import tkinter as tk
from tkinter import Button, Label, PhotoImage
from PIL import Image, ImageTk
import requests
from io import BytesIO

from features.product.screens.item_detail_page import ItemDetailPage
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH.parent.parent.parent / "assets/frame1"
# ASSETS_PATH = OUTPUT_PATH / Path(r"Monitor_App/assets/frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class DrinkTile(tk.Frame):
    def __init__(self, parent, drink_id, drink_flavour, drink_price, drink_description, drink_image):
        super().__init__(parent, bg="white", borderwidth=2, highlightbackground="red", highlightthickness=1)
        self.drink_id = drink_id
        self.drink_flavour = drink_flavour
        self.drink_price = drink_price
        self.drink_description = drink_description
        self.drink_image = drink_image
        self.create_widgets()
        self.pack(padx = 10, pady=10)
        
        # Bind left mouse button click event to the show_product_detail method
        self.bind("<Button-1>", self.show_product_detail)
    def load_image_from_url(self, url):
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img = img.resize((171, 171), Image.ADAPTIVE)
        
        return ImageTk.PhotoImage(img)
    
    def create_widgets(self):
        
        # Load drink image from Cloudinary URL
        image = self.load_image_from_url(self.drink_image)
        image_label = Label(self, image=image, width=171, height=171, background="white")
        image_label.image = image
        image_label.grid(row=0, column=0, rowspan=2, padx=8, pady=8)
        # image_label.bind("<Button-1>", self.show_product_detail)
        flavour_label = Label(self, text=self.drink_flavour, font=('Helvetica', 15),bg="white", padx=8)
        flavour_label.grid(row=2, column=0, sticky=tk.W)
        # flavour_label.bind("<Button-1>", self.show_product_detail)
        price_label = Label(self, text=f"${self.drink_price:.2f}", font=('Helvetica', 20), bg="white", padx=8)
        price_label.grid(row=3, column=0, sticky=tk.W)
        price_label.bind("<Button-1>", self.show_product_detail)
    
    def show_product_detail(self, event):
        print("product")
        ItemDetailPage(self.master, self.drink_id ,self.drink_flavour, self.drink_price, self.drink_description, self.drink_image)
