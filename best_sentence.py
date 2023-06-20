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

    dirnames = os.listdir(basedir + output_name)
    maxrat = 0
    minrat = 1
    maxfilename = ""
    maxoriginal = ""
    maxnew = ""
    minfilename = ""
    minoriginal = ""
    minnew = ""
    
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
            
            sim_rat = s.ratio()
            
            if sim_rat > maxrat or (sim_rat == maxrat and len(line_original) + len(line_new) > len(maxoriginal) + len(maxnew)):
            	maxrat = sim_rat
            	maxoriginal = line_original
            	maxnew = line_new
            	maxfilename = dirname + "/" + filename
            	
            if sim_rat < minrat or (sim_rat == maxrat and len(line_original) + len(line_new) > len(minoriginal) + len(minnew)):
            	minrat = sim_rat
            	minoriginal = line_original
            	minnew = line_new
            	minfilename = dirname + "/" + filename
            	
    print(minfilename)
    print(minrat)
    print(minoriginal)
    print(minnew)
    print(maxfilename)
    print(maxrat)
    print(maxoriginal)
    print(maxnew)
    
bets_for_dir = [11, 15, 13, 15, 13, 13, 13]

ind = -1
for dirs_to_include in ["z04", "VremenskaPrognoza", "a", "prvi", "hrt", "sz04", "sz08"]:
	
    excl_dirs = set() 
    ind += 1

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

    num2 = 9

    #for num in [8, 7, 11, 10, 13, 15]:
    for num in [bets_for_dir[ind]]:
        start = "all_outputs/outputs" + str(num)

        files_train = open(basedir + "my_db" + str(num2) + "_train.fileids", "r")
        train_files_list = files_train.readlines()
        for i in range(len(train_files_list)):
            train_files_list[i] = train_files_list[i].replace("\n", "").split("/")[1]
        files_train.close()
	
        new_str = str(num)
	
        print(dirs_to_include, num)
        predictions_grade(start + "_both_train" + new_str + "/")           
