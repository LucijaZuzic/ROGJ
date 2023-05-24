import os as os  

all_transcriptions = []
test_transcriptions = []
train_transcriptions = []
phone_unknown = set()

replace_transcript = {"{": "š",  
               "#": "dž", 
               "}": "đ", 
               "^": "ć",
               "`": "ž",
               "~": "č" }

basedir = "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/"

all_fileids_test_file = open(basedir + "my_db10_test.fileids", "r") 
testing_lines = all_fileids_test_file.readlines()
for i in range(len(testing_lines)):
    testing_lines[i] = testing_lines[i].replace("\n", "").split("/")[1]
    print(testing_lines[i])
all_fileids_test_file.close()

def find_files(my_home, txt_files): 

    txt_filenames = os.listdir(my_home + txt_files)
    txt_filenames.sort()
 
    print("txt:", len(txt_filenames)) 

    for name in txt_filenames:  

        file_text = open(my_home + txt_files + "/" + name, "r")

        read_text = file_text.readlines()

        new_text = ""

        for number_line in range(len(read_text)): 
            line_new = read_text[number_line]

            for replacement in replace_transcript:
                line_new = line_new.replace(replacement, replace_transcript[replacement])

            new_text += line_new

        new_text = new_text.replace("\t", " ").replace("\n", " ").replace(",", " ").replace(".", " ").lower() 

        while new_text.count("  ") != 0:
            new_text = new_text.replace("  ", " ")  

        all_new_words = new_text.split(" ")

        for one_word in all_new_words:

            if len(one_word) == 0:
                continue 

            if one_word[0] == '<': 
                phone_unknown.add(one_word) 
        
        all_transcriptions.append(new_text) 

        if name.replace(".txt", "") in testing_lines:
            test_transcriptions.append(new_text)
        else:
            train_transcriptions.append(new_text)

        file_text.close()    

file_words_from_txt_text = ""

for sample_num in range(1, 15):

    if sample_num == 4:
        continue

    print("Sample female", sample_num)

    string_number = str(sample_num)
    if sample_num < 10:
        string_number = '0' + string_number

    find_files(basedir, "text/z" + string_number,) 

for sample_num in range(1, 12):
    print("Sample male", sample_num)

    string_number = str(sample_num)
    if sample_num < 10:
        string_number = '0' + string_number

    find_files(basedir, "text/m" + string_number) 

prognoza_dir = "0069082557 1035 Battelli Piero/0069082557 1035 Battelli Piero/Train/"

for sample_num in range(1, 14):
    print("Sample prognoza", sample_num)

    find_files(basedir, prognoza_dir + "txt/VremenskaPrognoza" + str(sample_num)) 
 
cmu_dir = "16kHz_16bit/"

dir_cmu = os.listdir(basedir + cmu_dir)
new_cmu_dir = []

for new_dir_cmu in dir_cmu:
    if os.path.isdir(basedir + cmu_dir + new_dir_cmu) and new_dir_cmu != "Prompts" and new_dir_cmu != "db_files":
        new_cmu_dir.append(new_dir_cmu) 

for new_dir_cmu in new_cmu_dir: 
    print("Sample prognoza", new_dir_cmu)

    find_files(basedir, cmu_dir + "Prompts/txt/" + new_dir_cmu) 

find_files(basedir, "txt_sm04")
   
file_words_from_txt = open(basedir + "/words_from_txt12.txt", "w")

file_words_from_txt_text = ""

for content in all_transcriptions:
    line_new = content

    for unknown_phone in phone_unknown:
        line_new = line_new.replace(unknown_phone, "")

    file_words_from_txt_text += line_new + "\n"

file_words_from_txt.write(file_words_from_txt_text)
file_words_from_txt.close()

all_lines_file = open(basedir + "hrwikidirectory/my_db_all_lines.txt", "r") 
all_lines_file_line = all_lines_file.readlines()
all_lines_file.close()

file_words_from_txt = open(basedir + "/words_from_txt_word12.txt", "w")

file_words_from_txt_text = ""

for content in all_transcriptions:
    line_new = content

    for unknown_phone in phone_unknown:
        line_new = line_new.replace(unknown_phone, "")

    file_words_from_txt_text += line_new + "\n"

for line_new in all_lines_file_line:

    file_words_from_txt_text += line_new 

file_words_from_txt.write(file_words_from_txt_text)
file_words_from_txt.close()

file_words_from_txt = open(basedir + "/words_from_txt_word_test12.txt", "w")

file_words_from_txt_text = ""

for content in test_transcriptions:
    line_new = content

    for unknown_phone in phone_unknown:
        line_new = line_new.replace(unknown_phone, "")

    file_words_from_txt_text += line_new + "\n"

for line_new in all_lines_file_line:

    file_words_from_txt_text += line_new 

file_words_from_txt.write(file_words_from_txt_text)
file_words_from_txt.close()

file_words_from_txt = open(basedir + "/words_from_txt_word_train12.txt", "w")

file_words_from_txt_text = ""

for content in train_transcriptions:
    line_new = content

    for unknown_phone in phone_unknown:
        line_new = line_new.replace(unknown_phone, "")

    file_words_from_txt_text += line_new + "\n"

for line_new in all_lines_file_line:

    file_words_from_txt_text += line_new 

file_words_from_txt.write(file_words_from_txt_text)
file_words_from_txt.close()

file_words_from_txt = open(basedir + "/words_from_txt_test12.txt", "w")

file_words_from_txt_text = ""

for content in test_transcriptions:
    line_new = content

    for unknown_phone in phone_unknown:
        line_new = line_new.replace(unknown_phone, "")

    file_words_from_txt_text += line_new + "\n"

file_words_from_txt.write(file_words_from_txt_text)
file_words_from_txt.close()

file_words_from_txt = open(basedir + "/words_from_txt_train12.txt", "w")

file_words_from_txt_text = ""

for content in train_transcriptions:
    line_new = content

    for unknown_phone in phone_unknown:
        line_new = line_new.replace(unknown_phone, "")

    file_words_from_txt_text += line_new + "\n"

file_words_from_txt.write(file_words_from_txt_text)
file_words_from_txt.close()