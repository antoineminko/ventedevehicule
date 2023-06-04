from tkinter import Tk, Label, Entry, Button, messagebox
import mysql.connector
from datetime import datetime

def vendre_vehicule():
    # Récupérer les informations du véhicule à vendre
    marque = entry_marque.get()
    modele = entry_modele.get()
    annee = entry_annee.get()
    prix = entry_prix.get()

    # Vérifier si toutes les informations sont saisies
    if not marque or not modele or not annee or not prix:
        messagebox.showwarning("Erreur", "Veuillez remplir tous les champs")
        return

    # Connexion à la base de données
    try:
        cnx = mysql.connector.connect(user='root', password='',
                                      host='localhost', database='vv')
        cursor = cnx.cursor()

        # Insertion des informations du véhicule dans la base de données
        query = "INSERT INTO vehicules (marque, modele, annee, prix) VALUES (%s, %s, %s, %s)"
        values = (marque, modele, annee, prix)
        cursor.execute(query, values)
        cnx.commit()

        # Génération de la facture au format texte
        generate_invoice(marque, modele, annee, prix)

        # Fermeture de la connexion à la base de données
        cursor.close()
        cnx.close()

        # Afficher un message de confirmation
        messagebox.showinfo("Vente réussie", "Le véhicule a été vendu avec succès")

    except mysql.connector.Error as err:
        messagebox.showerror("Erreur de connexion", str(err))

def generate_invoice(marque, modele, annee, prix):
    # Générer le nom du fichier de facture avec la date et l'heure actuelles
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    filename = f"facture_{timestamp}.txt"

    # Créer le contenu de la facture
    content = f"FACTURE DE VENTE\n\n"
    content += f"Marque: {marque}\n"
    content += f"Modèle: {modele}\n"
    content += f"Année: {annee}\n"
    content += f"Prix: {prix}\n"

    try:
        # Écrire le contenu dans le fichier de facture
        with open(filename, "w") as file:
            file.write(content)

        messagebox.showinfo("Facture générée", f"La facture a été générée avec succès\nNom du fichier: {filename}")

    except Exception as e:
        messagebox.showerror("Erreur de génération de facture", str(e))

# Créer une fenêtre
fenetre = Tk()
fenetre.title("Vente de véhicule")
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

label_annee = Label(fenetre, text="Année:")
label_annee.grid(row=2, column=0, padx=10, pady=5)
entry_annee = Entry(fenetre)
entry_annee.grid(row=2, column=1, padx=10, pady=5)

label_prix = Label(fenetre, text="Prix:")
label_prix.grid(row=3, column=0, padx=10, pady=5)
entry_prix = Entry(fenetre)
entry_prix.grid(row=3, column=1, padx=10, pady=5)


bouton_vendre = Button(fenetre, text="Vendre", command=vendre_vehicule)
bouton_vendre.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Lancer la boucle principale de la fenêtre
fenetre.mainloop()
