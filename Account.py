import customtkinter as ctk
import Style as st
from PIL import Image, ImageDraw, ImageFont
import Main as mn

class AccountPage(ctk.CTkFrame):
    def __init__(self,master, switch_callback):
        super().__init__(master)
        self.callback = switch_callback
        self.assets = st.AppStyles()
        Montserrat_Medium_User = ImageFont.truetype(self.assets.font_path_Montserrat_Medium, 28)

        User_Name = "Oleksandr  Kostyrko"
        User_Plan = "Premium Plan"
        
        bg = self.assets.raw_images["Bg.png"].copy()
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

        films_list = [name for name, size in self.assets.image_config.items() if size == (156, 178)]

        row = 0
        col = 0

        for film_name in films_list:
            btn = ctk.CTkLabel(self.movies_frame, text="", image=self.assets.images[film_name], cursor="hand2")
            btn.grid(row=row, column=col, padx=16, pady=16)
            btn.bind("<Button-1>", lambda event, f=film_name: self.on_film_click(f))
            if col == 1:
                col = 0
                row += 1
            else:
                col += 1

        self.Сrown = ctk.CTkLabel(self, text="", image=self.assets.images["Crown"], width=13, height=12)
        self.Сrown.place (x=120, y=168)
    def on_film_click(self, film_name):
        print(f"Ти натиснув на фільм: {film_name}")
            
    

        
    def on_click(self, event):
        self.callback()