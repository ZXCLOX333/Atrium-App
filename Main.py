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
        
        self.geometry("375x812")
        self.title("Atrium")

        self.WelcomeScreen=ws.WelcomeScreen(self, switch_callback=self.show_menu)
        self.LogInApp=li.LogInApp(self, switch_callback=self.show_menu)

        self.WelcomeScreen.pack(fill="both", expand=True)
    def show_menu(self):
        self.WelcomeScreen.pack_forget()
        self.LogInApp.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()