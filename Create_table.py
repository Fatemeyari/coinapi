import mysql.connector
connect = mysql.connector.connect(
        host="127.0.0.1",
        database="vision",
        user='root',
        password="your_password", )
connect_object=connect.cursor()
create_table=connect_object.execute("CREATE TABLE Price_bahar("
                                    "column_ INT PRIMARY KEY AUTO_INCREMENT,"
                                    "value_ INT NOT NULL,"
                                    "change_ INT ,"
                                    "timestamp_ INT,"
                                    "date_ TIMESTAMP )")

