import customtkinter as ctk
from PIL import Image, ImageFont
import os

class AppStyles:
    White = "#FFFFFF"
    LightGray = "#DAD8D8"
    Gold = "#FF8F00"
    DarkGray = "#717171"
    Black = "#000000"
    Gray = "#8B8B8B"

    w = 375
    h = 812
    mw = w/2
    mh = h/2

    def __init__(self):
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self._load_fonts()
        self._load_images()

    def _load_fonts(self):
        self.font_path_Montserrat = os.path.join(self.current_path, "fonts", "Montserrat-Regular.ttf")
        self.font_path_Montserrat_Medium = os.path.join(self.current_path, "fonts", "Montserrat-Medium.ttf")
        self.font_path_GreatVibes = os.path.join(self.current_path, "fonts", "GreatVibes-Regular.ttf")
        self.font_path_Cinzel = os.path.join(self.current_path, "fonts", "Cinzel-Bold.ttf")

        ctk.FontManager.load_font(self.font_path_Montserrat)
        ctk.FontManager.load_font(self.font_path_GreatVibes)
        ctk.FontManager.load_font(self.font_path_Cinzel)

        self.H1 = ctk.CTkFont(family="Great Vibes", size=32)
        self.H2 = ctk.CTkFont(family="Montserrat", size=22)
        self.H3 = ctk.CTkFont(family="Cinzel", size=30)
        self.Body = ctk.CTkFont(family="Montserrat", size=16)
        self.Crumbs = ctk.CTkFont(family="Montserrat", size=12)

        self.H1_Pil = ImageFont.truetype(self.font_path_GreatVibes, 34)
        self.H2_Pil = ImageFont.truetype(self.font_path_Montserrat, 24)
        self.H3_Pil = ImageFont.truetype(self.font_path_Cinzel, 32)
        self.Body_Pil = ImageFont.truetype(self.font_path_Montserrat, 18)
        self.Crumbs_Pil = ImageFont.truetype(self.font_path_Montserrat, 14)

    def _load_images(self):
        self.image_config = {
            "Bg.png": (375, 812),
            "BtnEnter.png": (327, 55),
            "BtnJoin.png": (327, 55),
            "Home.png": (25, 25),
            "AI.png": (21, 25),
            "Microphone.png": (25, 25),
            "AddFile.png": (25, 25),
            "Account.png": (32, 41),
            "AddAccount.png": (32, 41),
            "Crown.png": (13, 12),
            "Exit.png": (42, 18),
            "Support.png": (41, 41),

        }

        self.images = {}
        self.raw_images = {}

        for filename, size in self.image_config.items():

            short_name = filename.replace(".png", "")

            self._load_single_image(filename, short_name, size)

    def _load_single_image(self, filename, save_as, size):
        try:
            path = os.path.join(self.current_path, "Imgs", filename)
            raw_img = Image.open(path)

            self.raw_images[save_as] = raw_img
            self.images[save_as] = ctk.CTkImage(light_image=raw_img, size=size)
        except Exception as e:
            print(f"Помилка завантаження {filename}: {e}")

    def get_poster(self, filename):
        short_name = filename.replace(".png", "")

        if short_name in self.images:
            return self.images[short_name]

        self._load_single_image(filename, short_name, (156, 178))
        return self.images.get(short_name)

    def camuflage(self, x, y, w, h):
        if "Bg" not in self.raw_images: return None
        
        crop = (x, y, x+w, y+h) 
        cropped_image = self.raw_images["Bg"].crop(crop)
        return ctk.CTkImage(light_image=cropped_image, size=(w, h))