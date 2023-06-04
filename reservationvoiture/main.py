from tkinter import *
from PIL import ImageTk, Image

fenetre = Tk()
fenetre.title("ESPACE COMMAND")
fenetre.geometry("1400x766")
fenetre.configure(bg="#ECF2F2")


def vioture():
    import voiture


def clien():
    import CLIEN

def achat():
    import achatvoiture


def location():
    import locationvehicule


lbl_title = Label(fenetre, text="MENU PRINCIPALE ", font=("times new roman", 17, "bold"), fg="white",  bg="#248936")
lbl_title.place(x=0, y=0, width=1355, height=50)



img = Image.open("C:/Users/DR_ANTOINE/Desktop/reservation voiture/image/voiture.jfif")
img = img.resize((300, 200), Image.ANTIALIAS)
photoimg = ImageTk.PhotoImage(img)
bnt_1 = Button(fenetre, image=photoimg, cursor="hand2",command=vioture)
bnt_1.place(x=20, y=300, width=300, height=160)
lbl_dep1 =Label(fenetre, text="VOITURE DISPONIBLE CHEZ JESS")
lbl_dep1.place(x=20, y=450)

img2 = Image.open("C:/Users/DR_ANTOINE/Desktop/reservation voiture/image/imare.jpg")
img2 = img2.resize((300, 200), Image.ANTIALIAS)
photoimg2 = ImageTk.PhotoImage(img2)
bnt_2 = Button(fenetre, image=photoimg2, cursor="hand2",command=clien)
bnt_2.place(x=370, y=300, width=300, height=160)
lbl_dep1 =Label(fenetre, text="CLIENTEL")
lbl_dep1.place(x=370, y=450)

img3 = Image.open("C:/Users/DR_ANTOINE/Desktop/reservation voiture/image/cash.png")
img3 = img3.resize((300, 200), Image.ANTIALIAS)
photoimg3 = ImageTk.PhotoImage(img3)
bnt_3 = Button(fenetre, image=photoimg3, cursor="hand2",command=achat)
bnt_3.place(x=700, y=300, width=300, height=160)
lbl_dep1 =Label(fenetre, text="ACHATE VOITURE")
lbl_dep1.place(x=700, y=450)


img4 = Image.open("C:/Users/DR_ANTOINE/Desktop/reservation voiture/image/location.jfif")
img4 = img4.resize((300, 200), Image.ANTIALIAS)
photoimg4 = ImageTk.PhotoImage(img4)
bnt_4 = Button(fenetre, image=photoimg4, cursor="hand2",command=location)
bnt_4.place(x=1050, y=300, width=300, height=160)
lbl_dep1 =Label(fenetre, text="LOCATION DE VOITURE",)
lbl_dep1.place(x=1050, y=450)





lbl_tit = Label(fenetre, text="SYSTEME DE GESTIONS VEHICULE DEVELOPPER PAR JESSICA ", font=("times new roman", 27, "bold"), fg="white",  bg="#248936")
lbl_tit.place(x=0, y=630, width=1400, height=50)

fenetre.mainloop()
