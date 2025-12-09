import customtkinter as ctk
import threading
import speech_recognition as sr
from tkinter import filedialog 
import google.generativeai as genai 

import Style as st
import WelcomeScrean as ws
import LogIn as li
import SignUp as su
import MainPage as mp
import DetailsPage as dp
import AIHelperPage as ai
import Support as sp
import Account as ac
import secrets_config as sc
import ForgotPassword as fp

GEMINI_API_KEY = sc.API_KEY 

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="#000000") 
        self.assets = st.AppStyles()
        
        self.geometry("375x812")
        self.title("Atrium")

        self.current_user = None 

        print("!!! Я ЗАВАНТАЖИВ ПРАВИЛЬНИЙ ФАЙЛ !!!")
        
        self.setup_gemini()
        self.recognizer = sr.Recognizer()

        self.setup_chat_history()
        self.setup_navigation()
        self.setup_message_bar()

        self.list_frames = {}
        self.list_frames["Welcome"] = ws.WelcomeScreen(self, switch_callback=lambda: self.show_menu("LogIn"))
        self.list_frames["Main"] = mp.MainPageGUI(self, switch_callback=self.show_menu)

        self.list_frames["LogIn"] = li.LogInApp(self, switch_callback=self.show_menu) 
        self.list_frames["SignUp"] = su.SignUpGUI(self, switch_callback=self.show_menu) 
        self.list_frames["Support"] = sp.SupportPage(self, switch_callback=self.show_menu)
        self.list_frames["Account"] = ac.AccountPage(self, switch_callback=self.show_menu)
        self.list_frames["AIHelper"] = ai.AiHelperPage(self, switch_callback=self.show_menu)
        self.list_frames["Details"] = dp.DetailsPageGUI(self, switch_callback=self.show_menu)
        self.list_frames["Forgot"] = fp.ForgotPasswordApp(self, switch_callback=self.show_menu)

        self.show_menu("Welcome")
    
    def setup_gemini(self):
        try:
            genai.configure(api_key=GEMINI_API_KEY)
            self.model = genai.GenerativeModel('gemini-2.0-flash') 
            self.chat_session = self.model.start_chat(history=[])
            print("Gemini успішно підключено!")
        except Exception as e:
            print(f"Помилка підключення Gemini: {e}")

    def ask_gemini_thread(self, user_text):
        try:
            response = self.chat_session.send_message(user_text)
            ai_text = response.text
            self.after(0, lambda: self.add_message(ai_text, sender="ai"))
        except Exception as e:
            error_msg = "Вибачте, у мене проблеми зі з'єднанням."
            print(f"Gemini Error: {e}")
            self.after(0, lambda: self.add_message(error_msg, sender="ai"))

    def setup_chat_history(self):
        self.chat_frame = ctk.CTkScrollableFrame(
            self, 
            fg_color="transparent", 
            width=375, 
            height=540,            
            scrollbar_button_color="#000000",      
            scrollbar_button_hover_color="#040D20"
        )

    def add_message(self, text, sender="user"):
        if sender == "user":
            align = "e" 
            bg_color = "#1F2937" 
            text_color = "white" 
            margin = (50, 20)    
        else: 
            align = "w"          
            bg_color = "#040D31" 
            text_color = "#E0E0E0"
            margin = (20, 50)    

        try:
            msg_font = self.assets.Body
        except AttributeError:
            msg_font = ("Arial", 14) 

        message_bubble = ctk.CTkLabel(
            self.chat_frame,
            text=text,
            fg_color=bg_color,
            text_color=text_color,
            corner_radius=15,    
            font=msg_font,       
            wraplength=250,      
            justify="left",
            padx=15, pady=10     
        )
        message_bubble.pack(anchor=align, pady=5, padx=margin)
        self.after(10, lambda: self.chat_frame._parent_canvas.yview_moveto(1.0))

    def send_user_message(self, event=None):
        text = self.message_entry.get()
        if text.strip() != "": 
            self.add_message(text, sender="user") 
            self.message_entry.delete(0, "end")
            threading.Thread(target=self.ask_gemini_thread, args=(text,), daemon=True).start()

    def setup_navigation(self):
        self.nav_bar = ctk.CTkFrame(self, height=80, corner_radius=0, fg_color="black")
        self.create_nav_btn(self.nav_bar, "Home", "Home", lambda: self.show_menu("Main"))
        self.create_nav_btn(self.nav_bar, "AI", "AI", lambda: self.show_menu("AIHelper"))

    def create_nav_btn(self, parent, text, image_key, command):
        btn_frame = ctk.CTkFrame(parent, fg_color="transparent")
        btn_frame.pack(side="left", expand=True, fill="y")
        icon = ctk.CTkLabel(btn_frame, text="", image=self.assets.images[image_key])
        icon.pack(side="top", pady=(10, 0))
        label = ctk.CTkLabel(btn_frame, text=text, font=self.assets.Body, text_color=self.assets.Gray)
        label.pack(side="top", pady=(5, 0)) 
        def on_click(event): command()
        btn_frame.bind("<Button-1>", on_click)
        icon.bind("<Button-1>", on_click)
        label.bind("<Button-1>", on_click)

    def setup_message_bar(self):
        self.msg_bar = ctk.CTkFrame(self, height=60, corner_radius=30, fg_color="#000000") 
        self.message_entry = ctk.CTkEntry(
            self.msg_bar, placeholder_text="Повідомлення...", font=self.assets.Body,   
            fg_color="transparent", border_width=0, text_color="white",       
            placeholder_text_color="gray", height=40                 
        )
        self.message_entry.pack(side="left", fill="x", expand=True, padx=(20, 10), pady=10)
        self.message_entry.bind("<Return>", self.send_user_message)

        btn_mic = ctk.CTkButton(
            self.msg_bar, text="", image=self.assets.images["Microphone"], 
            fg_color="transparent", hover_color="#1A1A1A", width=40, height=40,
            command=self.start_voice_input 
        )
        btn_mic.pack(side="right", padx=(0, 10))

        btn_add = ctk.CTkButton(
            self.msg_bar, text="", image=self.assets.images["AddFile"], 
            fg_color="transparent", hover_color="#1A1A1A", width=40, height=40,
            command=self.open_file_explorer 
        )
        btn_add.pack(side="right", padx=(10, 0))

    def open_file_explorer(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            filename = filepath.split('/')[-1]
            self.message_entry.delete(0, "end")
            self.message_entry.insert(0, f"Файл: {filename}")

    def start_voice_input(self):
        threading.Thread(target=self._listen_process, daemon=True).start()

    def _listen_process(self):
        try:
            self.after(0, lambda: self.message_entry.configure(placeholder_text="Слухаю..."))
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = self.recognizer.listen(source, timeout=5)
                text = self.recognizer.recognize_google(audio, language="uk-UA")
                self.after(0, lambda: self._update_entry(text))
        except Exception:
            self.after(0, lambda: self.message_entry.configure(placeholder_text="Повідомлення..."))

    def _update_entry(self, text):
        self.message_entry.delete(0, "end")
        self.message_entry.insert(0, text)
        self.message_entry.configure(placeholder_text="Повідомлення...")

    def show_menu(self, frame_name):
        for frame in self.list_frames.values():
            frame.pack_forget()
        
        if frame_name in self.list_frames:
            self.list_frames[frame_name].pack(fill="both", expand=True)

        screens_with_nav = ["Account", "Main"] 
        screens_with_chat = ["Support", "AIHelper"] 

        if frame_name in screens_with_nav:
            self.nav_bar.place(x=0, rely=1.0, relwidth=1.0, anchor="sw")
            self.nav_bar.lift()
        else:
            self.nav_bar.place_forget()

        if frame_name in screens_with_chat:
            self.msg_bar.place(relx=0.5, rely=0.98, relwidth=0.9, anchor="s") 
            self.msg_bar.lift()
            self.chat_frame.place(x=0, y=110, relwidth=1, relheight=0.75) 
            self.chat_frame.lift()
        else:
            self.msg_bar.place_forget()
            self.chat_frame.place_forget()

        if frame_name == "Details":
            self.list_frames["Details"].update_info()

        if frame_name in self.list_frames:
            self.list_frames[frame_name].pack(fill="both", expand=True)

if __name__ == "__main__":
    app = MainApp()
    app.resizable(False, False)
    app.mainloop()