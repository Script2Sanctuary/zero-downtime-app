import time
import requests
import pandas as pd
from datetime import datetime

# URL aplikasi Anda (ganti <EXTERNAL_IP> dengan IP atau URL aplikasi Anda)
url = "http://localhost:80"

# Buat list kosong untuk menyimpan data
data = []

# Fungsi untuk menyimpan data ke Excel
def save_to_excel(data):
    df = pd.DataFrame(data, columns=["Timestamp", "Status", "Response"])
    df.to_excel("request_log_no_zero_downtime.xlsx", index=False)

while True:
    try:
        response = requests.get(url)
        status_code = response.status_code
        response_text = response.text
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Timestamp: {timestamp}, Status: {status_code}, Response: {response_text}")

        # Simpan hasil ke list
        data.append([timestamp, status_code, response_text])

        # Simpan data ke Excel setiap 10 request (agar file tidak ditulis terus-menerus)
        if len(data) % 10 == 0:
            save_to_excel(data)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data.append([timestamp, "Error", str(e)])

    time.sleep(1)  # Jeda 1 detik antara request
