from flask import Flask, render_template, request, redirect, url_for
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory;
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory;
import data;

app = Flask(__name__)
class Angket:
	def __init__(self,kategori,teks):
		self.kategori=kategori
		self.teks=teks

		'''penggolongan tiap saran dengan menggunakan class Angket
wordlist = [Angket('Ketua','Jangan Sering Tidur di Sekret'),
			Angket('Eksternal','Terlalu Banyak Nganggur Cari Sponsor yang Banyak'),
			Angket('Ketua','Jangan Terlalu Sibuk Pacaran , Semangat Menyelesaikan Proker karena Sebentar Lagi Masa Jabatan Selesai'),
			Angket('Bendahara','Jangan Kebanyakan Tidur , Hidup Harus Produktif Agar Masa Depan Cerah'),
			Angket('Sekretaris','Semoga Menjadi Senior HIC yang dikenang Sepanjang Masa , Untuk Mendidik Adiknya dan dijadikan Panutan'),
			Angket('RnD','Lebih sering mengadakan Sharing Internal karena UKM Keilmuan'),
			Angket('Internal','Menerapkan Aturan untuk Kebersihan Sekret'),
			Angket('Internal','Tetap dengan suara Khasnya dan Menjadi Panutanku'),
			Angket('Internal','Lebih Pahami adik - adiknya Terutama dalam Hal Pemberian Tanggung Jawab dan Kurangi Menganak Emaskan')]	
'''
f = open('text.txt','r')
wordlist = f.read().split('\n')
for angket in wordlist :
	print(angket.split(','))
	


'''array untuk jumlah dokumen'''
document = {'Ketua':0,
			'Bendahara':0,
			'Sekretaris':0,
			'RnD':0,
			'Internal':0,
			'Eksternal':0}

'''stemmer'''
factory_stemmer = StemmerFactory()
stemmer = factory_stemmer.create_stemmer()

'''stopword'''
factory_stopword = StopWordRemoverFactory()
stopword = factory_stopword.create_stop_word_remover()

'''mecah dari semua saran jadi kumpulan kata yang sudah di stem dan stopword yang tidak berulang'''
unique_words = []
for i in range(len(wordlist)):
	hitung_document = 0
	text = wordlist[i].teks
	category = wordlist[i].kategori
	document[category]+=1 #menghitung jumlah dokumen tiap kategori
	stem = stemmer.stem(text)
	stem = stopword.remove(stem)
	wordlist[i]=Angket(category,stem) #mengisi wordlist dengan kata" yang sudah d stem dan stop
	words = stem.split(' ')
	for word in words:
		if word not in unique_words:
			unique_words.append(word)

@app.route('/')
def home():
	return render_template('form.html')
	
def hitung(saran_hitung):
	hasil_temp = {'Ketua':0,
				  'Bendahara':0,
				  'Sekretaris':0,
				  'RnD':0,
				  'Internal':0,
				  'Eksternal':0}
	hasil = {'Ketua':0,
				  'Bendahara':0,
				  'Sekretaris':0,
				  'RnD':0,
				  'Internal':0,
				  'Eksternal':0}
		 	 

	max = 0
	kategori = ''
	for i in range(len(saran_hitung)):
		for sentence in wordlist:
			words = sentence.teks.split(' ')
			category = sentence.kategori
			for word in words:
				if word == saran_hitung[i]:
					if hasil_temp[category] == 0:
						hasil_temp[category]=1/document[category]					
					else:
						hasil_temp[category]=1/document[category]
						hasil[category]=hasil_temp[category]*hasil_temp[category]
			if hasil[category] > max:
				max = hasil[category]
				kategori = category
	return kategori

@app.route('/calculate', methods = ['POST','GET'])
def calculate():
	if request.method == 'POST':
		saran = request.form['saran']
	else:
		saran = request.args.get('saran')
	saran = stemmer.stem(saran)
	saran = stopword.remove(saran)
	saran_spasi = saran.split(' ')
	saran_hitung = []
	for kata in saran_spasi:
		if kata in unique_words:
			saran_hitung.append(kata)
	return redirect(url_for('result',kategori=hitung(saran_hitung)))

@app.route('/result/')
def error_result():
	return render_template('form.html',hasil='Kata yang anda inputkan belum dapat kami klasifikasikan')
	
@app.route('/result/<kategori>')
def result(kategori):
	return render_template('form.html',hasil='Terimakasih atas saran Anda, kami akan sampaikan ke '+kategori)
	
if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')


