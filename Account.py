import customtkinter as ctk
import Style as st
from PIL import Image, ImageDraw, ImageFont
import Main as mn
import config as cfg
import Database as db

class AccountPage(ctk.CTkFrame):
    def __init__(self,master, switch_callback):
        super().__init__(master)
        self.callback = switch_callback
        self.assets = st.AppStyles()
        self.db_manager = db.DatabaseManager()
        Montserrat_Medium_User = ImageFont.truetype(self.assets.font_path_Montserrat_Medium, 28)

        User_Name = "Oleksandr  Kostyrko"
        User_Plan = "Premium Plan"
        
        bg = self.assets.raw_images["Bg"].copy()
        draw = ImageDraw.Draw(bg)
        draw.text((self.assets.mw+40, 90), "ATRIUM", fill=self.assets.White, font=self.assets.H3_Pil,anchor="mt")
        draw.text((30, 165), f"{User_Name}", fill=self.assets.White, font=Montserrat_Medium_User, anchor="lt")
        draw.text((30, 200), f"{User_Plan}", fill=self.assets.LightGray, font=self.assets.Crumbs_Pil, anchor="lt")
        draw.text((85, 320), "Liked films", fill=self.assets.Gold, font=self.assets.H1_Pil,anchor="mt")
        bg_image = ctk.CTkImage(light_image=bg, size=(375, 812))
        self.background = ctk.CTkLabel(self,text="", image=bg_image)
        self.background.pack()

        x,y=25,65
        self.BtnSupport = ctk.CTkLabel(self, text="", image=self.assets.images["Support"],font=self.assets.Crumbs,cursor="hand2")
        self.BtnSupport.place(x=x,y=y)
        self.BtnSupport.bind("<Button-1>", lambda event: self.callback("Support"))
        x,y=315,65
        self.BtnAddAccount = ctk.CTkLabel(self, text="", image=self.assets.images["AddAccount"],font=self.assets.Crumbs,cursor="hand2")
        self.BtnAddAccount.place(x=x,y=y)

        self.movies_frame = ctk.CTkScrollableFrame(self, width=375, height=600, fg_color="#0B121F", border_width=0, corner_radius=0,scrollbar_button_color="#0B121F",scrollbar_button_hover_color="#0B121F") 
        self.movies_frame.pack(fill="both", expand=True)
        self.movies_frame.place(x=0, y=310, relwidth=1, relheight=0.5)

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
                self.movies_frame, 
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
            
    
