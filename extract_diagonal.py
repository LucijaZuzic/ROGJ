import numpy as np

def format_table(file_name, rows_included, rows_order, decimal_places, name_the_table, chooseval):
    only_values = []
    only_rownames = []
    min_row = [] 
    min_row_text = [] 
    min_val = -1
    file_open = open(file_name, "r")
    file_text = file_open.readlines()
    file_open.close()
    string_to_print = []
    string_header = "\\begin{tabular}{|c|}\n\\hline"
    for i in range(len(file_text)):
        if i not in rows_included:
            continue
        file_text[i] = file_text[i].replace("\n", "").split(";")
        new_line = []
        for j in range(len(file_text[i])):
            if j == i or j == 0 or (i == 0 and j == 1):
                new_line.append(file_text[i][j])
        string_line_array = []
        for j in range(len(new_line)):
            text_to_add = new_line[j]
            if "." in text_to_add:
                text_to_add = np.round(float(new_line[j]), decimal_places)
            string_line_array.append(str(text_to_add))
        string_line = ""
        for j in range(len(string_line_array)):
            if not string_line_array[j][0].isalpha():
                only_values.append(float(string_line_array[j]))
            else:
                if string_line_array[j][0] != "A" and string_line_array[j][0] != "W":
                    only_rownames.append(string_line_array[j]) 
            if string_line_array[j][0].isdigit() and ((float(string_line_array[j]) <= min_val and chooseval == "min") or (float(string_line_array[j]) >= min_val and chooseval == "max") or min_val == -1):
                if float(string_line_array[j]) < min_val and chooseval == "min":
                    min_row = [] 
                if float(string_line_array[j]) > min_val and chooseval == "max":
                    min_row = [] 
                min_val = float(string_line_array[j])
                min_row.append(rows_order.index(len(string_to_print)))
            string_line += string_line_array[j]
            if j != len(string_line_array) - 1:
                string_line += " & "
            else:
                string_line += " \\\\ \\hline"
        string_to_print.append(string_line.replace("Wikipedia", name_the_table))
    string_footer = "\\end{tabular}"
    printed_value = string_header + "\n"
    for line_string_index in rows_order:
        for i in range(len(min_row)): 
            if rows_order.index(line_string_index) == min_row[i]:
                all_titles = string_to_print[line_string_index].replace(" \\\\ \\hline", "").split(" & ")
                min_row_text.append(all_titles[0])
        printed_value += string_to_print[line_string_index] + "\n"
    printed_value += string_footer
    #print(min_val)
    #for i in range(len(min_row)):
        #print(min_row[i], min_row_text[i]) 
    #print(printed_value)
    #print(file_name)  
    #print(only_values)  
    #print(rows_order)  
    only_values_new = [only_values[i - 1] for i in rows_order[1:]]
    only_rownames_new = [only_rownames[i - 1] for i in rows_order[1:]]
    #print(only_values_new)  
    return only_values_new, only_rownames_new, min_row[0]

basedir = "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/"
  
file_phones = open(basedir + "my_db14.phone", "r")
lines_phone = file_phones.readlines()
file_phones.close()

all_phones = [' ']
for line_phone in lines_phone:
    if line_phone[0].upper() == line_phone[0]:
        continue
    all_phones.append(line_phone.replace("\n", "")) 
    
dict_vals = {"WER": "min", "MER": "min", "WIL": "min"}   
dict_vals = {"WC": "max", "WA": "max"}   
dict_vals = {"WER": "min", "MER": "min", "WIL": "min", "WC": "max", "WA": "max"}   
dict_vals = {"Error": "min", "Accuracy": "max", "Percent correct": "max"}
dict_vals = {"Error": "min", "Accuracy": "max", "Percent correct": "max", "WC": "max", "WA": "max"}
dict_vals = {"WER": "min", "MER": "min", "WIL": "min", "Percent correct": "max", "Error": "min", "Accuracy": "max", "WC": "max", "WA": "max"}  
dict_vals = {"WER": "min", "MER": "min", "WIL": "min", "Percent correct": "max", "Error": "min", "Accuracy": "max"}  
dict_vals = {"Točne rečenice postotak": "max", "Netočne rečenice postotak": "min", 
            "Točne riječi postotak": "max", "Netočne riječi postotak": "min", 
            "Točne riječi inserted postotak": "max", "Netočne riječi inserted postotak": "min",
            "Zamijenjene riječi postotak": "min", "Zamijenjene riječi inserted postotak": "min", 
            "Ispuštene riječi postotak": "min", "Ispuštene riječi inserted postotak": "min", 
            "Dodane riječi postotak": "min", "Dodane riječi inserted postotak": "min", "WER": "min", "MER": "min", "WIL": "min",  
            "Točni znakovi postotak": "max", "Netočni znakovi postotak": "min", 
            "Dodani znakovi postotak": "min", "Ispušteni znakovi postotak": "min", 
            "Zamijenjeni znakovi postotak": "min", "Equal ALIGN postotak": "max",  
            "Incorrect ALIGN postotak": "min", "Insertions ALIGN postotak": "min", 
            "Deletions ALIGN postotak": "min", "Substitutions ALIGN postotak": "min",  
            "Ratio postotak": "max", "Percent correct": "max", 
            "Error": "min", "Accuracy": "max", "Word error rate": "min", "Sentence error rate": "min"}  
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
    
rows_table = ["Weather", "Weather and new source", "Expanded weather and new source", "Expanded weather",
              "Weather, new source and alka", "Expanded weather, new source and alka", "Expanded weather and alka", 
              "Weather and alka", "Expanded all sources", "All sources", "Expanded no TV", "No TV"]  
              
rows_range_all = [i for i in range(len(rows_table) + 1)] 
row_order_all = rows_range_all 

rows_range = [0]
for i in range(len(rows_table)): 
    if "Expanded" in rows_table[i]:
        rows_range.append(i + 1)

row_order = [0, 2, 1, 4, 3, 6, 5] 

excluded = ["Expanded weather", "Expanded weather and new source"] 
        
rows_range_shorter = [0]
for i in range(len(rows_table)): 
    if "Expanded" in rows_table[i] and rows_table[i] not in excluded:
        rows_range_shorter.append(i + 1)
        
row_order_shorter = [0, 1, 2, 4, 3] 
        
included = ["Expanded no TV", "Expanded all sources"]   
        
rows_range_shortest = [0]
for i in range(len(rows_table)): 
    if rows_table[i] in included:
        rows_range_shortest.append(i + 1)
        
row_order_shortest = [0, 2, 1] 

decimal_place = 2

directories_include = ["z04", "VremenskaPrognoza", "a", "prvi", "hrt", "sz04", "sz08"]
directories_include = ["z04", "VremenskaPrognoza", "a", "prvi", "hrt", "sz04", "sz08", "All dirs"]
models_include = []

occurences = dict()
for dirs_to_include in directories_include:
    occurences_dir = dict()
    for val in range(len(row_order)):
        occurences_dir[val] = 0
    occurences[dirs_to_include] = occurences_dir

dict_vals_letters1 = ["Točni znakovi postotak", "Dodani znakovi postotak", "Ispušteni znakovi postotak", "Zamijenjeni znakovi postotak"]
dict_vals_letters2 = ["Equal ALIGN postotak", "Insertions ALIGN postotak", "Deletions ALIGN postotak", "Substitutions ALIGN postotak"]
niz = [3, 5, 6, 5, 6, 6, 6, 6]

dict_vals = {"WER": "min", "MER": "min", "WC": "max", "WA": "max", "WIL": "min"}

for table_value in dict_vals:  
    #print(table_value)
    returned_vals = []
    best_vals = []
    for dirs_to_include in directories_include: 
        #print(dirs_to_include) 
        filename_table = basedir + "all_results/" + dirs_to_include + " " + table_value + ".csv" 
        #retval, models_include, best_val = format_table(filename_table, rows_range_all, row_order_all, decimal_place, dirs_to_include,  dict_vals[table_value])
        retval, models_include, best_val = format_table(filename_table, rows_range, row_order, decimal_place, dirs_to_include,  dict_vals[table_value])
        returned_vals.append(retval)
        best_vals.append(best_val)
        occurences[dirs_to_include][best_val] += 1
        #format_table(filename_table, rows_range_shorter, row_order_shorter, decimal_place, dirs_to_include,  dict_vals[table_value])
        #format_table(filename_table, rows_range_shortest, row_order_shortest, decimal_place, dirs_to_include,  dict_vals[table_value])                
    
    #print(best_vals)
    
    diffniz = []
    for i in range(len(best_vals)):
        diffniz.append(best_vals[i] == niz[i])
    
    '''
    if table_value in dict_vals_letters1:
        print("1", table_value)
        print(best_vals)
        print(diffniz)
        print(sum(diffniz))
        
    if table_value in dict_vals_letters2:
        print("2", table_value)
        print(best_vals)
        print(diffniz)
        print(sum(diffniz)) 
    '''
        
    if best_vals == niz:
        print(table_value) 
     
    string_rows_final = "\\begin{tabular}{|c"
    for i in range(len(directories_include)):
        string_rows_final += "|c"
    string_rows_final += "|}\n\\hline\n"

    string_rows_final += "& \multicolumn{" + str(len(directories_include)) +"}{c|}{\\textbf{Sample}}\\ \\hline \n"
    string_rows_final += "\\textbf{Model} & "
    for i in range(len(directories_include)):
        string_rows_final += str(directories_include[i]) 
        if i != len(directories_include) - 1:
            string_rows_final += " & "
        else:
            string_rows_final += " \\\\ \\hline" 
    string_rows_final += "\n"

    for j in range(len(returned_vals[0])):
        string_rows_final += str(models_include[j]) + " & "
        for i in range(len(directories_include)):
            if best_vals[i] == j + 1: 
                string_rows_final += "\\textbf{"
            string_rows_final += str(returned_vals[i][j]) 
            if best_vals[i] == j + 1: 
                string_rows_final += "}"
            if i != len(directories_include) - 1:
                string_rows_final += " & "
            else:
                string_rows_final += " \\\\ \\hline" 
        string_rows_final += "\n" 
		
    string_rows_final += "\\end{tabular}"
    
    print(string_rows_final) 
    
    string_rows_final = "\\begin{tabular}{|c"
    for i in range(len(models_include)):
        string_rows_final += "|c"
    string_rows_final += "|}\n\\hline\n"

    string_rows_final += "& \multicolumn{" + str(len(models_include)) +"}{c|}{\\textbf{Model}}\\ \\hline \n"
    string_rows_final += "\\textbf{Sample} & "
    for i in range(len(models_include)):
        string_rows_final += str(models_include[i]) 
        if i != len(models_include) - 1:
            string_rows_final += " & "
        else:
            string_rows_final += " \\\\ \\hline" 
    string_rows_final += "\n"

    for i in range(len(directories_include)):
        string_rows_final += str(directories_include[i]) + " & "
        for j in range(len(returned_vals[0])):
            if best_vals[i] == j + 1: 
                string_rows_final += "\\textbf{"
            string_rows_final += str(returned_vals[i][j]) 
            if best_vals[i] == j + 1: 
                string_rows_final += "}"
            if j != len(models_include) - 1:
                string_rows_final += " & "
            else:
                string_rows_final += " \\\\ \\hline" 
        string_rows_final += "\n" 
		
    string_rows_final += "\\end{tabular}"
    
    print(string_rows_final)  
    
for x in occurences:
	print(x, occurences[x]) 
    
directories_include = ["z04", "VremenskaPrognoza", "a", "prvi", "hrt", "sz04", "sz08"]
dict_vals = {"Točne rečenice": "max", "Netočne rečenice": "min", "Točne riječi": "max", "Netočne riječi": "min"}

retval_arr = []
for table_value in dict_vals:  
    print(table_value)
    returned_vals = []
    best_vals = []
    for dirs_to_include in directories_include: 
        #print(dirs_to_include) 
        filename_table = basedir + "all_results/" + dirs_to_include + " " + table_value + ".csv" 
        #retval, models_include, best_val = format_table(filename_table, rows_range_all, row_order_all, decimal_place, dirs_to_include,  dict_vals[table_value])
        retval, models_include, best_val = format_table(filename_table, rows_range, row_order, decimal_place, dirs_to_include,  dict_vals[table_value])
        returned_vals.append(retval)
        best_vals.append(best_val)
        #occurences[dirs_to_include][best_val] += 1
        #format_table(filename_table, rows_range_shorter, row_order_shorter, decimal_place, dirs_to_include,  dict_vals[table_value])
        #format_table(filename_table, rows_range_shortest, row_order_shortest, decimal_place, dirs_to_include,  dict_vals[table_value])                
    
    print(returned_vals) 
    retval_arr.append(returned_vals)
    
for i in range(len(retval_arr[0])):  
    new_retval = []
    for j in range(len(retval_arr[0][i])): 
        new_retval.append(retval_arr[0][i][j] + retval_arr[1][i][j])
    print(directories_include[i], new_retval)
    new_retval = []
    for j in range(len(retval_arr[3][i])): 
        new_retval.append(retval_arr[2][i][j] + retval_arr[3][i][j]) 
    print(directories_include[i], new_retval) 
