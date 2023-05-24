basedir = "/home/lucija/Documents/Zadnji semestar/ROGJ/Prezentacije/CMUspinx/"

all_fileids_test_file = open(basedir + "/my_db_test.fileids", "r") 
all_fileids_test_lines = all_fileids_test_file.readlines()
all_fileids_test_file.close()

all_fileids_train_file = open(basedir + "/my_db_train.fileids", "r") 
all_fileids_train_lines = all_fileids_train_file.readlines()
all_fileids_train_file.close()

print("my_db2")

all_fileids_test2_file = open(basedir + "/my_db2_test.fileids", "r") 
all_fileids_test2_lines = all_fileids_test2_file.readlines()
all_fileids_test2_file.close()

all_fileids_train2_file = open(basedir + "/my_db2_train.fileids", "r") 
all_fileids_train2_lines = all_fileids_train2_file.readlines()
all_fileids_train2_file.close()

aset = set()
bset = set()
abset = set()

for a in all_fileids_test_lines:
    if a in all_fileids_test2_lines:
        abset.add(a)
    else:
        aset.add(a)

for b in all_fileids_test2_lines:
    if b not in all_fileids_test_lines:
        bset.add(b)

print(len(aset), len(bset))
print("Test: Original:", len(all_fileids_test_lines), "New:", len(all_fileids_test2_lines))

aset = set()
bset = set()
abset = set()

for a in all_fileids_train_lines:
    if a in all_fileids_train2_lines:
        abset.add(a)
    else:
        aset.add(a)

for b in all_fileids_train2_lines:
    if b not in all_fileids_train_lines:
        bset.add(b)

print(len(aset), len(bset))
print("Train: Original:", len(all_fileids_train_lines), "New:", len(all_fileids_train2_lines))

print("my_db3")

all_fileids_test3_file = open(basedir + "/my_db3_test.fileids", "r") 
all_fileids_test3_lines = all_fileids_test3_file.readlines()
all_fileids_test3_file.close()

all_fileids_train3_file = open(basedir + "/my_db3_train.fileids", "r") 
all_fileids_train3_lines = all_fileids_train3_file.readlines()
all_fileids_train3_file.close()

aset = set()
bset = set()
abset = set()

for a in all_fileids_test_lines:
    if a in all_fileids_test3_lines:
        abset.add(a)
    else:
        aset.add(a)

for b in all_fileids_test3_lines:
    if b not in all_fileids_test_lines:
        bset.add(b)

print(len(aset), len(bset))
print("Test: Original:", len(all_fileids_test_lines), "New:", len(all_fileids_test3_lines))

aset = set()
bset = set()
abset = set()

for a in all_fileids_train_lines:
    if a in all_fileids_train3_lines:
        abset.add(a)
    else:
        aset.add(a)

for b in all_fileids_train3_lines:
    if b not in all_fileids_train_lines:
        bset.add(b)

print(len(aset), len(bset))
print("Train: Original:", len(all_fileids_train_lines), "New:", len(all_fileids_train3_lines))

print("my_db4")

all_fileids_test4_file = open(basedir + "/my_db4_test.fileids", "r") 
all_fileids_test4_lines = all_fileids_test4_file.readlines()
all_fileids_test4_file.close()

all_fileids_train4_file = open(basedir + "/my_db4_train.fileids", "r") 
all_fileids_train4_lines = all_fileids_train4_file.readlines()
all_fileids_train4_file.close()

aset = set()
bset = set()
abset = set()

for a in all_fileids_test_lines:
    if a in all_fileids_test4_lines:
        abset.add(a)
    else:
        aset.add(a)

for b in all_fileids_test4_lines:
    if b not in all_fileids_test_lines:
        bset.add(b)

print(len(aset), len(bset))
print("Test: Original:", len(all_fileids_test_lines), "New:", len(all_fileids_test4_lines))

aset = set()
bset = set()
abset = set()

for a in all_fileids_train_lines:
    if a in all_fileids_train4_lines:
        abset.add(a)
    else:
        aset.add(a)

for b in all_fileids_train4_lines:
    if b not in all_fileids_train_lines:
        bset.add(b)

print(len(aset), len(bset))
print("Train: Original:", len(all_fileids_train_lines), "New:", len(all_fileids_train4_lines))

print("my_db5")

all_fileids_test5_file = open(basedir + "/my_db5_test.fileids", "r") 
all_fileids_test5_lines = all_fileids_test5_file.readlines()
all_fileids_test5_file.close()

all_fileids_train5_file = open(basedir + "/my_db5_train.fileids", "r") 
all_fileids_train5_lines = all_fileids_train5_file.readlines()
all_fileids_train5_file.close()

aset = set()
bset = set()
abset = set()

for a in all_fileids_test_lines:
    if a in all_fileids_test5_lines:
        abset.add(a)
    else:
        aset.add(a)

for b in all_fileids_test5_lines:
    if b not in all_fileids_test_lines:
        bset.add(b)

print(len(aset), len(bset))
print("Test: Original:", len(all_fileids_test_lines), "New:", len(all_fileids_test5_lines))

aset = set()
bset = set()
abset = set()

for a in all_fileids_train_lines:
    if a in all_fileids_train5_lines:
        abset.add(a)
    else:
        aset.add(a)

for b in all_fileids_train5_lines:
    if b not in all_fileids_train_lines:
        bset.add(b)

print(len(aset), len(bset))
print("Train: Original:", len(all_fileids_train_lines), "New:", len(all_fileids_train5_lines))

print("my_db6")

all_fileids_test6_file = open(basedir + "/my_db6_test.fileids", "r") 
all_fileids_test6_lines = all_fileids_test6_file.readlines()
all_fileids_test6_file.close()

all_fileids_train6_file = open(basedir + "/my_db6_train.fileids", "r") 
all_fileids_train6_lines = all_fileids_train6_file.readlines()
all_fileids_train6_file.close()

aset = set()
bset = set()
abset = set()

for a in all_fileids_test_lines:
    if a in all_fileids_test6_lines:
        abset.add(a)
    else:
        aset.add(a)

for b in all_fileids_test6_lines:
    if b not in all_fileids_test_lines:
        bset.add(b)

print(len(aset), len(bset))
print("Test: Original:", len(all_fileids_test_lines), "New:", len(all_fileids_test6_lines))

aset = set()
bset = set()
abset = set()

for a in all_fileids_train_lines:
    if a in all_fileids_train6_lines:
        abset.add(a)
    else:
        aset.add(a)

for b in all_fileids_train6_lines:
    if b not in all_fileids_train_lines:
        bset.add(b)

print(len(aset), len(bset))
print("Train: Original:", len(all_fileids_train_lines), "New:", len(all_fileids_train6_lines))