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

    correct_sentences_total = 0
    incorrect_sentences_total = 0

    words_val_total = 0
    correct_val_total = 0
    errors_signs_val_total = 0

    ins_val_total = 0
    dele_val_total = 0
    sub_val_total = 0
 
    ok_sentences = 0
    wrong_sentences = 0

    words_ok = 0 
    words_deleted = 0 
    words_inserted = 0 
    words_modified = 0

    signs_ok = 0

    signs_replaced = 0
    signs_ommited = 0
    signs_added = 0

    signs_ok_dict = {sign_phone: 0 for sign_phone in all_phones}

    signs_replaced_dict = {sign_phone: 0 for sign_phone in all_phones}
    signs_ommited_dict = {sign_phone: 0 for sign_phone in all_phones}
    signs_added_dict = {sign_phone: 0 for sign_phone in all_phones}

    sim_rat = 0
  
    signs_inserted = 0
    signs_deleted = 0
    signs_substituted = 0
    signs_equal = 0 

    signs_inserted_dict = {sign_phone: 0 for sign_phone in all_phones}
    signs_deleted_dict = {sign_phone: 0 for sign_phone in all_phones}
    signs_substituted_dict = {sign_phone: 0 for sign_phone in all_phones}
    signs_equal_dict = {sign_phone: 0 for sign_phone in all_phones}

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
                        if i + 1 < len(seqb):
                            if sign_new + seqb[i + 1] in ["dž", "lj", "nj"]: 
                                sign_new += seqb[i + 1]  
                                 
                        signs_inserted += 1 
                        signs_inserted_dict[sign_new] += 1
                if opcode[0] == 'delete': 
                    for i in range(len(seqa)): 
                        sign_new = seqa[i]   
                        if i + 1 < len(seqa):
                            if sign_new + seqa[i + 1] in ["dž", "lj", "nj"]: 
                                sign_new += seqa[i + 1]  
                                
                        signs_deleted += 1 
                        signs_deleted_dict[sign_new] += 1   
                if opcode[0] == 'replace': 
                    for i in range(len(seqa)): 
                        sign_original = seqa[i] 
                        if i + 1 < len(seqa):
                            if sign_original + seqa[i + 1] in ["dž", "lj", "nj"]: 
                                sign_original += seqa[i + 1]  
                                
                        sign_new = seqb[i]   
                        if i + 1 < len(seqb):
                            if sign_new + seqb[i + 1] in ["dž", "lj", "nj"]: 
                                sign_new += seqb[i + 1]  
                                
                        if sign_original != '*' and sign_new != '*':
                            signs_substituted += 1
                            signs_substituted_dict[sign_original] += 1  
                        if sign_original != '*' and sign_new == '*':
                            signs_deleted += 1
                            signs_deleted_dict[sign_original] += 1  
                        if sign_original == '*' and sign_new != '*':
                            signs_inserted += 1
                            signs_inserted_dict[sign_new] += 1  
                if opcode[0] == 'equal': 
                    for i in range(len(seqa)): 
                        sign_new = seqa[i]   
                        if i + 1 < len(seqa):
                            if sign_new + seqa[i + 1] in ["dž", "lj", "nj"]: 
                                sign_new += seqa[i + 1]  
                                
                        signs_equal += 1 
                        signs_equal_dict[sign_new] += 1
                  
            sim_rat += s.ratio()
            
            while len(a1) > 0 and a1[-1] == '*':
                a1 = a1[:-1]

            while len(b1) > 0 and b1[-1] == '*':
                b1 = b1[:-1]

            for sign_num in range(len(a1)):
                sign_original = a1[sign_num] 
                if sign_num + 1 < len(a1):
                    if sign_original + a1[sign_num + 1] in ["dž", "lj", "nj"]: 
                    	sign_original += a1[sign_num + 1] 

                if sign_num >= len(b1):
                    signs_ommited += 1 
                    signs_ommited_dict[sign_original] += 1
                    continue

                sign_new = b1[sign_num]
                if sign_num + 1 < len(b1):
                    if sign_new + b1[sign_num + 1] in ["dž", "lj", "nj"]: 
                    	sign_new += b1[sign_num + 1] 

                if sign_original != sign_new:
                    if sign_original != '*' and sign_new != '*':
                        signs_replaced += 1 
                        signs_replaced_dict[sign_original] += 1
                    if sign_original == '*' and sign_new != '*':
                        signs_added += 1 
                        signs_added_dict[sign_new] += 1
                    if sign_original != '*' and sign_new == '*':
                        signs_ommited += 1 
                        signs_ommited_dict[sign_original] += 1
                    continue

                signs_ok += 1
                signs_ok_dict[sign_original] += 1 

            for sign_num in range(len(a1), len(b1)):
                sign_new = b1[sign_num]
                if sign_num + 1 < len(b1):
                    if sign_new + b1[sign_num + 1] in ["dž", "lj", "nj"]: 
                    	sign_new += b1[sign_num + 1] 

                signs_added += 1
                signs_added_dict[sign_new] += 1  
            
            sentence_ok = True
 
            current_pos = 0
            while current_pos < len(a1):
                word_correct = True
                word_deleted = False
                while current_pos < len(a1) and a1[current_pos] != ' ':
                    if current_pos < len(b1) and a1[current_pos] != b1[current_pos]:
                        word_correct = False
                    if current_pos >= len(b1):
                        word_correct = False
                        word_deleted = True
                    current_pos += 1
                current_pos += 1
                if word_correct:
                    words_ok += 1
                else: 
                    if word_deleted:
                        words_deleted += 1
                    else:
                        words_modified += 1 
                    sentence_ok = False
                    
            while current_pos < len(b1): 
                while current_pos < len(b1) and b1[current_pos] != ' ':
                    current_pos += 1
                current_pos += 1  
                words_inserted += 1
                sentence_ok = False

            if sentence_ok:
                ok_sentences += 1
            else:
                wrong_sentences += 1 

            if len(lines_from_file) >= 2:            
                compare_filename_to_open = basedir + output_name + "/" + dirname + "/" + filename.replace(".txt", "_compare.txt")

                file_compare_to_open = open(compare_filename_to_open, "r") 
                line_from_compare_file = file_compare_to_open.readlines()[0]  
                file_compare_to_open.close()  

                words = line_from_compare_file.find("Words:")
                correct_words = line_from_compare_file.find("Correct:")
                errors_signs = line_from_compare_file.find("Errors:")
                percor = line_from_compare_file.find("Percent correct")
                ins = line_from_compare_file.find("Insertions:")
                dele = line_from_compare_file.find("Deletions:")
                sub = line_from_compare_file.find("Substitutions:")
                tot = line_from_compare_file.find("TOTAL Words")
    
                words_val = int(line_from_compare_file[words + 7:correct_words - 1])
                correct_val = int(int(line_from_compare_file[correct_words + 9:errors_signs - 1]))
                errors_signs_val = int(line_from_compare_file[errors_signs + 8:percor - 1])

                ins_val = int(line_from_compare_file[ins + 12:dele - 1])
                dele_val = int(line_from_compare_file[dele + 11:sub - 1])
                sub_val = int(line_from_compare_file[sub + 15:tot - 2])
            else: 
                line_original = lines_from_file[0].replace("\n", "") 

                words_original = line_original.split(" ") 

                words_val = len(words_original)
                correct_val = 0
                errors_signs_val = len(line_original)

                ins_val = 0
                dele_val = errors_signs_val
                sub_val = 0

            words_val_total += words_val
            correct_val_total += correct_val
            errors_signs_val_total += errors_signs_val

            ins_val_total += ins_val
            dele_val_total += dele_val
            sub_val_total += sub_val 

            if words_val_total == correct_val_total:
                correct_sentences_total += 1
            else:
                incorrect_sentences_total += 1  

    print(output_name)

    print("Točne rečenice:", ok_sentences, "/", (ok_sentences + wrong_sentences), weird_divide(ok_sentences, ok_sentences + wrong_sentences) * 100, "%",
          "Netočne rečenice:", wrong_sentences, "/", (ok_sentences + wrong_sentences), weird_divide(wrong_sentences, ok_sentences + wrong_sentences)* 100, "%")

    words_not_ok_without = words_modified + words_deleted
    words_not_ok = words_modified + words_deleted + words_inserted

    print("Točne riječi:", words_ok, "/", (words_ok + words_not_ok_without), weird_divide(words_ok, words_ok + words_not_ok_without) * 100, "%",
          "Točne riječi inserted:", words_ok, "/", (words_ok + words_not_ok), weird_divide(words_ok, words_ok + words_not_ok) * 100, "%")
          
   
    print("Netočne riječi:", words_not_ok_without, "/", (words_ok + words_not_ok_without), weird_divide(words_not_ok_without, words_ok + words_not_ok_without) * 100, "%",
          "Netočne riječi inserted:", words_not_ok, "/", (words_ok + words_not_ok), weird_divide(words_not_ok, words_ok + words_not_ok) * 100, "%")
    
    print("Zamijenjene riječi:", words_modified, "/", (words_ok + words_not_ok_without), weird_divide(words_modified, words_ok + words_not_ok_without) * 100, "%",
          "Zamijenjene riječi inserted:", words_modified, "/", (words_ok + words_not_ok), weird_divide(words_modified, words_ok + words_not_ok) * 100, "%")
    
    print("Ispuštene riječi:", words_deleted, "/", (words_ok + words_not_ok_without), weird_divide(words_deleted, words_ok + words_not_ok_without) * 100, "%",
          "Ispuštene riječi inserted:", words_deleted, "/", (words_ok + words_not_ok), weird_divide(words_deleted, words_ok + words_not_ok) * 100, "%")
    
    print("Dodane riječi:", words_inserted, "/", (words_ok + words_not_ok_without), weird_divide(words_inserted, words_ok + words_not_ok_without) * 100, "%",
          "Dodane riječi inserted:", words_inserted, "/", (words_ok + words_not_ok), weird_divide(words_inserted, words_ok + words_not_ok) * 100, "%")

    print("WER:", (words_not_ok_without + words_inserted), "/", (words_ok + words_not_ok_without), weird_divide(words_not_ok_without + words_inserted, words_ok + words_not_ok_without) * 100, "%")
    
    print("MER:", (words_not_ok_without + words_inserted), "/", (words_ok + words_not_ok_without + words_inserted), weird_divide(words_not_ok_without + words_inserted, words_ok + words_not_ok_without + words_inserted) * 100, "%",
          "WIL:", ((words_ok + words_not_ok_without) * (words_ok + words_modified + words_inserted) - words_ok ** 2), "/", (words_ok + words_not_ok_without) * (words_ok + words_modified + words_inserted),
   weird_divide((words_ok + words_not_ok_without) * (words_ok + words_modified + words_inserted) - words_ok ** 2, (words_ok + words_not_ok_without) * (words_ok + words_modified + words_inserted)) * 100, "%")
   
    signs_total = signs_ok + signs_added + signs_ommited + signs_replaced
    signs_not_ok = signs_added + signs_ommited + signs_replaced

    print("Točni znakovi:", signs_ok, "/", signs_total, weird_divide(signs_ok, signs_total) * 100, "%",
          "Netočni znakovi:", signs_not_ok, "/", signs_total, weird_divide(signs_not_ok, signs_total) * 100, "%")
    
    print("Dodani znakovi:", signs_added, "/", signs_total, weird_divide(signs_added, signs_total) * 100, "%",
          "Ispušteni znakovi:", signs_ommited, "/", signs_total, weird_divide(signs_ommited, signs_total) * 100, "%")
    
    print("Zamijenjeni znakovi:", signs_replaced, "/", signs_total, weird_divide(signs_replaced, signs_total) * 100, "%")
    
    signs_all = signs_equal + signs_inserted + signs_deleted + signs_substituted
    signs_wrong = signs_inserted + signs_deleted + signs_substituted
    
    print("Equal ALIGN:", signs_equal, "/", signs_all, weird_divide(signs_equal, signs_all) * 100, "%",
          "Incorrect ALIGN:", signs_wrong, "/", signs_all, weird_divide(signs_wrong, signs_all) * 100, "%")
    
    print("Insertions ALIGN:", signs_inserted, "/", signs_all, weird_divide(signs_inserted, signs_all) * 100, "%",  
          "Deletions ALIGN:", signs_deleted, "/", signs_all, weird_divide(signs_deleted, signs_all) * 100, "%")
    
    print("Substitutions ALIGN:", signs_substituted, "/", signs_all, weird_divide(signs_substituted, signs_all) * 100, "%") 
     
    print("Ratio:", weird_divide(sim_rat, ok_sentences + wrong_sentences) * 100, "%")

    print("Words:", words_val_total, 
            "Correct:", correct_val_total, 
            "Errors:", errors_signs_val_total, 
            "Percent correct =", weird_divide(correct_val_total, words_val_total) * 100, "%",
            "Error =", weird_divide(errors_signs_val_total, words_val_total) * 100, "%",
            "Accuracy =", 100 - weird_divide(errors_signs_val_total, words_val_total) * 100, "%")
        
    print("Insertions:", ins_val_total, 
        "Substitutions:", sub_val_total, 
        "Deletions:", dele_val_total)
    
    print("Word error rate =", 100 - weird_divide(correct_val_total, words_val_total) * 100, "%", "(", words_val_total - correct_val_total, "/", words_val_total, ")",
        "Sentence error rate =", weird_divide(incorrect_sentences_total, correct_sentences_total + incorrect_sentences_total) * 100, "%", "(", incorrect_sentences_total, "/", correct_sentences_total + incorrect_sentences_total, ")")

    dict_vals[output_name] = {
        "Točne rečenice": ok_sentences,
        "Točne rečenice postotak": weird_divide(ok_sentences, ok_sentences + wrong_sentences) * 100,
        "Netočne rečenice": wrong_sentences,
        "Netočne rečenice postotak": weird_divide(wrong_sentences, ok_sentences + wrong_sentences) * 100,

        "Točne riječi": words_ok,  
        "Točne riječi postotak": weird_divide(words_ok, words_ok + words_not_ok_without) * 100,  
        "Točne riječi inserted postotak": weird_divide(words_ok, words_ok + words_not_ok) * 100, 

        "Netočne riječi": words_not_ok,  
        "Netočne riječi postotak": weird_divide(words_not_ok_without, words_ok + words_not_ok_without) * 100, 
        "Netočne riječi inserted postotak": weird_divide(words_not_ok, words_ok + words_not_ok) * 100,  
         
        "Zamijenjene riječi": words_modified, 
        "Zamijenjene riječi postotak": weird_divide(words_modified, words_ok + words_not_ok_without) * 100, 
        "Zamijenjene riječi inserted postotak": weird_divide(words_modified, words_ok + words_not_ok) * 100, 

        "Ispuštene riječi": words_deleted, 
        "Ispuštene riječi postotak": weird_divide(words_deleted, words_ok + words_not_ok_without) * 100, 
        "Ispuštene riječi inserted postotak": weird_divide(words_deleted, words_ok + words_not_ok) * 100, 

        "Dodane riječi": words_inserted, 
        "Dodane riječi postotak": weird_divide(words_inserted, words_ok + words_not_ok_without) * 100, 
        "Dodane riječi inserted postotak": weird_divide(words_inserted, words_ok + words_not_ok) * 100, 
     
        "WER": weird_divide(words_not_ok_without + words_inserted, words_ok + words_not_ok_without) * 100,   
        "MER": weird_divide(words_not_ok_without + words_inserted, words_ok + words_not_ok_without + words_inserted) * 100,
        "WIL": weird_divide((words_ok + words_not_ok_without) * (words_ok + words_modified + words_inserted) - words_ok ** 2, (words_ok + words_not_ok_without) * (words_ok + words_modified + words_inserted)) * 100,
   
        "Točni znakovi": signs_ok, 
        "Točni znakovi postotak": weird_divide(signs_ok, signs_total) * 100,
        "Netočni znakovi": signs_not_ok,
        "Netočni znakovi postotak": weird_divide(signs_not_ok, signs_total) * 100,
        "Dodani znakovi": signs_added,
        "Dodani znakovi postotak": weird_divide(signs_added, signs_total) * 100,
        "Ispušteni znakovi": signs_ommited, 
        "Ispušteni znakovi postotak": weird_divide(signs_ommited, signs_total) * 100,
        "Zamijenjeni znakovi": signs_replaced, 
        "Zamijenjeni znakovi postotak": weird_divide(signs_replaced, signs_total) * 100, 

        "Equal ALIGN": signs_equal, 
        "Equal ALIGN postotak": weird_divide(signs_equal, signs_all) * 100,   
        "Incorrect ALIGN": signs_wrong, 
        "Incorrect ALIGN postotak": weird_divide(signs_wrong, signs_all) * 100,   
        "Insertions ALIGN": signs_inserted,
        "Insertions ALIGN postotak": weird_divide(signs_inserted, signs_all) * 100,
        "Deletions ALIGN": signs_deleted,
        "Deletions ALIGN postotak": weird_divide(signs_deleted, signs_all) * 100,
        "Substitutions ALIGN": signs_substituted,
        "Substitutions ALIGN postotak": weird_divide(signs_substituted, signs_all) * 100, 

        "Ratio": sim_rat,
        "Ratio postotak": weird_divide(sim_rat, ok_sentences + wrong_sentences) * 100
    }
    
    dict_vals[output_name] = dict_vals[output_name] | {
        "Total words": words_val_total, 
        "Correct words": correct_val_total,  
        "Errors": errors_signs_val_total, 
        "Percent correct": weird_divide(correct_val_total, words_val_total) * 100,   
        "Error": weird_divide(errors_signs_val_total, words_val_total) * 100,  
        "Accuracy": 100 - weird_divide(errors_signs_val_total, words_val_total) * 100,
        "Insertions": ins_val_total, 
        "Substitutions": sub_val_total, 
        "Deletions": dele_val_total,
        "Correct sentences": correct_sentences_total,
        "Incorrect sentences": incorrect_sentences_total,
        "Word error rate": 100 - weird_divide(correct_val_total, words_val_total) * 100,  
        "Sentence error rate": weird_divide(incorrect_sentences_total, correct_sentences_total + incorrect_sentences_total) * 100}
    
    for phone in all_phones:

        signs_total_phone = signs_ok_dict[phone] + signs_added_dict[phone] + signs_ommited_dict[phone] + signs_replaced_dict[phone]
        signs_not_ok_phone = signs_added_dict[phone] + signs_ommited_dict[phone] + signs_replaced_dict[phone]

        signs_all_phone = signs_equal_dict[phone] + signs_inserted_dict[phone] + signs_deleted_dict[phone] + signs_substituted_dict[phone]
        signs_wrong_phone = signs_inserted_dict[phone] + signs_deleted_dict[phone] + signs_substituted_dict[phone]  

        dict_vals[output_name] = dict_vals[output_name] | {
            phone + " Točni znakovi": signs_ok_dict[phone], 
            phone + " Točni znakovi postotak": weird_divide(signs_ok_dict[phone], signs_total_phone) * 100,
            phone + " Netočni znakovi": signs_not_ok_phone,
            phone + " Netočni znakovi postotak":  weird_divide(signs_not_ok_phone, signs_total_phone) * 100, 
            phone + " Dodani znakovi": signs_added_dict[phone],
            phone + " Dodani znakovi postotak": weird_divide(signs_added_dict[phone], signs_total_phone) * 100,
            phone + " Ispušteni znakovi": signs_ommited_dict[phone], 
            phone + " Ispušteni znakovi postotak": weird_divide(signs_ommited_dict[phone], signs_total_phone) * 100, 
            phone + " Zamijenjeni znakovi": signs_replaced_dict[phone], 
            phone + " Zamijenjeni znakovi postotak": weird_divide(signs_replaced_dict[phone], signs_total_phone) * 100,
            
            phone + " Equal ALIGN": signs_equal_dict[phone], 
            phone + " Equal ALIGN postotak": weird_divide(signs_equal_dict[phone], signs_all_phone) * 100,  
            phone + " Incorrect ALIGN": signs_wrong_phone, 
            phone + " Incorrect ALIGN postotak": weird_divide(signs_wrong_phone, signs_all_phone) * 100,
            phone + " Insertions ALIGN": signs_inserted_dict[phone],
            phone + " Insertions ALIGN postotak": weird_divide(signs_inserted_dict[phone], signs_all_phone) * 100,
            phone + " Deletions ALIGN": signs_deleted_dict[phone],
            phone + " Deletions ALIGN postotak": weird_divide(signs_deleted_dict[phone], signs_all_phone) * 100,
            phone + " Substitutions ALIGN": signs_substituted_dict[phone],
            phone + " Substitutions ALIGN postotak": weird_divide(signs_substituted_dict[phone], signs_all_phone) * 100,
        }
         
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

    for num in ["", 3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
        start = "all_outputs/outputs" + str(num)

        files_train = open(basedir + "my_db" + str(num2) + "_train.fileids", "r")
        train_files_list = files_train.readlines()
        for i in range(len(train_files_list)):
            train_files_list[i] = train_files_list[i].replace("\n", "").split("/")[1]
        files_train.close()

        predictions_grade(start + "/") 
        predictions_grade(start + "_pruned/")
        predictions_grade(start + "_only_weather/")
        predictions_grade(start + "_only_weather_pruned/")
        predictions_grade(start + "_both/")
        predictions_grade(start + "_both_pruned/")

        for new_num in ["", 2, 3, 1, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
            new_str = str(new_num)

            predictions_grade(start + "_only_weather_train" + new_str + "/")
            predictions_grade(start + "_only_weather_train_pruned" + new_str + "/")

            predictions_grade(start + "_both_train" + new_str + "/")
            predictions_grade(start + "_both_train_pruned" + new_str + "/") 
            
    for table_value in dict_vals[start + "/"].keys():

        string_table = "Acoustic model;Wikipedia;Wikipedia pruned;"
        string_table += "Weather with test;Weather with test pruned;Wikipedia and weather with test;Wikipedia and weather with test pruned;"

        string_table += "Weather original;Weather original pruned;Wikipedia and weather original;Wikipedia and weather original pruned;"
        string_table += "New source original;New source original pruned;Wikipedia, weather and new source original;Wikipedia, weather and new source original pruned;"
        string_table += "Alka with test;Alka with test pruned;Wikipedia, weather, new source and alka with test;Wikipedia, weather, new source and alka with test pruned;"

        string_table += "Weather;Weather pruned;Wikipedia and weather;Wikipedia and weather pruned;"
        string_table += "Weather and new source;Weather and new source pruned;Wikipedia, weather and new source;Wikipedia, weather and new source pruned;"
        string_table += "Expanded weather and new source;Expanded weather and new source pruned;Wikipedia, expanded weather and new source;Wikipedia, expanded weather and new source pruned;"
        string_table += "Expanded weather;Expanded weather pruned;Wikipedia and expanded weather;Wikipedia and expanded weather pruned;"
        string_table += "Weather, new source and alka;Weather, new source and alka pruned;Wikipedia, weather, new source and alka;Wikipedia, weather, new source and alka pruned;"
        string_table += "Expanded weather, new source and alka;Expanded weather, new source and alka pruned;Wikipedia, expanded weather, new source and alka;Wikipedia, expanded weather, new source and alka pruned;"
        string_table += "Expanded weather and alka;Expanded weather and alka pruned;Wikipedia, expanded weather and alka;Wikipedia, expanded weather and alka pruned;"
        string_table += "Weather and alka;Weather and alka pruned;Wikipedia and alka;Wikipedia and alka pruned;"
        string_table += "Expanded all sources;Expanded all sources pruned;Wikipedia and expanded all sources;Wikipedia and expanded all sources pruned;"
        string_table += "All sources;All sources pruned;Wikipedia and all sources;Wikipedia and all sources pruned;"
        string_table += "Expanded no TV;Expanded no TV pruned;Wikipedia and expanded no TV;Wikipedia and expanded no TV pruned;"
        string_table += "No TV;No TV pruned;Wikipedia and no TV;Wikipedia and no TV pruned\n"

        for num in ["", 3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:

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

            if num == 15:
                name_model = "Expanded no TV"

            if num == 16:
                name_model = "No TV"

            string_table += name_model + ";"

            string_table += str(dict_vals[start + "/"][table_value]) + ";"
            string_table += str(dict_vals[start + "_pruned/"][table_value]) + ";"
            string_table += str(dict_vals[start + "_only_weather/"][table_value]) + ";"
            string_table += str(dict_vals[start + "_only_weather_pruned/"][table_value]) + ";"
            string_table += str(dict_vals[start + "_both/"][table_value]) + ";"
            string_table += str(dict_vals[start + "_both_pruned/"][table_value]) 

            for new_num in ["", 2, 3, 1, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
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
