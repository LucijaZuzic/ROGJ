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
                if tables_to_add[k][i][j][0].isdigit():
                    table_res[i][j] = int(table_res[i][j]) + int(tables_to_add[k][i][j])
    return table_res  
    
def divide_tables(tables_to_divide): 
    for k in range(1, len(tables_to_divide)):  
        for i in range(len(tables_to_divide[k])):
            for j in range(len(tables_to_divide[k][i])):
                if str(tables_to_divide[k][i][j])[0].isdigit():
                    if int(tables_to_divide[0][i][j]) != 0:
                        tables_to_divide[k][i][j] = 100 - float(tables_to_divide[k][i][j]) * 100 / float(tables_to_divide[0][i][j])
                    else:
                        tables_to_divide[k][i][j] = float(100)
    return tables_to_divide
    
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
 
dirs = ["z04", "VremenskaPrognoza", "a", "prvi", "hrt", "sz04", "sz08"] 
 
dict_vals_letters = ["Zamijenjene riječi", "Ispuštene riječi", "Dodane riječi"] 
table_correct_name = "Točne riječi" 
    
for dirs_to_include in dirs:   
    print(dirs_to_include, "Started")
    tables_add = []
    for table_value in dict_vals_letters:  
            filename_table = basedir + "all_results/" + dirs_to_include + " " + table_value + ".csv" 
            table_new = open_table(filename_table) 
            #print(table_new)
            tables_add.append(table_new)
    added_tables_WA = add_tables(tables_add)
    #print(added_tables_WA)
    added_tables_WC = add_tables(tables_add[:-1])
    #print(added_tables_WC)
    filename_table_correct = basedir + "all_results/" + dirs_to_include + " " + table_correct_name + ".csv" 
    table_correct = open_table(filename_table_correct)
    #print(table_correct)
    new_tables_add = tables_add
    new_tables_add.append(table_correct)
    table_divide = add_tables(new_tables_add)
    #print(table_divide)
    divided_tables_WA = [table_divide, added_tables_WA] 
    divided_table_res_WA = divide_tables(divided_tables_WA)
    #print(divided_table_res_WA)
    divided_tables_WC = [table_divide, added_tables_WC] 
    divided_table_res_WC = divide_tables(divided_tables_WC)
    #print(divided_table_res_WC)
    for table_ind in range(len(divided_table_res_WA[1:])):
        res_table = string_array_to_csv(divided_table_res_WA[table_ind + 1]) 
        filename_table = basedir + "all_results/" + dirs_to_include + " WA.csv" 
        #print(res_table)
        #print(filename_table)
        file_open = open(filename_table, "w")
        file_open.write(res_table)
        file_open.close()  
    for table_ind in range(len(divided_table_res_WC[1:])):
        res_table = string_array_to_csv(divided_table_res_WC[table_ind + 1]) 
        filename_table = basedir + "all_results/" + dirs_to_include + " WC.csv" 
        #print(res_table)
        #print(filename_table)
        file_open = open(filename_table, "w")
        file_open.write(res_table)
        file_open.close()  
    print(dirs_to_include, "Ok")
