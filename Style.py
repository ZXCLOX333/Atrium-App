import customtkinter as ctk
from PIL import Image
import os
#File path
current_path = os.path.dirname(os.path.realpath(__file__))

# Colors
White = "#FFFFFF"
LightGray = "#DAD8D8"
Gold = "#FF8F00"
DarkGray="#717171"
Black = "#000000"

#Gradients
_rawBgGradient = Image.open(os.path.join(current_path, "Imgs", "BgGradient.png"))
_rawBtnEnter = Image.open(os.path.join(current_path, "Imgs", "BtnEnter.png"))
_rawBtnBuy = Image.open(os.path.join(current_path, "Imgs", "BtnBuy.png"))
_rawBtnJoin = Image.open(os.path.join(current_path, "Imgs", "BtnJoin.png"))

BgGradient = ctk.CTkImage(light_image=_rawBgGradient , dark_image=_rawBgGradient , size=(375, 812))
BtnEnter = ctk.CTkImage(light_image=_rawBtnEnter , dark_image=_rawBtnEnter , size=(327, 55))
BtnBuy = ctk.CTkImage(light_image=_rawBtnBuy , dark_image=_rawBtnBuy , size=(327, 55))
BtnJoin = ctk.CTkImage(light_image=_rawBtnJoin , dark_image=_rawBtnJoin , size=(327, 55))

# Fonts
font_path_Montserrat = os.path.join(current_path, "fonts", "Montserrat-Regular.ttf")
font_path_GreatVibes = os.path.join(current_path, "fonts", "GreatVibes-Regular.ttf")
font_path_Cinzel = os.path.join(current_path, "fonts", "Cinzel-Regular.ttf")

ctk.FontManager.load_font(font_path_Montserrat)
ctk.FontManager.load_font(font_path_GreatVibes)
ctk.FontManager.load_font(font_path_Cinzel)

H1 = ctk.CTkFont(family="Great Vibes", size=32)
H2 = ctk.CTkFont(family="Montserrat", size=22)
H3 = ctk.CTkFont(family="Cinzel", size=30)

Body = ctk.CTkFont(family="Montserrat", size=16)
Crumbs = ctk.CTkFont(family="Montserrat", size=12)
