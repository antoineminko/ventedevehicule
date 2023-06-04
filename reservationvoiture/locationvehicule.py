from tkinter import *
from tkinter import messagebox
import mysql.connector

def louer_vehicule():
    # Récupérer les informations du véhicule à louer
    marque = entry_marque.get()
    modele = entry_modele.get()
    duree = entry_duree.get()

    # Vérifier si toutes les informations sont saisies
    if not marque or not modele or not duree:
        messagebox.showwarning("Erreur", "Veuillez remplir tous les champs")
        return

    # Connexion à la base de données
    try:
        cnx = mysql.connector.connect(user='root', password='',
                                      host='localhost', database='vv')
        cursor = cnx.cursor()

        # Insertion des informations de location dans la base de données
        query = "INSERT INTO locations (marque, modele, duree) VALUES (%s, %s, %s)"
        values = (marque, modele, duree)
        cursor.execute(query, values)
        cnx.commit()

        # Calculer le coût total de la location
        cout = 50 * int(duree)

        # Générer la facture au format texte
        facture = f"Facture de location\n\nMarque : {marque}\nModèle : {modele}\nDurée : {duree} jours\nCoût total : {cout} $"

        # Enregistrer la facture dans un fichier texte
        with open("facture.txt", "w") as file:
            file.write(facture)

        # Fermeture de la connexion à la base de données
        cursor.close()
        cnx.close()

        # Afficher la messagebox de confirmation de location
        messagebox.showinfo("Location réussie", "La location a été effectuée avec succès. La facture a été enregistrée.")

    except mysql.connector.Error as err:
        messagebox.showerror("Erreur de connexion", str(err))

# Créer une fenêtre
fenetre = Tk()
fenetre.title("Location de véhicule")
fenetre.resizable(False,False)

# Créer des libellés et des champs de saisie pour les informations du véhicule
label_marque = Label(fenetre, text="Marque:")
label_marque.grid(row=0, column=0, padx=10, pady=5)
entry_marque = Entry(fenetre)
entry_marque.grid(row=0, column=1, padx=10, pady=5)

label_modele = Label(fenetre, text="Modèle:")
label_modele.grid(row=1, column=0, padx=10, pady=5)
entry_modele = Entry(fenetre)
entry_modele.grid(row=1, column=1, padx=10, pady=5)

label_duree = Label(fenetre, text="Durée (en jours):")
label_duree.grid(row=2, column=0, padx=10, pady=5)
entry_duree = Entry(fenetre)
entry_duree.grid(row=2, column=1, padx=10, pady=5)

# Créer un bouton pour effectuer la location
bouton_louer = Button(fenetre, text="Louer", command=louer_vehicule)
bouton_louer.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Lancer la boucle principale de la fenêtre
fenetre.mainloop()
