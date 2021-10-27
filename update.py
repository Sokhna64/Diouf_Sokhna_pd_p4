import sqlite3
connexion = sqlite3.connect("gestion.db")
#methode associée à l'objet connexion qui permet de communiquer qvec la base de donnée via les requetes sql
cur= connexion.cursor()
query="Update contacts set Nom = 'BABACAR' where ID = 3 "
cur.execute(query)
connexion.commit()
query1= "select * from contacts"
result= cur.execute(query1)
for row in result:
    print("ID :", row[0])
    print("Nom : ", row[1])
    print("Email: ", row[2])
    print("Numero Tel : ", row[3])
    print("Adresse : ", row[4])
    print("---------------------------")
    connexion.commit()
connexion.close()

