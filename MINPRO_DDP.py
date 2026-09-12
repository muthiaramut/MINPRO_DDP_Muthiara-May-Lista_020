ebooks = []
kategori_ebook = ["Pembelajaran", "Penelitian", "Novel"]

ebooks_pembelajaran = [("DP", "Pak Amin"),("PTI", "Pak Hamdani"),("KSI", "Pak Putut")]
ebooks_penelitian = [("Research Design", "John W."), ("Study Case", "Robert K."), ("Metode Penelitian", "Wiratna S.")]
ebooks_novel = [("Hujan", "Tere Liye"), ("Rindu", "Tere Liye"), ("Sebelas", "Tere Liye")]

while True:
	print("Pilih Kategori:")
	print("1. Pembelajaran")
	print("2. Penelitian")
	print("3. Novel")
	print("4. Pilihan di kategori tidak ada")
	pilihan_kategori = input("Pilih kategori 1-4: ")

	if pilihan_kategori == "1":
		kategori = kategori_ebook[0]
		ebooks = ebooks_pembelajaran
		
	elif pilihan_kategori == "2":
		kategori = kategori_ebook[1]
		ebooks = ebooks_penelitian
		
	elif pilihan_kategori == "3":
		kategori = kategori_ebook[2]    
		ebooks = ebooks_novel
		
	elif pilihan_kategori == "4":
		print("Pilihan di kategori tidak ada")
		break
	
	else:   
		continue
	print("Kategori:", kategori)

	while True:
		print("1. Lihat Ebook")
		print("2. Tambah Ebook")
		print("3. Ubah Ebook")
		print("4. Hapus Ebook")
		print("5. Kembali ke Kategori")
		pilihan = input("Pilih menu 1-5: ")

		if pilihan == "1":
			print("Daftar Ebook:") 
			if ebooks:
				for ebook in ebooks:
					print(ebook[0], ebook[1])
			else:
				print("Belum ada ebook")                      

		elif pilihan == "2":
			print("Tambah Ebook:")
			judul = input("Judul: ")
			penulis = input("Penulis: ")
			ebook_baru = (judul, penulis)
			ebooks.append(ebook_baru)
			
			print("Ebook ditambahkan")
			for ebook in ebooks:
				print(ebook[0], ebook[1])

		elif pilihan == "3":
			if ebooks:
				for ebook in ebooks:
					print(ebook[0], ebook[1])

			ebook_lama = input("Masukkan judul ebook yang ingin diubah: ")
			for ebook in ebooks:
				if ebook[0] == ebook_lama:
					judul = input("Judul baru: ")
					penulis = input("Penulis baru: ")
					ebooks.remove(ebook)
					ebooks.append((judul, penulis))
					print("Ebook diubah")
					break
			else:
				print("Tidak ada ebook yang bisa diubah")

			print("Daftar Ebook sekarang:")
			for ebook in ebooks:
				print(ebook[0], ebook[1])

		elif pilihan == "4":
			if ebooks:
				for ebook in ebooks:
					print(ebook[0], ebook[1])

			ebook_hapus = input("Masukkan judul ebook yang dihapus: ")
			for ebook in ebooks:
				if ebook[0] == ebook_hapus:
					ebooks.remove(ebook)
					print("Ebook dihapus")
					break
			else:
				print("Tidak ada ebook yang bisa dihapus")

			print("Daftar Ebook sekarang:")
			for ebook in ebooks:
				print(ebook[0], ebook[1])

		elif pilihan == "5":
			break

		else:
			print("Pilihan menu tidak ada")
			
