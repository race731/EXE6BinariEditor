#!/usr/bin/python
# coding: utf-8
#! python3

import argparse #コマンドラインのためのもの
import os
from logging import getLogger, StreamHandler, INFO
import struct
import sys

#読み込みROM
romdata = b""

#書き出しROM
bindata = b""

writepath = "./mod.bin"
START = 0x144867
END = 0x144F33
count1 = 0
count2 = 1

datalist = []
def main():
    """ファイルを読み込む
    """
    with open('EXE6.bin','rb') as f:
        rom_data = f.read()
        offsetc = 0
        #rom_data1 = rom_data[:0xF6BD6] + b'\x05' + rom_data[0xF6BD6+1:]

        #改造カードのデータをスライス
        mod_data = rom_data[START:END + 1]
        print(type(mod_data))
        for i in mod_data:
            offsetc += 1
            if i == 0xAB:
                datalist = rom_data[START : START + offsetc]
                print(datalist)
                break


        
def writef(f):
    with open(writepath, "wb") as writeFile:

        writeFile.write(f)

def joinb(f):
    mojiretu = ""
    for x in f:
        mojiretu += x
    writef(mojiretu)


if __name__ == '__main__':
    main()
