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

def find_val_phone(dirinclude, tablevalues, acoustic, linguistic, decimalpl):
    string_new = "Char;"
    for tablevalue in tablevalues:
        string_new += tablevalue + ";"
    string_new = string_new[:-1] 
    for phone in all_phones:
        string_new += "\n" + phone
        for tablevalue in tablevalues:
            filename_table = basedir + "all_results/" + dirinclude + " " + phone + " " + tablevalue + ".csv"
            df = pd.read_csv(filename_table, sep = ";")

            firstrow = []
            for x in df.head():
                firstrow.append(x) 

            firstcol = []
            for x in df['Acoustic model'] :
                firstcol.append(x)  

            for i in range(len(firstcol)): 
                rowname = firstcol[i]  
                for colname in firstrow[1:]:  
                    if rowname == linguistic and colname == acoustic: 
                            string_new += ";" + str(round(float(df[colname][i]), decimalpl)) 

    #print(string_new)
    return string_new

def find_val_row(dirinclude, tablevalues, acoustic, linguistic, decimalpl):
    string_new = "Char;" 
    for tablevalue in tablevalues:
        string_new += tablevalue + ";"
    string_new = string_new[:-1] 

    for phone in all_phones:
        if phone == " ":
            continue
            
        sum_rows = []  
        string_new += "\n" + phone  
        sum_letter = 0 
        
        for tablevalue in tablevalues:
            sum_rows.append(0) 

            filename_table_absolute = basedir + "all_results/" + dirinclude + " " + tablevalue + ".csv"
            df_absolute = pd.read_csv(filename_table_absolute, sep = ";")

            firstrow_absolute = []
            for x in df_absolute.head():
                firstrow_absolute.append(x) 

            firstcol_absolute = []
            for x in df_absolute['Acoustic model'] :
                firstcol_absolute.append(x)  

            division_value = 1
            for i in range(len(firstcol_absolute)): 
                rowname_absolute = firstcol_absolute[i]  
                for colname_absolute in firstrow_absolute[1:]:  
                    if rowname_absolute == linguistic and colname_absolute == acoustic:
                        division_value = df_absolute[colname_absolute][i] 
                        
            filename_table_sp = basedir + "all_results/" + dirinclude  + " " + " " + " " + tablevalue + ".csv"
            df_sp = pd.read_csv(filename_table_sp, sep = ";")

            firstrow_sp = []
            for x in df_sp.head():
                firstrow_sp.append(x) 

            firstcol_sp = []
            for x in df_sp['Acoustic model'] :
                firstcol_sp.append(x)  

            division_value_sp = 1
            for i in range(len(firstcol_sp)): 
                rowname_sp = firstcol_sp[i]  
                for colname_sp in firstrow_sp[1:]:  
                    if rowname_sp == linguistic and colname_sp == acoustic:
                        division_value_sp = df_sp[colname_sp][i] 

            filename_table = basedir + "all_results/" + dirinclude + " " + phone + " " + tablevalue + ".csv"
            df = pd.read_csv(filename_table, sep = ";")

            firstrow = []
            for x in df.head():
                firstrow.append(x) 

            firstcol = []
            for x in df['Acoustic model'] :
                firstcol.append(x)  

            for i in range(len(firstcol)): 
                rowname = firstcol[i]  
                for colname in firstrow[1:]:  
                    if rowname == linguistic and colname == acoustic:
                        sum_letter += df[colname][i] 
                        if division_value != division_value_sp:
                            string_new += ";" + str(round(float(df[colname][i] / (division_value - division_value_sp) * 100), decimalpl)) 
                        else:
                            string_new += ";" + str(round(0, decimalpl)) 
                        sum_rows[-1] += df[colname][i] 
        
    #print(string_new) 
    return string_new

def find_val_table(dirinclude, tablevalues, acoustic, linguistic, decimalpl):
    string_new = "Char;" 
    for tablevalue in tablevalues:
        string_new += tablevalue + ";"
    string_new = string_new[:-1] 

    for phone in all_phones:
        if phone == " ":
            continue
            
        sum_rows = []  
        sum_letter = 0 
        sum_div_vals = 0 
        for tablevalue in tablevalues:
            sum_rows.append(0) 

            filename_table_absolute = basedir + "all_results/" + dirinclude + " " + tablevalue + ".csv"
            df_absolute = pd.read_csv(filename_table_absolute, sep = ";")

            firstrow_absolute = []
            for x in df_absolute.head():
                firstrow_absolute.append(x) 

            firstcol_absolute = []
            for x in df_absolute['Acoustic model'] :
                firstcol_absolute.append(x)  

            division_value = 1
            for i in range(len(firstcol_absolute)): 
                rowname_absolute = firstcol_absolute[i]  
                for colname_absolute in firstrow_absolute[1:]:  
                    if rowname_absolute == linguistic and colname_absolute == acoustic:
                        division_value = df_absolute[colname_absolute][i]
                        sum_div_vals += division_value 
                        
            filename_table = basedir + "all_results/" + dirinclude + " " + phone + " " + tablevalue + ".csv"
            df = pd.read_csv(filename_table, sep = ";")

            firstrow = []
            for x in df.head():
                firstrow.append(x) 

            firstcol = []
            for x in df['Acoustic model'] :
                firstcol.append(x)  

            for i in range(len(firstcol)): 
                rowname = firstcol[i]  
                for colname in firstrow[1:]:  
                    if rowname == linguistic and colname == acoustic:
                        sum_letter += df[colname][i] 
                        sum_rows[-1] += df[colname][i]

        string_new += "\n" + phone  
        for x in sum_rows:
            string_new += ";" + str(round(float(x / sum_div_vals * 100), decimalpl)) 
        
    #print(string_new)
    return string_new
    
def string_array_to_latex(table_string):  
    string_table = "\\begin{tabular}{"
    for x in range(len(table_string[0]) * 2):
        string_table += "|c"
    string_table += "|}\n\\hline\n" 
    for i in range(len(table_string) // 2 + 1): 
        for j in range(len(table_string[i])):
            string_table += str(table_string[i][j]) + " & "
        if i == 0:
            for j in range(len(table_string[i])):
                string_table += str(table_string[i][j])
                if j == len(table_string[i]) - 1: 
                    string_table += " \\\\ \\hline \n"
                else:
                    string_table += " & "
            continue 
        if i == 1 and len(table_string) % 2 == 0:
            for j in range(len(table_string[i])):
                string_table += ""
                if j == len(table_string[i]) - 1: 
                    string_table += " \\\\ \\hline \n"
                else:
                    string_table += " & "
            continue 
        if i > 0 and i + len(table_string) // 2 - 1 < len(table_string) and len(table_string) % 2 == 0:
            for j in range(len(table_string[i + len(table_string) // 2 - 1])):
                string_table += str(table_string[i + len(table_string) // 2 - 1][j])
                if j == len(table_string[i + len(table_string) // 2 - 1]) - 1: 
                    string_table += " \\\\ \\hline \n"
                else:
                    string_table += " & " 
        if i > 0 and i + len(table_string) // 2 < len(table_string) and len(table_string) % 2 != 0:
            for j in range(len(table_string[i + len(table_string) // 2])):
                string_table += str(table_string[i + len(table_string) // 2][j])
                if j == len(table_string[i + len(table_string) // 2]) - 1: 
                    string_table += " \\\\ \\hline \n"
                else:
                    string_table += " & "
    return(string_table + "\\end{tabular}")
   
dict_vals_letters = ["Točni znakovi", "Točni znakovi postotak", 
        "Netočni znakovi", "Netočni znakovi postotak",  
        "Dodani znakovi", "Dodani znakovi postotak", 
        "Ispušteni znakovi", "Ispušteni znakovi postotak",  
        "Zamijenjeni znakovi", "Zamijenjeni znakovi postotak",  
        "Equal ALIGN", "Equal ALIGN postotak",   
        "Incorrect ALIGN", "Incorrect ALIGN postotak", 
        "Insertions ALIGN", "Insertions ALIGN postotak", 
        "Deletions ALIGN", "Deletions ALIGN postotak", 
        "Substitutions ALIGN", "Substitutions ALIGN postotak"]  
        
def merge_two_tables(t1, t2):
    t1_lines = t1.split("\n")
    t2_lines = t2.split("\n")
    new_lines = ""
    for t_indeks in range(len(t2_lines)):
    	if t_indeks > 1 and t_indeks != len(t2_lines) - 1:
    	    new_line = t1_lines[t_indeks].replace("\\\\ \\hline", "&") + t2_lines[t_indeks]
    	else:
    	    if t_indeks == 0:
    	        new_line = t1_lines[t_indeks].replace("|}", "|") + t2_lines[t_indeks].replace("\\begin{tabular}{|", "") 
    	    else:
    	        new_line = t1_lines[t_indeks]
    	new_lines += new_line 
    	if  t_indeks != len(t2_lines) - 1:
    	    new_lines += "\n" 
    return new_lines 

dict_vals_letters1 = ["Točni znakovi postotak", "Dodani znakovi postotak", "Ispušteni znakovi postotak", "Zamijenjeni znakovi postotak"]
dict_vals_letters2 = ["Equal ALIGN postotak", "Insertions ALIGN postotak", "Deletions ALIGN postotak", "Substitutions ALIGN postotak"]

dict_vals_letters3 = ["Točni znakovi", "Dodani znakovi", "Ispušteni znakovi", "Zamijenjeni znakovi"]
dict_vals_letters4 = ["Equal ALIGN", "Insertions ALIGN", "Deletions ALIGN", "Substitutions ALIGN"]

dict_vals_letters5 = ["Equal ALIGN postotak", "Točni znakovi postotak"]
dict_vals_letters6 = ["Equal ALIGN", "Točni znakovi"]

dict_vals_letters7 = ["Točni znakovi postotak"]
dict_vals_letters7 = ["Svi znakovi", "Točni znakovi postotak"]
dict_vals_letters8 = ["Svi znakovi"]

dirs = ["z04", "VremenskaPrognoza", "a", "prvi", "hrt", "sz04", "sz08"]
niz = ["Expanded weather and alka", "Expanded no TV", "Expanded all sources", "Expanded no TV", "Expanded all sources", "Expanded all sources", "Expanded all sources"]

decimalplace = 2

returned_table = ""

for i in range(len(dirs) // 4 + 1):
    print(dirs[i])
    retval = find_val_phone(dirs[i], dict_vals_letters7, niz[i], niz[i], decimalplace)
    #retval = find_val_row(dirs[i], dict_vals_letters8, niz[i], niz[i], decimalplace)
    #retval = find_val_table(dirs[i], dict_vals_letters8, niz[i], niz[i], decimalplace)
    retval = retval.split("\n")
    for j in range(len(retval)):
        retval[j] = retval[j].replace("\n", "").split(";")
    #print(string_array_to_latex(retval))
    if returned_table == "":
        returned_table = string_array_to_latex(retval)
    else:
        returned_table = merge_two_tables(returned_table, string_array_to_latex(retval))
    #print(retval) 
print(returned_table)

returned_table = ""

for i in range(len(dirs) // 4 + 1, (len(dirs) // 4 + 1) * 2):
    print(dirs[i])
    retval = find_val_phone(dirs[i], dict_vals_letters7, niz[i], niz[i], decimalplace)
    #retval = find_val_row(dirs[i], dict_vals_letters8, niz[i], niz[i], decimalplace)
    #retval = find_val_table(dirs[i], dict_vals_letters8, niz[i], niz[i], decimalplace)
    retval = retval.split("\n")
    for j in range(len(retval)):
        retval[j] = retval[j].replace("\n", "").split(";")
    #print(string_array_to_latex(retval))
    if returned_table == "":
        returned_table = string_array_to_latex(retval)
    else:
        returned_table = merge_two_tables(returned_table, string_array_to_latex(retval))
    #print(retval) 
print(returned_table)

returned_table = ""

for i in range((len(dirs) // 4 + 1) * 2, (len(dirs) // 4 + 1) * 3):
    print(dirs[i])
    retval = find_val_phone(dirs[i], dict_vals_letters7, niz[i], niz[i], decimalplace)
    #retval = find_val_row(dirs[i], dict_vals_letters8, niz[i], niz[i], decimalplace)
    #retval = find_val_table(dirs[i], dict_vals_letters8, niz[i], niz[i], decimalplace)
    retval = retval.split("\n")
    for j in range(len(retval)):
        retval[j] = retval[j].replace("\n", "").split(";")
    #print(string_array_to_latex(retval))
    if returned_table == "":
        returned_table = string_array_to_latex(retval)
    else:
        returned_table = merge_two_tables(returned_table, string_array_to_latex(retval))
    #print(retval) 
print(returned_table)

returned_table = ""

for i in range((len(dirs) // 4 + 1) * 3, len(dirs)):
    print(dirs[i])
    retval = find_val_phone(dirs[i], dict_vals_letters7, niz[i], niz[i], decimalplace)
    #retval = find_val_row(dirs[i], dict_vals_letters8, niz[i], niz[i], decimalplace)
    #retval = find_val_table(dirs[i], dict_vals_letters8, niz[i], niz[i], decimalplace)
    retval = retval.split("\n")
    for j in range(len(retval)):
        retval[j] = retval[j].replace("\n", "").split(";")
    #print(string_array_to_latex(retval))
    if returned_table == "":
        returned_table = string_array_to_latex(retval)
    else:
        returned_table = merge_two_tables(returned_table, string_array_to_latex(retval))
    #print(retval) 
 
retval = find_val_phone("All dirs", dict_vals_letters7, niz[6], niz[6], decimalplace)
#retval = find_val_row("All dirs", dict_vals_letters8, niz[6], niz[6], decimalplace)
#retval = find_val_table("All dirs", dict_vals_letters8, niz[6], niz[6], decimalplace)
retval = retval.split("\n")
for j in range(len(retval)):
    retval[j] = retval[j].replace("\n", "").split(";")
#print(string_array_to_latex(retval))
if returned_table == "":
    returned_table = string_array_to_latex(retval)
else:
    returned_table = merge_two_tables(returned_table, string_array_to_latex(retval))
#print(string_array_to_latex(retval)) 

print(returned_table)
