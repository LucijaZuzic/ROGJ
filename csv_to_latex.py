import numpy as np

def format_table(file_name, cols_included, rows_included, rows_order, columns_order, decimal_places, chooseval):
    min_row = []
    min_col = []
    min_row_text = []
    min_col_text = []
    min_val = -1
    file_open = open(file_name, "r")
    file_text = file_open.readlines()
    file_open.close()
    string_to_print = []
    string_header = "\\begin{tabular}{"
    for x in range(len(cols_included)):
        string_header += "|c"
    string_header += "|}\n\\hline\n"
    string_header += "& \multicolumn{" + str(len(cols_included) - 1) +"}{c|}{\\textbf{Linguistic model}}\\ \\hline" 
    for i in range(len(file_text)):
        if i not in rows_included:
            continue
        file_text[i] = file_text[i].replace("\n", "").split(";")
        new_line = []
        for j in range(len(file_text[i])):
            if j in cols_included:
                new_line.append(file_text[i][j])
        string_line_array = []
        for j in range(len(new_line)):
            text_to_add = new_line[j]
            if "." in text_to_add:
                text_to_add = np.round(float(new_line[j]), decimal_places)
            string_line_array.append(str(text_to_add))
        new_string_line_array = [string_line_array[ind] for ind in columns_order]
        string_line = ""
        for j in range(len(new_string_line_array)):
            if new_string_line_array[j][0].isdigit() and ((float(new_string_line_array[j]) <= min_val and chooseval == "min") or (float(new_string_line_array[j]) >= min_val and chooseval == "max") or min_val == -1):
                if float(new_string_line_array[j]) < min_val and chooseval == "min":
                    min_row = []
                    min_col = []
                if float(new_string_line_array[j]) > min_val and chooseval == "max":
                    min_row = []
                    min_col = []
                min_val = float(new_string_line_array[j])
                min_row.append(columns_order.index(len(string_to_print)))
                min_col.append(rows_order.index(j))
            string_line += new_string_line_array[j]
            if j != len(new_string_line_array) - 1:
                string_line += " & "
            else:
                string_line += " \\\\ \\hline"
        string_to_print.append(string_line)
    string_footer = "\\end{tabular}"
    printed_value = string_header + "\n"
    for line_string_index in rows_order:
        for i in range(len(min_col)):
            if rows_order.index(line_string_index) == 0:
                all_titles = string_to_print[line_string_index].replace(" \\\\ \\hline", "").split(" & ")
                min_col_text.append(all_titles[min_col[i]])
            if rows_order.index(line_string_index) == min_row[i]:
                all_titles = string_to_print[line_string_index].replace(" \\\\ \\hline", "").split(" & ")
                min_row_text.append(all_titles[0])
        printed_value += string_to_print[line_string_index] + "\n"
    printed_value += string_footer
    print(min_val)
    for i in range(len(min_row)):
        if min_row[i] == min_col[i]:
            print(min_row[i], min_row_text[i])
        else:
            print(min_row[i], min_col[i], min_row_text[i], min_col_text[i])
    print(printed_value)
    return printed_value

basedir = "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/"
  
file_phones = open(basedir + "my_db14.phone", "r")
lines_phone = file_phones.readlines()
file_phones.close()

all_phones = [' ']
for line_phone in lines_phone:
    if line_phone[0].upper() == line_phone[0]:
        continue
    all_phones.append(line_phone.replace("\n", "")) 
    
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
            "Incorrect sentences": "min", "Word error rate": "min", "Sentence error rate": "min",
            "WC": "max", "WA": "max"}
          
dict_vals = {"WER": "min", "MER": "min", "WIL": "min"}
dict_vals = {"WER": "min"}
dict_vals = {"WC": "max", "WA": "max"} 

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
     
string_table = "Acoustic model;Wikipedia;Wikipedia pruned;"
string_table += "Weather with test;Weather with test pruned;Wikipedia and weather with test;Wikipedia and weather with test pruned;"
string_table += "Weather original;Weather original pruned;Wikipedia and weather original;Wikipedia and weather original pruned;"
string_table += "New source original;New source original pruned;Wikipedia, weather and new source original;Wikipedia, weather and new source original pruned;"
string_table += "Alka with test;Alka with test pruned;Wikipedia, weather, new source and alka with test;Wikipedia, weather, new source and alka with test pruned;"
string_table += "Weather;Weather pruned;Wikipedia and weather;Wikipedia and weather pruned;"
string_table += "Weather and new source;Weather and new source pruned;Wikipedia, weather and new source;Wikipedia, weather and new source pruned;"
string_table += "Expanded weather and new source;Expanded weather and new source pruned;Wikipedia, expanded weather and new source;Wikipedia, expanded weather and new source pruned;"
string_table += "Expanded weather;Expanded weather pruned;Wikipedia and expanded weather;Wikipedia and expanded weather pruned;"
string_table += "Weather, new source and alka;Weather, new source and alka pruned;Wikipedia, weather, new source and alka;Wikipedia, weather, new source and alka pruned;"
string_table += "Expanded weather, new source and alka;Expanded weather, new source and alka pruned;Wikipedia, expanded weather, new source and alka;Wikipedia, expanded weather, new source and alka pruned;"
string_table += "Expanded weather and alka;Expanded weather and alka pruned;Wikipedia, expanded weather and alka;Wikipedia, expanded weather and alka pruned;"
string_table += "Weather and alka;Weather and alka pruned;Wikipedia and alka;Wikipedia and alka pruned;"
string_table += "Expanded all sources;Expanded all sources pruned;Wikipedia and expanded all sources;Wikipedia and expanded all sources pruned;"
string_table += "All sources;All sources pruned;Wikipedia and all sources;Wikipedia and all sources pruned;"
string_table += "Expanded no TV;Expanded no TV pruned;Wikipedia and expanded no TV;Wikipedia and expanded no TV pruned;"
string_table += "No TV;No TV pruned;Wikipedia and no TV;Wikipedia and no TV pruned"
string_table = string_table.split(";")

rows_table = ["Weather", "Weather and new source", "Expanded weather and new source", "Expanded weather",
              "Weather, new source and alka", "Expanded weather, new source and alka", "Expanded weather and alka", 
              "Weather and alka", "Expanded all sources", "All sources", "Expanded no TV", "No TV"]

columns_range = [0]
for i in range(len(string_table)):
    if "Expanded" in string_table[i] and "pruned" not in string_table[i]:
        columns_range.append(i)
        
rows_range = [0]
for i in range(len(rows_table)): 
    if "Expanded" in rows_table[i]:
        rows_range.append(i + 1)

row_order = [0, 2, 1, 4, 3, 6, 5]
column_order = [0, 2, 1, 4, 3, 6, 5] 

excluded = ["Expanded weather", "Expanded weather and new source"]
columns_range_shorter = [0]
for i in range(len(string_table)):
    if "Expanded" in string_table[i] and "pruned" not in string_table[i] and string_table[i] not in excluded:
        columns_range_shorter.append(i)
        
rows_range_shorter = [0]
for i in range(len(rows_table)): 
    if "Expanded" in rows_table[i] and rows_table[i] not in excluded:
        rows_range_shorter.append(i + 1)
        
row_order_shorter = [0, 1, 2, 4, 3]
column_order_shorter = [0, 1, 2, 4, 3] 
        
included = ["Expanded no TV", "Expanded all sources"]  
columns_range_shortest = [0]
for i in range(len(string_table)):
    if string_table[i] in included:
        columns_range_shortest.append(i)
        
rows_range_shortest = [0]
for i in range(len(rows_table)): 
    if rows_table[i] in included:
        rows_range_shortest.append(i + 1)
        
row_order_shortest = [0, 2, 1]
column_order_shortest = [0, 2, 1] 

decimal_place = 2

for dirs_to_include in ["z04", "VremenskaPrognoza", "a", "prvi", "hrt", "sz04", "sz08"]:  
    print(dirs_to_include)
    for table_value in dict_vals:  
        print(table_value)
        filename_table = basedir + "all_results/" + dirs_to_include + " " + table_value + ".csv" 
        format_table(filename_table, columns_range, rows_range, row_order, column_order, decimal_place, dict_vals[table_value])
        format_table(filename_table, columns_range_shorter, rows_range_shorter, row_order_shorter, column_order_shorter, decimal_place, dict_vals[table_value])
        format_table(filename_table, columns_range_shortest, rows_range_shortest, row_order_shortest, column_order_shortest, decimal_place, dict_vals[table_value])

'''
for dirs_to_include in ["z04", "VremenskaPrognoza", "a", "prvi", "hrt", "sz04", "sz08"]:  
    for table_value in dict_vals_letters:  
        filename_table = basedir + "all_results/" + dirs_to_include + " " + table_value + ".csv"  
        format_table(filename_table, columns_range, rows_range, row_order, column_order) 
        break
    break
'''
