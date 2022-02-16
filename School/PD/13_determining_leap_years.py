# Program Python untuk memeriksa apakah tahun adalah tahun kabisat atau bukan
year = int(input("Masukan tahun: "))

# kita menggunakan module untuk mencari sisa bagi apabila bisa di bagi 4 dia berarti tahun kabisat
if (year % 4 ==0) and (year % 100 != 0):
    print("{0} ini adalah tahun kabisat".format(year))
else:
    print("{0} ini bukan tahun kabisat".format(year))
