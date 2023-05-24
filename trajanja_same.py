import os as os

from sklearn.model_selection import train_test_split

all_fileids =  []
all_transcriptions = []
all_fileids_new =  []
all_transcriptions_new = []

phone_unknown = set()
all_words = set() 
phone_known = ["a", "b", "c", "č", "ć", "d", "dž", "đ", "e", "f", "g", "h", "i", "j", "k", "l", "lj", "m", "n", "nj", "o", "p", "r", "s", "š", "t", "u", "v", "z", "ž"]

#banned = ["sm04310105101", "sm04300104338", "z08040502305", "z01281202403", "z03030402401", "m10220602201", "z03060502203", "sm04070105123",
       #   "sm04070105216", "sm04070105138", "sm04300104143", "m11190602401", "m01150402201", "sm04170105137", "sm04060105402", "sm04050204452"]

replace_transcript = {"{": "š",  
               "#": "dž", 
               "}": "đ", 
               "^": "ć",
               "`": "ž",
               "~": "č" }

def find_files(my_home, duration_file, wav_files, txt_files, dbname):
        
    lines_all = []

    if duration_file != "":

        trajanja = open(my_home + duration_file, "r")
        lines_all = trajanja.readlines() 
        for i in range(len(lines_all)):
            lines_all[i] = float(lines_all[i].replace("\n", ""))
        trajanja.close()

    wav_filenames = os.listdir(my_home + wav_files)
    wav_filenames.sort()
    txt_filenames = os.listdir(my_home + txt_files)
    txt_filenames.sort()

    print("wav:", len(wav_filenames))
    print("txt:", len(txt_filenames))

    messed_up = set()
    ok_names = []
    ok_text = []

    for i in range(len(wav_filenames)):
        wav_filenames[i] = wav_filenames[i].replace(".wav", "") 

    for i in range(len(txt_filenames)):
        txt_filenames[i] = txt_filenames[i].replace(".txt", "")  

    for name in txt_filenames: 

        #if name in banned:
           # continue
        
        if name not in wav_filenames:
            print("txt", name, "not in wav")
            messed_up.add(name)
        else:
            ok_names.append(dbname + "/" + name)

            file_text = open(my_home + txt_files + "/" + name + ".txt", "r")
            read_text = file_text.readlines()

            new_text = ""

            for number_line in range(len(read_text)): 
                line_new = read_text[number_line]

                for replacement in replace_transcript:
                    line_new = line_new.replace(replacement, replace_transcript[replacement])

                new_text += line_new

            new_text = new_text.replace("\n", " ").replace("\t", " ").replace(",", " ").replace(".", " ")
            new_text = new_text.lower()

            while new_text.count("  ") != 0:
                new_text = new_text.replace("  ", " ")

            all_new_words = new_text.split(" ")

            for one_word in all_new_words:

                if len(one_word) == 0:
                    continue 

                if one_word[0] == '<': 
                    phone_unknown.add(one_word)
                else:
                    all_words.add(one_word)
            
            ok_text.append("<s> " + new_text + " </s> (" + name + ")")

            file_text.close()

    print("Pogreška:", len(messed_up), messed_up)
    print("Točni:", len(ok_names)) 

    file_names_content = "" 

    for content in ok_names:

        file_names_content += content + "\n"

            
        if my_home.count("Battelli") > 0:
            all_fileids_new.append(content)
        else:
            all_fileids.append(content)

    if not os.path.isdir(my_home + "/db_files/"):  
        os.makedirs(my_home + "/db_files/")

    file_names = open(my_home + "/db_files/my_db3_" + dbname + ".fieldids", "w")
    file_names.write(file_names_content)
    file_names.close()

    file_text_content = "" 

    for new_content in ok_text: 

        file_text_content += new_content + "\n" 

        if my_home.count("Battelli") > 0:
            all_transcriptions_new.append(new_content)
        else:
            all_transcriptions.append(new_content)

    file_text = open(my_home + "/db_files/my_db3_" + dbname + ".transcription", "w") 
    file_text.write(file_text_content)
    file_text.close()

    return lines_all, messed_up

basedir = "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/"

lines_female = []
messed_up_female = set()

for sample_num in range(1, 15):

    if sample_num == 4:
        continue

    print("Sample female", sample_num)

    string_number = str(sample_num)
    if sample_num < 10:
        string_number = '0' + string_number

    lines_all, messed_up = find_files(basedir, "audio_z/trajanja_z" + string_number +".txt", "audio_z/z" + string_number, "text/z" + string_number, "z" + string_number)
    
    for line in lines_all:
        lines_female.append(line)

    for line in messed_up:
        messed_up_female.add(line)

    print("Broj zapisa ženskog uzorka:", len(lines_all), "Sekunde:", sum(lines_all), "Minute:", sum(lines_all) / 60, "Sati:", sum(lines_all) / 3600, "Maksimum:", max(lines_all))

lines_male = []
messed_up_male = set()

for sample_num in range(1, 12):
    print("Sample male", sample_num)

    string_number = str(sample_num)
    if sample_num < 10:
        string_number = '0' + string_number

    lines_all, messed_up = find_files(basedir, "audio_m/trajanja_m" + string_number +".txt", "audio_m/m" + string_number, "text/m" + string_number, "m" + string_number)
    
    for line in lines_all:
        lines_male.append(line)

    for line in messed_up:
        messed_up_male.add(line)

    print("Broj zapisa muškog uzorka:", len(lines_all), "Sekunde:", sum(lines_all), "Minute:", sum(lines_all) / 60, "Sati:", sum(lines_all) / 3600, "Maksimum:", max(lines_all))

lines_prognoza = [] 
messed_up_prognoza = set()
prognoza_dir = "0069082557 1035 Battelli Piero/0069082557 1035 Battelli Piero/Train/"

for sample_num in range(1, 14):

    print("Sample prognoza", sample_num)  

    lines_all, messed_up = find_files(basedir + prognoza_dir, "wav_sorted/trajanja_prognoza" + str(sample_num) + ".txt", "wav_sorted/VremenskaPrognoza" + str(sample_num), "txt/VremenskaPrognoza" + str(sample_num), "VremenskaPrognoza"  + str(sample_num))
    
    for line in lines_all:
        lines_prognoza.append(line)         

    for line in messed_up:
        messed_up_prognoza.add(line)

    print("Broj zapisa uzorka prognoze:", len(lines_all), "Sekunde:", sum(lines_all), "Minute:", sum(lines_all) / 60, "Sati:", sum(lines_all) / 3600, "Maksimum:", max(lines_all))

print("Prvi uzorak")
lines_all, messed_up = find_files(basedir, "trajanja_sm04.txt", "wav_sm04", "txt_sm04", "sm04")
print("Broj zapisa prvog uzorka:", len(lines_all), "Sekunde:", sum(lines_all), "Minute:", sum(lines_all) / 60, "Sati:", sum(lines_all) / 3600, "Maksimum:", max(lines_all))

print("Broj ženskih zapisa:", len(lines_female), "Sekunde:", sum(lines_female), "Minute:", sum(lines_female) / 60, "Sati:", sum(lines_female) / 3600, "Maksimum:", max(lines_female), "Pogreška:", len(messed_up_female), messed_up_female)
print("Broj muških zapisa:", len(lines_male), "Sekunde:", sum(lines_male), "Minute:", sum(lines_male) / 60, "Sati:", sum(lines_male) / 3600, "Maksimum:", max(lines_male), "Pogreška:", len(messed_up_male), messed_up_male)
print("Broj zapisa uzoraka prognoze:", len(lines_prognoza), "Sekunde:", sum(lines_prognoza), "Minute:", sum(lines_prognoza) / 60, "Sati:", sum(lines_prognoza) / 3600, "Maksimum:", max(lines_prognoza), "Pogreška:", len(messed_up_prognoza), messed_up_prognoza)

phone_unknown_file = open(basedir + "/my_db3.filler", "w") 

phone_unknown_content = ""

phone_unknown_list = []

for content in phone_unknown: 
    phone_unknown_list.append(content)

phone_unknown_list.sort()

for content in phone_unknown_list:  

    if content != "<sil>": 
        phone_unknown_content += content + " " + "NOISE" + "\n" 
    else:
        phone_unknown_content += content + " " + "SIL" + "\n" 
 
phone_unknown_file.write(phone_unknown_content + "<s> SIL\n</s> SIL")
phone_unknown_file.close()
 
dict_file = open(basedir + "/my_db3.dic", "w") 

dict_content = ""

dict_list = []

for content in all_words: 
    dict_list.append(content)

dict_list.sort()

for content in dict_list:  

    new_content = content
    letter_num = 0

    while letter_num != len(content):

        letter = content[letter_num]
        
        if letter_num != len(content) - 1:

            new_letter = content[letter_num + 1]

            if letter == 'd' and new_letter == 'ž':
                new_content += ' dž'
                letter_num += 2
                continue

            if letter == 'n' and new_letter == 'j':
                new_content += ' nj'
                letter_num += 2
                continue

            if letter == 'l' and new_letter == 'j':
                new_content += ' lj'
                letter_num += 2
                continue
        
        new_content += ' ' + letter

        letter_num += 1

    dict_content += new_content + "\n"
         
dict_file.write(dict_content)
dict_file.close() 

text_phones = ""

for phone in phone_known:
    text_phones += phone + "\n"  

phone_known_file = open(basedir + "/my_db3.phone", "w") 
phone_known_file.write((text_phones + "SIL\n" + "NOISE"))
phone_known_file.close()
 
all_transcriptions_file = open(basedir + "/my_db3.transcription", "w") 

text_transcriptions = ""

for transcription in all_transcriptions:
    text_transcriptions += transcription + "\n"

all_transcriptions_file.write(text_transcriptions)
all_transcriptions_file.close()
 
all_fileids_file = open(basedir + "/my_db3.fileids", "w") 

text_fileids = ""

for fileid in all_fileids:
    text_fileids += fileid + "\n"

all_fileids_file.write(text_fileids)
all_fileids_file.close()

all_fileids_train, all_fileids_test, all_transcriptions_train, all_transcriptions_test = train_test_split(all_fileids, all_transcriptions, test_size=0.1, random_state=42)
all_fileids_new_train, all_fileids_new_test, all_transcriptions_new_train, all_transcriptions_new_test = train_test_split(all_fileids_new, all_transcriptions_new, test_size=0.1, random_state=42)

all_transcriptions_test_file = open(basedir + "/my_db3_test.transcription", "w") 

text_transcriptions_test = ""

for transcription_test in all_transcriptions_test:
    text_transcriptions_test += transcription_test + "\n"

for transcription_test in all_transcriptions_new_test:
    text_transcriptions_test += transcription_test + "\n"

all_transcriptions_test_file.write(text_transcriptions_test)
all_transcriptions_test_file.close()
 
all_fileids_test_file = open(basedir + "/my_db3_test.fileids", "w") 

text_fileids_test = ""

for fileid_test in all_fileids_test:
    text_fileids_test += fileid_test + "\n"

for fileid_test in all_fileids_new_test:
    text_fileids_test += fileid_test + "\n"

all_fileids_test_file.write(text_fileids_test)
all_fileids_test_file.close()

all_transcriptions_train_file = open(basedir + "/my_db3_train.transcription", "w") 

text_transcriptions_train = ""

for transcription_train in all_transcriptions_train:
    text_transcriptions_train += transcription_train + "\n"

for transcription_train in all_transcriptions_new_train:
    text_transcriptions_train += transcription_train + "\n"

all_transcriptions_train_file.write(text_transcriptions_train)
all_transcriptions_train_file.close()
 
all_fileids_train_file = open(basedir + "/my_db3_train.fileids", "w") 

text_fileids_train = ""

for fileid_train in all_fileids_train:
    text_fileids_train += fileid_train + "\n"

for fileid_train in all_fileids_new_train:
    text_fileids_train += fileid_train + "\n"

all_fileids_train_file.write(text_fileids_train)
all_fileids_train_file.close()