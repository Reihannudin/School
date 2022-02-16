# Menggunakan Variabel Bantuan
print("Menggunakan variable bantuan")

cup_a = "Tea"
cup_b = "Coffe"

print('nilai awal')
print(f'cup_a = {cup_a}, cup_b = {cup_b}')

# variabel bantuan
cup_c = cup_a

# proses pertukaran
cup_a = cup_b
cup_b = cup_c

print('nilai akhir')
print(f'cup_a = {cup_a}, cup_b = {cup_b}\n')


# magic Python
print("Menggunakan Magic python")

box_a = "roti_bakar"
box_b = "martabak"

print("nilai awal")
print(f'box_a = {box_a}, box_b = {box_b}')

box_a, box_b = box_b, box_a
print("nilai akhir")
print(f'box_a = {box_a}, box_b = {box_b}')