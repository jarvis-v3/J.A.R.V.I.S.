# Jarvis Assistant

Jarvis Assistant adalah asisten virtual berbasis Python yang dapat berinteraksi dengan pengguna melalui terminal. Proyek ini terdiri dari tiga komponen utama yang saling terintegrasi untuk memberikan pengalaman interaktif.

## Struktur Proyek

## Deskripsi File
- **`jarvis.py`**: Berfungsi sebagai antarmuka pengguna. Menampilkan percakapan antara pengguna dan asisten. Menampilkan status daya, status internet, dan suhu perangkat. Mengelola interaksi dengan pengguna dan memanggil fungsi dari `blackboxai.py` dan `main.py`.
- **`main.py`**: Berfungsi sebagai shell bot. Menyediakan fungsi untuk mengeksekusi perintah shell yang diberikan oleh pengguna. Mengembalikan hasil dari perintah yang dieksekusi.
- **`blackboxai.py`**: Berfungsi sebagai otak dari asisten virtual. Menggunakan `BlackBoxAI` untuk menghasilkan respons berdasarkan input pengguna. Mengelola logika pemrosesan percakapan.

## Cara Menjalankan
1. Clone repositori ini dengan perintah `git clone https://github.com/jarvis-v3/J.A.R.V.I.S..git` dan masuk ke direktori proyek dengan `cd jarvis_assistant`.
2. Instal dependensi yang diperlukan dengan perintah `pip install blackboxai`.
3. Jalankan asisten dengan perintah `python3 jarvis.py`.

## Fitur
- Interaksi percakapan dengan asisten virtual.
- Eksekusi perintah shell langsung dari antarmuka.
- Menampilkan status daya, status internet, dan suhu perangkat secara berkala.

## Kontribusi
Jika Anda ingin berkontribusi pada proyek ini, silakan buat pull request atau buka isu untuk diskusi.

## Lisensi
Proyek ini dilisensikan di bawah [MIT License](LICENSE).
