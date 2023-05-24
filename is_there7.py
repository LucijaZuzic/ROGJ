import difflib
import subprocess
basedir = "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/"
a = "more na otvorenom pet do šest ponegdje neverini prvo na sjevernom jadranu"
b = "more na otvorenom pet do šest ponegdje neverini prvo na sjevernom jaka"
s = difflib.SequenceMatcher(None, a, b)
for tag, i1, i2, j1, j2 in s.get_opcodes():
    print('{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(
        tag, i1, i2, j1, j2, a[i1:i2], b[j1:j2]))
    
pipe = subprocess.Popen(['perl', basedir + "word_align.pl", basedir + "f1", basedir + "f2"], stdout=subprocess.PIPE)
x = str(pipe.stdout.read())
print(x)

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

errorsf = []

all_phones = [' ']
for line_phone in lines_phone:
    if line_phone[0].upper() == line_phone[0]:
        continue
    all_phones.append(line_phone.replace("\n", "")) 
 
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

            if filename.count("compare") > 0:
                continue

            if filename.count("new") > 0:
                continue

            if filename.count("original") > 0:
                continue
            
            compare_filename_to_open = basedir + output_name + dirname + "/" + filename.replace(".txt", "_compare.txt")
            if not os.path.isfile(compare_filename_to_open):
                print(compare_filename_to_open)
                errorsf.append(compare_filename_to_open)

all_dirs = os.listdir(basedir + "all_outputs/outputs/")
for dir_to_include in all_dirs: 

    excl_dirs = set() 
 
    for dirname in all_dirs: 
        if dirname != dir_to_include:
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

print(errorsf)