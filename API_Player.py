# TUGAS PASCA TM
# 1. get api sportsdb, daftar pemain suatu klub
# 2. input: klub apa? X
# 3. daftar pemain: nama, posisi, usia, negara
# 4. save to: X.xlsx, X.json, x.csv

#AMBIL DATA API
import requests
klub = input('Ketik klub: ')
url = f'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t={klub}'
data = requests.get(url)
players = data.json()['player']

#MEMBUAT FILE XLSX
import xlsxwriter
file = xlsxwriter.Workbook(f'{klub}.xlsx')
sheet = file.add_worksheet(f'player of {klub}')

#MEMBUAT HEADER
sheet.write(0, 0, 'Name') 
sheet.write(0, 1, 'Position') 
sheet.write(0, 2, 'Age') 
sheet.write(0, 3, 'Nationality')

#MEMBUAT LIST
list = []
myList = []
for player in players:
    list.append(player['strPlayer'])
    list.append(player['strPosition'])
    list.append(2019 - int(player['dateBorn'][:4]))
    list.append(player['strNationality'])
    myList.append(list)
    list = []
 
 #MENGISI SHEET DALAM XLSX
row = 1
for x,y,z,a in myList:
    sheet.write(row, 0, x)
    sheet.write(row, 1, y)
    sheet.write(row, 2, z)
    sheet.write(row, 3, a)
    row += 1

file.close()
# =========================================
# CONVERT TO CSV
judul = ['Name', 'Position', 'Age', 'Nationality']

import json
out = []
for i in myList:
    datax = dict(zip(judul, i))
    out.append(datax)

import csv
with open(f'{klub}.csv', 'w', newline='') as x:
    kolom = judul
    tulis = csv.DictWriter(x, fieldnames=kolom)
    tulis.writeheader()
    tulis.writerows(out)

# =========================================
# CONVERT TO JSON
import json

with open(f'{klub}.json', 'w') as y:
    json.dump(out, y)
