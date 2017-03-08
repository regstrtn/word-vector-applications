import random
import os
import sys

path = "./Q1/wordRep/pairs_from_wordnet/"

def writeanalogyfile(path):
    filelist = os.listdir(path)
    #print(filelist)
    fout = open('analogy_dataset.txt', 'w')
    for file in filelist:
        alist = []
        qfile = open(path+file, 'r')
        qlist = [line.strip() for line in qfile]
        for otherfiles in filelist:
            if(file != otherfiles):
                f = open(path+otherfiles, 'r')
                l = [line.strip() for line in f]
                #print(file, otherfiles, len(l))
                alist.extend(l)
        for q in qlist:
            option = random.randint(0,4)
            output = [None]*7
            output[0] = q
            optionpos = random.randint(0, len(qlist)-1)
            output[option+1] = qlist[optionpos]
            output[6] = chr(ord('a')+option)
            for i in range(1, 6):
                randop = random.randint(0, len(alist)-1)
                if(i!=option+1):
                    output[i] = alist[randop]
            for pair in output:
                pair = pair.replace('\t', ' ')
                fout.write(pair+'\n')
            fout.write('\n\n')
            fout.flush()

writeanalogyfile(path)
