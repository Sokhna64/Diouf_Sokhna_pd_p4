import sqlite3
import database
from database import createtable
print("--------(((BIENVENUE DANS VOTRE APPLICATION GESTION CONTACT--------- \n", " 1 : Ajouter un contact \n", " 2 : Modifier un contact un contact \n",
      " 3 : Supprimer un contact un contact \n", " 4 : Afficher tous les contacts \n", " 5 : Rechercher par un numéro de télephone \n",)
l = [1, 2, 3, 4, 5]
a = int(input("Taper le numéro de votre option:"))

if a not in l or a == '':
    print("Choix non disponible")
    exit()
if a == l[0]:
    nom = input("Donner le nom du contact ")
    mail = input("Donner l'adresse mail du contact ")
    tel = input("Donner le numéro de téléphone du contact ")
    adresse = input("Donner l'adresse du contact ")
    database.insert(nom, mail, tel, adresse)
    print("   Enregistrement réussi! ")
elif a == l[1]:
    database.listcontacts()
    c = int(input("Donner l'id du contact à modifier: "))
    database.recherchecontact(c)
    print("Choisir le numéro de l'attribut à modifier : \n",
          "1 Nom \n", "2 Mail \n", "3 Numero Tel \n", "4 Adresse")
    no = int(input("--> "))
    if no == 1:
        nom = input("Donner le nouveau nom")
        database.updatenom(nom, c)
        print("Modification réussi")
    elif no == 2:
        mail = input("Donner le nouveau mail")
        database.updatemail(mail, c)
        print("Modification réussi")
    elif no == 3:
        tel = input("Donner le nouveau numéro de téléphone")
        database.updatetel(tel, c)
        print("Modification réussi")
    elif no == 4:
        adresse = input("Donner le nouvel addresse")
        database.updateadr(adresse, c)
        print("Modification réussi")
    else:
        print("Choix non disponible")
elif a == l[2]:
    database.listcontacts()
    c = int(input("Donner l'id du contact à Supprimer: "))
    database.deletecontact(c)
    print("Contact supprimé !")
elif a == l[3]:
    database.listcontacts()
elif a == l[4]:
    num = input("Saisir le numéro de téléphone du contact demandé : ")
    database.recherchecontactNum(num)
