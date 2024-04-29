from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Function to create SQLite database and table
def create_table():
    conn = sqlite3.connect('registration.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS registrations
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, password TEXT)''')
    conn.commit()
    conn.close()

create_table()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_registration', methods=['POST'])
def submit_registration():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        
        if password != confirm_password:
            return "Passwords do not match!"
        
        # Insert the registration data into the database
        conn = sqlite3.connect('registration.db')
        c = conn.cursor()
        c.execute("INSERT INTO registrations (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        conn.close()
        
        return redirect('/success')

@app.route('/success')
def success():
    return "Registration successful!"

if __name__ == '__main__':
    app.run(debug=True)
