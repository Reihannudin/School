# membuat variabel global
nama = "Petanikode"
versi = "1.0.0"

def help():
    # ini variabel lokal
    nama = "Program Reihanr"
    versi = "1.0.2"
    # mengakses variabel lokal
    print("Nama: %s" ,nama)
    print ("Versi: %s", versi)
    

# rumus: sisi x sisi
def luas_persegi(sisi):
    luas = sisi * sisi
    print(luas)
    return luas


# rumus: sisi x sisi x sisi
def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi
    print(volume)

if __name__ == "__main__":
    luas_persegi(10)

    volume_persegi(40)
            