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

    # prevent crash if no file is selected
    if file.filename == "":
        return "Error: No file selected."

    vendor = request.form['vendor']
    amount = request.form['amount']
    date = request.form['date']
    category = request.form['category']

    # save file
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
    sort = request.args.get('sort', 'date')        # default sort by date
    category = request.args.get('category', '')    # filter category
    search = request.args.get('search', '')        # vendor search

    conn = get_db_connection()

    # Base query
    query = "SELECT * FROM receipts WHERE 1=1"
    params = []

    # Filter by category (if provided)
    if category:
        query += " AND category = ?"
        params.append(category)

    # Search by vendor (if provided)
    if search:
        query += " AND vendor LIKE ?"
        params.append(f"%{search}%")

    # Sorting
    if sort == 'amount':
        query += " ORDER BY amount DESC"
    elif sort == 'vendor':
        query += " ORDER BY vendor ASC"
    elif sort == 'category':
        query += " ORDER BY category ASC"
    else:
        # default: sort by date (assuming stored as text YYYY-MM-DD)
        query += " ORDER BY date DESC"

    receipts = conn.execute(query, params).fetchall()
    conn.close()

    # Pass current filters/sort to template so UI can reflect them
    return render_template('receipts.html',
                           receipts=receipts,
                           current_sort=sort,
                           current_category=category,
                           current_search=search)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_receipt(id):
    conn = get_db_connection()

    # Get file path so we can delete the image
    receipt = conn.execute("SELECT file_path FROM receipts WHERE id = ?", (id,)).fetchone()

    if receipt and receipt['file_path']:
        try:
            os.remove(receipt['file_path'])
        except FileNotFoundError:
            pass  # File already gone, ignore

    conn.execute("DELETE FROM receipts WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return redirect('/receipts')

@app.route('/edit/<int:id>')
def edit_receipt(id):
    conn = get_db_connection()
    receipt = conn.execute("SELECT * FROM receipts WHERE id = ?", (id,)).fetchone()
    conn.close()

    return render_template('edit.html', receipt=receipt)

@app.route('/update/<int:id>', methods=['POST'])
def update_receipt(id):
    vendor = request.form['vendor']
    amount = request.form['amount']
    date = request.form['date']
    category = request.form['category']

    conn = get_db_connection()
    conn.execute("""
        UPDATE receipts
        SET vendor = ?, amount = ?, date = ?, category = ?
        WHERE id = ?
    """, (vendor, amount, date, category, id))
    conn.commit()
    conn.close()

    return redirect('/receipts')

@app.route('/dashboard')
def dashboard():
    conn = get_db_connection()

    # Spending by category
    category_data = conn.execute("""
        SELECT category, SUM(amount) AS total
        FROM receipts
        GROUP BY category
    """).fetchall()

    # Spending by month (YYYY-MM)
    monthly_data = conn.execute("""
        SELECT substr(date, 1, 7) AS month, SUM(amount) AS total
        FROM receipts
        GROUP BY month
        ORDER BY month
    """).fetchall()

    # Top vendors
    vendor_data = conn.execute("""
        SELECT vendor, SUM(amount) AS total
        FROM receipts
        GROUP BY vendor
        ORDER BY total DESC
        LIMIT 5
    """).fetchall()

    conn.close()

    return render_template(
        'dashboard.html',
        category_data=category_data,
        monthly_data=monthly_data,
        vendor_data=vendor_data
    )

if __name__ == '__main__':
    app.run(debug=True)