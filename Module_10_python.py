import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="H$8PjYFU",
    database="outland_adventures"
)

#CHECK DATABASE CONNECTION
#print("Connection worked")
#print(mydb)

#INITLIZE CURSOR, OBJECT THAT COMMUNICATES WITH MYSQL SERVER
mycursor = mydb.cursor()

#CREATE DATABASE
#mycursor.execute("CREATE DATABASE IF NOT EXISTS outland_adventures")

#CHECK TO SEE IF DATABASE EXISTS
#mycursor.execute("SHOW DATABASES")
#for db in mycursor:
#    print(db)

#                                         EMPLOYEE                                                    #


mycursor.execute("CREATE TABLE IF NOT EXISTS employee \
(emp_id INTEGER(10) AUTO_INCREMENT \
,firstName VARCHAR(50) NOT NULL \
,lastName VARCHAR(50) NOT NULL \
,email VARCHAR(100) NOT NULL\
,phone VARCHAR(25) NOT NULL \
,job_title VARCHAR(25) NOT NULL \
,PRIMARY KEY (emp_id))")


# #ADDING DATA MANY ROWS
sqlFormula = "INSERT INTO employee (firstName, lastName, email, phone, job_title) VALUES (%s, %s, %s, %s, %s)"
array1 = [("Blythe","Timmerson","BTimmerson@Outland.com","652-555-1234","Owner"),
          ("Jim","Ford","JFord@Outland.com","650-555-6711","Owner"),
          ("John","MacNell","JMacNell@Outland.com","652-555-4444","Guide"),
          ("DB","Marland","DMarland@Outland.com","652-555-1886","Guide"),
          ("Anita","Gallegos","AGallegos@Outland.com","650-555-4775","Marketing Manager"),
          ("Dimitrios","Stravopolous","DStravopolous@Outland.com","652-555-1145","Supply Manager"),
          ("Mei","Wong","MWong@Outland.com","650-555-4587","Ecommerce Developer"),]

mycursor.executemany(sqlFormula,array1)
# #
mydb.commit()

#                                         CUSTOMER                                                    #

#
mycursor.execute("CREATE TABLE IF NOT EXISTS customer \
(customer_id INTEGER(10) AUTO_INCREMENT \
,firstName VARCHAR(50) NOT NULL \
,lastName VARCHAR(50) NOT NULL \
,email VARCHAR(100) NOT NULL\
,phone VARCHAR(25) NOT NULL \
,street_add VARCHAR(150) NOT NULL\
,city VARCHAR(50) NOT NULL \
,state VARCHAR(50) NOT NULL \
,zip INT (10) NOT NULL \
,PRIMARY KEY (customer_id))")

#
# SWOW TABLES
# mycursor.execute("SHOW TABLES")
# for tb in mycursor:
#    print(tb)

#ADDING DATA MANY ROWS
sqlFormula = "INSERT INTO customer (firstName, lastName, email, phone, street_add, city, state, zip) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
array1 = [("John","Smith","JSmith@email.com","555-234-5555","123 Beach St","Anywhere", "New Jersey", 23456),
           ("Amy","Brown","ABrown@email.com","555-456-5555","45688 Elm Ave","Nowhere", "New York", 45667),
          ("Marge","Johnson","MJohnson@email.com","555-222-5555","48886 Window St","Anytown", "Florida", 65482),
          ("Matt","Young","JSmith@email.com","555-441-5555","4177 Strait Rd","Anyplace", "California", 65333),
          ("Tiffany","White","JSmith@email.com","555-411-5555","75444 E Washington St","Noplace", "Ohio", 48555),
          ("Brad","Thompson","JSmith@email.com","555-854-5555","6811 Thompson St","Anytown", "California", 12564),
          ("Steve","Harris","JSmith@email.com","555-977-5555","41186 Harris Rd","Noplace", "Washington", 75562),
          ("Cynthia","Garcia","JSmith@email.com","555-853-5555","45 W Brook Way","Notown", "Montana", 45621),
          ("May","Smith","JSmith@email.com","555-545-5555","8411 12th St","Nowhere", "Florida", 32581),
          ("Scott","Jackson","JSmith@email.com","555-744-5555","4568 Circle Ct","Anywhere", "Kansas", 44568),
          ("David","Sorenson","JSmith@email.com","555-848-5555","74456 Obrien Rd","Notown", "Iowa", 33568),
          ("Qui","Nguyen","JSmith@email.com","555-651-5555","47715 Bloomingfield Pl","Anytown", "Texas", 74456),
          ("Kevon","Bradburry","JSmith@email.com","555-452-5555","711 Backroad Rd","Anywhere", "Kentucky", 18594),
          ("Wendy","White","JSmith@email.com","555-641-5555","6188 Ocean Way","Anywhere", "Florida", 45612),
          ("Ty","Harris","JSmith@email.com","555-744-5555","41 Sunset Dr","Notown", "California", 12348),
          ("Fred","Martinez","JSmith@email.com","555-321-5555","74111 Meadow Rd","Anywhere", "Wyoming", 12347),
          ("Amelia","Smith","JSmith@email.com","555-789-5555","7 River St","Anytown", "Ohio", 65411),
          ("Luke","Rodriguez","JSmith@email.com","555-451-5555","87 Pepper Ct","Notown", "New Mexico", 38541),
          ("Dan","Wilson","JSmith@email.com","555-777-5555","7944 Whale Watch St","Anywhere", "Washington", 17745),
          ("Bob","Martin","JSmith@email.com","555-899-5555","8947 Burbon St","Notown", "Louisiana", 65999),
          ("Mia","White","JSmith@email.com","555-748-5555","8842 Big Hat Circle","Anywhere", "Texas", 32177),
          ("George","Clark","JSmith@email.com","555-489-5555","7444 2nd St S","Anytown", "Michigan", 17775),]
#
mycursor.executemany(sqlFormula,array1)
#
mydb.commit()


#                                          TREK                                                    #
#
mycursor.execute("CREATE TABLE IF NOT EXISTS trek \
(trek_id INTEGER(10) AUTO_INCREMENT \
,region VARCHAR(50) NOT NULL \
,country VARCHAR(50) NOT NULL \
,hike VARCHAR(100) NOT NULL\
,days INT(5) NOT NULL \
,visa_req VARCHAR(20) NOT NULL\
,emp_id INTEGER \
,PRIMARY KEY (trek_id),\
 FOREIGN KEY (emp_id) REFERENCES employee(emp_id))")


#ADDING DATA MANY ROWS
sqlFormula = "INSERT INTO trek (region, country, hike, days, visa_req,emp_id) VALUES (%s, %s, %s, %s, %s, %s)"
array1 = [("Asia","Nepal","Annapurna",25,"VISA",1),
           ("Asia","Nepal","Everest",70,"VISA",1),
          ("S Europe","Italy","Dolomites",11,"ESTA",2),
          ("S Europe","Italy","Mt Faito",15,"ESTA",1),
          ("S Europe","Austria","Lynx Trail",13,"NO",2),
          ("Africa","Tanzania","Mt Kilimanjaro",12,"VISA",1),
          ("Africa","Tanzania","Ol Doinya Lengai",8,"VISA",2),
          ("Africa","Kenya","Mt Olokwe",7,"VISA",1)]
#
mycursor.executemany(sqlFormula,array1)
#
mydb.commit()




#                                 EQUIPMENT  INVENTORY                                                  #
#
mycursor.execute("CREATE TABLE IF NOT EXISTS equipment_inventory \
(equip_id INTEGER(10) AUTO_INCREMENT \
,equipName VARCHAR(50) NOT NULL \
,purchaseDate DATE NOT NULL \
,PRIMARY KEY (equip_id))")




sqlFormula = "INSERT INTO equipment_inventory (equipName, purchaseDate) VALUES (%s, %s)"
array1 = [("Hiking poles","2021.08.31"),
          ("Sleeping bag","2019.07.22"),
          ("Tent","2019.07.01"),
          ("Backpack","2018.05.01"),
          ("Sleeping bag","2022.07.01"),
          ("Tent","2016.09.23"),
          ("Head lamp","2022.05.13"),
          ("Tent","2019.07.01"),
          ("Rope equipment","2023.01.15"),
          ("Backpack","2020.10.14")]
#
mycursor.executemany(sqlFormula,array1)
#
mydb.commit()

#                                 INVOICE                                                 #
#
mycursor.execute("CREATE TABLE IF NOT EXISTS invoice \
(invoice_id INTEGER(10) AUTO_INCREMENT \
,Date DATE NOT NULL \
,total VARCHAR(50) NOT NULL \
,PRIMARY KEY (invoice_id))")

# ,rental_id INTEGER (50) NOT NULL \
# ,purchase_id INTEGER (50) NOT NULL \
# ,trek_id INTEGER (50) NOT NULL \
# ,customer_id INTEGER (50) NOT NULL \
# ,FOREIGN KEY (rental_id) REFERENCES equipment_rental(rental_id)\
# ,FOREIGN KEY (purchase_id) REFERENCES equipment_purchase(purchase_id)\
# ,FOREIGN KEY (trek_id) REFERENCES trek(trek_id)\
# ,FOREIGN KEY (customer_id) REFERENCES customer(customer_id)"




sqlFormula = "INSERT INTO invoice (Date, total) VALUES (%s, %s)"
array1 = [("2022.08.13","1299.50"),
          ("2022.05.22","1499.99"),
          ("2021.06.12","1122.99"),
          ("2019.07.01","1599.99"),
          ("2022.04.12","1299.99"),
          ("2022.08.10","1054.50"),
          ("2022.06.13","1044.99"),
          ("2021.07.23","1345.50"),
          ("2021.08.22","1555.50"),
          ("2022.06.13","1180.50"),]
#
mycursor.executemany(sqlFormula,array1)
#
mydb.commit()


#                                 EQUIPMENT PURCHASE                                                 #
#
mycursor.execute("CREATE TABLE IF NOT EXISTS equipment_purchase \
(purchase_id INTEGER(10) AUTO_INCREMENT \
,Date DATE NOT NULL \
,Amount INTEGER(10) NOT NULL \
,PRIMARY KEY (purchase_id))")




sqlFormula = "INSERT INTO equipment_purchase (Date, Amount) VALUES (%s, %s)"
array1 = [("2022.08.13","899.50"),
          ("2022.05.22","546.99"),
          ("2021.06.12","299.99"),
          ("2019.07.01","144.99"),
          ("2022.04.12","844.99"),
          ("2022.08.10","654.50"),
          ("2022.06.13","277.99"),
          ("2021.07.23","166.50"),
          ("2021.08.22","299.50"),
          ("2022.06.13","455.50"),]
#
mycursor.executemany(sqlFormula,array1)
#
mydb.commit()



#                                 EQUIPMENT RENTAL                                                 #
#
mycursor.execute("CREATE TABLE IF NOT EXISTS equipment_rental \
(rental_id INTEGER(10) AUTO_INCREMENT \
,Date DATE NOT NULL \
,Amount INTEGER(10) NOT NULL \
,PRIMARY KEY (rental_id))")




sqlFormula = "INSERT INTO equipment_rental (Date, Amount) VALUES (%s, %s)"
array1 = [("2022.08.13","225.50"),
          ("2022.05.22","199.99"),
          ("2021.06.12","299.99"),
          ("2019.07.01","199.99"),
          ("2022.04.12","189.99"),
          ("2022.08.10","159.50"),
          ("2022.06.13","399.99"),
          ("2021.07.23","499.50"),
          ("2021.08.22","199.50"),
          ("2022.06.13","159.50"),]
#
mycursor.executemany(sqlFormula,array1)
#
mydb.commit()

print("\n\nCUSTOMER TABLE")
mycursor.execute("SELECT * FROM customer")
for customer in mycursor:
    print(customer)

print("\n\nEMPLOYEE TABLE")
mycursor.execute("SELECT * FROM employee")
for employee in mycursor:
    print(employee)

print("\n\nEQUIPMENT INVENTORY TABLE")
mycursor.execute("SELECT * FROM equipment_inventory")
for inventory in mycursor:
    print(inventory)

print("\n\nEQUIPMENT RENTAL TABLE")
mycursor.execute("SELECT * FROM equipment_rental")
for rental in mycursor:
    print(rental)

print("\n\nEQUIPMENT PURCHASE TABLE")
mycursor.execute("SELECT * FROM equipment_purchase")
for purchase in mycursor:
    print(purchase)

print("\n\nINVOICE TABLE")
mycursor.execute("SELECT * FROM invoice")
for invoice in mycursor:
    print(invoice)

print("\n\nTREK TABLE")
mycursor.execute("SELECT * FROM trek")
for trek in mycursor:
    print(trek)


