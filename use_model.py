import pocketsphinx
import os

replace_transcript = {"{": "š",  
            "#": "dž", 
            "}": "đ", 
            "^": "ć",
            "`": "ž",
            "~": "č" }

basedir = "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/"
files_train = open(basedir + "my_db3_train.fileids", "r")
train_files_list = files_train.readlines()
for i in range(len(train_files_list)):
    train_files_list[i] = train_files_list[i].replace("\n", "").split("/")[1]
files_train.close()

def predictions_make(output_name, lmname, hmname, PREDICTION_DIR, PREDICTION_NUM):

    lmpath = basedir + lmname #"my_db_pruned.lm.DMP"
    hmmpath = basedir + hmname #"tutorial3/model_parameters/my_db.cd_cont_200"
    dictpath = basedir + "my_db.dic"

    if not os.path.isdir(basedir + output_name):  
        os.makedirs(basedir + output_name)

    # my_config = pocketsphinx.Config(hmm: = hmmpath, lm = lmpath, dict = dictpath)
    # my_decoder = pocketsphinx.Decoder(cofnig)

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

                predict_file(some_name, text_path, audio_sample_path, lmpath, hmmpath, dictpath, output_file_name)

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

                predict_file(some_name, text_path, audio_sample_path, lmpath, hmmpath, dictpath, output_file_name)

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

                predict_file(some_name, text_path, audio_sample_path, lmpath, hmmpath, dictpath, output_file_name, 1)

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

            predict_file(some_name, text_path, audio_sample_path, lmpath, hmmpath, dictpath, output_file_name)

def predict_file(some_name, text_path, audio_sample_path, lmpath, hmmpath, dictpath, output_file_name, padding = 0):

        if some_name.replace(".wav", "") in train_files_list:
            return

        text_file = open(text_path, "r")
        actual_text_lines = text_file.readlines()
        text_file.close()

        file_text_content = "" 

        for content in actual_text_lines:

            new_content = content

            for replacement in replace_transcript:
                new_content = new_content.replace(replacement, replace_transcript[replacement])

            file_text_content += new_content + "\n" 

        print(file_text_content.lower())

        audio_config = {
            'verbose': False,
            'audio_file': audio_sample_path,
            'hmm': hmmpath,
            'lm': lmpath,
            'dict': dictpath
        }

        sample_rate = 100

        audio_file = pocketsphinx.AudioFile(**audio_config)

        save_hyp = ""

        length_line = 38 + 2 * padding

        for phrase in audio_file:
            print(phrase)
            print('-' * length_line)
            if padding == 1:
                print('| %6s |  %4s  |        %4s        |' % ('start', 'end', 'word'))
            else:
                print('| %5s |  %3s  |        %4s        |' % ('start', 'end', 'word'))
            print('-' * length_line)
            for s in phrase.seg():
                if padding == 1:
                    print('| %5ss | %5ss | %18s |' % (s.start_frame / sample_rate, s.end_frame / sample_rate, s.word))
                else:
                    print('| %4ss | %4ss | %18s |' % (s.start_frame / sample_rate, s.end_frame / sample_rate, s.word))
            print('-' * length_line)

            save_hyp += file_text_content.lower() + str(phrase) + "\n"
            save_hyp += ('-' * length_line) + "\n"
            if padding == 1:
                save_hyp += ('| %6s |  %4s  |        %4s        |' % ('start', 'end', 'word')) + "\n"
            else:
                save_hyp += ('| %5s |  %3s  |        %4s        |' % ('start', 'end', 'word')) + "\n"
            save_hyp += ('-' * length_line) + "\n"
            for s in phrase.seg():
                if padding == 1:
                    save_hyp += ('| %5ss | %5ss | %18s |' % (s.start_frame / sample_rate, s.end_frame / sample_rate, s.word)) + "\n"
                else:
                    save_hyp += ('| %4ss | %4ss | %18s |' % (s.start_frame / sample_rate, s.end_frame / sample_rate, s.word)) + "\n"
            save_hyp += ('-' * length_line) + "\n"

            text_file = open(output_file_name, "w")
            text_file.write(save_hyp)
            text_file.close()

        '''
        with pocketsphinx.wave.open(audio_sample_path, "r") as w:
            segmenter = pocketsphinx.Segmenter(sample_rate=w.getframerate())
            for seg in segmenter.segment(w.getfp()):
                with pocketsphinx.wave.open("%.2f-%.2f.wav"
                            % (seg.start_time, seg.end_time), "w") as wo:
                    wo.setframerate(w.getframerate())
                    wo.writeframesraw(seg.pcm)
        '''

PRED_DIR = "VremenskaPrognoza"
PRED_NUM = [i for i in range(1, 14)]

predictions_make("outputs3/", "my_db.lm.DMP", "tutorial3/model_parameters/my_db.cd_cont_200", PRED_DIR, PRED_NUM)
predictions_make("outputs3_pruned/", "my_db_pruned.lm.DMP", "tutorial3_pruned/model_parameters/my_db.cd_cont_200", PRED_DIR, PRED_NUM)
predictions_make("outputs3_only_weather/", "words_from_txt.lm.DMP", "tutorial3_weather/model_parameters/my_db.cd_cont_200", PRED_DIR, PRED_NUM)
predictions_make("outputs3_only_weather_pruned/", "words_from_txt_pruned.lm.DMP", "tutorial3_weather_pruned/model_parameters/my_db.cd_cont_200", PRED_DIR, PRED_NUM)
#predictions_make("outputs3_both/", "words_from_txt_word.lm.DMP", "tutorial3_both/model_parameters/my_db.cd_cont_200", PRED_DIR, PRED_NUM)
#predictions_make("outputs3_both_pruned/", "words_from_txt_word_pruned.lm.DMP", "tutorial3_both_pruned/model_parameters/my_db.cd_cont_200", PRED_DIR, PRED_NUM)

predictions_make("outputs3_only_weather_train/", "my_db_from_txt_train.lm.DMP", "tutorial3_weather_train/model_parameters/my_db.cd_cont_200", PRED_DIR, PRED_NUM)
predictions_make("outputs3_only_weather_train_pruned/", "my_db_from_txt_train_pruned.lm.DMP", "tutorial3_weather_train_pruned/model_parameters/my_db.cd_cont_200", PRED_DIR, PRED_NUM)
#predictions_make("outputs3_both_train/", "my_db_from_txt_word_train.lm.DMP", "tutorial3_both_train/model_parameters/my_db.cd_cont_200", PRED_DIR, PRED_NUM)
#predictions_make("outputs3_both_train_pruned/", "my_db_from_txt_word_train_pruned.lm.DMP", "tutorial3_both_train_pruned/model_parameters/my_db.cd_cont_200", PRED_DIR, PRED_NUM)
