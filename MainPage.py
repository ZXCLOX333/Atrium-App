import customtkinter as ctk
from PIL import ImageDraw

import Style as st
import config as cfg
import Database as db

class MainPageGUI(ctk.CTkFrame):

    def __init__(self, master, switch_callback):
        super().__init__(master)
        self.assets = st.AppStyles()
        self.db_manager = db.DatabaseManager()
        self.callback = switch_callback

        bg = self.assets.raw_images["Bg"].copy()
        draw = ImageDraw.Draw(bg)
        draw.text((self.assets.mw+45,50), 'A T R I U M', font=self.assets.H3_Pil, anchor='mt')
        bg_img = ctk.CTkImage(light_image=bg, size=(375,812))
        bg_label = ctk.CTkLabel(self, image=bg_img, text='')
        bg_label.pack()

        x,y=25,35
        self.BtnSupport = ctk.CTkLabel(self, text="", image=self.assets.images["Support"],font=self.assets.Crumbs,cursor="hand2")
        self.BtnSupport.place(x=x,y=y)
        self.BtnSupport.bind("<Button-1>", lambda event: self.callback("Support"))

        x,y=315,35
        self.BtnAccount = ctk.CTkLabel(self, text="", image=self.assets.images["Account"],font=self.assets.Crumbs,cursor="hand2")
        self.BtnAccount.place(x=x,y=y)
        self.BtnAccount.bind("<Button-1>", lambda event: self.callback("Account"))

        self.enter_search = ctk.CTkEntry(self,placeholder_text_color='white', bg_color='#071227',text_color='white', placeholder_text='Search 🔍', fg_color="#071227",width=350, height=35, border_color=self.assets.Gold)
        self.enter_search.place(x=13, y=110)
        self.enter_search.bind("<Return>", self.on_search)
                               
        movies_frame = ctk.CTkScrollableFrame(self, width=375, height=600, fg_color='#0B121F', border_width=0,
                                              corner_radius=0, scrollbar_button_color="#0B121F",
                                              scrollbar_button_hover_color="#0B121F")
        movies_frame.pack(fill="both", expand=True)
        movies_frame.place(x=0, y=150, relwidth=1, relheight=0.7)

        movies_data = self.db_manager.get_all_movies()

        row = 0
        col = 0


        for movie in movies_data:
            title = movie[0]
            img_name = movie[1] 
            price = movie[2]
            desc = movie[3]
            poster_img = self.assets.get_poster(img_name)

            if poster_img is None:
                print(f"Файл {img_name} не знайдено в папці Imgs!")
                continue 
            btn = ctk.CTkLabel(
                movies_frame, 
                text="", 
                image=poster_img, 
                cursor="hand2"
            )
            btn.grid(row=row, column=col, padx=16, pady=16)
            btn.bind("<Button-1>", lambda event, t=title: self.on_movie_click(t))
            if col == 1:
                col = 0
                row += 1
            else:
                col += 1
    def on_search(self, event):
        query = self.enter_search.get()
        
        if query:
            print(f"Шукаю: {query}") 
            movie_data = self.db_manager.get_movies(query)
            
            if movie_data:
                print(f"Знайдено: {movie_data[0]}")
                cfg.FilmName = movie_data[0]
                cfg.ImageFileName = movie_data[1]
                cfg.Price = movie_data[2]
                cfg.Description = movie_data[3]
                self.callback("Details")

                self.enter_search.delete(0, "end")
            else:
                print("Фільм не знайдено.")
                self.enter_search.configure(border_color="red")
        else:
            self.enter_search.configure(border_color=self.assets.Gold)

    def on_movie_click(self, title):
        print(f"Клікнули на: {title}. Роблю запит в БД...")
        full_movie_data = self.db_manager.get_movies(title)
        
        if full_movie_data:
            cfg.FilmName = full_movie_data[0]
            cfg.ImageFileName = full_movie_data[1]
            cfg.Price = full_movie_data[2]
            cfg.Description = full_movie_data[3]
            
            self.callback("Details")
        else:
            print("Помилка: Не вдалося завантажити дані про фільм.")