import numpy as np

model_name = ["Expanded weather", "Expanded weather and new source", "Expanded weather and alka", "Expanded weather, new source and alka", "Expanded no TV", "Expanded all sources"]
model_num = [8, 7, 11, 10, 15, 13]
number2 = model_num[-1]
for i in range(len(model_name)): 
	line_string = "./ngram -lm my_db_from_txt_word_train" + str(model_num[i]) + '.lm -ppl "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/words_from_txt_word_test' + str(number2) + '.txt"'
	print(line_string)
	
'''
(base) lucija@lucija-B450-GAMING-X:~/Downloads/srilm-1.7.3/bin/i686-m64$ ./ngram -lm my_db_from_txt_word_train8.lm -ppl "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/words_from_txt_test13.txt"
file /home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/words_from_txt_test13.txt: 38 sentences, 749 words, 4 OOVs
0 zeroprobs, logprob= -1945.949 ppl= 305.6665 ppl1= 409.2722
(base) lucija@lucija-B450-GAMING-X:~/Downloads/srilm-1.7.3/bin/i686-m64$ ./ngram -lm my_db_from_txt_word_train7.lm -ppl "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/words_from_txt_test13.txt"
file /home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/words_from_txt_test13.txt: 38 sentences, 749 words, 1 OOVs
0 zeroprobs, logprob= -1877.65 ppl= 244.8316 ppl1= 323.7629
(base) lucija@lucija-B450-GAMING-X:~/Downloads/srilm-1.7.3/bin/i686-m64$ ./ngram -lm my_db_from_txt_word_train11.lm -ppl "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/words_from_txt_test13.txt"
file /home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/words_from_txt_test13.txt: 38 sentences, 749 words, 14 OOVs
0 zeroprobs, logprob= -2283.565 ppl= 899.8266 ppl1= 1279.06
(base) lucija@lucija-B450-GAMING-X:~/Downloads/srilm-1.7.3/bin/i686-m64$ ./ngram -lm my_db_from_txt_word_train10.lm -ppl "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/words_from_txt_test13.txt"
file /home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/words_from_txt_test13.txt: 38 sentences, 749 words, 14 OOVs
0 zeroprobs, logprob= -2283.565 ppl= 899.8266 ppl1= 1279.06
(base) lucija@lucija-B450-GAMING-X:~/Downloads/srilm-1.7.3/bin/i686-m64$ ./ngram -lm my_db_from_txt_word_train15.lm -ppl "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/words_from_txt_test13.txt"
file /home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/words_from_txt_test13.txt: 38 sentences, 749 words, 14 OOVs
0 zeroprobs, logprob= -2270.851 ppl= 866.3873 ppl1= 1229.119
(base) lucija@lucija-B450-GAMING-X:~/Downloads/srilm-1.7.3/bin/i686-m64$ ./ngram -lm my_db_from_txt_word_train13.lm -ppl "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/words_from_txt_test13.txt"
file /home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/words_from_txt_test13.txt: 38 sentences, 749 words, 14 OOVs
0 zeroprobs, logprob= -2270.851 ppl= 866.3873 ppl1= 1229.119

words = 749
ppls = [305.6665, 244.8316, 899.8266, 899.8266, 866.3873, 866.3873]
ppls1 = [409.2722, 323.7629, 1279.06, 1279.06, 1229.119, 1229.119]
logs = [-1945.949, -1877.65, -2283.565, -2283.565, -2270.851, -2270.851]

file /home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/words_from_txt_word_test13.txt: 1571616 sentences, 47465849 words, 4 OOVs
0 zeroprobs, logprob= -1.096776e+08 ppl= 172.4284 ppl1= 204.4861
file /home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/words_from_txt_word_test13.txt: 1571616 sentences, 47465849 words, 1 OOVs
0 zeroprobs, logprob= -1.096781e+08 ppl= 172.4321 ppl1= 204.4907
file /home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/words_from_txt_word_test13.txt: 1571616 sentences, 47465849 words, 14 OOVs
0 zeroprobs, logprob= -1.096785e+08 ppl= 172.436 ppl1= 204.4955
file /home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/words_from_txt_word_test13.txt: 1571616 sentences, 47465849 words, 14 OOVs
0 zeroprobs, logprob= -1.096785e+08 ppl= 172.436 ppl1= 204.4955
file /home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/words_from_txt_word_test13.txt: 1571616 sentences, 47465849 words, 14 OOVs
0 zeroprobs, logprob= -1.096874e+08 ppl= 172.5078 ppl1= 204.5835
file /home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/words_from_txt_word_test13.txt: 1571616 sentences, 47465849 words, 14 OOVs
0 zeroprobs, logprob= -1.096874e+08 ppl= 172.5078 ppl1= 204.5835 
'''

words = 47465849
ppls = [172.4284, 172.4321, 172.436, 172.436, 172.5078, 172.5078]
ppls1 = [204.4861, 204.4907, 204.4955, 204.4955, 204.5835, 204.5835]
logs = [-1.096776 * (10 ** 8), -1.096781 * (10 ** 8), -1.096785 * (10 ** 8), -1.096785 * (10 ** 8), -1.096874 * (10 ** 8), -1.096874 * (10 ** 8)]

words = 749
ppls = [305.6665, 244.8316, 899.8266, 899.8266, 866.3873, 866.3873]
ppls1 = [409.2722, 323.7629, 1279.06, 1279.06, 1229.119, 1229.119]
logs = [-1945.949, -1877.65, -2283.565, -2283.565, -2270.851, -2270.851]

entropy = [- logval / words for logval in logs]
ppl_new = [2 ** (- logval / words) for logval in logs]

stringp = ""

for i in range(len(ppls)): 
	stringp += str(np.round(float(ppls[i]), 2))
	if i != len(ppls) - 1:
		stringp += " & "
	else:
		stringp += " \\\\ \\hline\n"
		
for i in range(len(ppls1)): 
	stringp += str(np.round(float(ppls1[i]), 2))
	if i != len(ppls1) - 1:
		stringp += " & "
	else:
		stringp += " \\\\ \\hline\n"
		 
for i in range(len(logs)): 
	stringp += str(np.round(float(logs[i]), 2))
	if i != len(logs) - 1:
		stringp += " & "
	else:
		stringp += " \\\\ \\hline\n" 

for i in range(len(entropy)): 
	stringp += str(np.round(float(entropy[i]), 2))
	if i != len(entropy) - 1:
		stringp += " & "
	else:
		stringp += " \\\\ \\hline\n"
		
for i in range(len(ppl_new)): 
	stringp += str(np.round(float(ppl_new[i]), 2))
	if i != len(ppl_new) - 1:
		stringp += " & "
	else:
		stringp += " \\\\ \\hline\n"
		
print(stringp)
