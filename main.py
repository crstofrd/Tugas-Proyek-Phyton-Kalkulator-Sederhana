#Nantinya akan import fungsi operations dan input_handler

def main():
  while True:
    print("\n=== Kalkulator Sederhana ===")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")
    
    pilihan = input("Pilih operasi (1-5): ")
    
    if pilihan == '5':
      print("Terima kasih telah menggunakan kalkulatorr kami!")
      break
