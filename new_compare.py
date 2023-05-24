import os
import difflib
import subprocess

basedir = "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/"

def weird_divide(x, y):
    if y == 0:
        return 0
    return x / y

file_phones = open(basedir + "my_db14.phone", "r")
lines_phone = file_phones.readlines()
file_phones.close()

all_phones = [' ']
for line_phone in lines_phone:
    if line_phone[0].upper() == line_phone[0]:
        continue
    all_phones.append(line_phone.replace("\n", "")) 
 
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

    signs_ok_dict = {sign_phone: 0 for sign_phone in all_phones}

    signs_replaced_dict = {sign_phone: 0 for sign_phone in all_phones}
    signs_ommited_dict = {sign_phone: 0 for sign_phone in all_phones}
    signs_added_dict = {sign_phone: 0 for sign_phone in all_phones}

    signs_ok2 = 0

    signs_replaced2 = 0
    signs_ommited2 = 0
    signs_added2 = 0

    signs_ok2_dict = {sign_phone: 0 for sign_phone in all_phones}

    signs_replaced2_dict = {sign_phone: 0 for sign_phone in all_phones}
    signs_ommited2_dict = {sign_phone: 0 for sign_phone in all_phones}
    signs_added2_dict = {sign_phone: 0 for sign_phone in all_phones}

    sim_rat = 0
 
    signs_inserted = 0
    signs_deleted = 0
    signs_substituted = 0
    signs_equal = 0
    signs_all = 0

    signs_inserted2 = 0
    signs_deleted2 = 0
    signs_substituted2 = 0
    signs_equal2 = 0
    signs_all2 = 0

    signs_inserted_dict = {sign_phone: 0 for sign_phone in all_phones}
    signs_deleted_dict = {sign_phone: 0 for sign_phone in all_phones}
    signs_substituted_dict = {sign_phone: 0 for sign_phone in all_phones}
    signs_equal_dict = {sign_phone: 0 for sign_phone in all_phones}

    signs_inserted2_dict = {sign_phone: 0 for sign_phone in all_phones}
    signs_deleted2_dict = {sign_phone: 0 for sign_phone in all_phones}
    signs_substituted2_dict = {sign_phone: 0 for sign_phone in all_phones}
    signs_equal2_dict = {sign_phone: 0 for sign_phone in all_phones}
     
    dirnames = os.listdir(basedir + output_name)
    for dirname in dirnames:
        if dirname in excl_dirs:
            continue
        filenames = os.listdir(basedir + output_name + "/" + dirname)
        for filename in filenames:

            if filename.replace(".txt", "") in train_files_list:
                continue

            file_to_open = open(basedir + output_name + "/" + dirname + "/" + filename, "r")
            lines_from_file = file_to_open.readlines()
            file_to_open.close() 

            if filename.count("compare") > 0:
                continue

            if filename.count("new") > 0:
                continue

            if filename.count("original") > 0:
                continue

            line_original = lines_from_file[0].replace("\n", "")

            if len(lines_from_file) < 2:
                line_new = ""
            else:
                line_new = lines_from_file[1].replace("\n", "")

            dict_diff = {'delete': 0, 'insert': 0, 'equal': 0, 'replace': 0}
            s = difflib.SequenceMatcher(None, line_original, line_new)   
            
            a1 = ""
            b1 = "" 
            
            for opcode in s.get_opcodes():   
                dict_diff[opcode[0]] += max(abs(opcode[2] - opcode[1]), abs(opcode[4] - opcode[3])) 
 
                seqa = line_original[opcode[1]:opcode[2]]
                seqb = line_new[opcode[3]:opcode[4]]

                while len(seqa) < len(seqb):
                    seqa += '*'

                while len(seqb) < len(seqa):
                    seqb += '*'
                 
                a1 += seqa
                b1 += seqb
 
                if opcode[0] == 'insert': 
                    for i in range(len(seqb)): 
                        sign_new = seqb[i]
                        signs_inserted_dict[sign_new] += 1
                        signs_inserted2 += 1 
                        signs_inserted2_dict[sign_new] += 1
                if opcode[0] == 'delete': 
                    for i in range(len(seqa)): 
                        sign_new = seqa[i]
                        signs_deleted_dict[sign_new] += 1 
                        signs_deleted2 += 1 
                        signs_deleted2_dict[sign_new] += 1   
                if opcode[0] == 'replace': 
                    for i in range(len(seqa)): 
                        sign_original = seqa[i] 
                        sign_new = seqb[i] 
                        signs_substituted_dict[sign_new] += 1  
                        if sign_original != '*' and sign_new != '*':
                            signs_substituted2 += 1
                            signs_substituted2_dict[sign_original] += 1  
                        if sign_original != '*' and sign_new == '*':
                            signs_deleted2 += 1
                            signs_deleted2_dict[sign_original] += 1  
                        if sign_original == '*' and sign_new != '*':
                            signs_inserted2 += 1
                            signs_inserted2_dict[sign_new] += 1  
                if opcode[0] == 'equal': 
                    for i in range(len(seqa)): 
                        sign_new = seqa[i]
                        signs_equal_dict[sign_new] += 1  
                        signs_equal2 += 1 
                        signs_equal2_dict[sign_new] += 1
                 
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
                    signs_ommited_dict[sign_original] += 1
                    continue

                sign_new = line_new[sign_num]

                if sign_original != sign_new:
                    signs_replaced += 1 
                    signs_replaced_dict[sign_original] += 1
                    continue

                signs_ok += 1
                signs_ok_dict[sign_original] += 1

            for sign_num in range(len(line_original), len(line_new)):
                    sign_new = line_new[sign_num]

                    signs_added += 1
                    signs_added_dict[sign_new] += 1
            
            while len(a1) > 0 and a1[-1] == '*':
                a1 = a1[:-1]

            while len(b1) > 0 and b1[-1] == '*':
                b1 = b1[:-1]

            for sign_num in range(len(a1)):
                sign_original = a1[sign_num] 

                if sign_num >= len(b1):
                    signs_ommited2 += 1 
                    signs_ommited2_dict[sign_original] += 1
                    continue

                sign_new = b1[sign_num]

                if sign_original != sign_new:
                    if sign_original != '*' and sign_new != '*':
                        signs_replaced2 += 1 
                        signs_replaced2_dict[sign_original] += 1
                    if sign_original == '*' and sign_new != '*':
                        signs_added2 += 1 
                        signs_added2_dict[sign_new] += 1
                    if sign_original != '*' and sign_new == '*':
                        signs_ommited2 += 1 
                        signs_ommited2_dict[sign_original] += 1
                    continue

                signs_ok2 += 1
                signs_ok2_dict[sign_original] += 1 

            for sign_num in range(len(a1), len(b1)):
                sign_new = b1[sign_num]

                signs_added2 += 1
                signs_added2_dict[sign_new] += 1
 
            print(basedir + output_name + "/" + dirname + "/" + filename)
            print(line_original)
            print(a1)
            print(line_new)
            print(b1)
            for op in s.get_opcodes():
                print(op[0], max(op[2] - op[1], op[4] - op[3]))   
            print(signs_ok, signs_replaced, signs_ommited, signs_added)
            print(signs_ok2, signs_replaced2, signs_ommited2, signs_added2)
            print(signs_equal, signs_substituted, signs_deleted, signs_inserted)
            print(signs_equal2, signs_substituted2, signs_deleted2, signs_inserted2)

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

            break

    print(output_name)

    print("Točne rečenice:", ok_sentences, "/", (ok_sentences + wrong_sentences), weird_divide(ok_sentences, ok_sentences + wrong_sentences) * 100, "%",
          "Netočne rečenice:", wrong_sentences, "/", (ok_sentences + wrong_sentences), weird_divide(wrong_sentences, ok_sentences + wrong_sentences)* 100, "%")

    print("Točne riječi:", words_ok, "/", (words_ok + words_ommited + words_replaced + words_added), weird_divide(words_ok, words_ok + words_ommited + words_replaced + words_added) * 100, "%",
          "Netočne riječi:", (words_ommited + words_replaced + words_added), "/", (words_ok + words_ommited + words_replaced + words_added), weird_divide(words_ommited + words_replaced + words_added, words_ok + words_ommited + words_replaced + words_added) * 100, "%")
    print("Ispuštene riječi:", words_ommited, "/", (words_ok + words_ommited + words_replaced + words_added), weird_divide(words_ommited, words_ok + words_ommited + words_replaced + words_added) * 100, "%",
          "Zamijenjene riječi:", words_replaced, "/", (words_ok + words_ommited + words_replaced + words_added), weird_divide(words_replaced, words_ok + words_ommited + words_replaced + words_added) * 100, "%")
    print("Dodane riječi:", words_added, "/", (words_ok + words_ommited + words_replaced + words_added), weird_divide(words_added, words_ok + words_ommited + words_replaced + words_added) * 100, "%")

  
    print("Točni znakovi:", signs_ok, "/", (signs_ok + signs_ommited + signs_replaced + signs_added), weird_divide(signs_ok, signs_ok + signs_ommited + signs_replaced + signs_added)* 100, "%",
          "Netočni znakovi:", (signs_ommited + signs_replaced + signs_added), "/", (signs_ok + signs_ommited + signs_replaced + signs_added), weird_divide(signs_ommited + signs_replaced + signs_added, signs_ok + signs_ommited + signs_replaced + signs_added) * 100, "%")
    print("Ispušteni znakovi:", signs_ommited, "/", (signs_ok + signs_ommited + signs_replaced + signs_added), weird_divide(signs_ommited, signs_ok + signs_ommited + signs_replaced + signs_added) * 100, "%",
          "Zamijenjeni znakovi:", signs_replaced, "/", (signs_ok + signs_ommited + signs_replaced + signs_added), weird_divide(signs_replaced, signs_ok + signs_ommited + signs_replaced + signs_added) * 100, "%")
    print("Dodani znakovi:", signs_added, "/", (signs_ok + signs_ommited + signs_replaced + signs_added), weird_divide(signs_added, signs_ok + signs_ommited + signs_replaced + signs_added) * 100, "%")
    
    print("Insertions:", signs_inserted, "/", signs_all, weird_divide(signs_inserted, signs_all) * 100, "%",  
          "Deletions:", signs_deleted, "/", signs_all, weird_divide(signs_deleted, signs_all) * 100, "%")
    
    print("Substitutions:", signs_substituted, "/", signs_all, weird_divide(signs_substituted, signs_all) * 100, "%",
          "Equal:", signs_equal, "/", signs_all, weird_divide(signs_equal, signs_all) * 100, "%")

    print("Incorrect ALIGN:", signs_inserted + signs_deleted + signs_substituted, "/", signs_all, weird_divide(signs_inserted + signs_deleted + signs_substituted, signs_all) * 100, "%")
     
    print("Ratio:", weird_divide(sim_rat, ok_sentences + wrong_sentences) * 100, "%")

    print("Točni znakovi ALIGN:", signs_ok2, "/", (signs_ok2 + signs_ommited2 + signs_replaced2 + signs_added2), weird_divide(signs_ok2, signs_ok2 + signs_ommited2 + signs_replaced2  + signs_added2) * 100, "%",
          "Netočni znakovi ALIGN:", (signs_ommited2 + signs_replaced2 + signs_added2), "/", (signs_ok2 + signs_ommited2 + signs_replaced2 + signs_added2), weird_divide(signs_ommited2 + signs_replaced2 + signs_added2, signs_ok2 + signs_ommited2 + signs_replaced2 + signs_added2) * 100, "%")
    print("Ispušteni znakovi ALIGN:", signs_ommited2, "/", (signs_ok2 + signs_ommited2 + signs_replaced2 + signs_added2), weird_divide(signs_ommited2 , signs_ok2 + signs_ommited2 + signs_replaced2) * 100, "%",
          "Zamijenjeni znakovi ALIGN:", signs_replaced2, "/", (signs_ok2 + signs_ommited2 + signs_replaced2 + signs_added2), weird_divide(signs_replaced2, signs_ok2 + signs_ommited2 + signs_replaced2 + signs_added2) * 100, "%")
    print("Dodani znakovi ALIGN:", signs_added2, "/", (signs_ok2 + signs_ommited2 + signs_replaced2 + signs_added2), weird_divide(signs_added2, signs_ok2 + signs_ommited2 + signs_replaced2 + signs_added2) * 100, "%")
    
    print("Točne rečenice:", ok_sentences, "/", (ok_sentences + wrong_sentences), weird_divide(ok_sentences, ok_sentences + wrong_sentences) * 100, "%",
          "Netočne rečenice:", wrong_sentences, "/", (ok_sentences + wrong_sentences), weird_divide(wrong_sentences, ok_sentences + wrong_sentences)* 100, "%")

    dict_vals[output_name] = {
        "Točne rečenice": ok_sentences,
        "Točne rečenice postotak": ok_sentences / (ok_sentences + wrong_sentences) * 100,
        "Netočne rečenice": wrong_sentences,
        "Netočne rečenice postotak": wrong_sentences / (ok_sentences + wrong_sentences) * 100,
        "Točne riječi": words_ok,
        "Točne riječi postotak": words_ok / (words_ok + words_ommited + words_replaced + words_added) * 100,
        "Netočne riječi": words_ommited + words_replaced + words_added,
        "Netočne riječi postotak": (words_ommited + words_replaced + words_added) / (words_ok + words_ommited + words_replaced + words_added) * 100,
        "Ispuštene riječi": words_ommited,
        "Ispuštene riječi postotak": words_ommited / (words_ok + words_ommited + words_replaced + words_added) * 100,
        "Zamijenjene riječi": words_replaced, 
        "Zamijenjene riječi postotak": words_replaced / (words_ok + words_ommited + words_replaced + words_added) * 100,
        "Dodane riječi": words_added,
        "Dodane riječi postotak": words_added / (words_ok + words_ommited + words_replaced + words_added) * 100,
        "Točni znakovi": signs_ok, 
        "Točni znakovi postotak": signs_ok / (signs_ok + signs_ommited + signs_replaced + signs_added) * 100,
        "Netočni znakovi": signs_ommited + signs_replaced + signs_added,
        "Netočni znakovi postotak": (signs_ommited + signs_replaced + signs_added) / (signs_ok + signs_ommited + signs_replaced + signs_added) * 100,
        "Ispušteni znakovi": signs_ommited, 
        "Ispušteni znakovi postotak": signs_ommited / (signs_ok + signs_ommited + signs_replaced + signs_added) * 100,
        "Zamijenjeni znakovi": signs_replaced, 
        "Zamijenjeni znakovi postotak": signs_replaced / (signs_ok + signs_ommited + signs_replaced + signs_added) * 100,
        "Dodani znakovi": signs_added,
        "Dodani znakovi postotak": signs_added / (signs_ok + signs_ommited + signs_replaced + signs_added) * 100,
        "Insertions ALIGN": signs_inserted,
        "Insertions ALIGN postotak": signs_inserted / signs_all * 100,
        "Deletions ALIGN": signs_deleted,
        "Deletions ALIGN postotak": signs_deleted / signs_all * 100,
        "Substitutions ALIGN": signs_substituted,
        "Substitutions ALIGN postotak": signs_substituted / signs_all * 100,
        "Equal": signs_equal, 
        "Equal postotak": signs_equal / signs_all * 100, 
        "Incorrect ALIGN": signs_inserted + signs_deleted + signs_substituted, 
        "Incorrect ALIGN postotak": (signs_inserted + signs_deleted + signs_substituted) / signs_all * 100,   
        "Ratio": sim_rat,
        "Ratio postotak": sim_rat / (ok_sentences + wrong_sentences) * 100,
        "Točni znakovi ALIGN": signs_ok2,
        "Točni znakovi ALIGN postotak": signs_ok2 / (signs_ok2 + signs_ommited2 + signs_replaced2 + signs_added2) * 100,
        "Netočni znakovi ALIGN": signs_ommited2 + signs_replaced2 + signs_added2,
        "Netočni znakovi ALIGN postotak": (signs_ommited2 + signs_replaced2 + signs_added2) / (signs_ok2 + signs_ommited2 + signs_replaced2 + signs_added2) * 100,
        "Ispušteni znakovi ALIGN": signs_ommited2,
        "Ispušteni znakovi ALIGN postotak": signs_replaced2 / (signs_ok2 + signs_ommited2 + signs_replaced2 + signs_added2) * 100,
        "Zamijenjeni znakovi ALIGN": signs_replaced2, 
        "Zamijenjeni znakovi ALIGN postotak": signs_replaced2 / (signs_ok2 + signs_ommited2 + signs_replaced2 + signs_added2) * 100,
        "Dodani znakovi ALIGN": signs_added2,
        "Dodani znakovi ALIGN postotak": signs_added2 / (signs_ok2 + signs_ommited2 + signs_replaced2 + signs_added2) * 100}
    
    for phone in all_phones:
        signs_all_phone = signs_inserted_dict[phone] + signs_deleted_dict[phone] + signs_substituted_dict[phone] + signs_equal_dict[phone]
        dict_vals[output_name] = dict_vals[output_name] | {
            phone + " Točni znakovi": signs_ok_dict[phone], 
            phone + " Točni znakovi postotak": weird_divide(signs_ok_dict[phone], (signs_ok_dict[phone] + signs_ommited_dict[phone] + signs_replaced_dict[phone] + signs_added_dict[phone]) * 100),
            phone + " Netočni znakovi": signs_ommited_dict[phone] + signs_replaced_dict[phone] + signs_added_dict[phone],
            phone + " Netočni znakovi postotak": weird_divide(signs_ommited_dict[phone] + signs_replaced_dict[phone] + signs_added_dict[phone], (signs_ok_dict[phone] + signs_ommited_dict[phone] + signs_replaced_dict[phone] + signs_added_dict[phone]) * 100),
            phone + " Ispušteni znakovi": signs_ommited_dict[phone], 
            phone + " Ispušteni znakovi postotak": weird_divide(signs_ommited_dict[phone], (signs_ok_dict[phone] + signs_ommited_dict[phone] + signs_replaced_dict[phone] + signs_added_dict[phone]) * 100),
            phone + " Zamijenjeni znakovi": signs_replaced_dict[phone], 
            phone + " Zamijenjeni znakovi postotak": weird_divide(signs_replaced_dict[phone], (signs_ok_dict[phone] + signs_ommited_dict[phone] + signs_replaced_dict[phone] + signs_added_dict[phone]) * 100),
            phone + " Dodani znakovi": signs_added_dict[phone],
            phone + " Dodani znakovi postotak": weird_divide(signs_added_dict[phone], (signs_ok_dict[phone] + signs_ommited_dict[phone] + signs_replaced_dict[phone] + signs_added_dict[phone]) * 100),
            phone + " Insertions ALIGN": signs_inserted_dict[phone],
            phone + " Insertions ALIGN postotak": weird_divide(signs_inserted_dict[phone], signs_all_phone * 100),
            phone + " Deletions ALIGN": signs_deleted_dict[phone],
            phone + " Deletions ALIGN postotak": weird_divide(signs_deleted_dict[phone], signs_all_phone * 100),
            phone + " Substitutions ALIGN": signs_substituted_dict[phone],
            phone + " Substitutions ALIGN postotak": weird_divide(signs_substituted_dict[phone], signs_all_phone * 100),
            phone + " Equal": signs_equal_dict[phone], 
            phone + " Equal postotak": weird_divide(signs_equal_dict[phone], signs_all_phone * 100),  
            phone + " Incorrect ALIGN": signs_inserted_dict[phone] + signs_deleted_dict[phone] + signs_substituted_dict[phone], 
            phone + " Incorrect ALIGN postotak": weird_divide(signs_inserted_dict[phone] + signs_deleted_dict[phone] + signs_substituted_dict[phone], signs_all_phone * 100),   
            phone + " Točni znakovi ALIGN": signs_ok2_dict[phone],
            phone + " Točni znakovi ALIGN postotak": weird_divide(signs_ok2_dict[phone], (signs_ok2_dict[phone] + signs_ommited2_dict[phone] + signs_replaced2_dict[phone] + signs_added2_dict[phone]) * 100),
            phone + " Netočni znakovi ALIGN": signs_ommited2_dict[phone] + signs_replaced2_dict[phone] + signs_added2_dict[phone],
            phone + " Netočni znakovi ALIGN postotak": weird_divide(signs_ommited2_dict[phone] + signs_replaced2_dict[phone] + signs_added2_dict[phone], (signs_ok2_dict[phone] + signs_ommited2_dict[phone] + signs_replaced2_dict[phone] + signs_added2_dict[phone]) * 100),
            phone + " Ispušteni znakovi ALIGN": signs_ommited2_dict[phone],
            phone + " Ispušteni znakovi ALIGN postotak": weird_divide(signs_replaced2_dict[phone], (signs_ok2_dict[phone] + signs_ommited2_dict[phone] + signs_replaced2_dict[phone] + signs_added2_dict[phone]) * 100),
            phone + " Zamijenjeni znakovi ALIGN": signs_replaced2_dict[phone], 
            phone + " Zamijenjeni znakovi ALIGN postotak": weird_divide(signs_replaced2_dict[phone], (signs_ok2_dict[phone] + signs_ommited2_dict[phone] + signs_replaced2_dict[phone] + signs_added2_dict[phone]) * 100),
            phone + " Dodani znakovi ALIGN": signs_added2_dict[phone],
            phone + " Dodani znakovi ALIGN postotak": weird_divide(signs_added2_dict[phone], (signs_ok2_dict[phone] + signs_ommited2_dict[phone] + signs_replaced2_dict[phone] + signs_added2_dict[phone]) * 100)}
         
for dirs_to_include in ["z04", "VremenskaPrognoza", "a", "prvi", "hrt", "sz04", "sz08"]:

    excl_dirs = set() 

    dirnames_tmp = os.listdir(basedir + "all_outputs/outputs/")
    for dirname in dirnames_tmp:
        if dirs_to_include == 'z04' and dirname != 'z04':
            excl_dirs.add(dirname)
            continue
        if dirs_to_include == 'prvi' and dirname != 'prvi':
            excl_dirs.add(dirname)
            continue
        if dirs_to_include == 'hrt' and dirname != 'hrt':
            excl_dirs.add(dirname)
            continue
        if dirs_to_include == 'sz04' and dirname != 'sz04':
            excl_dirs.add(dirname)
            continue
        if dirs_to_include == 'sz08' and dirname != 'sz08':
            excl_dirs.add(dirname)
            continue
        if dirname[0] != dirs_to_include[0]:
            excl_dirs.add(dirname)
            continue

    dict_vals = {}

    num2 = 9

    for num in ["", 3, 7, 8, 9, 10, 11, 12, 13, 14]:
        start = "all_outputs/outputs" + str(num)

        files_train = open(basedir + "my_db" + str(num2) + "_train.fileids", "r")
        train_files_list = files_train.readlines()
        for i in range(len(train_files_list)):
            train_files_list[i] = train_files_list[i].replace("\n", "").split("/")[1]
        files_train.close()

        predictions_grade(start + "/")
        break
        predictions_grade(start + "_pruned/")
        predictions_grade(start + "_only_weather/")
        predictions_grade(start + "_only_weather_pruned/")
        predictions_grade(start + "_both/")
        predictions_grade(start + "_both_pruned/")

        for new_num in ["", 2, 3, 1, 4, 7, 8, 9, 10, 11, 12, 13, 14]:
            new_str = str(new_num)

            predictions_grade(start + "_only_weather_train" + new_str + "/")
            predictions_grade(start + "_only_weather_train_pruned" + new_str + "/")

            predictions_grade(start + "_both_train" + new_str + "/")
            predictions_grade(start + "_both_train_pruned" + new_str + "/") 
    break
    for table_value in dict_vals[start + "/"].keys():

        string_table = "Acoustic model;Wikipedia;Wikipedia pruned;"
        string_table += "Weather with test;Weather with test pruned;Wikipedia and weather with test;Wikipedia and weather with test pruned;"
        string_table += "Weather;Weather pruned;Wikipedia and weather;Wikipedia and weather pruned;"
        string_table += "New source;New source pruned;Wikipedia, weather and new source;Wikipedia, weather and new source pruned;"
        string_table += "Alka with test;Alka with test pruned;Wikipedia, weather, new source and alka with test;Wikipedia, weather, new source and alka with test pruned;"

        string_table += "Weather;Weather pruned;Wikipedia and weather;Wikipedia and weather pruned;"
        string_table += "Weather and new source;Weather and new source pruned;Wikipedia, weather and new source;Wikipedia, weather and new source pruned;"
        string_table += "Expanded weather and new source;Expanded weather and new source pruned;Wikipedia, expanded weather and new source;Wikipedia, expanded weather and new source pruned;"
        string_table += "Expanded weather;Expanded weather pruned;Wikipedia and expanded weather;Wikipedia and expanded weather pruned;"
        string_table += "Weather, new source and alka;Weather, new source and alka pruned;Wikipedia, weather, new source and alka;Wikipedia, weather, new source and alka pruned;"
        string_table += "Expanded weather, new source and alka;Expanded weather, new source and alka pruned;Wikipedia, expanded weather, new source and alka;Wikipedia, expanded weather, new source and alka pruned;"
        string_table += "Expanded weather and alka;Expanded weather and alka pruned;Wikipedia, expanded weather and alka;Wikipedia, expanded weather and alka pruned;"
        string_table += "Weather and alka;Weather and alka pruned;Wikipedia and alka;Wikipedia and alka pruned;"
        string_table += "All sources;All sources pruned;Wikipedia and all sources;Wikipedia and all sources pruned\n"

        for num in ["", 3, 7, 8, 9, 10, 11, 12, 13, 14]:

            start = "all_outputs/outputs" + str(num)

            name_model = "Weather"

            if num == 3:
                name_model = "Weather and new source"

            if num == 7:
                name_model = "Expanded weather and new source"

            if num == 8:
                name_model = "Expanded weather"

            if num == 9:
                name_model = "Weather, new source and alka"

            if num == 10:
                name_model = "Expanded weather, new source and alka"

            if num == 11:
                name_model = "Expanded weather and alka"

            if num == 12:
                name_model = "Weather and alka"

            if num == 13:
                name_model = "Expanded all sources"

            if num == 14:
                name_model = "All sources"

            string_table += name_model + ";"

            string_table += str(dict_vals[start + "/"][table_value]) + ";"
            string_table += str(dict_vals[start + "_pruned/"][table_value]) + ";"
            string_table += str(dict_vals[start + "_only_weather/"][table_value]) + ";"
            string_table += str(dict_vals[start + "_only_weather_pruned/"][table_value]) + ";"
            string_table += str(dict_vals[start + "_both/"][table_value]) + ";"
            string_table += str(dict_vals[start + "_both_pruned/"][table_value]) 

            for new_num in ["", 2, 3, 1, 4, 7, 8, 9, 10, 11, 12, 13, 14]:
                new_str = str(new_num)

                string_table += ";" 

                string_table += str(dict_vals[start + "_only_weather_train" + new_str + "/"][table_value]) + ";"
                string_table += str(dict_vals[start + "_only_weather_train_pruned" + new_str + "/"][table_value]) + ";"

                string_table += str(dict_vals[start + "_both_train" + new_str + "/"][table_value]) + ";"
                string_table += str(dict_vals[start + "_both_train_pruned" + new_str + "/"][table_value])

            string_table += "\n"

        filename_table = basedir + "all_results/" + dirs_to_include + " " + table_value + ".csv"

        print(filename_table)
        print(string_table)

        file_table = open(filename_table, "w")
        file_table.write(string_table)
        file_table.close()