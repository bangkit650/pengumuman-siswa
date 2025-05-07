from flask import Flask, render_template_string, request
import pandas as pd
import os

app = Flask(__name__)

# Load data from Excel
DATA_PATH = "data siswa.xlsx"
df = pd.read_excel(DATA_PATH)

# HTML Template (inline for simplicity)
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Login Pengumuman</title>
    <style>
        body { font-family: Arial; margin-top: 50px; text-align: center; }
        input { padding: 8px; margin: 5px; }
        .result { margin-top: 20px; font-size: 18px; }
    </style>
</head>
<body>
    <h2>Login Pengumuman Kelulusan</h2>
    <form method="post">
        <input type="text" name="nisn" placeholder="Masukkan NISN" required><br>
        <input type="date" name="tanggal_lahir" required><br>
        <button type="submit">Login</button>
    </form>
    {% if result %}
        <div class="result">
            {{ result|safe }}
        </div>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    result = ""
    if request.method == 'POST':
        nisn = request.form['nisn']
        tanggal_lahir = request.form['tanggal_lahir']

        # Filter data
        user = df[(df['NISN'].astype(str) == nisn) & (df['tanggal lahir'].astype(str) == tanggal_lahir)]

        if not user.empty:
            row = user.iloc[0]
            result = f"<strong>Selamat, {row['Nama']}</strong><br>Kelas: {row['Kelas']}<br>Status: <strong>{row['Status']}</strong>"
        else:
            result = "<span style='color:red;'>NISN atau Tanggal Lahir salah.</span>"

    return render_template_string(HTML, result=result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
