import sys
import socket
import time

mode = sys.argv[1]

# --- SERVER 1 (Penjumlahan + Panggil Server 2) ---
if mode == 'server1':
    s = socket.socket()
    s.bind(('0.0.0.0', 5001))
    s.listen(1)
    print("Server 1 (Tambah & Forward) siap...")
    while True:
        conn, addr = s.accept()
        data = conn.recv(1024).decode().split(',')
        hasil_tambah = float(data[0]) + float(data[1])
        
        # BARU: Server 1 bertindak sebagai client untuk Server 2
        s2 = socket.socket()
        s2.connect(('192.168.5.10', 5002))
        s2.send(str(hasil_tambah).encode())
        pajak, total = s2.recv(1024).decode().split(',')
        s2.close()
        
        # Server 1 mengembalikan semua hasil lengkap ke Client asli
        conn.send(f"{hasil_tambah},{pajak},{total}".encode())
        conn.close()

# --- SERVER 2 (Hitung Pajak 10% - Tetap Sama) ---
elif mode == 'server2':
    s = socket.socket()
    s.bind(('0.0.0.0', 5002))
    s.listen(1)
    print("Server 2 (Pajak) siap...")
    while True:
        conn, addr = s.accept()
        jumlah = float(conn.recv(1024).decode())
        pajak = jumlah * 0.10
        total = jumlah + pajak
        conn.send(f"{pajak},{total}".encode())
        conn.close()

elif mode == 'client':
    time.sleep(2)
    angka1, angka2 = "100", "50"

    s1 = socket.socket()
    s1.connect(('server1', 5001))
    s1.send(f"{angka1},{angka2}".encode())
    
    hasil_tambah, pajak, total_akhir = s1.recv(1024).decode().split(',')
    s1.close()

    print(f"\n=== HASIL DI CLIENT (POLA CHAINING) ===\nAngka: {angka1} + {angka2} = {hasil_tambah}\nPajak: {pajak}\nTotal: {total_akhir}\n")

