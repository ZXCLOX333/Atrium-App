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

        self.H1_Pil = ImageFont.truetype(self.font_path_GreatVibes,  34)
        self.H2_Pil = ImageFont.truetype(self.font_path_Montserrat, 24)
        self.H3_Pil = ImageFont.truetype(self.font_path_Cinzel, 32)
        self.Body_Pil = ImageFont.truetype(self.font_path_Montserrat, 18)
        self.Crumbs_Pil =  ImageFont.truetype(self.font_path_Montserrat, 14)

    def _load_images(self):
        self.image_config = {"Bg.png": (375, 812),
                        #buttons
                        "BtnEnter.png": (327, 55),
                        "BtnBuy.png": (327, 55),
                        "BtnJoin.png": (327, 55),
                        #icons
                        "Support.png": (41, 41),
                        "Account.png": (32, 41),
                        "AddAccount.png": (32, 41),
                        "Crown.png": (13, 12),
                        "Home.png": (19, 19),
                        "AI.png": (21, 27),
                        "Exit.png": (46, 18),
                        "AddFile.png": (32, 32),
                        "Microphone.png": (27, 32),
                        #films
                        "Five.png":(156,178),
                        "Zootopia.png":(156,178),
                        "Tramp.png":(156,178),
                        "Poppers.png":(156,178),
                        "Night.png":(156,178),
                        "Alvin.png":(156,178),
                        "JecyChan.png":(156,178),
                        "Titanic.png":(156,178),
                        "Game of thrones.png":(156,178),
                        "MazeRunner.png":(156,178),
                        "Dragon.png":(156,178),
                        "Pirates.png":(156,178),
                        "it.png":(156,178),
                        "Dedpool.png":(156,178)
                        }

        self.images = {} 
        self.raw_images = {} 

        for filename, size in self.image_config.items():
            raw_img = Image.open(os.path.join(self.current_path, "Imgs", filename))
            self.raw_images[filename] = raw_img

            ctk_img = ctk.CTkImage(light_image=raw_img, dark_image=raw_img, size=size)
            self.images[filename] = ctk_img

            key_name = filename.replace(".png", "") 
            self.images[key_name] = ctk_img

    def camuflage(self, x,y,w,h):

        crop = (x,y,x+w,y+h) 
        cropped_image = self.raw_images["Bg.png"].crop(crop)
        return ctk.CTkImage(light_image=cropped_image,size=(w,h))
