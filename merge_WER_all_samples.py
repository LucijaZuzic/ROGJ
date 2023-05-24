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

def open_table(file_name):
    min_row = []
    min_col = []
    min_row_text = []
    min_col_text = []
    min_val = -1
    file_open = open(file_name, "r")
    file_text = file_open.readlines()
    file_open.close()
    string_to_print = [] 
    for i in range(len(file_text)): 
        file_text[i] = file_text[i].replace("\n", "").split(";")
        new_line = []
        for j in range(len(file_text[i])):
            new_line.append(file_text[i][j])
        string_line_array = []
        for j in range(len(new_line)): 
            string_line_array.append(str(new_line[j]))  
        string_to_print.append(string_line_array) 
    return string_to_print
    
def add_tables(tables_to_add): 
    table_res = []
    for i in range(len(tables_to_add[0])):
        new_row = []
        for j in range(len(tables_to_add[0][i])):
            new_row.append(tables_to_add[0][i][j])
        table_res.append(new_row)
        
    for k in range(1, len(tables_to_add)):  
        for i in range(len(tables_to_add[k])):
            for j in range(len(tables_to_add[k][i])):
                if str(tables_to_add[k][i][j])[0].isdigit():
                    table_res[i][j] = int(table_res[i][j]) + int(tables_to_add[k][i][j])
    return table_res  
     
def duplicate_table(tables_dup): 
    table_res = []
    for i in range(len(tables_dup)):
        new_row = []
        for j in range(len(tables_dup[i])):
            new_row.append(tables_dup[i][j])
        table_res.append(new_row) 
    return table_res 
    
def divide_tables(tables_to_divide): 
    for k in range(1, len(tables_to_divide)):  
        for i in range(len(tables_to_divide[k])):
            for j in range(len(tables_to_divide[k][i])):
                if str(tables_to_divide[k][i][j])[0].isdigit():
                    if int(tables_to_divide[0][i][j]) != 0:
                        tables_to_divide[k][i][j] = float(tables_to_divide[k][i][j]) * 100 / float(tables_to_divide[0][i][j])
                    else:
                        tables_to_divide[k][i][j] = float(100)
    return tables_to_divide 
    
def WIL_tables(Tok, Ti, Ts, Td): 
    table_res = []
    for i in range(len(Tok)):
        new_row = []
        for j in range(len(Tok[i])):
            if str(Tok[i][j])[0].isdigit(): 
                down = (float(Tok[i][j]) + float(Ts[i][j]) + float(Td[i][j])) * (float(Tok[i][j]) + float(Ts[i][j]) + float(Ti[i][j]))
                up = down - float(Tok[i][j]) ** 2
                new_row.append(up / down * 100)
            else:
                new_row.append(Tok[i][j])
        table_res.append(new_row) 
    return table_res  
     
def string_array_to_csv(table_string):
    string_table = ""
    for i in range(len(table_string)):
        for j in range(len(table_string[i])):
            string_table += str(table_string[i][j])
            if j == len(table_string[i]) - 1:
                if i != len(table_string) - 1:
                    string_table += "\n"
            else:
                string_table += ";"
    return(string_table)
 
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
    
file_phones = open(basedir + "my_db14.phone", "r")
lines_phone = file_phones.readlines()
file_phones.close()

all_phones = [' ']
for line_phone in lines_phone:
    if line_phone[0].upper() == line_phone[0]:
        continue
    all_phones.append(line_phone.replace("\n", "")) 
    
dirs = ["z04", "VremenskaPrognoza", "a", "prvi", "hrt", "sz04", "sz08"] 
    
tables_ok = []
tables_ins = []
tables_del = []
tables_sub = [] 
tables_notok = []
tables_all = []
for dirs_to_include in dirs: 
    filename_table_corr = basedir + "all_results/" + dirs_to_include + " Točne riječi.csv" 
    table_new_corr = open_table(filename_table_corr) 
    #print(table_new_corr)
    tables_ok.append(table_new_corr) 
    tables_all.append(table_new_corr) 
    filename_table_incorr = basedir + "all_results/" + dirs_to_include + " Netočne riječi.csv" 
    table_new_incorr = open_table(filename_table_incorr) 
    #print(table_new_incorr) 
    tables_notok.append(table_new_incorr) 
    tables_all.append(table_new_incorr) 
    filename_table_sub = basedir + "all_results/" + dirs_to_include +  " Zamijenjene riječi.csv" 
    table_new_sub = open_table(filename_table_sub) 
    #print(table_new_sub) 
    tables_sub.append(table_new_sub) 
    filename_table_ins = basedir + "all_results/" + dirs_to_include + " Dodane riječi.csv" 
    table_new_ins = open_table(filename_table_ins) 
    #print(table_new_ins) 
    tables_ins.append(table_new_ins) 
    filename_table_del = basedir + "all_results/" + dirs_to_include + " Ispuštene riječi.csv" 
    table_new_del = open_table(filename_table_del) 
    #print(table_new_del) 
    tables_del.append(table_new_del) 
ok_tables = add_tables(tables_ok)
#print(ok_tables) 
notok_tables = add_tables(tables_notok)
#print(notok_tables) 
all_tables = add_tables(tables_all)
#print(all_tables) 
sub_tables = add_tables(tables_sub)
#print(sub_tables) 
ins_tables = add_tables(tables_ins)
#print(ins_tables) 
del_tables = add_tables(tables_del)
#print(del_tables) 
divided_tables_ok = [all_tables, duplicate_table(ok_tables)] 
divided_table_ok_res = divide_tables(divided_tables_ok)
#print(divided_table_ok_res) 
divided_tables_notok = [all_tables, duplicate_table(notok_tables)] 
divided_table_notok_res = divide_tables(divided_tables_notok)
#print(divided_table_notok_res) 
divided_tables_ins = [all_tables, duplicate_table(ins_tables)] 
divided_table_ins_res = divide_tables(divided_tables_ins)
#print(divided_table_ins_res) 
divided_tables_sub = [all_tables, duplicate_table(sub_tables)] 
divided_table_sub_res = divide_tables(divided_tables_sub)
#print(divided_table_sub_res) 
divided_tables_del = [all_tables, duplicate_table(del_tables)] 
divided_table_del_res = divide_tables(divided_tables_del)
#print(divided_table_del_res)  
tables_percent = [divided_table_del_res, divided_table_ins_res, divided_table_sub_res, divided_table_ok_res, divided_table_notok_res]
tables_number = [del_tables, ins_tables, sub_tables, ok_tables, notok_tables]

WIL_table = WIL_tables(duplicate_table(ok_tables), duplicate_table(ins_tables), duplicate_table(sub_tables), duplicate_table(del_tables))
res_table = string_array_to_csv(WIL_table) 
filename_table = basedir + "all_results/All dirs WIL.csv" 
#print(res_table)
#print(filename_table)
print(WIL_table)
file_open = open(filename_table, "w")
file_open.write(res_table)
file_open.close() 

WER_up_tables = add_tables([duplicate_table(sub_tables), duplicate_table(ins_tables), duplicate_table(del_tables)])
WER_down_tables = add_tables([duplicate_table(sub_tables), duplicate_table(ok_tables), duplicate_table(del_tables)])
WER_tables = divide_tables([duplicate_table(WER_down_tables), duplicate_table(WER_up_tables)])

res_table = string_array_to_csv(WER_tables[1]) 
filename_table = basedir + "all_results/All dirs WER.csv" 
#print(res_table)
#print(filename_table)
print(WER_tables[1])
file_open = open(filename_table, "w")
file_open.write(res_table)
file_open.close()  

MER_up_tables = add_tables([duplicate_table(sub_tables), duplicate_table(ins_tables), duplicate_table(del_tables)])
MER_down_tables = add_tables([duplicate_table(sub_tables), duplicate_table(ok_tables), duplicate_table(del_tables), duplicate_table(ins_tables)])
MER_tables = divide_tables([duplicate_table(MER_down_tables), duplicate_table(MER_up_tables)])

res_table = string_array_to_csv(MER_tables[1]) 
filename_table = basedir + "all_results/All dirs MER.csv" 
#print(res_table)
#print(filename_table)
print(MER_tables[1])
file_open = open(filename_table, "w")
file_open.write(res_table)
file_open.close()  

WC_up_tables = add_tables([duplicate_table(ok_tables), duplicate_table(ins_tables)])
WC_down_tables = add_tables([duplicate_table(sub_tables), duplicate_table(ok_tables), duplicate_table(del_tables), duplicate_table(ins_tables)])
WC_tables = divide_tables([duplicate_table(WC_down_tables), duplicate_table(WC_up_tables)])

res_table = string_array_to_csv(WC_tables[1]) 
filename_table = basedir + "all_results/All dirs WC.csv" 
#print(res_table)
#print(filename_table)
print(WC_tables[1])
file_open = open(filename_table, "w")
file_open.write(res_table)
file_open.close()  

WA_up_tables = add_tables([duplicate_table(ok_tables)])
WA_down_tables = add_tables([duplicate_table(sub_tables), duplicate_table(ok_tables), duplicate_table(del_tables), duplicate_table(ins_tables)])
WA_tables = divide_tables([duplicate_table(WA_down_tables), duplicate_table(WA_up_tables)])

res_table = string_array_to_csv(WA_tables[1]) 
filename_table = basedir + "all_results/All dirs WA.csv" 
#print(res_table)
#print(filename_table)
print(WC_tables[1])
file_open = open(filename_table, "w")
file_open.write(res_table)
file_open.close()  

names = ["Ispuštene", "Dodane", "Zamijenjene", "Točne", "Netočne"]
for num in range(len(names)):
    for table_ind in range(len(tables_percent[num][1:])):
        res_table = string_array_to_csv(tables_percent[num][table_ind + 1]) 
        filename_table = basedir + "all_results/All dirs " + names[num] + " riječi postotak.csv" 
        #print(res_table)
        #print(filename_table)
        file_open = open(filename_table, "w")
        file_open.write(res_table)
        file_open.close()   
    for table_ind in range(len(tables_number[num])):
        res_table = string_array_to_csv(tables_number[num]) 
        filename_table = basedir + "all_results/All dirs " + names[num] + " riječi.csv" 
        #print(res_table)
        #print(filename_table)
        file_open = open(filename_table, "w")
        file_open.write(res_table)
        file_open.close()    
