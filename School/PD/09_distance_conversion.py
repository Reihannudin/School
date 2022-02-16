# Km to Mil
# mengambil jumlah kilometer
kilometer = float(input("Masukan nilai kilometer: "))
                  
# faktor konversi
# yang artinya perbedaan antara mil dan kilometer itu adalah 0,621371
conv_fac = 0.621371

# menghitung mil
mil = kilometer * conv_fac
print('%0.2f Kilometer sama dengan %0.2f Mil' %(kilometer,mil))


# Mil to Km
# mengambil jumlah mil
mil = float(input("Masukan nilai mil: "))
                  
# faktor konversi
# yang artinya perbedaan antara mil dan kilometer itu adalah 0,621371
conv_fac = 1.621371

# menghitung mil
kilometer = mil * conv_fac
print('%0.2f Mil sama dengan %0.2f Kilometer' %(mil, kilometer))