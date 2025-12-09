import customtkinter as ctk
from PIL import ImageDraw
import Style as st
import re
from Database import DatabaseManager

class SignUpGUI(ctk.CTkFrame):

    def __init__(self, master, switch_callback):
        super().__init__(master)
        self.master = master 
        self.callback = switch_callback
        self.assets = st.AppStyles()

        bg = self.assets.raw_images["Bg"].copy()
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

        self.enter_fullname = ctk.CTkEntry(self, width=327, height=35,border_color=self.assets.Gold,fg_color="#071227",text_color='white')
        self.enter_fullname.place(x=30,y=270)
        self.enter_email = ctk.CTkEntry(self, width=327, height=35,border_color=self.assets.Gold,fg_color="#071227",text_color='white')
        self.enter_email.place(x=30,y=330)
        self.enter_password = ctk.CTkEntry(self, width=327, height=35,border_color=self.assets.Gold,fg_color="#071227",text_color='white')
        self.enter_password.place(x=30,y=390)
        self.label_login = ctk.CTkLabel(self, text="Sign up", width=self.assets.w,height=self.assets.h,image=self.assets.camuflage(self.assets.mw,830,self.assets.w,self.assets.h),font=self.assets.Crumbs,cursor="hand2")
        self.label_login.place(x=self.assets.mw,y=830)
        self.enter_confirmPassword = ctk.CTkEntry(self, width=327, height=35,border_color=self.assets.Gold,fg_color="#071227",text_color='white')
        self.enter_confirmPassword.place(x=30,y=450)
        self.terms_agreement = ctk.CTkCheckBox(self,text='I agree with terms of service and privacy policy.',bg_color="#071227", text_color='white', font=self.assets.Crumbs)
        self.terms_agreement.place(x=30,y=510)

        self.error_label = ctk.CTkLabel(
            self, text="", text_color="#FF4444", font=("Arial", 12)
        )
        self.error_label.place(x=self.assets.mw, y=560, anchor="center")

        
        x,y=205,679
        w,h=45,18
        self.BtnSignUp = ctk.CTkLabel(self, text="Log in", width=w,height=h,image=self.assets.camuflage(x,y,w,h),font=self.assets.Crumbs,cursor="hand2")
        self.BtnSignUp.place(y=y, x=x)
        self.BtnSignUp.bind("<Button-1>", lambda e: self.callback("LogIn"))

        self.BtnEnter = ctk.CTkButton(self, text="", image=self.assets.images["BtnJoin"], hover=False, border_width=0, width=327, height=55, fg_color="#040D20", corner_radius=0)
        self.BtnEnter.place(y=770, x=self.assets.mw, anchor="center")
        self.BtnEnter.bind("<Button-1>", self.on_click)

    def validate_password_complexity(self, password):
        if len(password) < 9:
            return False, "Password must be at least 9 characters."
        if not re.search(r"[0-9]", password):
            return False, "Password must contain at least one digit."
        if not re.search(r"[A-Z]", password):
            return False, "Password must contain at least one uppercase letter."
        if not re.search(r"[^a-zA-Z0-9]", password):
            return False, "Password must contain at least one special character."
        return True, ""
    
    def on_click(self, event=None):
        fullname = self.enter_fullname.get().strip()
        email = self.enter_email.get().strip()
        password = self.enter_password.get().strip()
        confirm = self.enter_confirmPassword.get().strip()
        agreed = self.terms_agreement.get()

        if not fullname or not email or not password or not confirm:
            self.error_label.configure(text="Please fill in all fields.")
            return

        if password != confirm:
            self.error_label.configure(text="Passwords do not match.")
            return

        if not agreed:
            self.error_label.configure(text="You must agree with terms of service.")
            return

        ok, msg = self.validate_password_complexity(password)
        if not ok:
            self.error_label.configure(text=msg)
            return

        db = DatabaseManager()
        success, message = db.register_user(fullname, email, password)

        if not success:
            self.error_label.configure(text=message)
            return

        user = db.login(email, password)
        if user:
            try:
                self.master.current_user = user
            except AttributeError:
                pass
            self.callback("Main")
        else:
            self.error_label.configure(
                text="Registered successfully, but auto-login failed. Please log in manually.")
