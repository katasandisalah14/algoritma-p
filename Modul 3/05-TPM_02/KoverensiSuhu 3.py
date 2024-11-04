# meminta input dari pengguna dalam fahrenheit
fahrenheit = float (input ("masuukan temperatur dalam fahrenheit :"))
 
# mengoferasi fahrenheit ke celcius
celcius = (fahrenheit - 32) * 5/9

# Menampilkan hasil konversi
print(f"{fahrenheit} derajat Fahrenheit = {celcius:.2f} derajat celcius. ")