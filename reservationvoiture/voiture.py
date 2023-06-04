from tkinter import *

voitures = [
    {"nom": "mercedes-benz", "prix": 1000000},
    {"nom": "KIA 2023  ", "prix": 1500000},
    {"nom": " JEEP ", "prix": 2000000},
    {"nom": " TOUDRA ", "prix": 2500000},
    {"nom": " DACIA ", "prix": 5000000},
    {"nom": " TESLA ", "prix": 6000000}
]


fenetre = Tk()
fenetre.title("Liste des voitures")

# Créer un cadre pour afficher la liste des voitures
cadre_voitures = Frame(fenetre)
cadre_voitures.pack(padx=10, pady=5)

# Parcourir la liste de voitures et créer des libellés pour chaque voiture


for i, voiture in enumerate(voitures):
    nom = voiture["nom"]
    prix = voiture["prix"]

    label_nom = Label(cadre_voitures, text=nom)
    label_nom.grid(row=i, column=0, sticky=W, padx=5, pady=2)

    label_prix = Label(cadre_voitures, text=f"Prix: {prix}$")
    label_prix.grid(row=i, column=1, sticky=E, padx=5, pady=2)

# Lancer la boucle principale de la fenêtre
fenetre.mainloop()
