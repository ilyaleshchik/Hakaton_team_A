import os
import sys

FILES = []


def GetFiles():
    global FILES
    FILES = [f for f in os.listdir("Inputs") if os.path.isfile(os.path.join("Inputs", f))]


def main():
    GetFiles()
    global FILES
    for FILE in FILES:
        os.chdir("Inputs")
        fin = open(FILE, "r")
        os.chdir("../")
        os.chdir("Outputs")
        fout = open(FILE, "w")
        os.chdir("../")
        tmp = ""
        for line in fin.readlines():
            a = line.split(' ')
            b = [x for x in a if x != '']
            tmp += b[1]
            if(b[2] == 'S'):
                if(len(tmp) > 5):
                    fout.write(tmp + "\n")
                tmp = ""
        if(len(tmp) > 5):
            fout.write(tmp + "\n")
        tmp = ""



if __name__ == '__main__':
    main()