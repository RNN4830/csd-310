
import mysql.connector
from datetime import datetime, timedelta

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="H$8PjYFU",
    database="outland_adventures"
)
#CHECK DATABASE CONNECTION
# print("Connection worked")
# print(mydb)

mycursor = mydb.cursor()

def generateDate():
    dateObj = datetime.now()
    timestamp = dateObj.strftime("%Y-%m-%d %H:%M:%S")
    print("Report generated:", timestamp)

generateDate()


#Do enough customers buy equipment to keep equipment sales?
#2022 Equipment Purchases
print("\nReport One\nEquipment Purchase Sales")
print("\n2022 Purchases")
sumpurchase2022 = '''
SELECT SUM(amount) from equipment_purchase
WHERE date BETWEEN '2022.01.01' AND '2022.12.31'
'''
mycursor.execute(sumpurchase2022)
equipPur22 = mycursor.fetchone()
print("Total equipment purchases for this year: $", equipPur22[0])

#2021 Equipment Purchases
print("\n2021 Purchases")
sumpurchase2021 = '''
SELECT SUM(amount) from equipment_purchase
WHERE date BETWEEN '2021.01.01' AND '2021.12.31'
'''
mycursor.execute(sumpurchase2021)
equipPur21 = mycursor.fetchone()
print("Total equipment purchases for this year: $", equipPur21[0])

#2020 Equipment Purchases

print("\n2020 Purchases")
sumpurchase2020 = '''
SELECT SUM(amount) from equipment_purchase
WHERE date BETWEEN '2020.01.01' AND '2020.12.31'
'''
mycursor.execute(sumpurchase2020)
equipPur20 = mycursor.fetchone()
print("Total equipment purchases for this year: $", equipPur20[0])

#Is there anyone of those locations that has a downward trend in bookings?
print("\nReport Two\nDownward Trends")
downward = '''
SELECT region, hike, YEAR(dateStart), (customersBooked/customersAllowed) * 100  AS PERCENT_BOOKED
FROM trek
ORDER BY
region, hike
'''
mycursor.execute(downward)
result4 = mycursor.fetchall()
for result in result4:
    print(result[0:])

#Are there inventory items that are over five years old?

print("\nReport Three\nMerchandise over 5 years\n")
oldmerch = '''SELECT equip_id, equipName, purchaseDate
FROM equipment_inventory
WHERE purchaseDate <= DATE_SUB(NOW(),INTERVAL 5 YEAR)
'''
mycursor.execute(oldmerch)

for result in mycursor:
    print(result)

#
#
#
