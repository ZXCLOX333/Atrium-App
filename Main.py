import customtkinter as ctk
import Style as st
import WelcomeScrean as ws
import LogIn as li
import SignUp as su
import MainPage as mp
import DetailsPage as dp
import AIHelperPage as ai
import Support as sp
import Account as ac

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.assets = st.AppStyles() 
        
        self.geometry("375x812")
        self.title("Atrium")
     
        self.list_frames = {}

        self.list_frames["Welcome"] = ws.WelcomeScreen(self, switch_callback=lambda: self.show_menu("LogIn"))
        self.list_frames["LogIn"] = li.LogInApp(self, switch_callback=lambda: self.show_menu("Account")) 
        self.list_frames["Account"] = ac.AccountPage(self, switch_callback=lambda: self.show_menu("Welcome"))

        self.setup_navigation()

        self.show_menu("Welcome")

    def create_nav_btn(self, parent, text, image_key, command):
        btn_frame = ctk.CTkFrame(parent, fg_color="transparent")
        btn_frame.pack(side="left", expand=True, fill="y")
        
        icon = ctk.CTkLabel(
            btn_frame, 
            text="", 
            image=self.assets.images[image_key] 
        )
        icon.pack(side="top", pady=(10, 0))

        label = ctk.CTkLabel(
            btn_frame, 
            text=text, 
            font=self.assets.Body,
            text_color=self.assets.Gray 
        )
        label.pack(side="top", pady=(5, 0)) 

        def on_click(event):
            command()
            
        btn_frame.bind("<Button-1>", on_click)
        icon.bind("<Button-1>", on_click)
        label.bind("<Button-1>", on_click)

    def setup_navigation(self):
        self.nav_bar = ctk.CTkFrame(self, height=80, corner_radius=0, fg_color="black")
        
        self.create_nav_btn(
            parent=self.nav_bar,
            text="Home",
            image_key="Home.png",  
            command=lambda: self.show_menu("Welcome")
        )

        self.create_nav_btn(
            parent=self.nav_bar,
            text="AI",
            image_key="AI.png",    
            command=lambda: self.show_menu("Account")
        )


    def show_menu(self, frame_name):
        for frame in self.list_frames.values():
            frame.pack_forget()


        if frame_name in self.list_frames:
            self.list_frames[frame_name].pack(fill="both", expand=True)

        screens_with_bar = ["Account"] 
        
        if frame_name in screens_with_bar:
            self.nav_bar.place(x=0, rely=1.0, relwidth=1.0, anchor="sw")
            self.nav_bar.lift() 
        else:
            self.nav_bar.place_forget()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()