import os
import difflib

basedir = "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/"

file_filler = open(basedir + "my_db.filler", "r")

lines_filler = file_filler.readlines()

for line_num in range(len(lines_filler)):
    lines_filler[line_num] = lines_filler[line_num].replace("\n", "").replace("NOISE", "").replace("SIL", "").replace(" ", "") 

file_filler.close()

files_train = open(basedir + "my_db3_train.fileids", "r")
train_files_list = files_train.readlines()
for i in range(len(train_files_list)):
    train_files_list[i] = train_files_list[i].replace("\n", "").split("/")[1]
files_train.close()

replace_transcript = {"{": "š",  
            "#": "dž", 
            "}": "đ", 
            "^": "ć",
            "`": "ž",
            "~": "č" }

def predictions_grade(output_name):
 
    ok_sentences = 0
    wrong_sentences = 0

    words_ok = 0

    words_replaced = 0
    words_ommited = 0
    words_added = 0

    signs_ok = 0

    signs_replaced = 0
    signs_ommited = 0
    signs_added = 0

    signs_inserted = 0
    signs_deleted = 0
    signs_substituted = 0
    signs_equal = 0
    signs_all = 0
    sim_rat = 0

    dirnames = os.listdir(basedir + output_name)
    for dirname in dirnames:
        if dirname == 'z04':
            continue
        filenames = os.listdir(basedir + output_name + "/" + dirname)
        for filename in filenames:

            if filename.replace(".txt", "") in train_files_list:
                continue

            file_to_open = open(basedir + output_name + "/" + dirname + "/" + filename, "r")
            lines_from_file = file_to_open.readlines()
            file_to_open.close() 

            line_original = ""
            
            for begining in range(len(lines_from_file)): 

                if begining + 1 < len(lines_from_file) and lines_from_file[begining + 1][0] == '-':
                    break

                one_line_original = lines_from_file[begining]
                for filler in lines_filler:
                    one_line_original = one_line_original.replace(filler, "")
                for replacement in replace_transcript:
                    one_line_original = one_line_original.replace(replacement, replace_transcript[replacement])
                one_line_original = one_line_original.replace("\t", "").replace("\n", "").replace(",", "").replace(".", "").lower() 
                while one_line_original.count("  ") != 0:
                    one_line_original = one_line_original.replace("  ", " ")
                while len(one_line_original) > 0 and one_line_original[0] == " ":
                    one_line_original = one_line_original[1:]  
                if line_original != "":
                    line_original += "\n"
                if len(one_line_original) == 0:
                    continue
                line_original += one_line_original

            line_new = ""

            for line_num in range(len(lines_from_file)):
                if line_num + 1 < len(lines_from_file) and lines_from_file[line_num + 1][0] == '-' and lines_from_file[line_num][0] != '|':
                    if line_new != "":
                        line_new += " "
                    line_new += lines_from_file[line_num].replace("\n", "")
            
            dict_diff = {'delete': 0, 'insert': 0, 'equal': 0, 'replace': 0}
            s = difflib.SequenceMatcher(None, line_original, line_new)
            for opcode in s.get_opcodes(): 
                if opcode[0] == 'delete' or opcode[0] == 'insert':              
                    dict_diff[opcode[0]] += abs((opcode[2] - opcode[1]) - (opcode[4] - opcode[3]))
                else:          
                    dict_diff[opcode[0]] += abs(opcode[2] - opcode[1])

            signs_inserted += dict_diff['insert']
            signs_deleted += dict_diff['delete']
            signs_substituted += dict_diff['replace']
            signs_equal += dict_diff['equal']
            signs_all += dict_diff['replace'] + dict_diff['insert'] + dict_diff['delete'] + dict_diff['equal']
            sim_rat += s.ratio()

            for sign_num in range(len(line_original)):
                sign_original = line_original[sign_num] 

                if sign_num >= len(line_new):
                    signs_ommited += 1 
                    continue

                sign_new = line_new[sign_num]

                if sign_original != sign_new:
                    signs_replaced += 1 
                    continue

                signs_ok += 1

            if len(line_new) > len(line_original):
                signs_added += len(line_new) - len(line_original)

            words_original = line_original.split(" ") 
            words_new = line_new.split(" ")
            
            sentence_ok = True

            for original_word_num in range(len(words_original)):
                word_original = words_original[original_word_num]

                if len(word_original) < 1:
                    continue

                if original_word_num >= len(words_new):
                    words_ommited += 1
                    sentence_ok = False
                    continue

                word_new = words_new[original_word_num]

                if word_original != word_new:
                    words_replaced += 1
                    sentence_ok = False
                    continue

                words_ok += 1

            if len(words_new) > len(words_original):
                words_added += len(words_new) - len(words_original)

            if sentence_ok:
                ok_sentences += 1
            else:
                wrong_sentences += 1

    print(output_name)

    print("Točne rečenice:", ok_sentences, "/", (ok_sentences + wrong_sentences), ok_sentences / (ok_sentences + wrong_sentences) * 100, "%",
          "Netočne rečenice:", wrong_sentences, "/", (ok_sentences + wrong_sentences), wrong_sentences / (ok_sentences + wrong_sentences)* 100, "%")

    print("Točne riječi:", words_ok, "/", (words_ok + words_ommited + words_replaced), words_ok / (words_ok + words_ommited + words_replaced)* 100, "%",
          "Netočne riječi:", (words_ommited + words_replaced), "/", (words_ok + words_ommited + words_replaced), (words_ommited + words_replaced) / (words_ok + words_ommited + words_replaced) * 100, "%")
    print("Ispuštene riječi:", words_ommited, "/", (words_ok + words_ommited + words_replaced), words_ommited / (words_ok + words_ommited + words_replaced) * 100, "%",
          "Zamijenjene riječi:", words_replaced, "/", (words_ok + words_ommited + words_replaced), words_replaced / (words_ok + words_ommited + words_replaced) * 100, "%")
    print("Dodane riječi:", words_added)
  
    print("Točni znakovi:", signs_ok, "/", (signs_ok + signs_ommited + signs_replaced), signs_ok / (signs_ok + signs_ommited + signs_replaced)* 100, "%",
          "Netočni znakovi:", (signs_ommited + signs_replaced), "/", (signs_ok + signs_ommited + signs_replaced), (signs_ommited + signs_replaced) / (signs_ok + signs_ommited + signs_replaced) * 100, "%")
    print("Ispušteni znakovi:", signs_ommited, "/", (signs_ok + signs_ommited + signs_replaced), signs_ommited / (signs_ok + signs_ommited + signs_replaced) * 100, "%",
          "Zamijenjeni znakovi:", signs_replaced, "/", (signs_ok + signs_ommited + signs_replaced), signs_replaced / (signs_ok + signs_ommited + signs_replaced) * 100, "%")
    print("Dodani znakovi:", signs_added)

    print("Insertions:", signs_inserted, "/", signs_all, signs_inserted / signs_all * 100, "%",  
          "Deletions:", signs_deleted, "/", signs_all, signs_deleted / signs_all * 100, "%")
    
    print("Substitutions:", signs_substituted, "/", signs_all, signs_substituted / signs_all * 100, "%",
          "Equal:", signs_equal, "/", signs_all, signs_equal / signs_all * 100, "%")
    
    print("Ratio:", sim_rat / (ok_sentences + wrong_sentences) * 100, "%")

#predictions_grade("outputs/")
#predictions_grade("outputs_pruned/")

predictions_grade("outputs_only_weather/")
predictions_grade("outputs_only_weather_pruned/")

predictions_grade("outputs3_only_weather/")
predictions_grade("outputs3_only_weather_pruned/")

#predictions_grade("outputs_both/")
#predictions_grade("outputs_both_pruned/")

predictions_grade("outputs_only_weather_train/")
predictions_grade("outputs_only_weather_train_pruned/")

predictions_grade("outputs3_only_weather_train/")
predictions_grade("outputs3_only_weather_train_pruned/")

#predictions_grade("outputs_both_train/")
#predictions_grade("outputs_both_train_pruned/")