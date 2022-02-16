# menggunakan library numpy
import numpy as np
from numpy import random

# 'Hasilkan Bilangan bulat acak dari 0 hingga 100'
print('Menghasilkan bilangan bulat acak dari 0 hingga 100')
x = random.randint(100)
print(x)


print('Menghasilkan bilangan bulat acak dari 0 hingga 100 dengan jumlah yang ditampilkan 10')
# Ini memiliki tiga parameter:
# n - jumlah percobaan.
# p - probabilitas terjadinya setiap percobaan (misalnya untuk lemparan koin 0,5 masing-masing).
# size - Bentuk array yang dikembalikan.

x = random.binomial(n=100, p=0.5, size=10)
print(x)


