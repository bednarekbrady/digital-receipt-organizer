from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_receipt():
    file = request.files['receipt']
    vendor = request.form['vendor']
    amount = request.form['amount']
    date = request.form['date']
    category = request.form['category']

    # Save file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    print("Uploaded Receipt:")
    print("Vendor:", vendor)
    print("Amount:", amount)
    print("Date:", date)
    print("Category:", category)
    print("File saved to:", file_path)

    return "Receipt uploaded successfully!"

if __name__ == '__main__':
    app.run(debug=True)