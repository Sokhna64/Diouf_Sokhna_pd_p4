import sqlite3
connexion = sqlite3.connect("gestion.db")
#methode associée à l'objet connexion qui permet de communiquer qvec la base de donnée via les requetes sql
cur= connexion.cursor()
#   Insertion contacts
query1= "insert into contacts (Nom, Email, Numero_Tel, Adresse) values ('Ndeye Oumy', 'niangomi@gmail.com', '776320075', 'Bab Septa'), ('Mohamed Barry', 'barry98@gmail.com', '778122863', 'Dakar'), ('Adjara Gueye', 'gueye845@gmail.com', '775496321', null), ('Ibrahim Diouf', 'idiouf9@gmail.com', '77334587', 'Kaolack'), ('Famata', 'matabintou@gmail.com', '774589234', 'Thies'), ('Mamadou Diouf', 'dioufacep@gmail.com', '775562798', 'Touba'), ('Ndeye Birame', 'mama10@gmail.com', '784055800', 'Rufisque')"
cur.execute(query1)
connexion.commit()


connexion.close()



