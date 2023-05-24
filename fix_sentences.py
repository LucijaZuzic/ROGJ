import os
import difflib
import subprocess

basedir = "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/"

files_train = open(basedir + "my_db7_train.fileids", "r")
train_files_list = files_train.readlines()
for i in range(len(train_files_list)):
    train_files_list[i] = train_files_list[i].replace("\n", "").split("/")[1]
files_train.close()

excl_dirs = set() 

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
 
            if line_original.count("<") != 0:
                print(line_original)
                print(line_original)
            else:
                continue

            line_original = line_original.replace("<", "").replace(">", "")

            file_to_open = open(basedir + output_name + "/" + dirname + "/" + filename, "w")
            file_to_open.write(line_original + "\n" + line_new)
            file_to_open.close() 

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

predictions_grade("outputs7/")
predictions_grade("outputs7_pruned/")

predictions_grade("outputs8/")
predictions_grade("outputs8_pruned/")

predictions_grade("outputs7_only_weather/")
predictions_grade("outputs7_only_weather_pruned/")

predictions_grade("outputs8_only_weather/")
predictions_grade("outputs8_only_weather_pruned/")

predictions_grade("outputs7_both/")
predictions_grade("outputs7_both_pruned/")

predictions_grade("outputs8_both/")
predictions_grade("outputs8_both_pruned/")

predictions_grade("outputs7_only_weather_train/")
predictions_grade("outputs7_only_weather_train_pruned/")

predictions_grade("outputs8_only_weather_train/")
predictions_grade("outputs8_only_weather_train_pruned/")

predictions_grade("outputs7_both_train/")
predictions_grade("outputs7_both_train_pruned/")

predictions_grade("outputs8_both_train/")
predictions_grade("outputs8_both_train_pruned/")

predictions_grade("outputs7_only_weather_train2/")
predictions_grade("outputs7_only_weather_train_pruned2/")

predictions_grade("outputs8_only_weather_train2/")
predictions_grade("outputs8_only_weather_train_pruned2/")

predictions_grade("outputs7_both_train2/")
predictions_grade("outputs7_both_train_pruned2/")

predictions_grade("outputs8_both_train2/")
predictions_grade("outputs8_both_train_pruned2/")
