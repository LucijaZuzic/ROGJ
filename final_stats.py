import os
import difflib
import subprocess
import pandas as pd
import numpy as np

basedir = "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/"
  
file_phones = open(basedir + "my_db14.phone", "r")
lines_phone = file_phones.readlines()
file_phones.close()

all_phones = [' ']
for line_phone in lines_phone:
    if line_phone[0].upper() == line_phone[0]:
        continue
    all_phones.append(line_phone.replace("\n", "")) 

def find_best(tablename, mode):
    df = pd.read_csv(tablename, sep = ";")
    firstrow = []
    for x in df.head():
        firstrow.append(x) 
    firstcol = []
    for x in df['Acoustic model'] :
        firstcol.append(x) 

    dict_best_acoustic = {}

    for name in firstrow[1:]: 
        somecol = df[name]
        bestval = max(somecol)
        bestindex = np.argmax(somecol)
        if mode == 'max':
            bestval = max(somecol)
            bestindex = np.argmax(somecol)
        else:
            bestval = min(somecol)
            bestindex = np.argmin(somecol) 
        #print(name, firstcol[bestindex], bestval) 
        if firstcol[bestindex] not in dict_best_acoustic:
            dict_best_acoustic[firstcol[bestindex]] = [name]
        else:
            dict_best_acoustic[firstcol[bestindex]].append(name)

    #for x in dict_best_acoustic: 
        #print(x, len(dict_best_acoustic[x])) 

    dict_best_linguistic = {}
    best_of_best_ling = firstrow[1]
    best_of_best_ac = firstcol[1]
    best_of_best = df[best_of_best_ling][0]
    ac_ling_metric = {}
    ac_metric = {}
    ling_metric = {}

    for i in range(len(firstcol)):
        valsrow = []
        rowname = firstcol[i]  
        for colname in firstrow[1:]:
            someval = float(df[colname][i])
            ac_ling_metric[(rowname, colname)] = someval
            if rowname in ac_metric:
                ac_metric[rowname] = max(ac_metric[rowname], someval)
            else:
                ac_metric[rowname] = someval
            if colname in ling_metric:
                ling_metric[colname] = max(ling_metric[colname], someval)
            else:
                ling_metric[colname] = someval
            if mode == 'max':
                if someval > best_of_best:
                    best_of_best_ling = colname
                    best_of_best_ac = rowname
                    best_of_best = someval
            else:
                if someval < best_of_best:
                    best_of_best_ling = colname
                    best_of_best_ac = rowname
                    best_of_best = someval
            valsrow.append(someval)

        bestval = max(valsrow)
        bestindex = np.argmax(valsrow)
        if mode == 'max':
            bestval = max(valsrow)
            bestindex = np.argmax(valsrow)
        else:
            bestval = min(valsrow)
            bestindex = np.argmin(valsrow) 
        #print(rowname, firstrow[bestindex], bestval) 
        if firstrow[bestindex] not in dict_best_linguistic:
            dict_best_linguistic[firstrow[bestindex]] = [rowname]
        else:
            dict_best_linguistic[firstrow[bestindex]].append(rowname)
            
    #for x in dict_best_linguistic:
        #print(x, len(dict_best_linguistic[x]))

    #print(best_of_best_ac, best_of_best_ling, best_of_best)

    return best_of_best_ac, best_of_best_ling, ac_ling_metric, ac_metric , ling_metric
  
dict_vals = {"Točne rečenice": "max", "Točne rečenice postotak": "max", "Netočne rečenice": "min", "Netočne rečenice postotak": "min", 
            "Točne riječi": "max", "Točne riječi postotak": "max", "Netočne riječi": "min", "Netočne riječi postotak": "min", 
            "Točne riječi inserted postotak": "max", "Netočne riječi inserted postotak": "min",
            "Zamijenjene riječi": "min", "Zamijenjene riječi postotak": "min", "Zamijenjene riječi inserted postotak": "min", 
            "Ispuštene riječi": "min", "Ispuštene riječi postotak": "min", "Ispuštene riječi inserted postotak": "min", 
            "Dodane riječi": "min", "Dodane riječi postotak": "min", "Dodane riječi inserted postotak": "min", "WER": "min", "MER": "min", "WIL": "min",  
            "Točni znakovi": "max", "Točni znakovi postotak": "max", "Netočni znakovi": "min", "Netočni znakovi postotak": "min", 
            "Dodani znakovi": "min", "Dodani znakovi postotak": "min", "Ispušteni znakovi": "min", "Ispušteni znakovi postotak": "min", 
            "Zamijenjeni znakovi": "min", "Zamijenjeni znakovi postotak": "min", "Equal ALIGN": "max", "Equal ALIGN postotak": "max",  
            "Incorrect ALIGN": "min", "Incorrect ALIGN postotak": "min", "Insertions ALIGN": "min", "Insertions ALIGN postotak": "min", 
            "Deletions ALIGN": "min", "Deletions ALIGN postotak": "min", "Substitutions ALIGN": "min", "Substitutions ALIGN postotak": "min",  
            "Ratio": "max", "Ratio postotak": "max", "Total words": "nan", "Correct words": "max", "Errors": "min", "Percent correct": "max", 
            "Error": "min", "Accuracy": "max", "Insertions": "min", "Substitutions": "min", "Deletions": "min", "Correct sentences": "max", 
            "Incorrect sentences": "min", "Word error rate": "min", "Sentence error rate": "min"}
             
dict_vals_letters = {}

dict_vals_all = dict_vals

for phone in all_phones:
 
    dict_vals_letters =  dict_vals_letters | {phone + " Točni znakovi": "max", phone + " Točni znakovi postotak": "max", 
        phone + " Netočni znakovi": "min", phone + " Netočni znakovi postotak": "min",  
        phone + " Dodani znakovi": "min", phone + " Dodani znakovi postotak": "min", 
        phone + " Ispušteni znakovi": "min", phone + " Ispušteni znakovi postotak": "min",  
        phone + " Zamijenjeni znakovi": "min", phone + " Zamijenjeni znakovi postotak": "min",  
        phone + " Equal ALIGN": "max", phone + " Equal ALIGN postotak": "max",   
        phone + " Incorrect ALIGN": "min", phone + " Incorrect ALIGN postotak": "min", 
        phone + " Insertions ALIGN": "min", phone + " Insertions ALIGN postotak": "min", 
        phone + " Deletions ALIGN": "min", phone + " Deletions ALIGN postotak": "min", 
        phone + " Substitutions ALIGN": "min", phone + " Substitutions ALIGN postotak": "min"} 
    
    dict_vals_all = dict_vals_all | dict_vals_letters

letter_success = {}

for dirs_to_include in ["z04", "VremenskaPrognoza", "a", "prvi", "hrt", "sz04", "sz08"]: 
    best_ac = {}
    best_ling = {}   
    ac_ling_dir = {} 
    ac_dir = {} 
    ling_dir = {}
    for table_value in dict_vals_all:
        
        filename_table = basedir + "all_results/" + dirs_to_include + " " + table_value + ".csv"
        file_table = open(filename_table, "r")
        string_table = file_table.readlines()
        file_table.close()
        
        x = "All sources;All sources pruned;Wikipedia and all sources;Wikipedia and all sources pruned"
        string_table[0] = string_table[0].replace("Wikipedia and alka pruned;" + x,
                 "Wikipedia and alka pruned;" + x.replace("all", "expanded all").replace("All", "Expanded all") + ";" + x)
        
        x1 = "Weather with test;Weather with test pruned;Wikipedia and weather with test;Wikipedia and weather with test pruned;"
        x2 = "Weather;Weather pruned;Wikipedia and weather;Wikipedia and weather pruned;" 
        string_table[0] = string_table[0].replace(x1 + x2,
                                x1 + x2.replace("eather", "eather original")) 
        
        x3 = "New source;New source pruned;Wikipedia, weather and new source;Wikipedia, weather and new source pruned;"
        string_table[0] = string_table[0].replace(x3,
                                x3.replace("source", "source original")) 

        new_text = ""
        for s in string_table:
            new_text += s   

        file_table = open(filename_table, "w")
        file_table.write(new_text)
        file_table.close() 

    for table_value in dict_vals: 
        filename_table = basedir + "all_results/" + dirs_to_include + " " + table_value + ".csv"
        file_table = open(filename_table, "r")
        string_table = file_table.readlines()
        file_table.close() 
        ba, bl, ac_ling_dir[table_value], ac_dir[table_value], ling_dir[table_value] = find_best(filename_table, dict_vals[table_value]) 
        
        if ba in best_ac:
            best_ac[ba].append(table_value)
        else:
            best_ac[ba] = [table_value]

        if bl in best_ling:
            best_ling[bl].append(table_value)
        else:
            best_ling[bl] = [table_value]

    maxiac = 0
    allac = 0
    selected_ac = "" 
    #print("Ac")
    for x in best_ac:
        #print(x, len(best_ac[x])) 
        allac += len(best_ac[x])
        if len(best_ac[x]) > maxiac:
            selected_ac = x
            maxiac = len(best_ac[x])

    maxiling = 0
    allling = 0
    selected_ling = "" 
    #print("Ling")
    #for x in sorted(best_ling.items(), key=lambda y:len(y[1])):
    for x in best_ling: 
        allling += len(best_ling[x])
        if len(best_ling[x]) > maxiling:
            selected_ling = x
            maxiling = len(best_ling[x])
  
    print(dirs_to_include, maxiac, "/", allac, selected_ac, maxiling, "/", allling, selected_ling) 

    if "Expanded all sources" in best_ac and "Expanded all sources" in best_ling: 
        print(len(best_ac["Expanded all sources"]), len(best_ling["Expanded all sources"]))

    #for table_value in dict_vals:  
    for table_value in ["WER", "MER", "WIL"]:  
        val_ac_ling_dir = -1
        val_ac_dir = -1
        val_ling_dir = -1
        counter_model = 0
        for amodel in ac_dir["Točne rečenice"].keys():
            for lmodel in ling_dir["Točne rečenice"].keys():
                    #print(ac_ling_dir[table_value][(amodel, lmodel)], ac_dir[table_value][amodel], ling_dir[table_value][lmodel])
                    if counter_model == 0: 
                        val_ac_ling_dir = ac_ling_dir[table_value][(amodel, lmodel)] 
                        val_ac_dir = ac_dir[table_value][amodel] 
                        val_ling_dir = ling_dir[table_value][lmodel] 
                        counter_model = 1
                    else:
                        if dict_vals[table_value] == 'max':
                            val_ac_ling_dir = max(val_ac_ling_dir, ac_ling_dir[table_value][(amodel, lmodel)])
                            val_ac_dir = max(val_ac_dir, ac_dir[table_value][amodel])
                            val_ling_dir = max(val_ling_dir, ling_dir[table_value][lmodel])
                        else:
                            val_ac_ling_dir = min(val_ac_ling_dir, ac_ling_dir[table_value][(amodel, lmodel)])
                            val_ac_dir = min(val_ac_dir, ac_dir[table_value][amodel])
                            val_ling_dir = min(val_ling_dir, ling_dir[table_value][lmodel]) 
                    break        
        print(ac_ling_dir[table_value][("Expanded no TV", "Expanded no TV")], ac_dir[table_value]["Expanded no TV"], ling_dir[table_value]["Expanded no TV"]) 
        print(ac_ling_dir[table_value][("Expanded all sources", "Expanded all sources")], ac_dir[table_value]["Expanded all sources"], ling_dir[table_value]["Expanded all sources"])
        print(table_value, val_ac_ling_dir, val_ac_dir, val_ling_dir)