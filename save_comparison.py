import os
import difflib
import subprocess

basedir = "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/"

excl_dirs = ["a", "VremenskaPrognoza", "m", "z", "sm04", "hrt", "prvi", "sz04", "sz08"] 
excl_dirs = ["a", "VremenskaPrognoza", "m", "z"] 
 
#dirnames_tmp = os.listdir(basedir + "all_outputs/outputs/")  

def predictions_grade(output_name): 

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

            if len(lines_from_file) < 2:
                continue
             
            line_original = lines_from_file[0].replace("\n", "")
            line_new = lines_from_file[1].replace("\n", "")

            original_filename_to_open = basedir + output_name + "/" + dirname + "/" + filename.replace(".txt", "_original.txt")
            new_filename_to_open = basedir + output_name + "/" + dirname + "/" + filename.replace(".txt", "_new.txt")

            file_original_to_open = open(original_filename_to_open, "w") 
            file_original_to_open.write(line_original + "\n")
            file_original_to_open.close() 

            file_new_to_open = open(new_filename_to_open, "w") 
            file_new_to_open.write(line_new + "\n")
            file_new_to_open.close()
            
            pipe = subprocess.Popen(['perl', basedir + "word_align.pl", original_filename_to_open, new_filename_to_open], stdout=subprocess.PIPE)

            x = str(pipe.stdout.read())

            compare_filename_to_open = basedir + output_name + "/" + dirname + "/" + filename.replace(".txt", "_compare.txt")

            file_compare_to_open = open(compare_filename_to_open, "w") 
            file_compare_to_open.write(x)
            file_compare_to_open.close() 

for num in ["", 3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
    start = "all_outputs/outputs" + str(num)

    files_train = open(basedir + "my_db" + str(num) + "_train.fileids", "r")
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

    for new_num in [15, 16]:
        new_str = str(new_num)

        predictions_grade(start + "_only_weather_train" + new_str + "/")
        predictions_grade(start + "_only_weather_train_pruned" + new_str + "/")

        predictions_grade(start + "_both_train" + new_str + "/")
        predictions_grade(start + "_both_train_pruned" + new_str + "/")