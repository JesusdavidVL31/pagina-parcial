from flask import Flask, request, jsonify
import pymysql
import bcrypt  

app = Flask(__name__)

# Configura la conexión a tu base de datos
db_config = {
    'host': '127.0.0.1',        
    'user': 'root',
    'password': '3108055310805Jvvv',  
    'database': 'masa_antioquiabd'
}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')  # Cambia "username" si tu campo se llama "usuario"
    password = data.get('password')  

    # Hashear la contraseña antes de almacenarla
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Conectar a la base de datos
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()

    # Insertar en la base de datos
    try:
        cursor.execute("INSERT INTO usuarios (usuario, contraseña) VALUES (%s, %s)", (username, hashed_password))
        conn.commit()
        return jsonify({"message": "Registro exitoso"}), 201
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({"message": "Error en el registro"}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
