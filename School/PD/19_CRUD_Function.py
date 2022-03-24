# define list
buku = []

# function show all data 
def show_data():
    if len(buku) == 0:
        print("Data is empty")
    else: 
        for index in range(len(buku)):
            print("[%d] %s" % (index, buku[index]))
            
            
#  function add data 
def add_data():
    buku_baru = input("Enter new book: ")
    buku.append(buku_baru)
    
# function for edit data
def edit_data():
    show_data()
    index = int(input("Enter ID Book: "))
    if(index > len(buku)):
        print("ID salah")
    else:
        judul_buku_baru = input("Enter new book: ")
        buku[index] = judul_buku_baru
        
# function for delete data
def delete_data():
    show_data()
    index = int(input("Enter ID Book "))
    if(index > len(buku)):
        print("ID salah")
    else:
        buku.remove(buku[index])
        
#  function show menu 
def show_menu():
    print ("\n")
    print ("----------- MENU ----------")
    print ("[1] Show Data")
    print ("[2] Add Data")
    print ("[3] Edit Data")
    print ("[4] Delete Data")
    print ("[5] Exit")
    
    menu = int(input("PILIH MENU> "))
    print("\n")

    if menu == 1:
       show_data()
    elif menu ==2:
       add_data()
    elif menu == 3:
       edit_data()
    elif menu ==4:
       delete_data()
    elif menu ==5:
       exit()
    else:
       print("Salah pilih!")
       
if __name__ == "__main__":
   while(True):
      show_menu()
            