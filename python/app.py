import mysql.connector

# Intenta conectarte a la base de datos
try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='310805310805Jvvv',
        database='masas_antioquiabd'
    )
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES ('testuser', 'testpassword')")
    connection.commit()
    print("Inserción exitosa")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    cursor.close()
    connection.close()
