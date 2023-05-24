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

            '''
            print("Words:", words_val, 
                "Correct:", correct_val, 
                "Errors:", errors_signs_val, 
                "Percent correct =", correct_val / words_val * 100, "%",
                "Error =", errors_signs_val / words_val * 100, "%",
                "Accuracy =", 100 - (errors_signs_val / words_val) * 100, "%")
            print("Insertions:", ins_val, 
                "Substitutions:", sub_val, 
                "Deletions:", dele_val)
            '''

            if words_val_total == correct_val_total:
                correct_sentences_total += 1
            else:
                incorrect_sentences_total += 1 

    print(output_name) 

    print("Words:", words_val_total, 
          "Correct:", correct_val_total, 
          "Errors:", errors_signs_val_total, 
          "Percent correct =", correct_val_total / words_val_total * 100, "%",
          "Error =", errors_signs_val_total / words_val_total * 100, "%",
          "Accuracy =", 100 - (errors_signs_val_total / words_val_total) * 100, "%")
    
    print("Insertions:", ins_val_total, 
        "Substitutions:", sub_val_total, 
        "Deletions:", dele_val_total)
    
    print(
          "Word error rate =", 100 - correct_val_total / words_val_total * 100, "%", "(", words_val_total - correct_val_total, "/", words_val_total, ")",
          "Sentence error rate =", incorrect_sentences_total / (correct_sentences_total + incorrect_sentences_total) * 100, "%", "(", incorrect_sentences_total, "/", correct_sentences_total + incorrect_sentences_total, ")")

    dict_vals[output_name] = {
        "Total words": words_val_total, 
        "Correct words": correct_val_total,  
        "Errors": errors_signs_val_total, 
        "Percent correct": correct_val_total / words_val_total * 100,   
        "Error": errors_signs_val_total / words_val_total * 100,  
        "Accuracy": 100 - (errors_signs_val_total / words_val_total) * 100,
        "Insertions": ins_val_total, 
        "Substitutions": sub_val_total, 
        "Deletions": dele_val_total,
        "Correct sentences": correct_sentences_total,
        "Incorrect sentences": incorrect_sentences_total,
        "Word error rate": 100 - correct_val_total / words_val_total * 100,  
        "Sentence error rate": incorrect_sentences_total / (correct_sentences_total + incorrect_sentences_total) * 100}
      
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
        string_table += "Weather and alka;Weather and alka pruned;Wikipedia and alka;Wikipedia and alka pruned\n"

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