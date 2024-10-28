#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2024/10/24 15:42
# @Author  : 兵
# @email    : 1747193328@qq.com
import os
import re
import shutil
import subprocess

from ase.data import chemical_symbols, atomic_numbers
from NepTrain import utils,Config

class RunInput:

    def __init__(self,train_xyz_path,nep_in_path=None,test_xyz_path=None):
        self.nep_in_path = nep_in_path
        self.train_xyz_path = train_xyz_path
        self.test_xyz_path = test_xyz_path
        self.run_in={}
        if self.nep_in_path is not None:
            self.read_run(self.nep_in_path)
        self.command=Config.get('environ','nep_path')
    def read_run(self,file_name):
        with open(file_name,'r',encoding="utf8") as f:
            groups=re.findall("(\w+)\s+(.*?)\n",f.read()+"\n")

            for group in groups:
                self.run_in[group[0]]=group[1]

    def build_run(self):
        """
        如果runin 不存在 就遍历训练集  然后找出所有的元素

        :return:
        """
        if os.path.exists(self.train_xyz_path):
            with open(self.train_xyz_path,'r',encoding="utf8") as f:
                trainxyz=f.read()
            groups=re.findall("^([A-Z][a-z]?)\s+",trainxyz,  re.MULTILINE)
            groups=set(groups)
            symbols=[]
            for symbol in groups:
                if symbol in chemical_symbols:
                    symbols.append(symbol)

            symbols = sorted(symbols,key=lambda x:atomic_numbers[x])

            self.run_in["type"]=f"{len(symbols)} {' '.join(symbols)}"

    def write_run(self,file_name):
        if  "type" not in   self.run_in :
            self.build_run()
        with open(file_name,'w',encoding="utf8") as f:
            for k,v in self.run_in.items():

                f.write(f"{k}     {v}\n" )


    def calculate(self,directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.write_run(os.path.join(directory,"nep.in"))
        shutil.copy(self.train_xyz_path,os.path.join(directory,"train.xyz"))
        if self.test_xyz_path is not None:
            shutil.copy(self.test_xyz_path, os.path.join(directory, "test.xyz"))

        with utils.cd(directory), open("nep.out", "w") as f_std, open("nep.err", "w", buffering=1) as f_err:
            subprocess.check_call(self.command, stdout=f_std, stderr=f_err )


class PredictionRunInput(RunInput):
    def __init__(self,*args,**kwargs):
        pass
        super().__init__(*args,**kwargs)

    def write_run(self,file_name):

        self.run_in["prediction"]=1
        super().write_run(file_name)

if __name__ == '__main__':
    run=RunInput("../../cli/train.xyz")
    # run.read_run("./nep.in")
    run.write_run("./nep.out")
    run.calculate("./")