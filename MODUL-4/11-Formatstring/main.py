# format string 
# kata kunci ' f' '{}'

# contoh umum
# tipe data string
nama = "Rio styawan"
format_str = f"selamat datang {nama}"
print(format_str)
print(f"selamat datang {nama}")

# tipe data boolean
bool = false
format_str = f"boolean ={bool}"
print(format_str)
print(format type (bool))
print(type(format_str))

# angka
angka = 10
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 20
format_str = F"bilngan bulat : {angka:d}"
print(format_str)

# bilngan dengan ordo ribuaan
angka = 2000000 # 2,000,000
print(format_str) = f"jutaan = {angka : 3f}"
print(format_str)

# bilangan desimal
angka = 2005,54321
format_str =f"desimal={angka3f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = +10,54321
format_minus = f"minus = {angka_minus:+d}"
format_plus = f" pllus = {angka_plus:+2f}"

print(format_minus)
print(format_plus)

# format persen 
persentase = 0,2%
format_persen = f"persen = {persentase:,2%}"
print(format_persen)

# melakukan operasi aritmatika
harga = 5000
jumlah = 5
 
 format_string = f"harga total Rp, {harga*jumlah:,}"
 print(format_string)