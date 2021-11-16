import sqlite3
with sqlite3.connect("contacts.db") as connexion:
      cur=connexion.cursor()
def createtable():
      query= "create table listcontacts (Id integer primary key autoincrement, Nom text, Email text, NumTel text, Adresse text)"
      cur.execute(query)
      connexion.commit()

def insert(nom, mail, tel, adresse):
      cur.execute("insert into listcontacts (Nom, Email, NumTel, Adresse) values (?, ?, ?, ?)", (nom, mail, tel,  adresse))
      connexion.commit()

def listcontacts():
      query="select * from listcontacts "
      result= cur.execute(query)
      for row in result:
          print("ID :", row[0])
          print("Nom : ", row[1])
          print("Email: ", row[2])
          print("Numero Tel : ", row[3])
          print("Adresse : ", row[4])
          print("---------------------------")
def recherchecontact(id):
       query="select * from listcontacts where Id==%s" %(id)
       result= cur.execute(query)
       for row in result:
          print("ID :", row[0])
          print("Nom : ", row[1])
          print("Email: ", row[2])
          print("Numero Tel : ", row[3])
          print("Adresse : ", row[4])

def updatenom(nom, id):
      cur.execute("update listcontacts set Nom = '%s' where Id= '%s' " %(nom, id))
      connexion.commit()
def updatemail(mail, id):
      cur.execute("update listcontacts set Email = '%s' where Id= '%s' " %(mail, id))
      connexion.commit()
def updatetel(tel, id):
      cur.execute("update listcontacts set NumTel = '%s' where Id= '%s' " %(tel, id))
      connexion.commit()
def updatenom(adr, id):
      cur.execute("update listcontacts set Adresse = '%s' where Id= '%s' " %(adr, id))
      connexion.commit()
def deletecontact(id):
      cur.execute("DELETE FROM listcontacts WHERE id=%s " %(id))
      connexion.commit()

def recherchecontactNum(num):
       query="select * from listcontacts where NumTel==%s" %(num)
       result= cur.execute(query)
       if not result:
             print("Ce numéro n'existe pas")
       else:
          for row in result:
             print("ID :", row[0])
             print("Nom : ", row[1])
             print("Email: ", row[2])
             print("Numero Tel : ", row[3])
             print("Adresse : ", row[4])



