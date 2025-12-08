import customtkinter as ctk
import Style as st
from PIL import Image, ImageDraw, ImageFont

class ForgotPasswordApp(ctk.CTkFrame):
    def __init__(self, master, switch_callback):
        super().__init__(master)
        self.callback = switch_callback
        self.assets = st.AppStyles()

        bg = self.assets.raw_images["Bg.png"].copy()
        draw = ImageDraw.Draw(bg)
        draw.text((self.assets.mw+30, 207), "Forgot Password", fill=self.assets.White, font=self.assets.H1_Pil,anchor="mt")
        draw.text((30, 400), "Email", fill=self.assets.LightGray, font=self.assets.Crumbs_Pil,anchor="lt")
        draw.text((self.assets.mw, 809), "Remembered your password?", fill=self.assets.LightGray, font=self.assets.Crumbs_Pil,anchor="mt")
        bg_image = ctk.CTkImage(light_image=bg, size=(375, 812))
        self.background = ctk.CTkLabel(self,text="", image=bg_image)
        self.background.pack()

        x,y=205,679
        w,h=45,18
        self.BtnLogIn = ctk.CTkLabel(self, text="Log in", width=w,height=h,image=self.assets.camuflage(x,y,w,h),font=self.assets.Crumbs,cursor="hand2")
        self.BtnLogIn.place(y=y, x=x)
        self.BtnLogIn.bind("<Button-1>", lambda e: self.callback("LogIn"))

        EnterEmail = ctk.CTkEntry(self,width=327, height=35, border_width=0.53, corner_radius=4, fg_color="#071227", font=self.assets.Body,border_color=self.assets.Gold)
        EnterEmail.place(y=375, x=self.assets.mw, anchor="center")

        self.BtnSubmit = ctk.CTkButton(self, text="", image=self.assets.images["BtnEnter"], hover=False, border_width=0, width=327, height=55, fg_color="#040D20", corner_radius=0)
        self.BtnSubmit.place(y=770, x=self.assets.mw, anchor="center")
        self.BtnSubmit.bind("<Button-1>", self.on_click)
        
    def on_click(self, event):
        self.callback("Main")