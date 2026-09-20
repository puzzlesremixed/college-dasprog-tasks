# inputs
print(f"Selamat datang di program Kasir Sembako!")
print()
while True:
    try:
        products_number: int = int(input("Masukkan berapa banyak produk yang hendak anda hitung: "))
        if 0 < products_number <= 3:
            break
        else:
            print("ERROR : Mohon masukkan angka antara 1 hingga 3.")
            print("----------------------------")
    except ValueError:
        print("ERROR : Mohon masukkan angka yang valid!")
        print("----------------------------")


class Product:
    def __init__(self, name, price, qty):
        self.name: string = name
        self.price: int = price
        self.qty: int = qty


products: list[Product] = []
for product in range(products_number):
    print("----------------------------")
    print(f"Anda sedang memasukan informasi untuk produk nomor {product + 1}")

    #  get product name input
    while True:
        try:
            name: string = input("Nama barang: ")
            if 0 < len(name) <= 255 :
                break
            else:
                print("ERROR : Nama harus memiliki jumlah karakter 1-255.")
                print("----------------------------")
        except ValueError:
            print("ERROR : Mohon masukkan teks yang valid!")
            print("----------------------------")


    while True:
        try:
            price: int = int(input("Harga: "))
            if 1000 <= price <= 10000000 :
                break
            else:
                print("ERROR : Harga harus memiliki nilai diantara 1000-10000000.")
                print("----------------------------")
        except ValueError:
            print("ERROR : Mohon masukkan angka yang valid!")
            print("----------------------------")
            
    while True:
        try:
            qty: int = int(input("Kelipatan barang: "))
            if 1 <= qty <= 100 :
                break
            else:
                print("ERROR : Kelipatan harus memiliki nilai diantara 1-100.")
                print("----------------------------")
        except ValueError:
            print("ERROR : Mohon masukkan angka yang valid!")
            print("----------------------------")

    product: Product = Product(name, price, qty)
    products.append(product)

print()
print()

discount = 5 / 100

# process and output
print("----------------------------")
print("INFORMASI TRANSAKSI")
print("----------------------------")

total_bought: int = 0

for product in products:
    current_total: int = product.qty * product.price
    total_bought += current_total
    print(f"{product.name} (Rp{product.price})")
    print(f"x{product.qty} (Rp{current_total})")
    print("----------------------------")

if total_bought > 200000:
    print(f"Total belanja awal: Rp{total_bought}")
    total_disc: int = int(total_bought * discount)
    print(f"Diskon 5% = -Rp{total_disc}")
    total_bought -= total_disc
    print("----------------------------")

print(f"Total belanja akhir: Rp{total_bought}")
