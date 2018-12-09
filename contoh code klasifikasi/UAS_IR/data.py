class Angket:
	def __init__(self,kategori,teks):
		self.kategori=kategori
		self.teks=teks

'''penggolongan tiap saran dengan menggunakan class Angket'''
wordlist = [Angket('Ketua','Jangan Sering Tidur di Sekret'),
			Angket('Eksternal','Terlalu Banyak Nganggur Cari Sponsor yang Banyak'),
			Angket('Ketua','Jangan Terlalu Sibuk Pacaran , Semangat Menyelesaikan Proker karena Sebentar Lagi Masa Jabatan Selesai'),
			Angket('Bendahara','Jangan Kebanyakan Tidur , Hidup Harus Produktif Agar Masa Depan Cerah'),
			Angket('Sekretaris','Semoga Menjadi Senior HIC yang dikenang Sepanjang Masa , Untuk Mendidik Adiknya dan dijadikan Panutan'),
			Angket('RnD','Lebih sering mengadakan Sharing Internal karena UKM Keilmuan'),
			Angket('Internal','Menerapkan Aturan untuk Kebersihan Sekret'),
			Angket('Internal','Tetap dengan suara Khasnya dan Menjadi Panutanku'),
			Angket('Internal','Lebih Pahami adik - adiknya Terutama dalam Hal Pemberian Tanggung Jawab dan Kurangi Menganak Emaskan')]	
