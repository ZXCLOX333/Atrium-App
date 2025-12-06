import customtkinter as ctk
import Style as st
from PIL import Image, ImageDraw, ImageFont

class AiHelperPage(ctk.CTkFrame):
    def __init__(self, master, switch_callback):
        super().__init__(master, fg_color="#040D20") 
        self.callback = switch_callback
        self.assets = st.AppStyles()

        bg = self.assets.raw_images["Bg.png"].copy()
        draw = ImageDraw.Draw(bg)
        draw.text((self.assets.mw + 40, 90), "ATRIUM", fill=self.assets.White, font=self.assets.H3_Pil, anchor="mt")
        
        bg_image = ctk.CTkImage(light_image=bg, size=(375, 812))
        self.background = ctk.CTkLabel(self, text="", image=bg_image)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)

        self.BtnAccount = ctk.CTkLabel(self, text="", image=self.assets.images["Account.png"], cursor="hand2")
        self.BtnAccount.place(x=315, y=65)
        self.BtnAccount.bind("<Button-1>", lambda event: self.callback("Account"))

        self.BtnExit = ctk.CTkLabel(self, text="", image=self.assets.images["Exit.png"], cursor="hand2", height=18)
        self.BtnExit.place(x=20, y=77)
        self.BtnExit.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        self.callback("Account")