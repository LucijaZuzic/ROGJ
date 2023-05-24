import os

basepath = "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/16kHz_16bit/Prompts/"
file_all_path = basepath + "master_prompts_train_16kHz-16bit"
file_all = open(file_all_path, "r")
all_prompts = file_all.readlines()
file_all.close()

all_prompts_split = []
all_names = []

for prompt in all_prompts:
    
    foldername = prompt.split("/")[0]
    name_prompt = prompt.split("/")[-1] 
    
    name = name_prompt.split(" ")[0]
    prompt_new = name_prompt.replace(name + " ", "").replace("\n", "").replace("-", "").replace("160 M", "sto šezdeset metara").replace("2", "dva").replace("1", "jedan").lower()
  
    all_names.append(name)
    all_prompts_split.append(prompt_new)

    if not os.path.isdir(basepath + "/txt/" + foldername  + "/"):
        os.makedirs(basepath + "/txt/" + foldername  + "/")

    file_one = open(basepath + "/txt/" + foldername  + "/" + name + ".txt", "w")
    file_one.write(prompt_new)
    file_one.close()

    file_one = open(basepath + "/txt/" + name + ".txt", "w")
    file_one.write(prompt_new)
    file_one.close()
 
print(all_names)
print(all_prompts_split)