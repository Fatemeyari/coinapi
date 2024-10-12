import requests
import mysql.connector
import datetime

response = requests.get("https://api.navasan.tech/latest/?api_key=freeHa3gPoBDxeHY2jVMrhV5BPpWPyIZ")
result = response.json()
value = ''
change = ''
timestamp = ''
for i in result['bahar']:
    value = result['bahar']["value"]
    change = result['bahar']["change"]
    timestamp = result['bahar']["timestamp"]

try:
    connect = mysql.connector.connect(
        host="127.0.0.1",
        database="vision",
        user='root',
        password="your_password ", )

except mysql.connector.Error as e:
    print(e)

connect_object=connect.cursor()
insert_mysql=("INSERT INTO price_bahar(value_ ,change_ ,timestamp_ ,date_)VALUES(%s,%s ,%s ,%s)")
mysql_value=(value,change,timestamp,datetime.datetime.now())
connect_object.execute(insert_mysql,mysql_value)
connect.commit()
