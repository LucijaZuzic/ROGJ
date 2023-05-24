import os
import difflib
import subprocess

basedir = "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/"

excl_dirs = ["prvi", "hrt", "sz04", "sz08"]
okdirs = set() 
errorsdirs = set()

'''
dirnames_tmp = os.listdir(basedir + "outputs/")
for dirname in dirnames_tmp:
    if dirname != 'z04':
        excl_dirs.add(dirname)
        continue
''' 
def check_present(output_name): 

    dirnames = os.listdir(basedir + output_name)
 
    if len(dirnames) % 4 != 0:
        errorsdirs.add(output_name) 
    else:
        okdirs.add(output_name)
            
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
print(len(okdirs))

print(len(os.listdir(basedir + "/all_outputs")))

for x in os.listdir(basedir + "/all_outputs"):
    if "all_outputs/" + x + "/" not in okdirs:
        print(x)  

for x in okdirs:
    if len(os.listdir(basedir + x)) != 56:
        print(x)
        print(len(os.listdir(basedir + x)))

print(os.listdir(basedir + "/all_outputs/outputs4_only_weather_train1"))