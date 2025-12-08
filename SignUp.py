import customtkinter as ctk
from PIL import ImageDraw
import Style as st

class SignUpGUI(ctk.CTkFrame):

    def __init__(self, master, switch_callback):
        super().__init__(master)
        self.callback = switch_callback
        self.assets = st.AppStyles()
        bg = self.assets.raw_images["Bg.png"].copy()

        draw = ImageDraw.Draw(bg)
        draw.text(xy=(self.assets.mw+43,200),text='Become a member', fill='white', font=self.assets.H1_Pil, anchor='mt')
        draw.text(xy=(30, 300), text='Full name', fill=self.assets.LightGray, font=self.assets.Crumbs_Pil, anchor='lt')
        draw.text(xy=(30, 370), text='Email', fill=self.assets.LightGray, font=self.assets.Crumbs_Pil, anchor='lt')
        draw.text(xy=(30, 440), text='Password', fill=self.assets.LightGray, font=self.assets.Crumbs_Pil, anchor='lt')
        draw.text(xy=(30, 510), text='Confirm password', fill=self.assets.LightGray, font=self.assets.Crumbs_Pil, anchor='lt')
        draw.text((self.assets.mw, 809), "Already a member?", fill=self.assets.LightGray, font=self.assets.Crumbs_Pil,anchor="mt")
        bg_image = ctk.CTkImage(light_image=bg, size=(375, 812))
        self.bgLabel = ctk.CTkLabel(self, image=bg_image, text='')
        self.bgLabel.pack()

        enter_fullname = ctk.CTkEntry(self, width=327, height=35,border_color=self.assets.Gold,fg_color="#071227",text_color='white')
        enter_fullname.place(x=30,y=270)
        enter_email = ctk.CTkEntry(self, width=327, height=35,border_color=self.assets.Gold,fg_color="#071227",text_color='white')
        enter_email.place(x=30,y=330)
        enter_password = ctk.CTkEntry(self, width=327, height=35,border_color=self.assets.Gold,fg_color="#071227",text_color='white')
        enter_password.place(x=30,y=390)
        label_login = ctk.CTkLabel(self, text="Sign up", width=self.assets.w,height=self.assets.h,image=self.assets.camuflage(self.assets.mw,830,self.assets.w,self.assets.h),font=self.assets.Crumbs,cursor="hand2")
        label_login.place(x=self.assets.mw,y=830)
        enter_confirmPassword = ctk.CTkEntry(self, width=327, height=35,border_color=self.assets.Gold,fg_color="#071227",text_color='white')
        enter_confirmPassword.place(x=30,y=450)
        terms_agreement = ctk.CTkCheckBox(self,text='I agree with terms of service and privacy policy.',bg_color="#071227", text_color='white', font=self.assets.Crumbs)
        terms_agreement.place(x=30,y=510)

        x,y=205,679
        w,h=45,18
        self.BtnSignUp = ctk.CTkLabel(self, text="Log in", width=w,height=h,image=self.assets.camuflage(x,y,w,h),font=self.assets.Crumbs,cursor="hand2")
        self.BtnSignUp.place(y=y, x=x)
        self.BtnSignUp.bind("<Button-1>", lambda e: self.callback("LogIn"))

        self.BtnEnter = ctk.CTkButton(self, text="", image=self.assets.images["BtnJoin"], hover=False, border_width=0, width=327, height=55, fg_color="#040D20", corner_radius=0)
        self.BtnEnter.place(y=770, x=self.assets.mw, anchor="center")
        self.BtnEnter.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        self.callback("Main")
