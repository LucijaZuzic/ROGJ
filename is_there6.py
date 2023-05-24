 
import os
import difflib
import subprocess

basedir = "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/"

all_dirs = os.listdir(basedir + "all_outputs/outputs/")
wrongd = set()
wrongdd = set()
wrongs = set()
oks = set()
def check_present(output_name, dirname, last_good): 
    filenames = os.listdir(basedir + output_name + dirname)
    
    for filename in filenames:
        
        if filename.count("compare") > 0:
            continue

        if filename.count("new") > 0:
            continue

        if filename.count("original") > 0:
            continue 

        compare_filename_to_open = basedir + output_name + dirname + "/" + filename.replace(".txt", "_compare.txt")
        
        if not os.path.isfile(compare_filename_to_open):
            wrongdd.add(output_name)
            wrongd.add(dirname)
            wrongs.add(basedir + output_name + dirname)
            return last_good
        else:
            oks.add(basedir + output_name + dirname) 
            return basedir + output_name + dirname  
         
    oks.add(basedir + output_name + dirname) 
    return basedir + output_name + dirname

def check_dirname(dirname):
    last_good = " "
    for num in ["", 3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
        start = "all_outputs/outputs" + str(num)

        files_train = open(basedir + "my_db" + str(num) + "_train.fileids", "r")
        train_files_list = files_train.readlines()
        for i in range(len(train_files_list)):
            train_files_list[i] = train_files_list[i].replace("\n", "").split("/")[1]
        files_train.close() 

        last_good = check_present(start + "/", dirname, last_good)
        last_good = check_present(start + "_pruned/", dirname, last_good)
        last_good = check_present(start + "_only_weather/", dirname, last_good)
        last_good = check_present(start + "_only_weather_pruned/", dirname, last_good)
        last_good = check_present(start + "_both/", dirname, last_good)
        last_good = check_present(start + "_both_pruned/", dirname, last_good)

        for new_num in ["", 2, 3, 1, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
            new_str = str(new_num)

            last_good = check_present(start + "_only_weather_train" + new_str + "/", dirname, last_good)
            last_good = check_present(start + "_only_weather_train_pruned" + new_str + "/", dirname, last_good)

            last_good = check_present(start + "_both_train" + new_str + "/", dirname, last_good)
            last_good = check_present(start + "_both_train_pruned" + new_str + "/", dirname, last_good)
    
    if last_good.count("outputs16_both_train_pruned16") == 0:
        print(dirname)
        print(last_good)  

for dirname in all_dirs:
    check_dirname(dirname)

print(wrongdd)
print(wrongd)  
print(len(wrongs))
print(len(oks))