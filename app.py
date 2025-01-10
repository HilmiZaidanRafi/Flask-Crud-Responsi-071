from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Database configuration
DB_CONFIG = {
    'host': 'nwsxf.h.filess.io',
    'user': 'dbmhs1_movieisput',
    'password': 'c892b3a6133623a1b839a36e4b561a67d795d4e7',
    'database': 'dbmhs1_movieisput',
    'port': '3305'
}

# Database connection function
def get_db_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

@app.route('/')
def index():
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM mahasiswa")
        mahasiswa = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('index.html', mahasiswa=mahasiswa)
    return "Database connection error", 500

@app.route('/add', methods=['POST'])
def add_mahasiswa():
    nim = request.form['nim']
    nama = request.form['nama']
    asal = request.form['asal']
    
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO mahasiswa (nim, nama, asal) VALUES (%s, %s, %s)",
                         (nim, nama, asal))
            connection.commit()
            flash('Data mahasiswa berhasil ditambahkan!', 'success')
        except Error as e:
            flash(f'Error: {str(e)}', 'error')
        finally:
            cursor.close()
            connection.close()
    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update_mahasiswa():
    nim = request.form['nim']
    nama = request.form['nama']
    asal = request.form['asal']
    
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE mahasiswa SET nama=%s, asal=%s WHERE nim=%s",
                         (nama, asal, nim))
            connection.commit()
            flash('Data mahasiswa berhasil diupdate!', 'success')
        except Error as e:
            flash(f'Error: {str(e)}', 'error')
        finally:
            cursor.close()
            connection.close()
    return redirect(url_for('index'))

@app.route('/delete/<string:nim>')
def delete_mahasiswa(nim):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM mahasiswa WHERE nim=%s", (nim,))
            connection.commit()
            flash('Data mahasiswa berhasil dihapus!', 'success')
        except Error as e:
            flash(f'Error: {str(e)}', 'error')
        finally:
            cursor.close()
            connection.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
