namescheck = {'all_outputs/outputs7_both_train12/', 'all_outputs/outputs_both_train15/', 'all_outputs/outputs3_both_train_pruned10/', 'all_outputs/outputs3_both/', 'all_outputs/outputs8_both_train_pruned3/', 'all_outputs/outputs_both_train3/', 'all_outputs/outputs7_both_train3/', 'all_outputs/outputs7_both_pruned/', 'all_outputs/outputs_both_train_pruned8/', 'all_outputs/outputs3_both_train9/', 'all_outputs/outputs_pruned/', 'all_outputs/outputs3_both_train7/', 'all_outputs/outputs3_both_train_pruned2/', 'all_outputs/outputs7_both_train15/', 'all_outputs/outputs3_both_train10/', 'all_outputs/outputs3_both_train12/', 'all_outputs/outputs_both_train_pruned15/', 'all_outputs/outputs8_both_train_pruned16/', 'all_outputs/outputs3_both_train_pruned1/', 'all_outputs/outputs7_both_train_pruned8/', 'all_outputs/outputs8_both_train3/', 'all_outputs/outputs7_both_train_pruned7/', 'all_outputs/outputs8_both_train8/', 'all_outputs/outputs_both_train_pruned12/', 'all_outputs/outputs8_both_train_pruned12/', 'all_outputs/outputs8_both/', 'all_outputs/outputs_both_train_pruned16/', 'all_outputs/outputs_both_train1/', 'all_outputs/outputs_both_train16/', 'all_outputs/outputs3_pruned/', 'all_outputs/outputs3_both_train_pruned14/', 'all_outputs/outputs3_both_train_pruned8/', 'all_outputs/outputs3_both_train11/', 'all_outputs/outputs7_both_train_pruned10/', 'all_outputs/outputs7_both_train_pruned13/', 'all_outputs/outputs8_both_train_pruned7/', 'all_outputs/outputs7_both_train11/', 'all_outputs/outputs7_both/', 'all_outputs/outputs7_both_train_pruned11/', 'all_outputs/outputs7_both_train14/', 'all_outputs/outputs8_both_train_pruned4/', 'all_outputs/outputs8_both_train_pruned13/', 'all_outputs/outputs3/', 'all_outputs/outputs_both/', 'all_outputs/outputs8_both_train10/', 'all_outputs/outputs3_both_train_pruned9/', 'all_outputs/outputs_both_pruned/', 'all_outputs/outputs7_both_train_pruned9/', 'all_outputs/outputs8_both_train_pruned11/', 'all_outputs/outputs_both_train4/', 'all_outputs/outputs_both_train_pruned10/', 'all_outputs/outputs3_both_train16/', 'all_outputs/outputs7_both_train_pruned12/', 'all_outputs/outputs7_both_train9/', 'all_outputs/outputs3_both_train_pruned13/', 'all_outputs/outputs3_both_train_pruned7/', 'all_outputs/outputs7_both_train_pruned3/', 'all_outputs/outputs8_both_train_pruned10/', 'all_outputs/outputs_both_train_pruned2/', 'all_outputs/outputs7_both_train8/', 'all_outputs/outputs8_both_train15/', 'all_outputs/outputs8_both_train/', 'all_outputs/outputs_both_train_pruned/', 'all_outputs/outputs7_both_train_pruned4/', 'all_outputs/outputs7_both_train_pruned2/', 'all_outputs/outputs7_both_train/', 'all_outputs/outputs8_both_train9/', 'all_outputs/outputs8_both_train2/', 'all_outputs/outputs8_both_train_pruned9/', 'all_outputs/outputs8_both_train_pruned/', 'all_outputs/outputs7_both_train16/', 'all_outputs/outputs8_both_train4/', 'all_outputs/outputs_both_train_pruned7/', 'all_outputs/outputs3_both_train_pruned16/', 'all_outputs/outputs8_both_train1/', 'all_outputs/outputs_both_train14/', 'all_outputs/outputs_both_train8/', 'all_outputs/outputs3_both_train14/', 'all_outputs/outputs8_both_train12/', 'all_outputs/outputs8_both_pruned/', 'all_outputs/outputs_both_train/', 'all_outputs/outputs7_both_train_pruned/', 'all_outputs/outputs7_both_train1/', 'all_outputs/outputs3_both_train3/', 'all_outputs/outputs_both_train9/', 'all_outputs/outputs7_both_train_pruned14/', 'all_outputs/outputs7_both_train_pruned15/', 'all_outputs/outputs7_both_train4/', 'all_outputs/outputs7/', 'all_outputs/outputs_both_train_pruned11/', 'all_outputs/outputs7_both_train_pruned16/', 'all_outputs/outputs8_both_train13/', 'all_outputs/outputs7_both_train2/', 'all_outputs/outputs3_both_train4/', 'all_outputs/outputs8_both_train16/', 'all_outputs/outputs8/', 'all_outputs/outputs_both_train2/', 'all_outputs/outputs/', 'all_outputs/outputs_both_train_pruned9/', 'all_outputs/outputs3_both_train_pruned11/', 'all_outputs/outputs3_both_train13/', 'all_outputs/outputs3_both_train15/', 'all_outputs/outputs_both_train_pruned14/', 'all_outputs/outputs_both_train12/', 'all_outputs/outputs3_both_train_pruned15/', 'all_outputs/outputs3_both_pruned/', 'all_outputs/outputs3_both_train/', 'all_outputs/outputs3_both_train1/', 'all_outputs/outputs7_both_train13/', 'all_outputs/outputs8_both_train_pruned14/', 'all_outputs/outputs_both_train_pruned3/', 'all_outputs/outputs3_both_train_pruned/', 'all_outputs/outputs_both_train_pruned4/', 'all_outputs/outputs3_both_train_pruned12/', 'all_outputs/outputs_both_train_pruned1/', 'all_outputs/outputs7_both_train7/', 'all_outputs/outputs3_both_train_pruned3/', 'all_outputs/outputs_both_train_pruned13/', 'all_outputs/outputs8_both_train7/', 'all_outputs/outputs8_both_train_pruned15/', 'all_outputs/outputs8_pruned/', 'all_outputs/outputs8_both_train14/', 'all_outputs/outputs8_both_train_pruned1/', 'all_outputs/outputs3_both_train2/', 'all_outputs/outputs7_pruned/', 'all_outputs/outputs8_both_train_pruned2/', 'all_outputs/outputs7_both_train10/', 'all_outputs/outputs8_both_train_pruned8/', 'all_outputs/outputs_both_train11/', 'all_outputs/outputs3_both_train_pruned4/', 'all_outputs/outputs7_both_train_pruned1/', 'all_outputs/outputs_both_train13/', 'all_outputs/outputs_both_train7/', 'all_outputs/outputs_both_train10/', 'all_outputs/outputs3_both_train8/', 'all_outputs/outputs8_both_train11/'}
dirscheck = {'anonymous-20131010-coh'}

import os
import difflib
import subprocess

basedir = "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/"
  
def predictions_grade(output_name): 
    if output_name not in namescheck:
        print(output_name)
        print("moving on")
        return

    dirnames = os.listdir(basedir + output_name)
    for dirname in dirnames: 
        if dirname not in dirscheck:
            print(dirname)
            print("moving on 2")
            return
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

    for new_num in ["", 2, 3, 1, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
        new_str = str(new_num)

        predictions_grade(start + "_only_weather_train" + new_str + "/")
        predictions_grade(start + "_only_weather_train_pruned" + new_str + "/")

        predictions_grade(start + "_both_train" + new_str + "/")
        predictions_grade(start + "_both_train_pruned" + new_str + "/")