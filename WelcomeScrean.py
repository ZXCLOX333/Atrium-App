import customtkinter as ctk
import Style as st
from PIL import Image, ImageDraw, ImageFont

class WelcomeScreen(ctk.CTkFrame):
    def __init__(self,master, switch_callback):
        super().__init__(master)
        self.callback = switch_callback
        self.assets = st.AppStyles()
        
        Cizel65 = ImageFont.truetype(self.assets.font_path_Cinzel, 65)

        bg = self.assets.raw_images["Bg"].copy()
        draw = ImageDraw.Draw(bg)
        draw.text((self.assets.mw+30, 207), "Wellcome to", fill=self.assets.White, font=self.assets.H1_Pil,anchor="mt")
        draw.text((self.assets.mw+30, 315), "ATRIUM", fill=self.assets.Gold, font=Cizel65,anchor="mt")
        draw.text((self.assets.mw+30, 430), "To your private collection.", fill=self.assets.White, font=self.assets.H2_Pil,anchor="mt")
        draw.text((self.assets.mw+30, 465), "Cinema as a privilege.", fill=self.assets.White, font=self.assets.H2_Pil ,anchor="mt")
        bg_image = ctk.CTkImage(light_image=bg, size=(375, 812))
        self.background = ctk.CTkLabel(self,text="", image=bg_image)
        self.background.pack()

    
        self.BtnEnter = ctk.CTkButton(self, text="", image=self.assets.images["BtnEnter"], hover=False, border_width=0, width=327, height=55, fg_color="#040D20", corner_radius=0)
        self.BtnEnter.place(y=770, x=self.assets.mw, anchor="center")
        self.BtnEnter.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        self.callback()