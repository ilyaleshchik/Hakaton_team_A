import os
import sys

FILES = []

"""
В Inputs кидаете файлы для вырезки, запускаете прогу, для каждого ввоидите промежуток
В Outputs будут резы

"""

def GetFiles():
    global FILES
    FILES = [f for f in os.listdir("Inputs") if os.path.isfile(os.path.join("Inputs", f))]


def main():
    global FILES
    GetFiles()
    for FILE in FILES:
        os.chdir("Inputs")
        fin = open(FILE, "r")
        os.chdir("../")
        os.chdir("Outputs")
        fout = open(FILE, "w")
        os.chdir("../")
        line = fin.readline()
       # out.write(line + "\n")
        line = fin.readline()
       # print(line)
        print(FILE)
        l = int(input("Левая граница: "))
        r = int(input("Правая граница: "))
        ans = line[l - 1: r]
        fout.write(ans + "\n")




if __name__ == '__main__':
    main()