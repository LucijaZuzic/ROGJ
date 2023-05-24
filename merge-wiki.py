import os

all_lines = []

basedir = "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/hrwikidirectory/"

def format_files(homedir, subdir):

    filenames = os.listdir(homedir + subdir)
    filenames.sort()

    for filename in filenames:
        file_new = open(homedir + subdir + "/" + filename, "r")

        lines_new = file_new.readlines()

        for new_line in lines_new:
            if new_line[0] == "<":
                continue
            if len(new_line.replace("\n", "")) < 1:
                continue
            all_lines.append(new_line.replace("\n", ""))

        file_new.close() 

for somedir in os.listdir(basedir): 
    if somedir == 'my_db_all_lines.txt':
        continue
    format_files(basedir, somedir) 

print(len(all_lines))

all_lines_file = open(basedir + "/my_db_all_lines.txt", "w") 

all_lines_text = ""

my_counter = 0

for line_some in all_lines:
    all_lines_text += line_some

    my_counter += 1

    if my_counter != len(all_lines):
        all_lines_text += "\n"

all_lines_file.write(all_lines_text)
all_lines_file.close()