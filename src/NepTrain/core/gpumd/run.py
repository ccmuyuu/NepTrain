#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2024/10/29 15:06
# @Author  : 兵
# @email    : 1747193328@qq.com

import os.path

from ase import Atoms
from ase.io import read as ase_read
from ase.io import write as ase_write

from NepTrain import utils
from ..select import select_structures, filter_by_bonds
from .io import RunInput
from .plot import plot_md_selected
from ..utils import check_env

atoms_index = 0

@utils.iter_path_to_atoms(["*.vasp","*.xyz"],show_progress=False)
def calculate_gpumd(atoms:Atoms,argparse):
    global atoms_index
    atoms_index+=1

    new_atoms=[]


    for temperature in argparse.temperature:

        run = RunInput(argparse.nep_txt_path)
        run.read_run(argparse.run_in_path)
        run.set_time_temp(argparse.time,temperature)
        directory=os.path.join(argparse.directory,f"{atoms_index}-{atoms.symbols}@{temperature}k-{argparse.time}ps")
        utils.print_msg(f"GPUMD is running, temperature: {temperature}k. Time: {argparse.time*run.time_step}ps" )

        run.calculate(atoms,directory)

        dump = ase_read(os.path.join(directory,"dump.xyz"), ":", format="extxyz", do_not_split_by_at_sign=True)
        for i, atom in enumerate(dump):
            atom.info["Config_type"] = f"{atom.symbols}-epoch-{argparse.time}ps-{temperature}k-{i + 1}"


        if argparse.filter:
            good,bad=filter_by_bonds(dump,model=atoms)
            dump=good
            ase_write(os.path.join(directory,"remove_by_bond_structures.xyz"),bad)
        ase_write(argparse.out_file_path,dump,append=True)

        continue


        selected = select_structures(trainxyz + new_atoms,
                                     dump,
                                     os.path.join(directory,"nep.txt"),
                                     max_selected=max_selected,
                                     min_distance=min_distance,
                                     )



        utils.print_msg(f"得到{len(selected)}个结构" )

        for i, atom in enumerate(selected):
            atom.info["Config_type"] = f"{atom.symbols}-epoch-{argparse.time}ps-{temperature}k-{i + 1}"
        new_atoms.extend(selected)
        ase_write(os.path.join(directory,"selected.xyz"),selected)

        plot_md_selected(argparse.train_xyz_path,
                         os.path.join(directory, "dump.xyz"),
                         os.path.join(directory, "selected.xyz"),
                         os.path.join(directory, "nep.txt"),
                         os.path.join(directory, "selected.png"),

                         )

    utils.print_msg(f"结构：{atoms.symbols}，本次主动学习共得到{len(new_atoms)}个结构")


    return new_atoms
def run_gpumd(argparse):
    check_env()
    utils.verify_path(os.path.dirname(argparse.out_file_path))
    result = calculate_gpumd(argparse.model_path,argparse)









