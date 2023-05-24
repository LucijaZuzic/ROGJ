import os

basedir = "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/"
vepardir = basedir + "veprad/podaci_radio/"

def compdirs(va, oa, vt, ot):

    vaf = os.listdir(va)
    oaf = os.listdir(oa)
    vtf = os.listdir(vt)
    otf = os.listdir(ot)

    ma = set()
    d1a = set()
    d2a = set()

    mt = set()
    d1t = set()
    d2t = set()

    for f in vaf:
        if f not in oaf:
            d1a.add(f)
        else:
            ma.add(f)

    for f in oaf:
        if f not in vaf:
            d2a.add(f) 

    for f in vtf:
        if f not in otf:
            d1t.add(f)
        else:
            mt.add(f)

    for f in oaf:
        if f not in vaf:
            d2t.add(f) 

    print(len(ma), len(d1a), len(d2a))
    print(len(mt), len(d1t), len(d2t))

for sample_num in range(1, 15):
    string_number = str(sample_num)
    if sample_num < 10:
        string_number = '0' + string_number
    vepar = vepardir + "audio/z" + string_number + "/"
    orig = basedir + "audio_z/z" + string_number + "/"
    vepartxt = vepardir + "text/z" + string_number + "/"
    origtxt = basedir + "text/z" + string_number + "/"
    compdirs(vepar, orig, vepartxt, origtxt)

for sample_num in range(1, 12):
    string_number = str(sample_num)
    if sample_num < 10:
        string_number = '0' + string_number
    vepar = vepardir + "audio/m" + string_number + "/"
    orig = basedir + "audio_m/m" + string_number + "/"
    vepartxt = vepardir + "text/m" + string_number + "/"
    origtxt = basedir + "text/m" + string_number + "/"
    compdirs(vepar, orig, vepartxt, origtxt)

vepardir = basedir + "veprad/podaci_sinteza/sm04/"
vepar = vepardir + "audio/wav/"
orig = basedir + "wav_sm04/"
vepartxt = vepardir + "text/"
origtxt = basedir + "txt_sm04/"
compdirs(vepar, orig, vepartxt, origtxt)

vepardir = basedir + "veprad/podaci_sinteza/"

file_entry = open(vepardir + "sz04/audio/trajanje_sz04.txt", "r")
lines_entry = file_entry.readlines()
file_entry.close()

suma = 0
maksi = 0 

for line in lines_entry:
    maksi = max(maksi,float(line.replace("\n", "")))
    suma += float(line.replace("\n", ""))
    maksi 

print(len(lines_entry), suma, suma / 60, suma / 3600, maksi, suma / len(lines_entry))
print(suma / 3600)

file_entry = open(vepardir + "sz08/audio/trajanje_sz08.txt", "r")
lines_entry = file_entry.readlines()
file_entry.close()

suma = 0
maksi = 0 

for line in lines_entry:
    maksi = max(maksi,float(line.replace("\n", "")))
    suma += float(line.replace("\n", ""))
    maksi 

print(len(lines_entry), suma, suma / 60, suma / 3600, maksi, suma / len(lines_entry))
print(suma / 3600)

vepardir = basedir + "veprad/podaci_radio/"

file_entry = open(vepardir + "audio/trajanje_prvi.txt", "r")
lines_entry = file_entry.readlines()
file_entry.close()

suma = 0
maksi = 0 

for line in lines_entry:
    maksi = max(maksi,float(line.replace("\n", "")))
    suma += float(line.replace("\n", ""))
    maksi 

print(len(lines_entry), suma, suma / 60, suma / 3600, maksi, suma / len(lines_entry))
print(suma / 3600)