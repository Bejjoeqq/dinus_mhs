import requests
import json
from bs4 import BeautifulSoup

nama = str(input("Nama:"))

url = "https://dinus.ac.id//search/"
headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/87.0.4280.141",
        "Content-Type": "application/x-www-form-urlencoded",
        "Connection": "keep-alive"
    }
with requests.session() as session:
    asw = ("nama=" + nama + "&kategori=People&search=")

    r_post = session.post(url, data=asw, headers=headers)

src = r_post.content
soup = BeautifulSoup(src, "html.parser")

namamhs = []
nimmhs = []
for nama in soup.find_all("a", style="font-size: 1.1em;"):
    if "mahasiswa" in nama["href"]:
        namamhs.append(nama.text)
        nimmhs.append(nama["href"].replace("https://dinus.ac.id/mahasiswa/",""))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
resultdata = {
    "status" : 200,
    "message" : "",
    "result" : {
        "nim" : "",
        "nama" : "",
        "photo" : "",
        "status_mahasiswa" : "",
        "dosen_pembimbing " : {
            "npp" : "",
            "nama_asli" : "",
            "nama_title" : ""
            },
        "email" : [],
        "agama" : "",
        "jenis_kelamin" : "",
        "lahir" : {
            "tempat" : "",
            "tanggal" : "",
            "bulan" : "",
            "tahun" : ""
            },
        "ipk" : "",
        "angkatan" : "",
        "program_studi" : "",
        "fakultas" : "",
        "krs" : [
                {
                    "kode" : "",
                    "grup_kelas" : "",
                    "mata_kuliah" : "",
                    "sks" : "",
                    "status_kelas" : ""
                }
            ],
        "organisasi" : [
                {
                    "nama_organisasi" : "",
                    "status" : "",
                    "periode" : ""
                }
            ],
        "beasiswa" : []
        }
}

url1 = f"https://dinus.ac.id/mahasiswa/{nimmhs[0]}"
response = session.get(url1).content
soup1 = BeautifulSoup(response,"html.parser")
resultdata["result"]["photo"] = soup1.find("a","fotonews").img["src"]

data = []
table = soup1.find("table", "table")
rows = table.find_all("tr")

resultdata["status"] = 200
resultdata["message"] = "success"

resultdata["result"]["nama"] = rows[0].find_all("td")[-1].text
resultdata["result"]["nim"] = rows[1].find_all("td")[-1].text
resultdata["result"]["status_mahasiswa"] = rows[3].find_all("td")[-1].text
resultdata["result"]["dosen_pembimbing "]["nama_asli"] = rows[2].find_all("td")[-1].text
email = rows[5].find_all("td")[-1].text.replace("\n","").split()
resultdata["result"]["email"] = list(set([x.strip().replace("[a]","@") for x in email]))
resultdata["result"]["agama"] = rows[6].find_all("td")[-1].text


# print(namamhs,nimmhs,foto)
print(json.dumps(resultdata))