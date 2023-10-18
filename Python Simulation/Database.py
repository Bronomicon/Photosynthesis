import mysql.connector 

def CreateSimRunDatabase(DataHost, DataUser, DataPassword, DataName):
    Database = mysql.connector.connect(
        host = DataHost,
        user = DataUser,
        password = DataPassword,
        database = DataName
        )
    return Database


def OpenSimRunDatabase():
    return


mydb = mysql.connector.connect(

)

#mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE testdatabase")
#mycursor.execute("SHOW DATABASES")
#for x in mycursor:
#    print(x)

#mycursor.execute("CREATE TABLE testtable (testrow1 VARCHAR(50), testrow2 VARCHAR(50))")
#mycursor.execute("SHOW TABLES")

#for x in mycursor:
#    print(x)
#print(mydb)