from flask import Flask, render_template, request, redirect
import os
import sqlite3

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_receipt():
    file = request.files['receipt']

    # Prevent crash if no file is selected
    if file.filename == "":
        return "Error: No file selected."

    vendor = request.form['vendor']
    amount = request.form['amount']
    date = request.form['date']
    category = request.form['category']

    # Save file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Insert into database
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO receipts (vendor, amount, date, category, file_path) VALUES (?, ?, ?, ?, ?)",
        (vendor, amount, date, category, file_path)
    )
    conn.commit()
    conn.close()

    return redirect('/receipts')

@app.route('/receipts')
def receipts():
    conn = get_db_connection()
    receipts = conn.execute("SELECT * FROM receipts ORDER BY date DESC").fetchall()
    conn.close()
    return render_template('receipts.html', receipts=receipts)

@app.route('/view/<int:id>')
def view_receipt(id):
    conn = get_db_connection()
    receipt = conn.execute("SELECT * FROM receipts WHERE id = ?", (id,)).fetchone()
    conn.close()
    return render_template('view_receipt.html', receipt=receipt)

if __name__ == '__main__':
    app.run(debug=True)