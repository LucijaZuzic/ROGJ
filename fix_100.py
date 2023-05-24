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
                if tables_to_divide[k][i][j][0].isdigit():
                    if int(tables_to_divide[0][i][j]) != 0:
                        tables_to_divide[k][i][j] = float(tables_to_divide[k][i][j]) * 100 / float(tables_to_divide[0][i][j])
                    else:
                        tables_to_divide[k][i][j] = float(0)
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
 
dict_vals_letters = ["Equal ALIGN", "Insertions ALIGN", "Deletions ALIGN", "Substitutions ALIGN"] 

tables_dict = dict()
added_tables = dict() 
    
for dirs_to_include in dirs:  
    for phone in all_phones:
        print(dirs_to_include, phone, "Started")
        tables_add = []
        for table_value in dict_vals_letters:  
            filename_table = basedir + "all_results/" + dirs_to_include + " " + phone + " " + table_value + ".csv" 
            tables_dict[(dirs_to_include, phone, table_value)] = open_table(filename_table) 
            #print(tables_dict[(dirs_to_include, phone, table_value)])
            tables_add.append(tables_dict[(dirs_to_include, phone, table_value)])
        added_tables[(dirs_to_include, phone)] = add_tables(tables_add)
        #print(added_tables[(dirs_to_include, phone)])
        divided_tables = [added_tables[(dirs_to_include, phone)]]
        for table in tables_add[1:]:
            divided_tables.append(table)
        divided_table_res = divide_tables(divided_tables)
        #print(divided_table_res[1:])
        for table_ind in range(len(divided_table_res[1:])):
            res_table = string_array_to_csv(divided_table_res[table_ind + 1]) 
            filename_table = basedir + "all_results/" + dirs_to_include + " " + phone + " " + dict_vals_letters[table_ind + 1] + " postotak.csv" 
            #print(res_table)
            #print(filename_table)
            file_open = open(filename_table, "w")
            file_open.write(res_table)
            file_open.close()  
        print(dirs_to_include, phone, "Ok") 
