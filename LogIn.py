import customtkinter as ctk
import Style as st
import config as cfg
from PIL import Image, ImageDraw, ImageFont
from Database import DatabaseManager  

class LogInApp(ctk.CTkFrame):
     
    def __init__(self, master, switch_callback):
        super().__init__(master)
        self.callback = switch_callback
        self.assets = st.AppStyles()
        self.master = master 

        bg = self.assets.raw_images["Bg"].copy()
        draw = ImageDraw.Draw(bg)
        draw.text((self.assets.mw+30, 207), "Welcome back.", fill=self.assets.White, font=self.assets.H1_Pil, anchor="mt")
        draw.text((30, 400), "Login", fill=self.assets.LightGray, font=self.assets.Crumbs_Pil, anchor="lt")
        draw.text((30, 500), "Password", fill=self.assets.LightGray, font=self.assets.Crumbs_Pil, anchor="lt")
        draw.text((self.assets.mw, 809), "New member?", fill=self.assets.LightGray, font=self.assets.Crumbs_Pil, anchor="mt")
        bg_image = ctk.CTkImage(light_image=bg, size=(375, 812))
        self.background = ctk.CTkLabel(self, text="", image=bg_image)
        self.background.pack()

        x, y = 25, 480
        w, h = 112, 30
        self.BtnForgotPassword = ctk.CTkLabel(self, text="Forgot password?", image=self.assets.camuflage(x,y,w,h), font=self.assets.Crumbs, cursor="hand2")
        self.BtnForgotPassword.place(y=y, x=x)
        self.BtnForgotPassword.bind("<Button-1>", lambda e: self.callback("Forgot") )
        

        x, y = 205, 679
        w, h = 60, 18
        self.BtnSignUp = ctk.CTkLabel(self, text="SignUp", width=w, height=h, image=self.assets.camuflage(x,y,w,h), font=self.assets.Crumbs, cursor="hand2")
        self.BtnSignUp.place(y=y, x=x)
        self.BtnSignUp.bind("<Button-1>", lambda e: self.callback("SignUp"))
        
        self.EnterLogin = ctk.CTkEntry(self,width=327, height=35, border_width=0.53, corner_radius=4, fg_color="#071227", font=self.assets.Body,border_color=self.assets.Gold)
        self.EnterLogin.place(y=375, x=self.assets.mw, anchor="center")
        self.EnterPassword = ctk.CTkEntry(self,width=327, height=35, border_width=0.53, corner_radius=4, fg_color="#071227", font=self.assets.Body,border_color=self.assets.Gold)
        self.EnterPassword.place(y=459, x=self.assets.mw, anchor="center")
        self.error_label = ctk.CTkLabel(self, text="", text_color="#FF4444", font=("Arial", 12), width = 150, height = h, image = self.assets.camuflage(self.assets.mw, 530, 150, h))
        self.error_label.place(y=530, x=self.assets.mw, anchor="center")

        self.BtnEnter = ctk.CTkButton(self, text="", image=self.assets.images["BtnEnter"], hover=False, border_width=0, width=327, height=55, fg_color="#040D20", corner_radius=0)
        self.BtnEnter.place(y=770, x=self.assets.mw, anchor="center")

        self.BtnEnter.bind("<Button-1>", self.on_login_click)

    def on_login_click(self, event=None):
        email = self.EnterLogin.get()
        password = self.EnterPassword.get()
        
        if not email or not password:
            self.error_label.configure(text="Please fill in all fields")
            return

        db = DatabaseManager()
        user = db.login(email, password)
        
        if user:
            print(f"Login is succesfull: {user['name']}")
            self.error_label.configure(text="")

            cfg.UserName = user['name']  
            cfg.UserEmail = email        

            self.EnterLogin.delete(0, 'end')
            self.EnterPassword.delete(0, 'end')
            
            self.callback("Main") 
        else:
            print("Login error")
            self.error_label.configure(text="Incorrect login or password")