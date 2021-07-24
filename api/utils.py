# coding: utf-8

import requests
import bs4
import string
import re

link = "http://www.koeri.boun.edu.tr/scripts/lst0.asp"

class Deprem:
	def __init__(self,bilgiler):
		self.tarih    = bilgiler[0].split(" ")[0]
		self.saat     = bilgiler[0].split(" ")[1]
		self.enlem    = bilgiler[1]
		self.boylam   = bilgiler[2]
		self.derinlik = bilgiler[3]
		self.md       = None if bilgiler[4]=="-.-" else bilgiler[4]
		self.ml       = None if bilgiler[5]=="-.-" else bilgiler[5]
		self.mw       = None if bilgiler[6]=="-.-" else bilgiler[6]
		self.yer      = bilgiler[7]
		self.nitelik  = bilgiler[8]

def parse(text):
    veri = re.split(" {2,}",text)
    if(len(veri) > 9):
        veri = [*veri[:8]," ".join(veri[8:])]
    elif len(veri) == 8:
    	veri.append(veri[7][50:])
    	veri[7] = veri[7][:50]

    return veri

def get_source():
	try:
		headers = {
			"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"
		}
		return requests.get(link,headers=headers,timeout=5).content
	except Exception as e:
		print("HATA!\n",str(e))
		return None

def get_veriler():
	kaynak = get_source()
	veriler = []

	if(kaynak):
		parser = bs4.BeautifulSoup(kaynak,"html.parser")
		for i in parser.pre.text.split("\r\n"):
			if i and (i[0] in string.digits):
				x = parse(i)
				veriler.append(Deprem(x))
	
	return veriler