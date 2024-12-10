# percabangan
# struktur
"""
    1. if -nya
    2. punya kondisi
    3. punya aksi
  """
nama = input("masukkan nama : ")
  
  # percabangan yang inline (satu baris)
  #if nama == "Rio" : print("selamat datang")
  #print("terima kasih")
  
  # percabangan identasi 
if nama == "Rio":
      print("selamat datang")
      print("selamat belajar python")
print("bukan bagian percabangan")
  
  # percabangan 1 kondisi dan 2 aksi
  # pakai kata kunci 'else'
  
if nama == "Rio":
      print("selamat datang")
else:
      print(f'anda {nama}), bukan Rio')
print("Terima kasih")