# Praktikum-docker
# 🐳 Praktikum Docker - Manajemen Data

**Nama:** Hafizh Muhammad Ilham  
**NRP:** 3324600043  
**Program Studi:** D4 Sains Data Terapan  
**Mata Kuliah:** Manajemen Data  
**Dosen:** Isbat uzzin Nadhori S.Kom., M.T.

---

## 📋 Deskripsi

Repository ini berisi hasil praktikum Docker yang mencakup:
- Script monitoring dan analisa data menggunakan Bash
- Aplikasi web sederhana untuk analisa data menggunakan Python Flask
- Implementasi containerization dengan Docker
- Integrasi dengan database PostgreSQL


## 📁 Struktur Repository

```
docker-praktikum/
├── tugas1/                    # Script Bash untuk monitoring
│   ├── ssh_monitor.sh         # Monitor SSH service
│   ├── backup_script.sh       # Script backup otomatis
│   ├── max_temp.sh           # Analisa suhu maksimum
│   ├── avg_humidity.sh       # Analisa rata-rata kelembaban
│   └── data.txt              # Data sensor suhu dan kelembaban
├── tugas2/                    # Aplikasi Web Docker
│   ├── app.py                # Aplikasi Flask
│   ├── Dockerfile            # Docker configuration
│   ├── requirements.txt      # Python dependencies
├── docs/                      # Dokumentasi
│   └── laporan.pdf           # Laporan lengkap
└── README.md                 # File ini
```

## 🚀 Quick Start

### Prerequisites
- Docker Desktop terinstall
- Git terinstall
- Python 3.9+ (untuk development)

### 1. Clone Repository
```bash
git clone https://github.com/[username]/docker-praktikum.git
cd docker-praktikum
```

### 2. Jalankan Aplikasi Web
```bash
cd tugas2
docker build -t analisa-data-app .
docker run -p 5000:5000 analisa-data-app
```

### 3. Akses Aplikasi
`http://localhost:5000`


## 🛠️ Script Monitoring (Tugas 1)

### 1. SSH Monitor (`ssh_monitor.sh`)
```bash
# Menjalankan monitoring SSH
chmod +x tugas1/ssh_monitor.sh
./tugas1/ssh_monitor.sh
```
**Fungsi:** Monitor status SSH service setiap 10 detik

### 2. Backup Script (`backup_script.sh`)
```bash
# Menjalankan backup otomatis
chmod +x tugas1/backup_script.sh
./tugas1/backup_script.sh
```
**Fungsi:** Backup direktori secara berkala dengan rotasi file

### 3. Analisa Data Sensor
```bash
# Analisa suhu maksimum
./tugas1/max_temp.sh

# Analisa rata-rata kelembaban
./tugas1/avg_humidity.sh
```

