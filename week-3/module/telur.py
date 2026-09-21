telur = int(input("Jumlah telur: ")) 
per_lusin = 12

lusin = telur // per_lusin 
sisa = telur % per_lusin
harga_per_butir = telur / per_lusin

print(f"Lusin utuh : {lusin}") 
print(f"Sisa butir : {sisa}") 
print(f"Harga/butir : {harga_per_butir}")
print(f"Tipe /	: {type(harga_per_butir)}") 
print(f"Tipe //	: {type(lusin)}")
