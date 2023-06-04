import tkinter as tk
from tkinter import ttk
import mysql.connector


def modifier_location():
    selected_item = table_location.focus()
    if selected_item:
        values = table_location.item(selected_item, 'values')
        # Récupérer les valeurs des colonnes ID, Marque, Modèle, Durée
        id = values[0]
        marque = values[1]
        modele = values[2]
        duree = values[3]

        # Code pour la modification des données dans la base de données
        # ...
        # Modifier les valeurs nécessaires dans la base de données

        # Mettre à jour l'affichage du tableau
        table_location.item(selected_item, values=(id, marque, modele, duree))


def supprimer_location():
    selected_item = table_location.focus()
    if selected_item:
        values = table_location.item(selected_item, 'values')
        id = values[0]

        # Code pour la suppression des données dans la base de données
        # ...
        # Supprimer l'enregistrement correspondant à l'ID de la base de données

        # Supprimer l'élément sélectionné du tableau
        table_location.delete(selected_item)


def modifier_achat():
    selected_item = table_achat.focus()
    if selected_item:
        values = table_achat.item(selected_item, 'values')
        # Récupérer les valeurs des colonnes ID, Marque, Modèle, Année, Prix
        id = values[0]
        marque = values[1]
        modele = values[2]
        annee = values[3]
        prix = values[4]

        # Code pour la modification des données dans la base de données
        # ...
        # Modifier les valeurs nécessaires dans la base de données

        # Mettre à jour l'affichage du tableau
        table_achat.item(selected_item, values=(id, marque, modele, annee, prix))


def supprimer_achat():
    selected_item = table_achat.focus()
    if selected_item:
        values = table_achat.item(selected_item, 'values')
        id = values[0]

        # Code pour la suppression des données dans la base de données
        # ...
        # Supprimer l'enregistrement correspondant à l'ID de la base de données

        # Supprimer l'élément sélectionné du tableau
        table_achat.delete(selected_item)


root = tk.Tk()
root.title("MENU PRINCIPAL")
root.geometry("1350x700+0+0")
root.resizable(False, False)

lbltitre = tk.Label(root, borderwidth=3, relief="sunken", text="ADMINISTRATION", font=("Sans Serif", 25),
                    background="#248936", fg="#FFFAFA")
lbltitre.place(x=0, y=0, width=1350, height=100)

frame_location = tk.Frame(root, bd=3, relief="sunken")
frame_location.place(x=0, y=100, width=1350, height=300)

lbl_location = tk.Label(frame_location, text="ADMINISTRATION LOCATION", font=("Sans Serif", 20))
lbl_location.pack(side="top", pady=10)

table_location = ttk.Treeview(frame_location, columns=("ID", "Marque", "Modèle", "Durée"), height=5, show="headings")
table_location.pack(side="top", padx=10, pady=10)

table_location.heading("ID", text="ID")
table_location.heading("Marque", text="Marque")
table_location.heading("Modèle", text="Modèle")
table_location.heading("Durée", text="Durée")

table_location.column("ID", width=70)
table_location.column("Marque", width=70)
table_location.column("Modèle", width=70)
table_location.column("Durée", width=70)

# Connexion à la base de données et récupération des données
maBase_location = mysql.connector.connect(host="localhost", user="root", password="", database="vv")
meConnect_location = maBase_location.cursor()
meConnect_location.execute("SELECT * FROM location")
result_location = meConnect_location.fetchall()
for row in result_location:
    table_location.insert("", "end", values=row)

btn_modifier_location = tk.Button(frame_location, text="Modifier", command=modifier_location)
btn_modifier_location.pack(side="left", padx=10, pady=10)

btn_supprimer_location = tk.Button(frame_location, text="Supprimer", command=supprimer_location)
btn_supprimer_location.pack(side="left", padx=10, pady=10)

frame_achat = tk.Frame(root, bd=3, relief="sunken")
frame_achat.place(x=0, y=400, width=1350, height=300)

lbl_achat = tk.Label(frame_achat, text="ADMINISTRATION ACHAT VOITURE", font=("Sans Serif", 20))
lbl_achat.pack(side="top", pady=10)

table_achat = ttk.Treeview(frame_achat, columns=("ID", "Marque", "Modèle", "Année", "Prix"), height=5, show="headings")
table_achat.pack(side="top", padx=10, pady=10)

table_achat.heading("ID", text="ID")
table_achat.heading("Marque", text="Marque")
table_achat.heading("Modèle", text="Modèle")
table_achat.heading("Année", text="Année")
table_achat.heading("Prix", text="Prix")

table_achat.column("ID", width=70)
table_achat.column("Marque", width=150)
table_achat.column("Modèle", width=150)
table_achat.column("Année", width=70)
table_achat.column("Prix", width=70)

maBase_achat = mysql.connector.connect(host="localhost", user="root", password="", database="vv")
meConnect_achat = maBase_achat.cursor()
meConnect_achat.execute("SELECT * FROM vehicules")
result_achat = meConnect_achat.fetchall()
for row in result_achat:
    table_achat.insert("", "end", values=row)

btn_modifier_achat = tk.Button(frame_achat, text="Modifier", command=modifier_achat)
btn_modifier_achat.pack(side="left", padx=10, pady=10)

btn_supprimer_achat = tk.Button(frame_achat, text="Supprimer", command=supprimer_achat)
btn_supprimer_achat.pack(side="left", padx=10, pady=10)

root.mainloop()
