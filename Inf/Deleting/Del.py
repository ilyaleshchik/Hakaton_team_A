import os 
import sys

FILE_NAMES = ["USA.MD", "Australi", "Mexico", "Serbia", "USA", "USA.FL", "USA.Washington"]
FILE_FORMAT = ".fasta"


def GetFile(name):
    os.chdir("Inputs")
    ret = open(name, "r")
    os.chdir("../")
    return ret  


def main():
    Tp = {}
    for FILE_NAME in FILE_NAMES:
        CURFILE = FILE_NAME + FILE_FORMAT
        In = GetFile(CURFILE)
        cnt = 0
        for line in In.readlines():
            tmp = ""
            if line[0] != '>':
                continue
            i = 0
            cnt += 1
            while(line[i] != ' '):
                tmp += line[i]
                i += 1
            Tp[tmp] = 1
        print(cnt)
    os.chdir("Outputs")
    out = open("Ids.txt", "w")
    for t in Tp:
        out.write(t + "\n")
            

if __name__ == '__main__':
    main()