import pafy
from youtubesearchpython import VideosSearch

class Risultato:
	def __init__(self, link, durata, titolo):
		self.link = link
		self.durata = durata
		self.titolo = titolo


class Music_downloader:

	selettore_automatico = True
	canzoni = []

	def __init__(self):
		self.canzoni = self.inizializza()
		print("[+] Inserimento canzoni avvenuto con successo\n")
		print("[!] Inserire il tipo di ricerca canzoni [A(utomatico)/M(anuale)]")

		temp = input("[A/M] -->").lower()
		while (temp != "a" and temp != "m" ):
			print("\nInserisci un'opzione valida\n")
			temp = input("[A/M] -->").lower()

		if ( temp == "m" ):
			self.selettore_automatico = False
		else:
			self.selettore_automatico = True



	def chiedi_canzoni( self ):

		print("[!] File \"input.txt\" non trovato, procededrò a chiedere in input da stdin\n")
		print("[!] Inserisci il nome delle canzoni separate da un \"a capo\"")
		print("\nInserisci -1 per fermare l'inserimento\n")
		temp = input("-->")
		lista_canzoni = []
		while  temp!="-1":
			lista_canzoni.append(temp)
			temp = input("-->")
		return lista_canzoni.copy()

	def inizializza( self ):

		file = True
		try:
			with open("input.txt") as fin:
				lines = fin.readlines()
				fin.close()
		except IOError:
			file = False

		if ( file ):
			return lines.copy()
		else:
			return self.chiedi_canzoni()

	def start_searching_music( self ):
		results = []
		for canzone in self.canzoni:
			if( self.selettore_automatico ):
				to_download = self.trova_canzone_automatico(canzone)
			else:
				to_download = self.trova_canzone_manuale(canzone)

			results.append(to_download)
		for canzone in results:
			self.download( canzone )

	def trova_canzone_automatico( self, search ):

		videoSearch = VideosSearch(search)
		link = videoSearch.result()["result"][0]["link"]
		durata = videoSearch.result()["result"][0]["duration"]
		titolo = videoSearch.result()["result"][0]["title"]
		print(titolo)
		return Risultato(link, durata, titolo)


	def trova_canzone_manuale ( self, search):

		videoSearch = VideosSearch(search, limit=5)
		i=0
		for result in videoSearch.result()["result"]:
			print("["+str(i+1)+"] "+ result["title"] + " Durata: " + result["duration"]+"\n")
			i+=1

		print("[!] Inserire l'id della canzone da scaricare\n")
		scelta = input("-->")
		while(int(scelta)-1 > 4 and int(scelta)-1 < 0  ):
			print("[!] Inserire l'id della canzone da scaricare\n")
			scelta = input("-->")
		scelta = int(scelta) - 1
		link = videoSearch.result()["result"][scelta]["link"]
		durata = videoSearch.result()["result"][scelta]["duration"]
		titolo = videoSearch.result()["result"][scelta]["title"]
		return Risultato(link, durata, titolo)

	def download(self, canzone):
		link = canzone.link
		nome = canzone.titolo
		durata = canzone.durata
		result = pafy.new(link)

		print("[+] Scarico " + nome + "\n")

		best_quality_audio = result.getbestaudio()
		best_quality_audio.download( quiet=True )

		print("[+] Download completato\n")

downloader = Music_downloader()
downloader.start_searching_music()


