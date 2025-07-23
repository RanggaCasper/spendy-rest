
# Spendy - FastAPI MongoDB (Async)

Spendy adalah aplikasi manajemen transaksi keuangan sederhana menggunakan **FastAPI** dan **MongoDB (Motor Async)**.

## 🚀 Fitur
- Tambah, lihat, dan hapus transaksi keuangan
- Filter transaksi berdasarkan tipe (pemasukan/pengeluaran)
- Koneksi MongoDB menggunakan `motor`
- Validasi data dengan Pydantic
- Struktur modular (routers, models, controllers)

## 🧱 Struktur Direktori

````

├── app/
│   ├── controllers/
│   │   └── transactions.py
│   ├── models/
│   │   └── transactions.py
│   ├── routes/
│   │   └── transactions.py
│   ├── database.py
├── main.py
└── .env

````

## 🔧 Instalasi

1. **Clone Repository**
```bash
git clone https://github.com/username/spendy.git
cd spendy
````

2. **Buat Virtual Enviroment**

```bash
python -m venv venv
source venv/bin/activate   # atau venv\Scripts\activate untuk Windows
```

3. **Install Dependensi**

```bash
pip install -r requirements.txt
```

4. **Setup File Env**
```
cp .env.example .env
```

4. **Atur Koneksi MongoDB di `.env`**

```
MONGODB_URL=mongodb://localhost:27017/spendy
```

5. **Jalankan Server**

```bash
uvicorn main:app --reload
```

## 📡 Endpoint API

* `POST /transactions` - Tambah transaksi
* `GET /transactions` - Lihat semua transaksi
* `GET /transactions/{id}` - Lihat detail transaksi
* `GET /transactions/type/{type}` - Filter berdasarkan tipe
* `DELETE /transactions/{id}` - Hapus transaksi

## 🧪 Contoh Request

```bash
curl -X POST http://localhost:8000/transactions \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Beli Kopi",
    "notes": "Starbucks",
    "amount": 30000,
    "type": "pengeluaran"
}'
```

## 📄 Lisensi

MIT License
Proyek ini dilisensikan di bawah [MIT License](LICENSE).

