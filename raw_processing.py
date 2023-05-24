import pocketsphinx
import os

basedir = "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/"

replace_transcript = {"{": "š",  
            "#": "dž", 
            "}": "đ", 
            "^": "ć",
            "`": "ž",
            "~": "č" }

def predictions_make(output_name, lmname, hmname, dbname, PREDICTION_DIR_LIST, PREDICTION_NUM_LIST):

    lmpath = basedir + lmname #"my_db_pruned.lm.DMP"
    hmmpath = basedir + hmname #some_hm, some_dict
    dictpath = basedir + dbname

    if not os.path.isdir(basedir + output_name):  
        os.makedirs(basedir + output_name)

    my_config = pocketsphinx.Config(hmm = hmmpath, lm = lmpath, dict = dictpath)
    my_decoder = pocketsphinx.Decoder(my_config)

    for INDEX_PRED in range(len(PREDICTION_DIR_LIST)):

        PREDICTION_DIR = PREDICTION_DIR_LIST[INDEX_PRED]
        PREDICTION_NUM = PREDICTION_NUM_LIST[INDEX_PRED]

        if PREDICTION_DIR == "z":

            for sample_num in PREDICTION_NUM:

                string_number = str(sample_num)
                if sample_num < 10:
                    string_number = '0' + string_number

                wav_filenames = os.listdir(basedir + "audio_z/z" + string_number)

                print("Sample female", sample_num)
                counter = 0
                for some_name in wav_filenames:

                    audio_sample_path = basedir + "audio_z/z" + string_number + "/" + some_name
                    text_path = basedir + "text/z" + string_number + "/" + some_name.replace("wav", "txt")
                    counter += 1
                    print(str(sample_num) + "/" + str(len(PREDICTION_NUM)), str(counter) + "/" + str(len(wav_filenames)))
                    print(some_name.replace("wav", "txt"))

                    if not os.path.isdir(basedir + output_name + "z" + string_number):  
                        os.makedirs(basedir + output_name + "z" + string_number)

                    output_file_name = basedir + output_name + "z" + string_number + "/" + some_name.replace("wav", "txt")

                    predict_file(some_name, text_path, audio_sample_path, my_decoder, output_file_name)

        if PREDICTION_DIR == "m":

            for sample_num in PREDICTION_NUM:

                string_number = str(sample_num)
                if sample_num < 10:
                    string_number = '0' + string_number

                wav_filenames = os.listdir(basedir + "audio_m/m" + string_number)

                print("Sample male", sample_num)
                counter = 0
                for some_name in wav_filenames:

                    audio_sample_path = basedir + "audio_m/m" + string_number + "/" + some_name
                    text_path = basedir + "text/m" + string_number + "/" + some_name.replace("wav", "txt")
                    counter += 1
                    print(str(sample_num) + "/" + str(len(PREDICTION_NUM)), str(counter) + "/" + str(len(wav_filenames)))
                    print(some_name.replace("wav", "txt"))

                    if not os.path.isdir(basedir + output_name + "m" + string_number):  
                        os.makedirs(basedir + output_name + "m" + string_number)

                    output_file_name = basedir + output_name + "m" + string_number + "/" + some_name.replace("wav", "txt")

                    predict_file(some_name, text_path, audio_sample_path, my_decoder, output_file_name)

        if PREDICTION_DIR == "VremenskaPrognoza":
    
            prognoza_dir = "0069082557 1035 Battelli Piero/0069082557 1035 Battelli Piero/Train/"

            for sample_num in PREDICTION_NUM:

                wav_filenames = os.listdir(basedir + prognoza_dir + "wav_sorted/VremenskaPrognoza" + str(sample_num))

                print("Sample prognoza", sample_num)
                counter = 0
                for some_name in wav_filenames:

                    audio_sample_path = basedir + prognoza_dir + "wav_sorted/VremenskaPrognoza" + str(sample_num) + "/" + some_name
                    text_path = basedir + prognoza_dir + "txt/VremenskaPrognoza" + str(sample_num) + "/" + some_name.replace("wav", "txt")
                    counter += 1
                    print(str(sample_num) + "/" + str(len(PREDICTION_NUM)), str(counter) + "/" + str(len(wav_filenames)))
                    print(some_name.replace("wav", "txt"))

                    if not os.path.isdir(basedir + output_name + "VremenskaPrognoza" + str(sample_num)):  
                        os.makedirs(basedir + output_name + "VremenskaPrognoza" + str(sample_num))

                    output_file_name = basedir + output_name + "VremenskaPrognoza" + str(sample_num) + "/" + some_name.replace("wav", "txt")

                    predict_file(some_name, text_path, audio_sample_path, my_decoder, output_file_name)

        if PREDICTION_DIR == "sm04":  

            wav_filenames = os.listdir(basedir + "wav_sm04")

            print("Sample sm04")
            counter = 0
            for some_name in wav_filenames:

                audio_sample_path = basedir + "wav_sm04/" + some_name
                text_path = basedir + "txt_sm04/" + some_name.replace("wav", "txt")
                counter += 1
                print(str(counter) + "/" + str(len(wav_filenames)))
                print(some_name.replace("wav", "txt"))

                if not os.path.isdir(basedir + output_name + "sm04"):  
                    os.makedirs(basedir + output_name + "sm04")

                output_file_name = basedir + output_name + "sm04/" + some_name.replace("wav", "txt")

                predict_file(some_name, text_path, audio_sample_path, my_decoder, output_file_name)

        if PREDICTION_DIR == "a":  
    
            cmu_dir = "16kHz_16bit/"

            dir_cmu = os.listdir(basedir + cmu_dir)
            new_cmu_dir = []

            for new_dir_cmu in dir_cmu:
                if os.path.isdir(basedir + cmu_dir + new_dir_cmu) and new_dir_cmu != "Prompts" and new_dir_cmu != "db_files":
                    new_cmu_dir.append(new_dir_cmu)  

            for cmu in new_cmu_dir:
                print("Sample CMU", cmu)
                counter = 0
                wav_filenames = os.listdir(basedir + "16kHz_16bit/" + cmu + "/wav/")
                for some_name in wav_filenames:

                    audio_sample_path = basedir + "16kHz_16bit/" + cmu + "/wav/" + some_name
                    text_path = basedir + "16kHz_16bit/" + "/Prompts/txt/" + cmu + "/" + some_name.replace("wav", "txt")
                    counter += 1
                    print(str(counter) + "/" + str(len(wav_filenames)))
                    print(some_name.replace("wav", "txt"))

                    if not os.path.isdir(basedir + output_name + cmu):  
                        os.makedirs(basedir + output_name + cmu)

                    output_file_name = basedir + output_name + cmu + "/" + some_name.replace("wav", "txt")

                    predict_file(some_name, text_path, audio_sample_path, my_decoder, output_file_name)

        if PREDICTION_DIR == "hrt":  

            wav_filenames = os.listdir(basedir + "veprad/podaci-BCN/audio_kopija")
            counter = 0

            for some_name in wav_filenames:

                audio_sample_path = basedir + "veprad/podaci-BCN/audio_kopija/" + some_name
                text_path = basedir + "veprad/podaci-BCN/tekst_popravljeno/" + some_name.replace("wav", "txt")
                counter += 1
                print(str(counter) + "/" + str(len(wav_filenames)))
                print(some_name.replace("wav", "txt"))

                if not os.path.isdir(basedir + output_name + "hrt/"):  
                    os.makedirs(basedir + output_name + "hrt/")

                output_file_name = basedir + output_name + "hrt/" + some_name.replace("wav", "txt")

                predict_file(some_name, text_path, audio_sample_path, my_decoder, output_file_name)

        if PREDICTION_DIR == "prvi":  

            wav_filenames = os.listdir(basedir + "veprad/podaci_radio/audio/prvi")
            counter = 0

            for some_name in wav_filenames:

                audio_sample_path = basedir + "veprad/podaci_radio/audio/prvi/" + some_name
                text_path = basedir + "veprad/podaci_radio/text/prvi/" + some_name.replace("wav", "txt")
                counter += 1
                print(str(counter) + "/" + str(len(wav_filenames)))
                print(some_name.replace("wav", "txt"))

                if not os.path.isdir(basedir + output_name + "prvi/"):  
                    os.makedirs(basedir + output_name + "prvi/")

                output_file_name = basedir + output_name + "prvi/" + some_name.replace("wav", "txt")

                predict_file(some_name, text_path, audio_sample_path, my_decoder, output_file_name)

        if PREDICTION_DIR == "sz04":  

            wav_filenames = os.listdir(basedir + "veprad/podaci_sinteza/sz04/audio/wav")
            counter = 0

            for some_name in wav_filenames:

                audio_sample_path = basedir + "veprad/podaci_sinteza/sz04/audio/wav/" + some_name
                text_path = basedir + "veprad/podaci_sinteza/sz04/text/" + some_name.replace("wav", "txt")
                counter += 1
                print(str(counter) + "/" + str(len(wav_filenames)))
                print(some_name.replace("wav", "txt"))

                if not os.path.isdir(basedir + output_name + "sz04/"):  
                    os.makedirs(basedir + output_name + "sz04/")

                output_file_name = basedir + output_name + "sz04/" + some_name.replace("wav", "txt")

                predict_file(some_name, text_path, audio_sample_path, my_decoder, output_file_name)

        if PREDICTION_DIR == "sz08":  

            wav_filenames = os.listdir(basedir + "veprad/podaci_sinteza/sz08/audio/wav")
            counter = 0

            for some_name in wav_filenames:

                audio_sample_path = basedir + "veprad/podaci_sinteza/sz08/audio/wav/" + some_name
                text_path = basedir + "veprad/podaci_sinteza/sz08/text/" + some_name.replace("wav", "txt")
                counter += 1
                print(str(counter) + "/" + str(len(wav_filenames)))
                print(some_name.replace("wav", "txt"))

                if not os.path.isdir(basedir + output_name + "sz08/"):  
                    os.makedirs(basedir + output_name + "sz08/")

                output_file_name = basedir + output_name + "sz08/" + some_name.replace("wav", "txt")

                predict_file(some_name, text_path, audio_sample_path, my_decoder, output_file_name)

def predict_file(some_name, text_path, audio_sample_path, my_decoder, output_file_name):

        if some_name.replace(".wav", "") in train_files_list:
            print("in train")
            return  
        
        if not os.path.isfile(text_path):
            print("no .txt")
            return

        text_file = open(text_path, "r")
        actual_text_lines = text_file.readlines()
        text_file.close()

        file_text_content = "" 

        for content in actual_text_lines: 

            one_line_original = content
            for filler in lines_filler:
                one_line_original = one_line_original.replace(filler, "")
            for replacement in replace_transcript:
                one_line_original = one_line_original.replace(replacement, replace_transcript[replacement])
            one_line_original = one_line_original.replace("\t", "").replace("\n", "").replace(",", "").replace(".", "").lower().replace("<", "").replace(">", "")
            while one_line_original.count("  ") != 0:
                one_line_original = one_line_original.replace("  ", " ")
            while len(one_line_original) > 0 and one_line_original[0] == " ":
                one_line_original = one_line_original[1:]  
            if file_text_content != "":
                file_text_content += " "
            if len(one_line_original) == 0:
                continue
            file_text_content += one_line_original.lower()

        with open(audio_sample_path, 'rb') as fd:
            contents = fd.read()

            #my_decoder.set_align_text(file_text_content)
            my_decoder.start_utt()
            my_decoder.process_raw(contents, full_utt=True)
            my_decoder.end_utt()
            my_hyp = my_decoder.hyp()

            retvalue = ""
            if my_hyp is not None:
                retvalue = my_hyp.hypstr

            print(file_text_content)
            print(retvalue)

            text_file = open(output_file_name, "w")
            text_file.write(file_text_content + "\n" + retvalue)
            text_file.close()

PRED_DIR = ["a", "VremenskaPrognoza", "m", "z", "sm04", "hrt", "prvi", "sz04", "sz08"]
PRED_NUM = [[], [i for i in range(1, 14)], [i for i in range(1, 12)], [i for i in range(1, 15)], [], [], [], [], []] 

for num in ["", 3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
    some_hm = "tutorial" + str(num) + "/model_parameters/my_db.cd_cont_200"
    some_dict = "my_db" + str(num) + ".dic"
    start = "all_outputs/outputs" + str(num)

    file_filler = open(basedir + "my_db" + str(num) + ".filler", "r")

    lines_filler = file_filler.readlines()

    for line_num in range(len(lines_filler)):
        lines_filler[line_num] = lines_filler[line_num].replace("\n", "").replace("NOISE", "").replace("SIL", "").replace(" ", "") 

    file_filler.close()

    files_train = open(basedir + "my_db" + str(num) + "_train.fileids", "r")
    train_files_list = files_train.readlines()
    for i in range(len(train_files_list)):
        train_files_list[i] = train_files_list[i].replace("\n", "").split("/")[1]
    files_train.close() 
 
    predictions_make(start + "/", "my_db.lm.DMP", some_hm, some_dict, PRED_DIR, PRED_NUM)
    predictions_make(start + "_pruned/", "my_db_pruned.lm.DMP", some_hm, some_dict, PRED_DIR, PRED_NUM)
    predictions_make(start + "_only_weather/", "words_from_txt.lm.DMP", some_hm, some_dict, PRED_DIR, PRED_NUM)
    predictions_make(start + "_only_weather_pruned/", "words_from_txt_pruned.lm.DMP", some_hm, some_dict, PRED_DIR, PRED_NUM)
    predictions_make(start + "_both/", "words_from_txt_word.lm.DMP", some_hm, some_dict, PRED_DIR, PRED_NUM)
    predictions_make(start + "_both_pruned/", "words_from_txt_word_pruned.lm.DMP", some_hm, some_dict, PRED_DIR, PRED_NUM)
    
    for new_num in ["", 2, 3, 1, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
        new_str = str(new_num)

        predictions_make(start + "_only_weather_train" + new_str + "/", "my_db_from_txt_train" + new_str + ".lm.DMP", some_hm, some_dict, PRED_DIR, PRED_NUM)
        predictions_make(start + "_only_weather_train_pruned" + new_str + "/", "my_db_from_txt_train_pruned" + new_str + ".lm.DMP", some_hm, some_dict, PRED_DIR, PRED_NUM)

        predictions_make(start + "_both_train" + new_str + "/", "my_db_from_txt_word_train" + new_str + ".lm.DMP", some_hm, some_dict, PRED_DIR, PRED_NUM)
        predictions_make(start + "_both_train_pruned" + new_str + "/", "my_db_from_txt_word_train_pruned" + new_str + ".lm.DMP", some_hm, some_dict, PRED_DIR, PRED_NUM)