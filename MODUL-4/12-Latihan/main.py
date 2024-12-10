tinggi_badan = tinggi_badan = float(input("masukkan tinggi_badan"))
berat_badan = float (input("masukkan berat_badan"))
 
tinggi_badan = tinggi_badan / 100
BMI = berat_badan / (tinggi_badan **2)

print(f"skor bmi adalah : {BMI:1f}")