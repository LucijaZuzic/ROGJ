import os
import shutil

basedir = "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/veprad/podaci-BCN/"

txt_hrt = os.listdir(basedir + "tekst")
audio_hrt = os.listdir(basedir + "audio")

ok_entry = set()
not_ok_entry = set()
not_present_entry = set()
not_ok_present_entry = set()

for entry in txt_hrt:
    if entry[0] != "H":
        continue
    file_entry = open(basedir + "tekst/" + entry, "r")
    lines_entry = file_entry.readlines()[0][0]
    file_entry.close()

    if lines_entry[0] == "n":
        if audio_hrt.count(entry.replace("txt", "wav")) != 0:
            not_ok_entry.add(entry.replace("txt", "wav"))
        else:
            not_ok_present_entry.add(entry.replace("txt", "wav"))
    else:
        if audio_hrt.count(entry.replace("txt", "wav")) != 0:
            ok_entry.add(entry.replace("txt", "wav"))
        else:
            not_present_entry.add(entry.replace("txt", "wav"))

print(len(ok_entry), len(not_ok_entry), len(not_present_entry), len(not_ok_present_entry))

'''
if not os.path.isdir(basedir + "audio_bad"):
    os.makedirs(basedir + "audio_bad")

if not os.path.isdir(basedir + "tekst_bad"):
    os.makedirs(basedir + "tekst_bad")

for entry in not_ok_entry:
    shutil.copyfile(basedir + "audio/" + entry, basedir + "audio_bad/" + entry)
    file_entry = open(basedir + "tekst_bad/" + entry.replace("wav", "txt"), "w")
    file_entry.write("")
    file_entry.close()
'''

file_entry = open(basedir + "trajanja_hrt_all.txt", "r")
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

file_entry = open(basedir + "trajanja_hrt.txt", "r")
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

file_entry = open(basedir + "trajanja_hrt_novo.txt", "r")
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

if not os.path.isdir(basedir + "tekst_popravljeno"):
    os.makedirs(basedir + "tekst_popravljeno")

new_text = os.listdir(basedir + "tekst_novo")

wrong_wrong = set()

banned = set()

for entry in new_text: 

    if entry[11] != "3":
        continue

    file_entry = open(basedir + "tekst_novo/" + entry, "r")
    lines_entry = file_entry.readlines()

    whole_text = ""

    for line in lines_entry:
        whole_text += line

    whole_text = whole_text.replace("\n", " ").replace(".", " ").replace(",", " ").replace(":", " ").replace("?", " ").replace("\"", " ").lower()

    while whole_text.count("  ") > 0:
        whole_text = whole_text.replace("  ", " ")
    
    if len(whole_text) == 0:
        wrong_wrong.add(entry)
        continue

    while whole_text[0] == " ":
        whole_text = whole_text[1:]
     
    while whole_text[-1] == " ":
        whole_text = whole_text[:-1]

    whole_text = whole_text.replace("{", "š").replace("}", "đ").replace("~", "č").replace("`", "ž").replace("^", "ć").replace("ð", "đ")

    wr = False

    for some_char in whole_text:
        if (ord(some_char) < ord("a") or ord(some_char) > ord("z")) and some_char not in['š', 'ć', 'č', 'ž', 'đ', ' ']:
            banned.add(some_char)
            wr = True 

    if whole_text.count("w") > 0 or whole_text.count("q") > 0 or whole_text.count("x") > 0 or whole_text.count("y") > 0:
        print(entry) 
        #print(whole_text) 

    file_entry.close()
    
    file_entry = open(basedir + "tekst_popravljeno/" + entry, "w")
    file_entry.write(whole_text + "\n")
    file_entry.close() 

print(banned)

banned = set()

for entry in new_text: 

    if entry[11] != "4":
        continue

    file_entry = open(basedir + "tekst_novo/" + entry, "r")
    lines_entry = file_entry.readlines()

    whole_text = ""

    for line in lines_entry:
        whole_text += line

    whole_text = whole_text.replace("\n", " ").replace(".", " ").replace(",", " ").replace(":", " ").replace("?", " ").replace("\"", " ").replace("-", " ").replace("!", " ").replace("'", " ").lower()

    while whole_text.count("  ") > 0:
        whole_text = whole_text.replace("  ", " ")
    
    if len(whole_text) == 0:
        wrong_wrong.add(entry)
        continue

    while whole_text[0] == " ":
        whole_text = whole_text[1:]
     
    while whole_text[-1] == " ":
        whole_text = whole_text[:-1]

    wr = False

    for some_char in whole_text:
        if (ord(some_char) < ord("a") or ord(some_char) > ord("z")) and some_char not in['š', 'ć', 'č', 'ž', 'đ', ' ']:
            banned.add(some_char)
            wr = True

    if whole_text.count("w") > 0 or whole_text.count("q") > 0 or whole_text.count("x") > 0 or whole_text.count("y") > 0:
        print(entry) 
        #print(whole_text) 

    file_entry.close() 

    file_entry = open(basedir + "tekst_popravljeno/" + entry, "w")
    file_entry.write(whole_text + "\n")
    file_entry.close() 

print(banned)

for entry in new_text: 

    if entry[11] != "5":
        continue

    file_entry = open(basedir + "tekst_novo/" + entry, "r")
    lines_entry = file_entry.readlines()

    whole_text = ""

    for line in lines_entry:
        whole_text += line

    whole_text = whole_text.replace("\n", " ").replace(".", " ").replace(",", " ").replace(":", " ").replace("?", " ").replace("\"", " ").replace("-", " ").replace("!", " ").replace("'", " ").lower()
 
    while whole_text.count("  ") > 0:
        whole_text = whole_text.replace("  ", " ")
    
    if len(whole_text) == 0:
        wrong_wrong.add(entry)
        continue

    while whole_text[0] == " ":
        whole_text = whole_text[1:]
     
    while whole_text[-1] == " ":
        whole_text = whole_text[:-1]

    wr = False

    for some_char in whole_text:
        if (ord(some_char) < ord("a") or ord(some_char) > ord("z")) and some_char not in['š', 'ć', 'č', 'ž', 'đ', ' ']:
            banned.add(some_char)
            wr = True

    if whole_text.count("w") > 0 or whole_text.count("q") > 0 or whole_text.count("x") > 0 or whole_text.count("y") > 0:
        print(entry) 
        #print(whole_text) 

    file_entry.close() 

    file_entry = open(basedir + "tekst_popravljeno/" + entry, "w")
    file_entry.write(whole_text + "\n")
    file_entry.close() 

print(banned)

for entry in new_text: 

    if entry[11] != "6":
        continue

    file_entry = open(basedir + "tekst_novo/" + entry, "r")
    lines_entry = file_entry.readlines()

    whole_text = ""

    for line in lines_entry:
        whole_text += line

    whole_text = whole_text.replace("\n", " ").replace(".", " ").replace(",", " ").replace(":", " ").replace("?", " ").replace("\"", " ").replace("-", " ").replace("!", " ").replace("'", " ").lower()

    while whole_text.count("  ") > 0:
        whole_text = whole_text.replace("  ", " ")
    
    if len(whole_text) == 0:
        wrong_wrong.add(entry)
        continue

    while whole_text[0] == " ":
        whole_text = whole_text[1:]
     
    while whole_text[-1] == " ":
        whole_text = whole_text[:-1]

    wr = False

    for some_char in whole_text:
        if (ord(some_char) < ord("a") or ord(some_char) > ord("z")) and some_char not in['š', 'ć', 'č', 'ž', 'đ', ' ']:
            banned.add(some_char)
            wr = True 

    if whole_text.count("w") > 0 or whole_text.count("q") > 0 or whole_text.count("x") > 0 or whole_text.count("y") > 0:
        print(entry) 
        #print(whole_text) 

    file_entry.close() 

    file_entry = open(basedir + "tekst_popravljeno/" + entry, "w")
    file_entry.write(whole_text + "\n")
    file_entry.close() 

print(banned)

for entry in new_text: 

    if entry[11] != "7":
        continue

    file_entry = open(basedir + "tekst_novo/" + entry, "r")
    lines_entry = file_entry.readlines()

    whole_text = ""

    for line in lines_entry:
        whole_text += line

    whole_text = whole_text.replace("\n", " ").replace(".", " ").replace(",", " ").replace(":", " ").replace("?", " ").replace("\"", " ").replace("-", " ").replace("!", " ").replace("'", " ").replace("^", " ").lower()
 
    while whole_text.count("  ") > 0:
        whole_text = whole_text.replace("  ", " ")
    
    if len(whole_text) == 0:
        wrong_wrong.add(entry)
        continue

    while whole_text[0] == " ":
        whole_text = whole_text[1:]
     
    while whole_text[-1] == " ":
        whole_text = whole_text[:-1]

    wr = False

    for some_char in whole_text:
        if (ord(some_char) < ord("a") or ord(some_char) > ord("z")) and some_char not in['š', 'ć', 'č', 'ž', 'đ', ' ']:
            banned.add(some_char)
            wr = True 

    if whole_text.count("w") > 0 or whole_text.count("q") > 0 or whole_text.count("x") > 0 or whole_text.count("y") > 0:
        print(entry) 
        #print(whole_text) 

    file_entry.close() 

    file_entry = open(basedir + "tekst_popravljeno/" + entry, "w")
    file_entry.write(whole_text + "\n")
    file_entry.close() 

print(banned)

for entry in new_text: 

    if entry[11] != "0":
        continue

    file_entry = open(basedir + "tekst_novo/" + entry, "r")
    lines_entry = file_entry.readlines()

    whole_text = ""

    for line in lines_entry:
        whole_text += line

    whole_text = whole_text.replace("\n", " ").replace(".", " ").replace(",", " ").replace(":", " ").replace("?", " ").replace("\"", " ").replace("-", " ").replace("!", " ").replace("'", " ").replace("^", " ").lower()

    while whole_text.count("  ") > 0:
        whole_text = whole_text.replace("  ", " ")
    
    if len(whole_text) == 0:
        wrong_wrong.add(entry)
        continue

    while whole_text[0] == " ":
        whole_text = whole_text[1:]
     
    while whole_text[-1] == " ":
        whole_text = whole_text[:-1]
 
    # whole_text = whole_text.replace("æ", "c").replace("è", "č").replace("ð", "đ").replace("\x9a", "š").replace("\x9e", "ž").replace("\x8a", "š").replace("\x8e", "ž") 

    wr = False

    for some_char in whole_text:
        if (ord(some_char) < ord("a") or ord(some_char) > ord("z")) and some_char not in['š', 'ć', 'č', 'ž', 'đ', ' ']:
            banned.add(some_char)
            wr = True

    if whole_text.count("w") > 0 or whole_text.count("q") > 0 or whole_text.count("x") > 0 or whole_text.count("y") > 0:
        print(entry) 
        #print(whole_text) 
  
    file_entry.close() 

    file_entry = open(basedir + "tekst_popravljeno/" + entry, "w")
    file_entry.write(whole_text + "\n")
    file_entry.close() 

print(banned)

print(wrong_wrong)

for entry in new_text: 

    file_entry = open(basedir + "tekst_novo/" + entry, "r")
    lines_entry = file_entry.readlines()

    whole_text = ""

    for line in lines_entry:
        whole_text += line

    whole_text = whole_text.replace("\n", " ").replace(".", " ").replace(",", " ").replace(":", " ").replace("?", " ").replace("\"", " ").replace("-", " ").replace("!", " ").replace("'", " ").replace("^", " ").lower()

    while whole_text.count("  ") > 0:
        whole_text = whole_text.replace("  ", " ")
    
    if len(whole_text) == 0:
        wrong_wrong.add(entry)
        continue

    while whole_text[0] == " ":
        whole_text = whole_text[1:]
     
    while whole_text[-1] == " ":
        whole_text = whole_text[:-1]
 
    # whole_text = whole_text.replace("æ", "c").replace("è", "č").replace("ð", "đ").replace("\x9a", "š").replace("\x9e", "ž").replace("\x8a", "š").replace("\x8e", "ž") 

    if whole_text.count("evrop") > 0:
        print(entry)
        print(whole_text)
    