
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
print("\nREPORT ONE \n\nEquipment Purchase Sales\n")
# print("\n2022 Purchases")

sumpurchase2022 = '''
SELECT SUM(amount) AS `2022 TOTAL SALES` from equipment_purchase
WHERE date BETWEEN '2022.01.01' AND '2022.12.31'
'''
mycursor.execute(sumpurchase2022)
equipPur22 = mycursor.fetchone()
headers = [desc[0] for desc in mycursor.description]

max_width = [len(header) for header in headers]
for row in sumpurchase2022:
    for i, cell in enumerate(row):
        max_width[i] = max(max_width[i], len(str(cell)))
header_str = " | ".join(header.center(max_width[i]) for i, header in enumerate(headers))
print(header_str)

separator_str = "-+-".join("-" * width for width in max_width)
print(separator_str)

for row in sumpurchase2022:
    row_str = " | ".join(str(cell).center(max_width[i]) for i, cell in enumerate(row))
print(equipPur22[0])
print("\n")

# print("Total equipment purchases for this year: $", equipPur22[0])

#2021 Equipment Purchases
# print("\n2021 Purchases")
sumpurchase2021 = '''
SELECT SUM(amount) AS `2021 TOTAL SALES` from equipment_purchase
WHERE date BETWEEN '2021.01.01' AND '2021.12.31'
'''
mycursor.execute(sumpurchase2021)
equipPur21 = mycursor.fetchone()
# print("Total equipment purchases for this year: $", equipPur21[0])

headers = [desc[0] for desc in mycursor.description]

max_width = [len(header) for header in headers]
for row in sumpurchase2022:
    for i, cell in enumerate(row):
        max_width[i] = max(max_width[i], len(str(cell)))
header_str = " | ".join(header.center(max_width[i]) for i, header in enumerate(headers))
print(header_str)

separator_str = "-+-".join("-" * width for width in max_width)
print(separator_str)

for row in sumpurchase2022:
    row_str = " | ".join(str(cell).center(max_width[i]) for i, cell in enumerate(row))
print(equipPur21[0])
print("\n")
#2020 Equipment Purchases

# print("\n2020 Purchases")
sumpurchase2020 = '''
SELECT SUM(amount) AS `2020 TOTAL SALES` from equipment_purchase
WHERE date BETWEEN '2020.01.01' AND '2020.12.31'
'''
mycursor.execute(sumpurchase2020)
equipPur20 = mycursor.fetchone()
# print("Total equipment purchases for this year: $", equipPur20[0])

headers = [desc[0] for desc in mycursor.description]

max_width = [len(header) for header in headers]
for row in sumpurchase2022:
    for i, cell in enumerate(row):
        max_width[i] = max(max_width[i], len(str(cell)))
header_str = " | ".join(header.center(max_width[i]) for i, header in enumerate(headers))
print(header_str)

separator_str = "-+-".join("-" * width for width in max_width)
print(separator_str)

for row in sumpurchase2022:
    row_str = " | ".join(str(cell).center(max_width[i]) for i, cell in enumerate(row))
print(equipPur20[0])



#
# # #Is there anyone of those locations that has a downward trend in bookings?
print("\nReport Two\nDownward Trends")
downward = '''
SELECT region, hike, YEAR(dateStart), (customersBooked/customersAllowed) * 100  AS PERCENT_BOOKED
FROM trek
ORDER BY
region, hike
'''

mycursor.execute(downward)
result4 = mycursor.fetchall()

print("| {:^10} | {:^17} | {:^8} | {:^10} |".format("Region", "Hike", "Year", "% Booked"))
print("|{:-^12}|{:-^19}|{:-^10}|{:-^12}|".format("", "", "", ""))


for row in result4:
    print("| {:^10} | {:^17} | {:^8} | {:^10f} |".format(row[0], row[1], row[2], row[3]))



#Are there inventory items that are over five years old?

import datetime
oldmerch = '''SELECT equip_id, equipName, purchaseDate
FROM equipment_inventory
WHERE purchaseDate <= DATE_SUB(NOW(),INTERVAL 5 YEAR)
'''
mycursor.execute(oldmerch)
print("\nReport Three\nMerchandise over 5 years\n")
now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

result5= mycursor.fetchall()

print("equip_id".ljust(10) + "|", "equipName".ljust(15) + "|", "purchaseDate".ljust(15) + "|")
print("-" * 45)
for row in result5:
    equip_id = str(row[0])
    equipName = str(row[1])
    purchaseDate = str(row[2])
    print(equip_id.ljust(10) + "|", equipName.ljust(15) + "|", purchaseDate.ljust(15) + "|")
print("-" * 45)



