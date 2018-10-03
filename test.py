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
END = 0x144F2F
count1 = 0
count2 = 1

def main():
    """ファイルを読み込む
    """
    with open('EXE6.gba','rb') as f:
        rom_data = f.read()
        
        #rom_data1 = rom_data[:0xF6BD6] + b'\x05' + rom_data[0xF6BD6+1:]
        #rom_data = rom_data[START + count1 : START + count2]
        rom_data = rom_data[START:END + 1]

        count = 0
        for i in rom_data:
            if i == b'\xab':
                print("ok")
                count += 1
        print(count)

        '''
        test = list(rom_data)
        #リストを2つの要素ずつ連結してサブリストを作る
        test2 = [test[i:i+2] for i in range(0,238,2)]
        print(test2)
        '''
        
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
