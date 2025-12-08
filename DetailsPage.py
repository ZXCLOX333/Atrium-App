import customtkinter as ctk
import Style as st
import config as cfg 
from PIL import Image, ImageDraw, ImageFont

class DetailsPageGUI(ctk.CTkFrame):

    def __init__(self, master, switch_callback):
        super().__init__(master, fg_color="#040D20")
        self.assets = st.AppStyles()
        self.callback = switch_callback

        bg = self.assets.raw_images["Bg"].copy()
        draw = ImageDraw.Draw(bg)
        draw.text((self.assets.mw + 40, 70), "ATRIUM", fill=self.assets.White, font=self.assets.H3_Pil, anchor="mt")
        
        bg_image = ctk.CTkImage(light_image=bg, size=(375, 812))
        self.background = ctk.CTkLabel(self, text="", image=bg_image)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)

        self.BtnAccount = ctk.CTkLabel(self, text="", image=self.assets.images["Account"], cursor="hand2")
        self.BtnAccount.place(x=315, y=45)
        self.BtnAccount.bind("<Button-1>", lambda event: self.callback("Account"))

        self.BtnExit = ctk.CTkLabel(self, text="", image=self.assets.images["Exit"], cursor="hand2", height=18)
        self.BtnExit.place(x=20, y=60)
        self.BtnExit.bind("<Button-1>", self.on_click)

        
        self.lbl_title = ctk.CTkLabel(self, text="", font=self.assets.H1, text_color=self.assets.Gold, image=self.assets.camuflage(170,130,100,70)
        )
        self.lbl_title.place(x=170, y=130, anchor="nw")


        self.lbl_price = ctk.CTkLabel(self, text="", font=self.assets.H2, text_color="white", image=self.assets.camuflage(200,210,100,50)
        )
        self.lbl_price.place(x=170, y=210, anchor="nw")

        self.lbl_desc = ctk.CTkLabel(self, text="", font=self.assets.Body, text_color="white",wraplength=350,justify="left",anchor="nw")
        self.lbl_desc.place(x=0, y=280, relwidth=1, relheight=0.6)

        self.lbl_image = ctk.CTkLabel(self, text="", width=156, height=178)
        self.lbl_image.place(x=10, y=100)

    def update_info(self):
        self.lbl_title.configure(text=cfg.FilmName)
        self.lbl_price.configure(text=f"${cfg.Price}")
        self.lbl_desc.configure(text=cfg.Description)
        img_name = cfg.ImageFileName
        new_img = self.assets.get_poster(img_name) 
        
        if new_img:
            self.lbl_image.configure(image=new_img)
        else:
            print(f"Не вдалося завантажити постер: {img_name}")

    def on_click(self, event):
        self.callback("Main")