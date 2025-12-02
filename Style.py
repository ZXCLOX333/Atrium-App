import customtkinter as ctk
from PIL import Image, ImageFont
import os

class AppStyles:
    White = "#FFFFFF"
    LightGray = "#DAD8D8"
    Gold = "#FF8F00"
    DarkGray = "#717171"
    Black = "#000000"

    w = 375
    h = 812

    mw = w/2
    mh = h/2

    def __init__(self):
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        
        self._load_fonts()
        self._load_images()

    def _load_fonts(self):
        font_path_Montserrat = os.path.join(self.current_path, "fonts", "Montserrat-Regular.ttf")
        font_path_GreatVibes = os.path.join(self.current_path, "fonts", "GreatVibes-Regular.ttf")
        self.font_path_Cinzel = os.path.join(self.current_path, "fonts", "Cinzel-Bold.ttf")

        ctk.FontManager.load_font(font_path_Montserrat)
        ctk.FontManager.load_font(font_path_GreatVibes)
        ctk.FontManager.load_font(self.font_path_Cinzel)

        self.H1 = ctk.CTkFont(family="Great Vibes", size=32)
        self.H2 = ctk.CTkFont(family="Montserrat", size=22)
        self.H3 = ctk.CTkFont(family="Cinzel", size=30)
        self.Body = ctk.CTkFont(family="Montserrat", size=16)
        self.Crumbs = ctk.CTkFont(family="Montserrat", size=12)

        self.H1_Pil = ImageFont.truetype(font_path_GreatVibes,  34)
        self.H2_Pil = ImageFont.truetype(font_path_Montserrat, 22)
        self.H3_Pil = ImageFont.truetype(self.font_path_Cinzel, 30)
        self.Body_Pil = ImageFont.truetype(font_path_Montserrat, 16)
        self.Crumbs_Pil =  ImageFont.truetype(font_path_Montserrat, 12)

    def _load_images(self):
        self.rawBgGradient = Image.open(os.path.join(self.current_path, "Imgs", "Bg.png"))
        self.rawBtnEnter = Image.open(os.path.join(self.current_path, "Imgs", "BtnEnter.png"))
        self.rawBtnBuy = Image.open(os.path.join(self.current_path, "Imgs", "BtnBuy.png"))
        self.rawBtnJoin = Image.open(os.path.join(self.current_path, "Imgs", "BtnJoin.png"))

        self.BgGradient = ctk.CTkImage(light_image=self.rawBgGradient, dark_image=self.rawBgGradient, size=(375, 812))
        self.BtnEnter = ctk.CTkImage(light_image=self.rawBtnEnter , dark_image=self.rawBtnEnter , size=(327, 55))
        self.BtnBuy = ctk.CTkImage(light_image=self.rawBtnBuy , dark_image=self.rawBtnBuy , size=(327, 55))
        self.BtnJoin = ctk.CTkImage(light_image=self.rawBtnJoin , dark_image=self.rawBtnJoin , size=(327, 55))
