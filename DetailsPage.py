import customtkinter as ctk
from PIL import ImageDraw
import Style as st

class DetailsPageGUI(ctk.CTkFrame):

    def __init__(self, master, switch_callback):
        super().__init__(master)
        assets = st.AppStyles()

        bg = assets.raw_images["Bg.png"].copy()

        draw = ImageDraw.Draw(bg)
        draw.text((assets.mw + 40, 60), text='A T R I U M', font=assets.H3_Pil, anchor='mt')
        draw.text((210, 130), text='film', font=assets.H1_Pil)
        draw.text((200, 210), text='$6.0', font=assets.H2_Pil)

        bg_image = ctk.CTkImage(light_image=bg, size=(375, 812))
        bgLabel = ctk.CTkLabel(self, image=bg_image, text='')
        bgLabel.pack()

        exit_img = ctk.CTkImage(light_image=(assets.raw_images['Exit.png'].copy()), size=(42, 18))
        labelExit = ctk.CTkButton(self, hover_color='black',width=42, height=18, fg_color='black',bg_color='black', image=exit_img, text='', cursor='hand2')
        labelExit.place(x=20,y=50)

        account_img = ctk.CTkImage(light_image=(assets.raw_images["Account.png"].copy()), size=(32, 41))
        label_account = ctk.CTkLabel(self, image=account_img, text='')
        label_account.place(x=320, y=40)

        film_label = ctk.CTkLabel(self,width=156,height=178, fg_color='#071227', text='')
        film_label.place(x=10,y=100)

        description = ctk.CTkLabel(self,text='', bg_color='#071227', fg_color='#071227', text_color='white')
        description.place(x=0, y=280, relwidth=1, relheight=0.6)
        
    def on_click(self, event):
        self.callback()
  
