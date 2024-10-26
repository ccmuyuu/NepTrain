#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2024/10/24 16:22
# @Author  : 兵
# @email    : 1747193328@qq.com
import configparser
import os
import shutil
from NepTrain import utils
from ase.calculators.vasp.setups import setups_defaults
config_path = utils.get_config_path()

current_path = os.path.dirname(__file__)

if not os.path.exists(config_path)  :
    shutil.copy(os.path.join(current_path,"config.ini"), config_path)

Config = configparser.RawConfigParser()
Config.read(config_path,encoding="utf8")


