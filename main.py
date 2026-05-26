import sys
import time
import os
pen = "penjual : "


class uhh:
    def __init__(self):
        self.lokasi_sekarang = "Kasir"
        self.Keranjang = []
        self.Keranjang_di_tangan = False  



game = uhh()


def cls():
    os.system('cls')

def pss(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def _pss(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def delay(waktu):
    time.sleep(waktu)

def animate_sliding_doors():
    HEIGHT = 4
    WIDTH = 10
    FRAMES = 45
    DELAY = 0.30

    WALL, SPACE = "█", " "
    V_BORDER, H_BORDER = "║", "═"
    TL, TR, BL, BR = "╔", "╗", "╚", "╝"

    def ease_out_cubic(t):
        return 1 - pow(1 - t, 3)

    try:
        for i in range(FRAMES + 1):
            cls()
            progress = i / FRAMES
            eased = ease_out_cubic(progress)
            
            open_w = int(eased * WIDTH)
            closed_w = max(0, WIDTH - open_w)

            lines = []
            lines.append(f"{TL}{H_BORDER * (2 * WIDTH)}{TR}")

            for h in range(HEIGHT):
                if i == FRAMES:
                    if h in (1, 2):
                        msg = " "
                        pad = (2 * WIDTH - len(msg)) // 2
                        rem = (2 * WIDTH - len(msg)) % 2
                        content = f"{' ' * pad}{msg}{' ' * (pad + rem)}"
                    else:
                        content = SPACE * (2 * WIDTH)
                else:
                    left  = WALL * closed_w
                    right = WALL * closed_w
                    mid   = SPACE * (2 * open_w)
                    content = f"{left}{mid}{right}"
                    if len(content) < 2 * WIDTH:
                        content += SPACE * (2 * WIDTH - len(content))
                
                lines.append(f"{V_BORDER}{content}{V_BORDER}")

            lines.append(f"{BL}{H_BORDER * (2 * WIDTH)}{BR}")
            print("\n".join(lines))
            time.sleep(DELAY)

    except KeyboardInterrupt:
        pass
    finally:
        cls()

def awal():
    animate_sliding_doors()
    delay(1)
    _pss("........",0.4)
    print(" (pintu terbuka)")
    delay(1)
    cls()
    _pss(pen,0.1)
    pss("Selamat datang di toko Aing macan",0.1)
    _pss(pen,0.1)
    pss("Kami Menjual Berbagai Barang, Silahkan Melihat lihat",0.1)
    delay(1)
    cls()
    _pss("......",0.2)
    print(" (Berjalan Masuk)")
    delay(2)
    cls()
    ui()
    delay(1)

def get_database():
    if not hasattr(game, 'db'):
        game.db = {
            "Makanan": {
                "silver_queen": {
                    "id": 1,
                    "nama": "Silver Queen",
                    "harga": 21000,      
                    "stok": 100,         
                    "satuan": "pcs",
                    "berat": 55,          
                    "varian": ["Almond", "Green Tea", "Mede"],
                    "Status_Promo": True, 
                    "Diskon": 10,         
                    "Lokasi":"Rak Makanan"
                },
                "fishermans_friend": {
                    "id": 2,
                    "nama": "FISHERMAN'S FRIEND",
                    "harga": 20000,
                    "stok": 10,
                    "satuan": "pcs",
                    "varian": ["Mint", "Lemon", "Blackcurrant"],
                    "Status_Promo": False,
                    "Diskon": 0,
                    "Lokasi":"Rak Makanan"
                }
            },
            "Peralatan": {
                "baygon": {
                    "id": 3,
                    "nama": "Baygon Cair",
                    "harga": 15000,
                    "stok": 5,
                    "satuan": "botol",
                    "berat": 165,
                    "varian": ["Jeruk", "Anggur"],
                    "Status_Promo": False,
                    "Diskon": 0,
                    "Lokasi":"Rak Peralatan"
                }
            }
        }
    return game.db

def kurangi_stok_database(nama_barang, qty):
    db = get_database()
    for kategori, items in db.items():
        for key, item in items.items():
            if item['nama'] == nama_barang:
                item['stok'] -= qty
                if item['stok'] < 0:
                    item['stok'] = 0 
                return True
    return False

def cari_barang_di_database(nama_input):
    db = get_database()
    nama_input_lower = nama_input.lower()
    for kategori, items in db.items():
        for key, item in items.items():
            if nama_input_lower in item['nama'].lower():
                return item
    return None

def get_barang_di_lokasi(lokasi):
    db = get_database()
    barang_ditemukan = []
    for kategori, items in db.items():
        for key, item in items.items():
            if item['Lokasi'] == lokasi:
                barang_ditemukan.append(item)
    return barang_ditemukan

def tindakan_tanya():
    pertanyaan = ["1. Tanya Barang","2. Lokasi Barang", "3. Promosi Terbaru","0. Tidak jadi Bertanya"]
    for i in pertanyaan:
        pss(i,0.03)
    print("")
    tindakan = input("Tindakan > ").strip()
    if tindakan == "0" or tindakan == "":
        cls()
        ui()
    elif tindakan == "1":
        cls()
        print("="*7," Bertanya Pada Kasir ","="*7)
        print("")
        _pss(pen)
        pss("barang apa yang ingin anda tanyakan?")
        print("# Masukan nama Barang atau enter untuk kembali")
        tanya_barang = str(input("Tindakan > ").strip())
        if tanya_barang == "":
            cls()
            ui()
            return
        
        hasil = cari_barang_di_database(tanya_barang)
        if hasil:
            cls()
            print("="*7,f" {hasil['nama']} ","="*7)
            print(f"Nama    : {hasil['nama']}")
            print(f"Harga   : {hasil['harga']}")
            print(f"Varian  : {hasil['varian']}")
            print(f"Stock   : {hasil['stok']}")
            if hasil["Status_Promo"]:
                print(f"Promo    : YES (Diskon {hasil['Diskon']}%)")
            else:
                print("Promo    : Tidak ada promo")
            print("# Tekan Enter Untuk Kembali")
            input()
            cls()
            ui()
        else:
            cls()
            _pss(pen)
            pss("Maaf Barang Tidak Tersedia")
            delay(3)
            cls()
            ui()

    elif tindakan == "2":
        cls()
        print("="*7," Cek Lokasi Barang ","="*7)
        print("")
        _pss(pen)
        pss("barang apa yang ingin anda Cari lokasinya?")
        print("# Masukan nama Barang atau enter untuk kembali")
        tanya_barang = str(input("Tindakan > ").strip())
        if tanya_barang == "":
            cls()
            ui()
            return
        
        hasil = cari_barang_di_database(tanya_barang)
        if hasil:
            cls()
            print("="*7,f" {hasil['nama']} ","="*7,"\n")
            _pss(pen)
            pss(f"{hasil['nama']} Berada di {hasil['Lokasi']}")
            print("\n\n# Tekan Enter Untuk Kembali")
            input()
            cls()
            ui()
        else:
            cls()
            _pss(pen)
            pss("Maaf Barang Tidak Tersedia")
            delay(3)
            cls()
            ui()

def ambil_keranjang_fisik():
    cls()
    print("="*7, " Ambil Keranjang ", "="*7)
    print("")
    if game.Keranjang_di_tangan:
        _pss(pen)
        pss("Anda sudah memegang keranjang.")
    else:
        _pss(pen)
        pss("Anda mengambil sebuah keranjang belanja.")
        game.Keranjang_di_tangan = True
        print("\n>> Sekarang Anda bisa memasukkan barang ke keranjang!")
    
    delay(2)
    cls()
    ui()

def pindah_lokasi():
    cls()
    print("="*7," Pindah Lokasi ","="*7)
    print("\n1. Rak Makanan")
    print("2. Rak Peralatan")
    print("3. Kasir")
    print("0. Batal")
    
    pilih = input("\nPilih Tujuan > ").strip()
    
    if pilih == "1":
        game.lokasi_sekarang = "Rak Makanan"
        print("\n>> Anda berjalan ke Rak Makanan...")
    elif pilih == "2":
        game.lokasi_sekarang = "Rak Peralatan"
        print("\n>> Anda berjalan ke Rak Peralatan...")
    elif pilih == "3":
        game.lokasi_sekarang = "Kasir"
        print("\n>> Anda berjalan ke Kasir...")
    else:
        print("\n>> Perjalanan dibatalkan.")
        
    delay(1.5)
    cls()
    ui()

def menu_ambil_barang():
    cls()
    lokasi = game.lokasi_sekarang
    
    if lokasi == "Kasir":
        print("Tidak ada barang untuk diambil di Kasir.")
        delay(1.5)
        ui()
        return

    if not game.Keranjang_di_tangan:
        print("Anda butuh keranjang untuk mengambil barang!")
        print("Silakan kembali ke Kasir dan pilih 'Ambil Keranjang'.")
        delay(2)
        ui()
        return

    barang_rak = get_barang_di_lokasi(lokasi)
    
    print("="*7, f" Isi {lokasi} ", "="*7)
    if not barang_rak:
        print("\nRak ini kosong.")
        input("\nTekan Enter...")
        ui()
        return

    for i, item in enumerate(barang_rak, 1):
        print(f"[{i}] {item['nama']} - Rp {item['harga']:,} (Stok: {item['stok']})")
    
    print("\n0. Kembali")
    
    try:
        pilih_idx = int(input("\nPilih Nomor Barang > "))
        if pilih_idx == 0:
            ui()
            return
        
        if 1 <= pilih_idx <= len(barang_rak):
            item_terpilih = barang_rak[pilih_idx - 1]
            
            try:
                qty = int(input(f"Masukkan Jumlah {item_terpilih['nama']} > "))
                if qty > 0:
                    if qty <= item_terpilih['stok']:
                        game.Keranjang.append({
                            'nama': item_terpilih['nama'],
                            'harga': item_terpilih['harga'],
                            'qty': qty,
                            'promo': item_terpilih['Status_Promo'],
                            'diskon_persen': item_terpilih['Diskon']
                        })
                        
                        print(f"\n>> {qty} {item_terpilih['nama']} berhasil dimasukkan ke keranjang!")
                        delay(1.5)
                        ui()
                    else:
                        print("Stok tidak cukup!")
                        delay(1.5)
                        menu_ambil_barang()
                else:
                    print("Jumlah harus lebih dari 0")
                    delay(1)
                    menu_ambil_barang()
            except ValueError:
                print("Input jumlah tidak valid")
                delay(1)
                menu_ambil_barang()
        else:
            print("Nomor barang tidak valid")
            delay(1)
            menu_ambil_barang()
            
    except ValueError:
        print("Input harus angka")
        delay(1)
        menu_ambil_barang()

def bayar_belanjaan():
    cls()
    print("="*7, " PEMBAYARAN ", "="*7)
    print("")
    
    if not game.Keranjang:
        print("Keranjang Anda kosong.")
        delay(1.5)
        ui()
        return

    total_bayar = 0
    print("Rincian Belanja:")
    for item in game.Keranjang:
        harga_final = item['harga']
        potongan = 0
        
        if item.get('promo', False):
            persen = item.get('diskon_persen', 0)
            potongan = int(harga_final * (persen / 100))
            harga_final = harga_final - potongan
            
        subtotal = harga_final * item['qty']
        total_bayar += subtotal
        
        info_diskon = f"(Disc {item['diskon_persen']}%)" if item.get('promo', False) else ""
        print(f"- {item['nama']} x{item['qty']} @ Rp {harga_final:,} {info_diskon} : Rp {subtotal:,}")
    
    print("")
    print(f"TOTAL TAGIHAN: Rp {total_bayar:,}")
    print("")
    
    konfirmasi = input("Apakah Anda yakin ingin membayar? (y/n) > ").strip().lower()
    
    if konfirmasi == 'y':
        for item in game.Keranjang:
            kurangi_stok_database(item['nama'], item['qty'])
        
        print("")
        _pss(pen)
        pss("Terima kasih! Pembayaran berhasil.")
        print("\n>> Stok barang telah diperbarui.")
        print(">> Keranjang belanja dikembalikan ke kasir.")
        
        # RESET TOTAL: Kosongkan isi keranjang DAN status pegang keranjang
        game.Keranjang = []
        game.Keranjang_di_tangan = False 
        
        delay(3)
        ui()
    else:
        print("Pembayaran dibatalkan.")
        delay(1)
        ui()

def uhh_tindakan(tindakannya_cik =0):
    if tindakannya_cik == 1:
        if game.lokasi_sekarang == "Kasir":
            tindakan_tanya()
        else:
            print("Anda harus kembali ke Kasir untuk bertanya pada penjaga.")
            delay(2)
            ui()
            
    elif tindakannya_cik == 2:
        ambil_keranjang_fisik()
        
    elif tindakannya_cik == 3:
        pindah_lokasi()
        
    elif tindakannya_cik == 4:
        cls()
        print("="*7, " Promosi Toko ", "="*7)
        print("\nPromo Hari Ini:")
        print("- Diskon 10% untuk semua Coklat (Silver Queen)")
        print("- Beli 2 Baygon Gratis 1 (Fake gaes, nanti saya rugi)")
        input("\nTekan Enter...")
        ui()

    elif tindakannya_cik == 5:
        bayar_belanjaan() 
        
    elif tindakannya_cik == 6:
        cls()
        print("Terima kasih sudah berbelanja!")
        exit()
        
    else:
        ui()

def ui():
    cls()
    print("="*7," Toko Bintnag ","="*7)
    print()
    print(f"Lokasi : {game.lokasi_sekarang}")
    print()
    
    if game.lokasi_sekarang != "Kasir":
        barang_rak = get_barang_di_lokasi(game.lokasi_sekarang)
        if barang_rak:
            print(f"[Barang Tersedia di {game.lokasi_sekarang}]:")
            for item in barang_rak:
                print(f"- {item['nama']} (Rp {item['harga']:,})")
            print()

    no_menu = 1
    
    if game.lokasi_sekarang == "Kasir":
        print(f"{no_menu}. Bertanya Pada Kasir")
        no_menu += 1
        
    if not game.Keranjang_di_tangan:
        print(f"{no_menu}. Ambil Keranjang")
        no_menu += 1
        
    if game.Keranjang_di_tangan and game.lokasi_sekarang != "Kasir":
        print(f"{no_menu}. Ambil Barang dari Rak")
        no_menu += 1

    print(f"{no_menu}. Pindah Lokasi")
    no_menu += 1
    
    if game.lokasi_sekarang == "Kasir":
        print(f"{no_menu}. Minta Kertas Promosi Toko")
        no_menu += 1

    if game.lokasi_sekarang == "Kasir" and len(game.Keranjang) > 0:
        print(f"{no_menu}. Bayar Belanjaan")
        no_menu += 1
        
    
    if not (game.Keranjang_di_tangan and len(game.Keranjang) > 0):
        print(f"{no_menu}. Keluar dari Toko")
        idx_keluar = no_menu
    else:
        idx_keluar = -1  

    print()
    
    try:
        tindakan = int(input("Tindakan > "))
        
         
        current_idx = 1
        if game.lokasi_sekarang == "Kasir":
            if tindakan == current_idx: uhh_tindakan(1)  
            current_idx += 1
            
        if not game.Keranjang_di_tangan:
            if tindakan == current_idx: uhh_tindakan(2)  
            current_idx += 1
            
        if game.Keranjang_di_tangan and game.lokasi_sekarang != "Kasir":
            if tindakan == current_idx: menu_ambil_barang()  
            current_idx += 1
            
        if tindakan == current_idx: uhh_tindakan(3)  
        current_idx += 1
        
        if game.lokasi_sekarang == "Kasir":
            if tindakan == current_idx: uhh_tindakan(4)  
            current_idx += 1
            
        if game.lokasi_sekarang == "Kasir" and len(game.Keranjang) > 0:
            if tindakan == current_idx: uhh_tindakan(5)  
            current_idx += 1
            
        # Cek Keluar
        if idx_keluar != -1 and tindakan == current_idx:
            uhh_tindakan(6)  
        
    except ValueError:
        ui()

 
awal()