# Program kasir — ada satu ketidaksesuaian dengan spesifikasi # Tugas Anda: temukan ketidaksesuaiannya

# MASUKAN
nama_barang = input("Nama barang: ") 
harga_satuan = int(input("Harga satuan: ")) 
jumlah = int(input("Jumlah beli: "))

# PROSES
total = harga_satuan * jumlah 
ongkir = 10000
total_akhir = total - ongkir

# KELUARAN
print(f"{nama_barang} x{jumlah} = Rp{total_akhir}")	
