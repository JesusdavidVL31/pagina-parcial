 install mysql-connector-python


import mysql.connector

conexion= mysql.connect(user='root', password='3108053108055',
                        
                  host='localhost' ,
                  database='masas_antioquia' ,
                  port=3306      
                        )

print(conexion)