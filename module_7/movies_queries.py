
import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd = "",
    database = "movies"
)

mycursor = mydb.cursor()

print("-- DISPLAYING Studio RECORDS --")
mycursor.execute("SELECT * FROM studio")

myresult = mycursor.fetchall()

for row in myresult:
    print ("Studio ID: " + str(row[0]))
    print ("Studio Name: " + str(row[1]))

print ("\n\n-- DISPLAYING Genre RECORDS --")
mycursor.execute("SELECT * FROM genre")

myresult2 = mycursor.fetchall()
for row in myresult2:
    print ("Genre ID: " + str(row[0]))
    print ("Genre Name: " + str(row[1]))

print("\n\n-- DISPLAYING Short Film RECORDS --")
sql = "SELECT * FROM film WHERE film_runtime < 120"
mycursor.execute(sql)
myresult3 = mycursor.fetchall()
for result in myresult3:
    print("Film Name: " + str(result[1]))
    print("Runtime: " + str(result[3]))

print("\n\n-- DISPLAYING Director RECORDS in Order --")
sql = "SELECT * FROM film ORDER BY film_director"
mycursor.execute(sql)
myresult3 = mycursor.fetchall()
for result in myresult3:
    print("Film Name: " + str(result[1]))
    print("Director: " + str(result[4]))