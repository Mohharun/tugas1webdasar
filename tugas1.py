class manusia: 
 def __init__(self, nama, umur, jenis_kelamin, pekerjaan, alamat):
    self.nama =nama
    self.umur =umur
    self.jenis_kelamin = jenis_kelamin
    self.pekerjaan = pekerjaan
    self.alamat = alamat

 def sayhello(self):
   print("data orang")
   print("nama",orang.nama)
   print("umur",orang.umur)
   print("jenis_kelamin",orang.jenis_kelamin)
   print("pekerjaan",orang.pekerjaan)
   print("alamat",orang.alamat)

nama = input("masukan nama: ")
umur = input("masukan umur: ")
jenis_kelamin =input("masukan jenis_kelamin:")
pekerjaan =input("masukan pekerjaan: ")
alamat =input("masukan alamat: ")

orang = manusia(nama, umur, jenis_kelamin, pekerjaan, alamat)
orang.sayhello()

