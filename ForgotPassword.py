import customtkinter as ctk
import Style as st
from PIL import Image, ImageDraw
import random
import smtplib
from email.mime.text import MIMEText
from Database import DatabaseManager
import re


class ForgotPasswordApp(ctk.CTkFrame):
    def __init__(self, master, switch_callback):
        super().__init__(master)
        self.master = master
        self.callback = switch_callback
        self.assets = st.AppStyles()

        self.state = 1
        self.recovery_email = None
        self.generated_code = None

        self.build_ui()
        
    def send_recovery_code(self, to_email, code):
        MY_EMAIL = "Atrium32@outlook.com"
        MY_PASSWORD = "lzxogvnwauvcsqet" 

        msg = MIMEText(f"Your ATRIUM password recovery code is: {code}")
        msg["Subject"] = "ATRIUM — Password Recovery"
        msg["From"] = MY_EMAIL
        msg["To"] = to_email
        try:
            server = smtplib.SMTP("smtp-mail.outlook.com", 587)
            server.ehlo() 
            server.starttls() 
            server.ehlo() 
            
            server.login(MY_EMAIL, MY_PASSWORD)
            server.sendmail(MY_EMAIL, to_email, msg.as_string())
            server.quit()
            print(f"✅ Code sent to {to_email}")
        except Exception as e:
            print("❌ EMAIL ERROR:", e)

    def build_ui(self):
        for widget in self.winfo_children():
            widget.destroy()

        bg = self.assets.raw_images["Bg"].copy()
        draw = ImageDraw.Draw(bg)

        draw.text(
            (self.assets.mw + 30, 207),
            "Forgot Password",
            fill=self.assets.White,
            font=self.assets.H1_Pil,
            anchor="mt"
        )

        draw.text(
            (self.assets.mw, 809),
            "Remembered your password?",
            fill=self.assets.LightGray,
            font=self.assets.Crumbs_Pil,
            anchor="mt"
        )

        if self.state == 1:
            field_label = "Email"
        elif self.state == 2:
            field_label = "Enter code from email"
        else:
            field_label = "New password"

        draw.text(
            (30, 400),
            field_label,
            fill=self.assets.LightGray,
            font=self.assets.Crumbs_Pil,
            anchor="lt"
        )

        bg_image = ctk.CTkImage(light_image=bg, size=(375, 812))
        self.background = ctk.CTkLabel(self, text="", image=bg_image)
        self.background.pack()

        x, y = 205, 679
        w, h = 45, 18
        self.BtnLogIn = ctk.CTkLabel(
            self, text="Log in", width=w, height=h,
            image=self.assets.camuflage(x, y, w, h),
            font=self.assets.Crumbs,
            cursor="hand2"
        )
        self.BtnLogIn.place(y=y, x=x)
        self.BtnLogIn.bind("<Button-1>", lambda e: self.callback("LogIn"))

        self.error_label = ctk.CTkLabel(
            self, text="", text_color="#FF4444",
            font=("Arial", 12),
            width=200, height=20,
            image=self.assets.camuflage(self.assets.mw, 430, 200, 20)
        )
        self.error_label.place(y=430, x=self.assets.mw, anchor="center")

        if self.state == 1:
            self.email_entry = ctk.CTkEntry(
                self, width=327, height=35,
                border_width=0.53, corner_radius=4,
                fg_color="#071227",
                font=self.assets.Body,
                border_color=self.assets.Gold,
                placeholder_text="Enter your email"
            )
            self.email_entry.place(y=375, x=self.assets.mw, anchor="center")

        elif self.state == 2:
            self.code_entry = ctk.CTkEntry(
                self, width=200, height=35,
                border_width=0.53, corner_radius=4,
                fg_color="#071227",
                font=self.assets.Body,
                border_color=self.assets.Gold,
                placeholder_text="6-digit code"
            )
            self.code_entry.place(y=375, x=self.assets.mw, anchor="center")

        else:
            self.new_pass_entry = ctk.CTkEntry(
                self, width=327, height=35,
                border_width=0.53, corner_radius=4,
                fg_color="#071227",
                font=self.assets.Body,
                border_color=self.assets.Gold,
                placeholder_text="New password",
                show="*"
            )
            self.new_pass_entry.place(y=360, x=self.assets.mw, anchor="center")

            self.confirm_pass_entry = ctk.CTkEntry(
                self, width=327, height=35,
                border_width=0.53, corner_radius=4,
                fg_color="#071227",
                font=self.assets.Body,
                border_color=self.assets.Gold,
                placeholder_text="Confirm password",
                show="*"
            )
            self.confirm_pass_entry.place(y=410, x=self.assets.mw, anchor="center")

        self.BtnSubmit = ctk.CTkButton(
            self, text="",
            image=self.assets.images["BtnEnter"],
            hover=False, border_width=0,
            width=327, height=55,
            fg_color="#040D20", corner_radius=0
        )
        self.BtnSubmit.place(y=770, x=self.assets.mw, anchor="center")
        self.BtnSubmit.bind("<Button-1>", self.on_click)

    def validate_password(self, password: str):
        if len(password) < 5:
            return False, "Password must be at least 5 characters."
        if not re.search(r"[0-9]", password):
            return False, "Password must contain a digit."
        if not re.search(r"[A-Z]", password):
            return False, "Password must contain an uppercase letter."
        if not re.search(r"[^a-zA-Z0-9]", password):
            return False, "Password must contain a special character."
        return True, ""

    def on_click(self, event=None):
        if self.state == 1:
            self.handle_email_stage()
        elif self.state == 2:
            self.handle_code_stage()
        else:
            self.handle_new_password_stage()

    def handle_email_stage(self):
        email = self.email_entry.get().strip()
        if not email:
            self.error_label.configure(text="Please enter your email.")
            return

        db = DatabaseManager()
        if not db.check_email_exists(email):
            self.error_label.configure(text="Email not found.")
            return

        code = str(random.randint(100000, 999999))
        self.recovery_email = email
        self.generated_code = code

        self.send_recovery_code(email, code)

        self.state = 2
        self.build_ui()

    def handle_code_stage(self):
        entered = self.code_entry.get().strip()
        if not entered:
            self.error_label.configure(text="Please enter the code.")
            return

        if entered != self.generated_code:
            self.error_label.configure(text="Incorrect code.")
            return

        self.state = 3
        self.build_ui()

    def handle_new_password_stage(self):
        p1 = self.new_pass_entry.get().strip()
        p2 = self.confirm_pass_entry.get().strip()

        if not p1 or not p2:
            self.error_label.configure(text="Fill in both password fields.")
            return

        if p1 != p2:
            self.error_label.configure(text="Passwords do not match.")
            return

        ok, msg = self.validate_password(p1)
        if not ok:
            self.error_label.configure(text=msg)
            return

        db = DatabaseManager()
        if db.update_password(self.recovery_email, p1):
            self.callback("LogIn")
        else:
            self.error_label.configure(text="Failed to update password. Try again.")