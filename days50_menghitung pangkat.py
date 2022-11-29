#program cara menghitung angka berpangkatan

number = int(input("masukkan angka : "))
pan = int(input("masukkan pangkat : "))

def perpangkatan (angka,pangkat):
	hasil = angka ** pangkat	
	print(hasil)
perpangkatan (number,pan)