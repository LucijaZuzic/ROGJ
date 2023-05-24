import os
import wave
import numpy as np 

basedir = "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/"
dirnames = ["z04", "VremenskaPrognoza", "a", "prvi", "hrt", "sz04", "sz08", "other", "all", "noTV"]

samples = [13]

for sample_num in samples:

	test_sum_len = dict()
	test_sum_words = dict()
	test_sum_chars = dict()
	test_sum_chars_no_space = dict()
	test_num_sentences = dict()

	train_sum_len = dict()
	train_sum_words = dict()
	train_sum_chars = dict()
	train_sum_chars_no_space = dict()
	train_num_sentences = dict()
		
	for dirname in dirnames:
		test_sum_len[dirname] = 0
		test_sum_words[dirname] = 0
		test_sum_chars[dirname] = 0
		test_sum_chars_no_space[dirname] = 0
		test_num_sentences[dirname] = 0
		
		train_sum_len[dirname] = 0
		train_sum_words[dirname] = 0
		train_sum_chars[dirname] = 0
		train_sum_chars_no_space[dirname] = 0
		train_num_sentences[dirname] = 0
		
	filename_transcript_test = basedir + "my_db" + str(sample_num) + "_test.transcription"
	file_transcript_test = open(filename_transcript_test, "r")
	lines_transcript_test = file_transcript_test.readlines()
	file_transcript_test.close()
	
	filename_transcript_train = basedir + "my_db" + str(sample_num) + "_train.transcription"
	file_transcript_train = open(filename_transcript_train, "r")
	lines_transcript_train = file_transcript_train.readlines()
	file_transcript_train.close()
	
	filename_list_test = basedir + "my_db" + str(sample_num) + "_test.fileids"
	file_list_test = open(filename_list_test, "r")
	lines_list_test = file_list_test.readlines()
	file_list_test.close()
	
	filename_list_train = basedir + "my_db" + str(sample_num) + "_train.fileids"
	file_list_train = open(filename_list_train, "r")
	lines_list_train = file_list_train.readlines()
	file_list_train.close()  
	
	for filesome in os.listdir(basedir + "tutorial" + str(sample_num) + "/wav/sz04/"):
		filename = basedir + "tutorial" + str(sample_num) + "/wav/sz04/" + filesome
		mywav = wave.open(filename)  
		duration_seconds = mywav.getnframes() / mywav.getframerate()
		filenameline = basedir + "all_outputs/outputs" + str(sample_num) + "/sz04/" + filesome.replace(".wav", "_original.txt")
		linesfile = open(filenameline, "r") 
		line = linesfile.readlines()[0].replace("\n", "")
		linesfile.close()
		words = line.split(" ") 
		
		class_of_file = "sz04"
			
		if class_of_file not in test_sum_len:
			test_sum_len[class_of_file] = duration_seconds
			test_sum_words[class_of_file] = len(words)
			test_sum_chars[class_of_file] = len(line)
			test_sum_chars_no_space[class_of_file] = len(line.replace(" ", ""))
			test_num_sentences[class_of_file] = 1
		else:		
			test_sum_len[class_of_file] += duration_seconds
			test_sum_words[class_of_file] += len(words)
			test_sum_chars[class_of_file] += len(line)
			test_sum_chars_no_space[class_of_file] += len(line.replace(" ", ""))
			test_num_sentences[class_of_file] += 1
			
		if class_of_file not in dirnames: 
			class_of_file = "other" 
			
			if class_of_file not in test_sum_len:
				test_sum_len[class_of_file] = duration_seconds
				test_sum_words[class_of_file] = len(words)
				test_sum_chars[class_of_file] = len(line)
				test_sum_chars_no_space[class_of_file] = len(line.replace(" ", ""))
				test_num_sentences[class_of_file] = 1
			else:		
				test_sum_len[class_of_file] += duration_seconds
				test_sum_words[class_of_file] += len(words)
				test_sum_chars[class_of_file] += len(line)
				test_sum_chars_no_space[class_of_file] += len(line.replace(" ", ""))
				test_num_sentences[class_of_file] += 1
		
		class_of_file = "all" 
			
		if class_of_file not in test_sum_len:
			test_sum_len[class_of_file] = duration_seconds
			test_sum_words[class_of_file] = len(words)
			test_sum_chars[class_of_file] = len(line)
			test_sum_chars_no_space[class_of_file] = len(line.replace(" ", ""))
			test_num_sentences[class_of_file] = 1
		else:		
			test_sum_len[class_of_file] += duration_seconds
			test_sum_words[class_of_file] += len(words)
			test_sum_chars[class_of_file] += len(line)
			test_sum_chars_no_space[class_of_file] += len(line.replace(" ", ""))
			test_num_sentences[class_of_file] += 1  
			
		class_of_file = "noTV" 
			
		if class_of_file not in test_sum_len:
			test_sum_len[class_of_file] = duration_seconds
			test_sum_words[class_of_file] = len(words)
			test_sum_chars[class_of_file] = len(line)
			test_sum_chars_no_space[class_of_file] = len(line.replace(" ", ""))
			test_num_sentences[class_of_file] = 1
		else:		
			test_sum_len[class_of_file] += duration_seconds
			test_sum_words[class_of_file] += len(words)
			test_sum_chars[class_of_file] += len(line)
			test_sum_chars_no_space[class_of_file] += len(line.replace(" ", ""))
			test_num_sentences[class_of_file] += 1 
			
	for filesome in os.listdir(basedir + "tutorial" + str(sample_num) + "/wav/z04/"):
		filename = basedir + "tutorial" + str(sample_num) + "/wav/z04/" + filesome
		mywav = wave.open(filename)  
		duration_seconds = mywav.getnframes() / mywav.getframerate()
		filenameline = basedir + "all_outputs/outputs" + str(sample_num) + "/z04/" + filesome.replace(".wav", "_original.txt")
		linesfile = open(filenameline, "r") 
		line = linesfile.readlines()[0].replace("\n", "")
		linesfile.close()
		words = line.split(" ") 
		
		class_of_file = "z04"
			
		if class_of_file not in test_sum_len:
			test_sum_len[class_of_file] = duration_seconds
			test_sum_words[class_of_file] = len(words)
			test_sum_chars[class_of_file] = len(line)
			test_sum_chars_no_space[class_of_file] = len(line.replace(" ", ""))
			test_num_sentences[class_of_file] = 1
		else:		
			test_sum_len[class_of_file] += duration_seconds
			test_sum_words[class_of_file] += len(words)
			test_sum_chars[class_of_file] += len(line)
			test_sum_chars_no_space[class_of_file] += len(line.replace(" ", ""))
			test_num_sentences[class_of_file] += 1
			
		if class_of_file not in dirnames: 
			class_of_file = "other" 
			
			if class_of_file not in test_sum_len:
				test_sum_len[class_of_file] = duration_seconds
				test_sum_words[class_of_file] = len(words)
				test_sum_chars[class_of_file] = len(line)
				test_sum_chars_no_space[class_of_file] = len(line.replace(" ", ""))
				test_num_sentences[class_of_file] = 1
			else:		
				test_sum_len[class_of_file] += duration_seconds
				test_sum_words[class_of_file] += len(words)
				test_sum_chars[class_of_file] += len(line)
				test_sum_chars_no_space[class_of_file] += len(line.replace(" ", ""))
				test_num_sentences[class_of_file] += 1
		
		class_of_file = "all" 
			
		if class_of_file not in test_sum_len:
			test_sum_len[class_of_file] = duration_seconds
			test_sum_words[class_of_file] = len(words)
			test_sum_chars[class_of_file] = len(line)
			test_sum_chars_no_space[class_of_file] = len(line.replace(" ", ""))
			test_num_sentences[class_of_file] = 1
		else:		
			test_sum_len[class_of_file] += duration_seconds
			test_sum_words[class_of_file] += len(words)
			test_sum_chars[class_of_file] += len(line)
			test_sum_chars_no_space[class_of_file] += len(line.replace(" ", ""))
			test_num_sentences[class_of_file] += 1 
			 
		class_of_file = "noTV" 
			
		if class_of_file not in test_sum_len:
			test_sum_len[class_of_file] = duration_seconds
			test_sum_words[class_of_file] = len(words)
			test_sum_chars[class_of_file] = len(line)
			test_sum_chars_no_space[class_of_file] = len(line.replace(" ", ""))
			test_num_sentences[class_of_file] = 1
		else:		
			test_sum_len[class_of_file] += duration_seconds
			test_sum_words[class_of_file] += len(words)
			test_sum_chars[class_of_file] += len(line)
			test_sum_chars_no_space[class_of_file] += len(line.replace(" ", ""))
			test_num_sentences[class_of_file] += 1 
	
	for line_num in range(len(lines_list_test)):
		filename = basedir + "tutorial" + str(sample_num) + "/wav/" + lines_list_test[line_num].replace("\n", ".wav") 
		mywav = wave.open(filename)  
		duration_seconds = mywav.getnframes() / mywav.getframerate()
		line = lines_transcript_test[line_num][4:lines_transcript_test[line_num].find("</s> (")]
		words = line.split(" ") 
		
		class_of_file = lines_list_test[line_num].split("/")[0] 
		
		if class_of_file[0] == "a":
			class_of_file = "a" 
			
		if class_of_file[0] == "V":
			class_of_file = "VremenskaPrognoza" 
			
		if class_of_file not in test_sum_len:
			test_sum_len[class_of_file] = duration_seconds
			test_sum_words[class_of_file] = len(words)
			test_sum_chars[class_of_file] = len(line)
			test_sum_chars_no_space[class_of_file] = len(line.replace(" ", ""))
			test_num_sentences[class_of_file] = 1
		else:		
			test_sum_len[class_of_file] += duration_seconds
			test_sum_words[class_of_file] += len(words)
			test_sum_chars[class_of_file] += len(line)
			test_sum_chars_no_space[class_of_file] += len(line.replace(" ", ""))
			test_num_sentences[class_of_file] += 1
			
		if class_of_file not in dirnames: 
			class_of_file = "other" 
			
			if class_of_file not in test_sum_len:
				test_sum_len[class_of_file] = duration_seconds
				test_sum_words[class_of_file] = len(words)
				test_sum_chars[class_of_file] = len(line)
				test_sum_chars_no_space[class_of_file] = len(line.replace(" ", ""))
				test_num_sentences[class_of_file] = 1
			else:		
				test_sum_len[class_of_file] += duration_seconds
				test_sum_words[class_of_file] += len(words)
				test_sum_chars[class_of_file] += len(line)
				test_sum_chars_no_space[class_of_file] += len(line.replace(" ", ""))
				test_num_sentences[class_of_file] += 1
		
		class_of_file = "all" 
			
		if class_of_file not in test_sum_len:
			test_sum_len[class_of_file] = duration_seconds
			test_sum_words[class_of_file] = len(words)
			test_sum_chars[class_of_file] = len(line)
			test_sum_chars_no_space[class_of_file] = len(line.replace(" ", ""))
			test_num_sentences[class_of_file] = 1
		else:		
			test_sum_len[class_of_file] += duration_seconds
			test_sum_words[class_of_file] += len(words)
			test_sum_chars[class_of_file] += len(line)
			test_sum_chars_no_space[class_of_file] += len(line.replace(" ", ""))
			test_num_sentences[class_of_file] += 1 
			
		if lines_list_test[line_num].split("/")[0] != "hrt": 
		
			class_of_file = "noTV" 
			
			if class_of_file not in test_sum_len:
				test_sum_len[class_of_file] = duration_seconds
				test_sum_words[class_of_file] = len(words)
				test_sum_chars[class_of_file] = len(line)
				test_sum_chars_no_space[class_of_file] = len(line.replace(" ", ""))
				test_num_sentences[class_of_file] = 1
			else:		
				test_sum_len[class_of_file] += duration_seconds
				test_sum_words[class_of_file] += len(words)
				test_sum_chars[class_of_file] += len(line)
				test_sum_chars_no_space[class_of_file] += len(line.replace(" ", ""))
				test_num_sentences[class_of_file] += 1 
			
	for line_num in range(len(lines_list_train)):
		filename = basedir + "tutorial" + str(sample_num) + "/wav/" + lines_list_train[line_num].replace("\n", ".wav") 
		mywav = wave.open(filename)  
		duration_seconds = mywav.getnframes() / mywav.getframerate()
		line = lines_transcript_train[line_num][4:lines_transcript_train[line_num].find("</s> (")]
		words = line.split(" ")  
		
		class_of_file = lines_list_train[line_num].split("/")[0] 
		
		if class_of_file[0] == "a":
			class_of_file = "a" 
			
		if class_of_file[0] == "V":
			class_of_file = "VremenskaPrognoza" 
			
		if class_of_file not in train_sum_len.keys():
			train_sum_len[class_of_file] = duration_seconds
			train_sum_words[class_of_file] = len(words)
			train_sum_chars[class_of_file] = len(line)
			train_sum_chars_no_space[class_of_file] = len(line.replace(" ", ""))
			train_num_sentences[class_of_file] = 1
		else:		
			train_sum_len[class_of_file] += duration_seconds
			train_sum_words[class_of_file] += len(words)
			train_sum_chars[class_of_file] += len(line)
			train_sum_chars_no_space[class_of_file] += len(line.replace(" ", ""))
			train_num_sentences[class_of_file] += 1
			
		if class_of_file not in dirnames: 
			class_of_file = "other" 
			
			if class_of_file not in train_sum_len.keys():
				train_sum_len[class_of_file] = duration_seconds
				train_sum_words[class_of_file] = len(words)
				train_sum_chars[class_of_file] = len(line)
				train_sum_chars_no_space[class_of_file] = len(line.replace(" ", ""))
				train_num_sentences[class_of_file] = 1
			else:		
				train_sum_len[class_of_file] += duration_seconds
				train_sum_words[class_of_file] += len(words)
				train_sum_chars[class_of_file] += len(line)
				train_sum_chars_no_space[class_of_file] += len(line.replace(" ", ""))
				train_num_sentences[class_of_file] += 1
			
		class_of_file = "all"
			
		if class_of_file not in train_sum_len.keys():
			train_sum_len[class_of_file] = duration_seconds
			train_sum_words[class_of_file] = len(words)
			train_sum_chars[class_of_file] = len(line)
			train_sum_chars_no_space[class_of_file] = len(line.replace(" ", ""))
			train_num_sentences[class_of_file] = 1
		else:		
			train_sum_len[class_of_file] += duration_seconds
			train_sum_words[class_of_file] += len(words)
			train_sum_chars[class_of_file] += len(line)
			train_sum_chars_no_space[class_of_file] += len(line.replace(" ", ""))
			train_num_sentences[class_of_file] += 1
			
		if lines_list_train[line_num].split("/")[0] != "hrt": 
			
			class_of_file = "noTV" 
				
			if class_of_file not in train_sum_len.keys():
				train_sum_len[class_of_file] = duration_seconds
				train_sum_words[class_of_file] = len(words)
				train_sum_chars[class_of_file] = len(line)
				train_sum_chars_no_space[class_of_file] = len(line.replace(" ", ""))
				train_num_sentences[class_of_file] = 1
			else:		
				train_sum_len[class_of_file] += duration_seconds
				train_sum_words[class_of_file] += len(words)
				train_sum_chars[class_of_file] += len(line)
				train_sum_chars_no_space[class_of_file] += len(line.replace(" ", ""))
				train_num_sentences[class_of_file] += 1
		
for class_of_file in train_sum_len.keys(): 
	if class_of_file not in test_sum_len:
		test_sum_len[class_of_file] = 0
		test_sum_words[class_of_file] = 0
		test_sum_chars[class_of_file] = 0
		test_sum_chars_no_space[class_of_file] = 0
		test_num_sentences[class_of_file] = 0
	
def time_format(times):
	times = float(times) 
	timesec = int(times)
	hours = timesec // 3600
	minutes = (timesec - hours * 3600) // 60
	seconds = timesec % 60
	rest = times - timesec 
	return str(hours) + " h " + str(minutes) + " m " + str(seconds + np.round(rest, 2)) + " s"
			
for dirname in train_sum_len.keys(): 
	print(dirname, "&", time_format(test_sum_len[dirname]), "&", time_format(train_sum_len[dirname]), "&", 
	test_num_sentences[dirname], "&", train_num_sentences[dirname], "&", 
	test_sum_words[dirname], "&", train_sum_words[dirname], "&", 
	#test_sum_chars[dirname], "&", train_sum_chars[dirname], "&", 
	test_sum_chars_no_space[dirname], "&", train_sum_chars_no_space[dirname], "\\\\ \\hline")  
	
for dirname in train_sum_len.keys(): 
	print(dirname, "&", time_format(test_sum_len[dirname]), "&",
	test_num_sentences[dirname], "&", 
	test_sum_words[dirname], "&", 
	#test_sum_chars[dirname], "&", 
	test_sum_chars_no_space[dirname], "\\\\ \\hline") 
	
for dirname in train_sum_len.keys(): 
	print(dirname, "&", time_format(train_sum_len[dirname]), "&", 
	train_num_sentences[dirname], "&", 
	train_sum_words[dirname], "&", 
	#train_sum_chars[dirname], "&", 
	train_sum_chars_no_space[dirname], "\\\\ \\hline") 
	
for dirname in train_sum_len.keys(): 
	print(dirname, "&", time_format(test_sum_len[dirname] + train_sum_len[dirname]), "&", 
	test_num_sentences[dirname] + train_num_sentences[dirname], "&", 
	test_sum_words[dirname] + train_sum_words[dirname], "&", 
	#test_sum_chars[dirname] + train_sum_chars[dirname], "&", 
	test_sum_chars_no_space[dirname] + train_sum_chars_no_space[dirname], "\\\\ \\hline")  
