import os
import difflib
import subprocess

basedir = "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/"

excl_dirs = ["prvi", "hrt", "sz04", "sz08"]
errorsdirs = set()

'''
dirnames_tmp = os.listdir(basedir + "outputs/")
for dirname in dirnames_tmp:
    if dirname != 'z04':
        excl_dirs.add(dirname)
        continue
'''

def predictions_grade(output_name): 

    dirnames = os.listdir(basedir + output_name)
    for dirname in dirnames:
        if dirname not in excl_dirs:
            continue
        if output_name + "/" + dirname not in errorsdirs:
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

def check_present(output_name): 

    dirnames = os.listdir(basedir + output_name)
    for dirname in dirnames:
        if dirname not in excl_dirs:
            continue
        filenames = os.listdir(basedir + output_name + "/" + dirname)

        compare = False
        
        for filename in filenames:
            
            if filename.count("compare") > 0:
                compare = True
                break

        if not compare:
            errorsdirs.add(output_name + "/" + dirname)
            
        '''
        for filename in filenames:

            if filename.replace(".txt", "") in train_files_list:
                continue  

            if filename.count("compare") > 0:
                continue

            if filename.count("new") > 0:
                continue

            if filename.count("original") > 0:
                continue 

            compare_filename_to_open = basedir + output_name + "/" + dirname + "/" + filename.replace(".txt", "_compare.txt")

            if not os.path.isfile(compare_filename_to_open):
                errorsdirs.add(output_name + "/" + dirname)
        '''

            
for num in ["", 3, 7, 8, 9, 10, 11, 12, 13, 14]:
    start = "all_outputs/outputs" + str(num)

    files_train = open(basedir + "my_db" + str(num) + "_train.fileids", "r")
    train_files_list = files_train.readlines()
    for i in range(len(train_files_list)):
        train_files_list[i] = train_files_list[i].replace("\n", "").split("/")[1]
    files_train.close() 

    check_present(start + "/")
    check_present(start + "_pruned/")
    check_present(start + "_only_weather/")
    check_present(start + "_only_weather_pruned/")
    check_present(start + "_both/")
    check_present(start + "_both_pruned/")

    for new_num in ["", 2, 3, 1, 4, 7, 8, 9, 10, 11, 12, 13, 14]:
        new_str = str(new_num)

        check_present(start + "_only_weather_train" + new_str + "/")
        check_present(start + "_only_weather_train_pruned" + new_str + "/")

        check_present(start + "_both_train" + new_str + "/")
        check_present(start + "_both_train_pruned" + new_str + "/")

print(errorsdirs)  

for num in ["", 3, 7, 8, 9, 10, 11, 12, 13, 14]:
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

    for new_num in ["", 2, 3, 1, 4, 7, 8, 9, 10, 11, 12, 13, 14]:
        new_str = str(new_num)

        predictions_grade(start + "_only_weather_train" + new_str + "/")
        predictions_grade(start + "_only_weather_train_pruned" + new_str + "/")

        predictions_grade(start + "_both_train" + new_str + "/")
        predictions_grade(start + "_both_train_pruned" + new_str + "/")

print(errorsdirs)