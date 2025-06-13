from flask import Flask

app = Flask(__name__)

# Data sederhana
data = [
    {"nama": "Alice", "nilai": 85},
    {"nama": "Bob", "nilai": 92},
    {"nama": "Charlie", "nilai": 78},
    {"nama": "Diana", "nilai": 88}
]

@app.route('/')
def home():
    return '''
    <h1>Aplikasi Analisa Data Sederhana</h1>
    <p><a href="/data">Lihat Data</a></p>
    <p><a href="/rata">Lihat Rata-rata</a></p>
    '''

@app.route('/data')
def show_data():
    html = "<h2>Data Siswa:</h2><ul>"
    for siswa in data:
        html += f"<li>{siswa['nama']}: {siswa['nilai']}</li>"
    html += "</ul><p><a href='/'>Kembali</a></p>"
    return html

@app.route('/rata')
def rata_rata():
    total = sum(siswa['nilai'] for siswa in data)
    rata = total / len(data)
    return f'''
    <h2>Analisa Data:</h2>
    <p>Jumlah Siswa: {len(data)}</p>
    <p>Total Nilai: {total}</p>
    <p>Rata-rata: {rata:.1f}</p>
    <p><a href="/">Kembali</a></p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)