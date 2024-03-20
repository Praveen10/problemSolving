# Connect MySQL with python

import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1254",
        database="dbname"
    )

    mycursor = db.cursor()
    # mycursor.execute("create table person (personID int primary key AUTO_INCREMENT, name varchar(50))")
    # mycursor.execute("describe person")
    # mycursor.execute("insert into person (name) values (%s)", ("Bob",))
    # db.commit()
    # for i in mycursor:
    #     print(i)
    print("Connection established successfully!")
except mysql.connector.Error as err:
    print("Error: {}".format(err))